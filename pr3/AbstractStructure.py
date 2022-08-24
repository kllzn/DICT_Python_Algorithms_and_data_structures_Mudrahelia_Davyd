from abc import ABC, abstractmethod


class AbstractStructure(ABC):
    """Абстрактный класс - шаблон с необходимыми для реализации базовыми методами структур данных без самой их
    реализации"""

    @abstractmethod
    def add(self, value, index) -> bool:
        """Добавление новых элементов в структуру данных в позицию по умолчанию или в конкретную позицию со смещением
        (где это требуется)"""
        ...

    @abstractmethod
    def insert(self, value, index) -> bool:
        """Вставка с заменой нового значение в позицию существующего элемента"""
        ...

    @abstractmethod
    def find(self, value) -> [int, None]:
        """Поиск элемента структуры данных по его значению, возвращает индекс"""
        ...

    @abstractmethod
    def get(self, index) -> object:
        """Поиск элемента структуры данных по его ключу(индексу)"""
        ...

    @abstractmethod
    def remove(self, value) -> bool:
        """Удаление элемента структуры данных по значению"""
        ...

    @abstractmethod
    def get_all(self) -> list:
        """Вывод списком всех элементов структуры данных"""
        ...