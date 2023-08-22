import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_string: str):
        if len(name_string) >= 10:
            self.__name = name_string[:10] + '...'
        else:
            self.__name = name_string

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, filename='C:/Users/007sh/Desktop/electronics-shop-project/src/items.csv'):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """

        with open(cls.CSV_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string: str) -> float:
        """
        Возвращает число из числа-строки
        """
        return int(float(string))
