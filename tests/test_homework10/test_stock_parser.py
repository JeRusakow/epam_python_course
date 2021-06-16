from homework10.hw_stonks import SnP500Parser

test_table_page_path = "tests/test_data/hw_10/page_for_table_and_link_parse_test.html"
test_company_page_path = "tests/test_data/hw_10/page_for_company_parse_test.html"

main_page_url = "https://markets.businessinsider.com/index/components/s&p_500"
company_page_prefix = "https://markets.businessinsider.com"


def test_parse_links_to_other_pages():
    parser = SnP500Parser()

    expected_urls = [
        main_page_url + "?p=1",
        main_page_url + "?p=2",
        main_page_url + "?p=3",
        main_page_url + "?p=4",
        main_page_url + "?p=5",
        main_page_url + "?p=6",
    ]
    with open(test_table_page_path, "r") as page:
        page_urls = parser.parse_pages_urls(page.read())
        assert page_urls == expected_urls


def test_parse_company_info_from_table():
    parser = SnP500Parser()

    expected_companies = [
        {"url": company_page_prefix + "/stocks/yum-stock", "yearly_change": 17.04},
        {"url": company_page_prefix + "/stocks/zbh-stock", "yearly_change": 12.46},
        {"url": company_page_prefix + "/stocks/zion-stock", "yearly_change": 43.13},
        {"url": company_page_prefix + "/stocks/zts-stock", "yearly_change": 28.71},
    ]

    with open(test_table_page_path, "r") as page:
        cmps = list(parser.parse_company_list(page.read()))
        assert cmps == expected_companies


def test_parse_company_page():
    parser = SnP500Parser()

    expected_data = {
        "name": "YUM! Brands Inc.",
        "price": 117.51,
        "code": "YUM",
        "max_profit": 122.73 - 84.17,
        "P/E": 30.29,
    }

    with open(test_company_page_path, "r") as page:
        cmp_data = parser.parse_company_page(page.read())
        assert expected_data == cmp_data
