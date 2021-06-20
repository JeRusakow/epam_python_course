"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
from typing import Callable


class Order:
    """
    Order class.

    Args:
        price: A basic order price
        weight: An order's weight in kilos
        discount_strategy: A strategy of discount to apply
    """

    def __init__(
        self, price: float, weight: float, discount_strategy: "DiscountStrategy"
    ):
        self.price = price
        self.weight = weight

        if not isinstance(discount_strategy, DiscountStrategy):
            raise TypeError("Not a strategy passed")
        self.discount_strategy = discount_strategy

    @property
    def final_price(self):
        return self.discount_strategy(self)

    def set_discount_strategy(self, strategy):
        self.discount_strategy = strategy


class DiscountStrategy:
    """
    A class for discount strategy

    Args:
        strategy: A callable to compute price for an order
    """

    def __init__(self, strategy: Callable[[Order], float]):
        self.strategy_func = strategy

    def __call__(self, order_instance: Order) -> float:
        return self.strategy_func(order_instance)
