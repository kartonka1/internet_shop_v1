"""Загрузка категорий и товаров из JSON.

Этот модуль предоставляет функцию для загрузки данных о категориях
и товарах из JSON-файла и создания соответствующих объектов.
"""

import json
from pathlib import Path

from src.category import Category
from src.product import Product


def load_categories_from_json(file_path: str) -> list[Category]:
    """Читает JSON-файл и возвращает список объектов Category с товарами Product.
    
    Args:
        file_path: Путь к JSON-файлу с данными о категориях и товарах
        
    Returns:
        Список объектов Category с добавленными товарами Product
        
    Примечания:
        Ожидаемая структура JSON-файла:
        [
            {
                "name": "Название категории",
                "description": "Описание категории",
                "products": [
                    {
                        "name": "Название товара",
                        "description": "Описание товара",
                        "price": "Цена товара",
                        "quantity": "Количество товара"
                    }
                ]
            }
        ]
    """
    path = Path(file_path)
    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    categories: list[Category] = []
    for item in data:
        # Создаем список товаров для каждой категории
        products = [
            Product(
                name=product["name"],
                description=product["description"],
                price=float(product["price"]),
                quantity=int(product["quantity"]),
            )
            for product in item["products"]
        ]
        # Создаем категорию с товарами
        categories.append(
            Category(
                name=item["name"],
                description=item["description"],
                products=products,
            )
        )
    return categories
