"""Модель категории для домашней работы по каталогу"""

from src.product import Product


class Category:
    """Представляет категорию товаров со списком продуктов"""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
