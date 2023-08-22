"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
item4 = Item("Холодильная камера", 36000, 7)


def test_class_Item():
    """
    Тест, проверяющий правильность создания экземпляра
    """
    item3 = Item('Холодильник', 30000, 15)
    assert item3.name == 'Холодильник'
    assert item3.price == 30000
    assert item3.quantity == 15


def test_calculate_total_price():
    """
    Тест, проверяющий функцию calculate_total_price
    """
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    """
    Тест, проверяющий функцию apply_discount
    """
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0


def test_name_length():
    """
    Тест, проверяющий количество символов в названии и обрезающий текст, если символов больше 10
    добавляя три точки в конце
    """
    item4.name = 'Микроволновая печь'
    assert item4.name == 'Микроволно...'


def test_instantiate_from_csv():
    """
    тест, проверяющий создание объектов из файла .csv
    и правильность чтения объектов
    """
    Item.all = []
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'
