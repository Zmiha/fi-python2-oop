class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленным числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть целочисленным числом")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}. Страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудио книги должна быть числом с плавающей запятой")
        if duration <= 0:
            raise ValueError("Продолжительность аудио книги должна быть положительным числом")
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, int):
            raise TypeError("Количество страниц должно быть целочисленным числом")
        if new_duration <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}. Продолжительность {self.duration} минут"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    book1 = Book("Мастер и Маргарита", "М. А. Булгаков")
    print(book1)
    print(repr(book1))

    paper_book = PaperBook("Гамлет", "У. Шекспир", 400)
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook("Мертвые души", "Н. В. Гоголь", 231.4)
    print(audio_book)
    print(repr(audio_book))

    #book1.author = "A. C. Пушкин"
    #book1.name = "Собачье сердце"
    #paper_book.pages = 120.8
    #audio_book.duration = -13
