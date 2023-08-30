"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

def test_class_Item():
    """Тест, проверяющий правильность создания экземпляра """
    item3 = Item('Холодильник', 30000, 15)
    assert item3.name == 'Холодильник'
    assert item3.price == 30000
    assert item3.quantity == 15

def test_calculate():
    """Тест, проверяющий функцию calculate_total_price"""
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_discount():
    """Тест, проверяющий функцию apply_discount"""
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0