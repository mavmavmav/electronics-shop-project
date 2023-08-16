"""Здесь надо написать тесты с использованием pytest для модуля item."""
from poetry.console.commands import self

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_calculate():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_pay_rate():
    assert Item.pay_rate == 0.8


def test_discount():
    assert item1.apply_discount() == 8000.0