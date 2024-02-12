from typing import Union


class Restaurant:
    """
    Класс ресторан, состоит из названия ресторана и средней цены чека в нем
    """

    def __init__(self, name: str, average_price: Union[float, int]):
        """
        Конструктор класса
        :param name: Название ресторана
        :param average_price: Средняя цена чека
        """
        self.average_price = average_price
        self.name = name

    def __repr__(self):
        """
        Магический метод __repr__
        :return: Валидный python код
        """
        return f'Restaurant(name={self.name!r},average_price={self.average_price})'

    def __str__(self):
        """
        Магический метод __str__
        :return: Понятная пользователю информация о классе
        """
        return f'Ресторан "{self.name}", средняя цена чека = {self.average_price} рублей'

    def change_price(self, new_price: Union[int, float]):
        """
        Метод изменения средней цены. Цена должна быть неотрицательным числом
        :param new_price: Новая цена
        :return: Новая цена, при соблюдении условий
        """
        if not isinstance(new_price, Union[int, float]):
            raise TypeError("Новая цена должна быть типа int или float")
        if new_price < 0:
            raise ValueError("Цена должна быть неотрицательной")
        self.average_price = new_price

    def change_name(self, new_name: str):
        """
        Метод изменения названия. Новое название должно быть непустой строкой
        :param new_name: Новое название
        :return: Новое название, при соблюдении условий
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое название должно быть типа str")
        if new_name == "":
            raise ValueError("Название не может быть пустым")
        self.name = new_name


class FastFood(Restaurant):
    """
    Дочерний класс ресторана быстрого питания, состоит из названия и средней цены чека в нем
    """

    def __repr__(self):
        """
        Перегрузка метода __repr__ с целью вывода валидного кода
        :return: Валидный python код
        """
        return f'FastFood(name={self.name!r},average_price={self.average_price})'

    def change_price(self, new_price: Union[int, float]):
        """
        Перегрузка метода change_price с целью добавления нового условия, не позволяющего указать цену,
        которая будет больше 1000 рублей (так как ресторан быстрого питания предполагает бюджетный ценник)
        :param new_price: Новая цена
        :return: Новая цена, при соблюдении условий
        """
        if not isinstance(new_price, Union[int, float]):
            raise TypeError("Новая цена должна быть типа int или float")
        if new_price < 0:
            raise ValueError("Цена должна быть неотрицательной")
        if new_price >= 1000:
            raise ValueError("Цена для класса FastFood слишком высока")
        self.average_price = new_price


if __name__ == "__main__":
    def print_all(name):
        print(name)
        print(repr(name))
        print("-----------------------------")


    restaurant = Restaurant("Черный тигр", 12565.3)
    fast_food = FastFood("Бургер Кинг", 378)

    print_all(restaurant)
    print_all(fast_food)

    restaurant.change_name("Черный котик")
    restaurant.change_price(4831)
    # restaurant.change_price(-1000)

    fast_food.change_name("Мак Доналдс")
    fast_food.change_price(500.1)
    # fast_food.change_price(1005)

    print_all(restaurant)
    print_all(fast_food)
    pass
