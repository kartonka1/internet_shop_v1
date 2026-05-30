"""Загрузка категорий и товаров из JSON."""

import json
from pathlib import Path

from src.category import Category
from src.product import Product


def load_categories_from_json(file_path: str) -> list[Category]:
    """Читает JSON-файл и возвращает список объектов Category с товарами Product."""
    path = Path(file_path)
    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    categories: list[Category] = []
    for item in data:
        products = [
            Product(
                name=product["name"],
                description=product["description"],
                price=float(product["price"]),
                quantity=int(product["quantity"]),
            )
            for product in item["products"]
        ]
        categories.append(
            Category(
                name=item["name"],
                description=item["description"],
                products=products,
            )
        )
    return categories
