from src.phone import Phone
from src.item import Item


def test_phone():
    """
    Тест на создание и чтение экземпляра класса Phone()
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
    assert str(phone1) == "iPhone 14"


def test_phone_add():
    """
    Тест функии add() в классе Phone()
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + item1 == 40
