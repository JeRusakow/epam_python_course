import pytest

from homework11.hw2 import DiscountStrategy, Order

strategy_no_discount = DiscountStrategy(lambda order: order.price)
strategy_morning_discount = DiscountStrategy(lambda order: order.price * 0.75)
strategy_bulk_discount = DiscountStrategy(
    lambda order: order.price * 0.9 if order.weight > 1.0 else order.price
)

simple_order = Order(100.0, 0.55, strategy_morning_discount)
bulk_order = Order(100.0, 2.35, strategy_bulk_discount)


def test_morning_discount():
    assert simple_order.final_price == 100.0 * 0.75


def test_weight_discount():
    assert bulk_order.final_price == 100.0 * 0.9


def test_pass_only_dicsount_strategy_instance():
    with pytest.raises(TypeError, match="Not a strategy passed"):
        _ = Order(100.0, 1.2, lambda order: order.price)
