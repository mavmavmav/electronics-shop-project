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
        self.name = name

        self.price = price
        self.quantity = quantity


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

    def instantiate_from_csv(self) -> list:
        with open('C:/Users/007sh/Desktop/electronics-shop-project/src/items.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(dict(row))





    def string_to_number(self=str) -> int:

        pass

item = Item('Телефон', 10000, 5)
print(Item.instantiate_from_csv(self=item))
