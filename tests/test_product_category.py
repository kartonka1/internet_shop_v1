"""Тесты для Product, Category и загрузки из JSON."""

from pathlib import Path

import pytest

from src.category import Category
from src.product import Product
from src.utils.products_loader import load_categories_from_json

PRODUCTS_JSON = Path(__file__).resolve().parents[1] / "data" / "products.json"


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Сбрасывает счётчики класса, чтобы тесты не влияли друг на друга."""
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization() -> None:
    product = Product(
        name="iPhone 15",
        description="128 ГБ",
        price=89990.50,
        quantity=14,
    )

    assert product.name == "iPhone 15"
    assert product.description == "128 ГБ"
    assert product.price == 89990.50
    assert product.quantity == 14


def test_product_price_setter_rejects_non_positive(capsys: pytest.CaptureFixture[str]) -> None:
    product = Product("Товар", "Описание", 1000.0, 1)

    product.price = 0
    captured = capsys.readouterr()
    assert product.price == 1000.0
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"

    product.price = -10
    captured = capsys.readouterr()
    assert product.price == 1000.0
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product_price_setter_accepts_positive() -> None:
    product = Product("Товар", "Описание", 1000.0, 1)

    product.price = 1500.0

    assert product.price == 1500.0


def test_product_price_setter_decrease_requires_confirmation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    product = Product("Товар", "Описание", 1000.0, 1)

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 500.0
    assert product.price == 1000.0

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 500.0
    assert product.price == 500.0


def test_product_new_product_from_dict() -> None:
    product = Product.new_product(
        {
            "name": "Планшет",
            "description": "10 дюймов",
            "price": 25000.0,
            "quantity": 3,
        }
    )

    assert product.name == "Планшет"
    assert product.description == "10 дюймов"
    assert product.price == 25000.0
    assert product.quantity == 3


def test_product_format_for_catalog_fractional_price() -> None:
    product = Product("Молоко", "2.5%", 89.90, 12)

    assert product.format_for_catalog() == "Молоко, 89.9 руб. Остаток: 12 шт.\n"


def test_category_initialization() -> None:
    product = Product("Наушники", "Беспроводные", 19990.0, 8)
    category = Category(
        name="Аудио",
        description="Звуковая техника",
        products=[product],
    )

    assert category.name == "Аудио"
    assert category.description == "Звуковая техника"
    assert category.products == "Наушники, 19990 руб. Остаток: 8 шт.\n"


def test_category_add_product() -> None:
    category = Category("Аудио", "Описание", [])
    product = Product("Колонка", "Портативная", 4990.0, 4)

    category.add_product(product)

    assert category.products == "Колонка, 4990 руб. Остаток: 4 шт.\n"
    assert Category.product_count == 1


def test_category_count() -> None:
    Category("Первая", "Описание", [])
    Category("Вторая", "Описание", [])
    Category("Третья", "Описание", [])

    assert Category.category_count == 3


def test_product_count() -> None:
    first_product = Product("Товар 1", "Описание", 1000.0, 1)
    second_product = Product("Товар 2", "Описание", 2000.0, 2)
    third_product = Product("Товар 3", "Описание", 3000.0, 3)

    Category("Категория 1", "Описание", [first_product, second_product])
    Category("Категория 2", "Описание", [third_product])

    assert Category.product_count == 3


def test_load_categories_from_json() -> None:
    categories = load_categories_from_json(str(PRODUCTS_JSON))

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[0].products.count("шт.") == 3
    assert "Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт." in categories[0].products
    assert categories[1].name == "Телевизоры"
    assert "Остаток: 7 шт." in categories[1].products
    assert Category.category_count == 2
    assert Category.product_count == 4
