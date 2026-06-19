"""Абстрактный базовый класс для всех типов продуктов."""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс продукта со стандартным функционалом."""

    name: str
    description: str
    quantity: int

    @property
    @abstractmethod
    def price(self) -> float:
        """Возвращает цену продукта."""
        pass

    @abstractmethod
    def format_for_catalog(self) -> str:
        """Форматирует информацию о продукте для вывода в каталоге."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Возвращает общую стоимость при сложении двух продуктов."""
        pass
