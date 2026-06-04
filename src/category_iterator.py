"""Итератор для перебора товаров категории."""


from src.category import Category
from src.product import Product


class CategoryIterator:
    """Итератор для перебора товаров категории.
    
    Позволяет использовать объект категории в цикле for для
    последовательного доступа к каждому товару в категории.
    
    Атрибуты:
        _category: Объект категории для итерации
        _index: Текущий индекс в списке товаров
        _products: Список товаров категории (получен через приватный атрибут)
    """

    def __init__(self, category: Category) -> None:
        """Инициализирует итератор категорией.
        
        Args:
            category: Объект категории, по которой будет производиться итерация
        """
        self._category = category
        self._index = 0
        self._products = category._Category__products

    def __iter__(self) -> "CategoryIterator":
        """Возвращает сам итератор.
        
        Returns:
            Сам объект итератора для использования в цикле for
        """
        return self

    def __next__(self) -> Product:
        """Возвращает следующий товар категории.
        
        Returns:
            Следующий товар в списке товаров категории
            
        Raises:
            StopIteration: Когда достигнут конец списка товаров
        """
        if self._index >= len(self._products):
            raise StopIteration
        product = self._products[self._index]
        self._index += 1
        return product
