"""Модель категории для домашней работы по каталогу"""

from src.product import Product


class Category:
    """Представляет категорию товаров со списком продуктов.
    
    Атрибуты класса:
        category_count: Общее количество созданных категорий
        product_count: Общее количество добавленных товаров во все категории
    
    Атрибуты экземпляра:
        name: Название категории
        description: Описание категории
        _Category__products: Приватный список товаров в категории
    """

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        """Инициализирует категорию.
        
        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров для добавления в категорию (опционально)
        """
        self.name = name
        self.description = description
        self.__products: list[Product] = []
        Category.category_count += 1
        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в приватный список категории.
        
        Args:
            product: Товар для добавления в категорию
            
        Примечания:
            Увеличивает счетчик product_count на 1
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает отформатированный список товаров категории.
        
        Returns:
            Строка с информацией о всех товарах в категории
        """
        result = ""
        for product in self.__products:
            result += product.format_for_catalog()
        return result

    def __str__(self) -> str:
        """Строковое представление категории.
        
        Returns:
            Строка в формате: Название категории, количество продуктов: X шт.
            Количество продуктов считается как сумма quantity всех товаров
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
