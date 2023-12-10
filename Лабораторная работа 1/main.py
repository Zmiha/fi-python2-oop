# TODO Написать 3 класса с документацией и аннотацией типов
import random
from typing import Union
import doctest


class Drink:
    def __init__(self, name: str, volume: Union[int, float], grade: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Напиток"

        :param name: Название напитка
        :param volume: Объем напитка
        :param grade: Оценка напитка

        Примеры:
        >>> milk = Drink("Молоко", 500, 7.1)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название напитка должно быть типа str")
        if name == "":
            raise ValueError("Название напитка не может быть пустым")
        self.name = name

        if not isinstance(volume, (int, float)):
            raise TypeError("Объем напитка должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем напитка должен быть больше нуля")
        self.volume = volume

        if not isinstance(grade, (int, float)):
            raise TypeError("Оценка напитка должна быть типа int или float")
        if not (0 <= grade <= 10):
            raise ValueError("Оценка напитка должна принадлежать промежутку от нуля до десяти")
        self.grade = grade

    def take_sip(self, sip=Union[10, 10.0]) -> None:
        """
        Сделать глоток напитка (по умолчанию глоток равен 10мл)

        :param sip: Объем глотка
        :raises TypeError: Если объем глотка не является типом int или float
        :raises ValueError: Если объем глотка меньше нуля или больше, чем осталось напитка

        Примеры:
        >>> tea = Drink("Чай", 250, 9)
        >>> tea.take_sip()
        >>> tea.take_sip(40)
        """
        if not isinstance(sip, (int, float)):
            raise TypeError("Объем глотка должен быть типа int или float")
        if sip <= 0:
            raise ValueError("Объем глотка должен быть больше нуля")
        if sip > self.volume:
            raise ValueError("Слишком большой глоток")
        self.volume -= sip

    def is_good_drink(self) -> bool:
        """
        Функция которая проверяет является ли напиток хорошим (хорошим напитком считается тот, у которого
        оценка >= 7)

        :return: Является ли напиток хорошим

        Примеры:
        >>> milk = Drink("Молоко", 500, 7.0)
        >>> milk.is_good_drink()
        True
        >>> cola = Drink("Кока-Кола", 1500, 6.9)
        >>> cola.is_good_drink()
        False
        """
        return self.grade >= 7

    def change_grade(self, new_grade: Union[int, float]) -> None:
        """
        Функция, которая изменяет оценку напитка

        :param new_grade: Новая оценка
        :raises TypeError: Если новая оценка не является типом int или float
        :raises ValueError: Если новая оценка меньше 0 или больше 10, то вызываем ошибку

        Примеры:
        >>> water = Drink("Вода", 100, 10)
        >>> water.change_grade(8.1)
        """
        if not isinstance(new_grade, (int, float)):
            raise TypeError("Новая оценка напитка должна быть типа int или float")
        if not (0 <= new_grade <= 10):
            raise ValueError("Новая оценка напитка должна принадлежать промежутку от нуля до десяти")
        self.grade = new_grade


class Cat:
    def __init__(self, name: str, age: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Кот"

        :param name: Имя кота
        :param age: Возраст кота

        Примеры:
        >>> cat = Cat("Борис", 2)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должно быть типа str")
        if name == "":
            raise ValueError("Имя кота не может быть пустым")
        self.name = name

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть типа int или float")
        if age <= 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

    def grow_up(self, change: Union[int, float]) -> None:
        """
        Функция, которая увеличивает возраст кота

        :param change: На сколько кот повзрослел
        :raises TypeError: Если изменение возраста не является типом int или float
        :raises ValueError: Если изменение возраста отрицательно

        Примеры:
        >>> cat = Cat("Жора", 5)
        >>> cat.grow_up(3)
        """
        if not isinstance(change, (int, float)):
            raise TypeError("Изменение возраста должно быть типа int или float")
        if change <= 0:
            raise ValueError("Изменение возраста не должно быть отрицательно")
        self.age += change

    def grow_down(self, change: Union[int, float]) -> None:
        """
        Функция, которая уменьшает возраст кота

        :param change: На сколько кот повзрослел
        :raises TypeError: Если изменение возраста не является типом int или float
        :raises ValueError: Если изменение возраста отрицательно или больше текущего возраста кота

        Примеры:
        >>> cat = Cat("Даниил", 2)
        >>> cat.grow_down(1)
        """
        if not isinstance(change, (int, float)):
            raise TypeError("Изменение возраста должно быть типа int или float")
        if (change <= 0) or (change > self.age):
            raise ValueError("Изменение возраста не должно быть отрицательно или больше текущего возраста кота")
        self.age -= change


class DiceGame:
    """
    Игра в кости для нескольких человек. Правила следующие: играть могут от 1 до 10 людей, у каждого игрока два
    20-ти гранных кубика, каждый ход игроки делают бросок, получают за него количество очков, равных выпавшему
    значению (кроме дополнительных правил) и суммируют свои очки, кто первый набирает необходимое количество
    очков для победы - тот и победил.
    Дополнительные правила:
    Если на одном из кубиков выпало 20,то он приносит 40 очков, вместо 20.
    Если на обоих кубиках выпало 20, то они мгновенно приносят победу игроку, который их бросил.
    Если на одном из кубиков выпало 1,то игрок, который их бросил, теряет 20 очков.
    Если на обоих кубиках выпало 1, то игрок, который их бросил, теряет 40 очков.
    """
    def __init__(self, players: int, win_score: int):
        """
        Создание и подготовка к работе объекта "Игра в кости"

        :param players: Количество игроков от 1 до 10
        :param win_score: Количество очков, необходимые для победы
        """
        if not isinstance(players, int):
            raise TypeError("Количество игроков должно иметь тип  int")
        if not (1 <= players <= 10):
            raise ValueError("Недопустимое количество игроков")
        self.players = players

        if not isinstance(win_score, int):
            raise TypeError("Количество очков необходимое для победы должно иметь тип  int")
        self.win_score = win_score

        self.players_score = [0] * players

    def next_turn(self) -> None:
        """
        Функция, отвечающая за продвижение игры в кости и подсчитывающая результаты ходов
        """
        for i in range(self.players):
            dice1 = random.randint(1, 20)
            dice2 = random.randint(1, 20)
            if dice1 == dice2 == 20:
                print(f"Игрок под номером {i+1} выбрасывает две 20 и становится победителем!")
                self.refresh_score()
                break
            elif dice1 == 20 or dice2 == 20:
                dice_sum = dice1 + dice2 + 20
                self.players_score[i] += dice_sum
                print(f"Игроку под номером {i+1} повезло! Он выкинул {dice1} и {dice2}, "
                      f"за что получает {dice_sum} очков, и его счет становится равен {self.players_score[i]}")
                if self.players_score[i] >= self.win_score:
                    print(f"Игрок под номером {i+1} набирает необходимое количество очков и побеждает!")
                    self.refresh_score()
                    break
            elif dice1 == dice2 == 1:
                print(f"Игрок под номером {i+1} потерпел ужасную неудачу и теряет 40 очков :( "
                      f"теперь его счет становится равен {self.players_score[i]}")
                self.players_score[i - 1] -= 40
            elif dice1 == 1 or dice2 == 1:
                self.players_score[i - 1] -= 20
                print(f"Игрок под номером {i+1} потерпел неудачу и теряет 20 очков :( "
                      f"теперь его счет становится равен {self.players_score[i]}")
            else:
                dice_sum = dice1 + dice2
                self.players_score[i] += dice_sum
                print(f"Игрок под номером {i+1} бросает {dice1} и {dice2}, "
                      f"его счет становится равен {self.players_score[i]}")
                if self.players_score[i] >= self.win_score:
                    print(f"Игрок под номером {i+1} набирает необходимое количество очков и побеждает!")
                    self.refresh_score()
                    break

    def refresh_score(self) -> None:
        """
        Функция, отвечающая за обнуления списка с текущими очками игроков при победе одного из них или же по желанию

        Например:
        >>> game = DiceGame(3, 50)
        >>> game.refresh_score()
        """
        self.players_score = [0] * self.players

    def change_win_score(self, new_win_score) -> None:
        """
        Функция для увеличения количество очков, необходимых для победы.

        :param new_win_score: Новое победное число
        :raise TypeError: Если новое значение необходимое для победы не является типом int или float
        :raise ValueError: Если новое значение необходимое для победы не больше предыдущего

        Например:
        >>> game = DiceGame(3, 50)
        >>> game.change_win_score(100)
        """
        if not isinstance(new_win_score, (int, float)):
            raise TypeError("Изменение очков для победы должно быть типа int или float")
        if new_win_score <= self.win_score:
            raise ValueError("Новое значение очков для победы должно быть больше текущего")
        self.win_score = new_win_score


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
    # Проверка игры в кости
    """game = DiceGame(3, 50)
    continue_ = input()
    while continue_ is not None:
        game.next_turn()
        continue_ = input()"""
