from src.keyboard import Keyboard, Mixinlang

k1 = Keyboard('Dark Project KD87A', 9600, 5)

def test_keyboard():
    """
    Тест на создание экземляра класса Keyboard()
    """
    assert str(k1) == "Dark Project KD87A"
    assert k1.price == 9600
    assert k1.quantity == 5

def test_change_lang():
    k1.change_lang()
    assert str(k1.language) == 'RU'
    k1.change_lang()
    assert str(k1.language) == 'EN'