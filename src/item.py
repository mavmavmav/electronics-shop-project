import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        """
        Метод для отображения информации для пользователя
        """
        return f'{self.__name}'

    def __repr__(self):
        """
        Метод для отображения информации для разработчика
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        """
        Метод для операций сложения
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_string: str):
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
    def instantiate_from_csv(cls, filename='../src/items.csv'):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all = []
        with open(filename, newline='') as csvfile:
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


