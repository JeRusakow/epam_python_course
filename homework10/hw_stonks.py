import asyncio
import json
from collections import defaultdict
from itertools import chain
from typing import Collection, Dict, Iterable, List

import aiohttp
import requests
from bs4 import BeautifulSoup


class SnP500Parser:
    def __init__(self):
        self.base_url = "https://markets.businessinsider.com"
        self.snp500_url = "https://markets.businessinsider.com/index/components/s&p_500"
        self.pages_urls = []
        self.cmp_urls = []
        self.cmp_list = []

        self.usd_rub_ratio = 1.0

    @staticmethod
    def get_rouble_to_dollar_ratio() -> float:
        xml = requests.get("https://www.cbr.ru/scripts/XML_daily.asp").content
        soup = BeautifulSoup(xml, "xml")
        (ratio,) = soup.find("Valute", ID="R01235").Value.contents
        return float(ratio.replace(",", "."))

    async def get_html_page_from_url(
        self, url: str, session: aiohttp.ClientSession
    ) -> str:
        """Downloads an HTML page from stated URL"""
        async with session.get(url) as response:
            return await response.text()

    async def get_pages(self, urls: Iterable) -> Collection[str]:
        async with aiohttp.ClientSession() as session:
            return await asyncio.gather(
                *[self.get_html_page_from_url(url, session) for url in urls]
            )

    def parse_pages_urls(self, page: str) -> List[str]:
        """
        Parses S&P 500 main page to find URLs to other pages

        Returns:
            A list of rating's pages URLs
        """
        soup = BeautifulSoup(page, "html.parser")

        page_nums_section = soup.find("div", class_="finando_paging margin-top--small")
        page_nums = page_nums_section.find_all("a")

        return [self.snp500_url + num_tag["href"] for num_tag in page_nums]

    def parse_company_list(self, page: str):
        """
        Parses a page of rating to find URLs to companies

        Yields:
            A Company instance with partly filled information
        """
        soup = BeautifulSoup(page, "html.parser")
        table_body = soup.find("tbody", class_="table__tbody")
        table_entries = table_body.find_all("tr")

        for table_entry in table_entries:
            cells = table_entry.find_all("td")

            full_url = self.base_url + cells[0].a["href"]
            span = cells[7].find_all("span")[1]
            yearly_change = round(float(span.contents[0].strip("%")), 4)

            yield {"url": full_url, "yearly_change": yearly_change}

    def parse_company_page(self, page: str) -> defaultdict:  # noqa: CCR001
        soup = BeautifulSoup(page, "html.parser")
        data = defaultdict(None)

        (name,) = soup.find("span", class_="price-section__label")
        data["name"] = name.strip()

        (price,) = soup.find("span", class_="price-section__current-value").contents
        data["price"] = round(float(price.replace(",", "")) * self.usd_rub_ratio, 4)

        (code,) = soup.find("span", class_="price-section__category").span.contents
        code = code.strip(" ,")
        data["code"] = code

        snapshot = soup.find("div", class_="snapshot")

        try:
            pe_ratio = (
                snapshot.find("div", text="P/E Ratio")
                .parent.contents[0]
                .strip()
                .replace(",", "")
            )
            price_earnings = round(float(pe_ratio), 4)
        except AttributeError:
            price_earnings = 0.0
        finally:
            data["P/E"] = price_earnings

        try:
            week_54_low = float(
                snapshot.find("div", text="52 Week Low")
                .parent.contents[0]
                .strip()
                .replace(",", "")
            )
            week_54_high = float(
                snapshot.find("div", text="52 Week High")
                .parent.contents[0]
                .strip()
                .replace(",", "")
            )
            max_profit = round((week_54_high - week_54_low) * self.usd_rub_ratio, 4)
        except AttributeError:
            max_profit = 0.0
        finally:
            data["max_profit"] = max_profit

        return data

    async def parse_companies_async(self):
        self.usd_rub_ratio = self.get_rouble_to_dollar_ratio()

        (page,) = await self.get_pages([self.snp500_url])
        self.pages_urls = self.parse_pages_urls(page)

        cmp_list_pages = await self.get_pages(self.pages_urls)

        cmp_map = map(self.parse_company_list, cmp_list_pages)
        self.cmp_list = list(chain.from_iterable(cmp_map))

        cmp_pages = await self.get_pages((cmp["url"] for cmp in self.cmp_list))

        for idx, cmp_page in enumerate(cmp_pages):
            data = self.parse_company_page(cmp_page)
            self.cmp_list[idx] = {**self.cmp_list[idx], **data}

    def parse_snp500(self):
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(self.parse_companies_async())

    def take_top10_rating(self, param: str, desc=True) -> List[Dict]:
        cmp_top = sorted(self.cmp_list, key=lambda x: x[param], reverse=desc)[:10]
        return [
            {"code": cmp["code"], "name": cmp["name"], param: cmp[param]}
            for cmp in cmp_top
        ]


if __name__ == "__main__":
    parser = SnP500Parser()
    parser.parse_snp500()

    ratings = [("price",), ("P/E", False), ("yearly_change",), ("max_profit",)]
    filenames = [
        "highest_price.json",
        "lowest_pe_ratio.json",
        "highest_yearly_growth.json",
        "highest_max_profit.json",
    ]

    for filename, params in zip(filenames, ratings):
        with open(filename, "w") as file:
            rating = parser.take_top10_rating(*params)
            json.dump(rating, file, indent=4)
