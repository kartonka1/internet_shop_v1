"""Модель категории для домашней работы по каталогу."""

from src.product import Product


class Category:
    """Представляет категорию товаров со списком продуктов."""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        self.name = name
        self.description = description
        self.__products: list[Product] = []
        Category.category_count += 1
        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        # Защищаем список: сюда попадают только реальные товары и их наследники.
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только товары")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[Product]:
        return self.__products

    def products_string(self) -> str:
        result = ""
        for product in self.__products:
            result += product.format_for_catalog()
        return result

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
