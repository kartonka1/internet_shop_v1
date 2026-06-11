"""Тесты для Product, Category и загрузки из JSON."""

from pathlib import Path

import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone
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


def test_product_str() -> None:
    product = Product("iPhone 15", "128 ГБ", 89990.50, 14)
    result = str(product)
    assert result == "iPhone 15, 89990.5 руб. Остаток: 14 шт."


def test_product_str_integer_price() -> None:
    product = Product("Наушники", "Беспроводные", 19990.0, 8)
    result = str(product)
    assert result == "Наушники, 19990 руб. Остаток: 8 шт."


def test_product_add() -> None:
    product1 = Product("Товар 1", "Описание", 100.0, 10)
    product2 = Product("Товар 2", "Описание", 200.0, 2)
    result = product1 + product2
    assert result == 100.0 * 10 + 200.0 * 2  # 1000 + 400 = 1400


def test_product_add_different_types_raises_type_error() -> None:
    smartphone = Smartphone("Телефон", "Описание", 1000.0, 2, 90.0, "Model X", 128, "Черный")
    grass = LawnGrass("Трава", "Описание", 100.0, 3, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        _ = smartphone + grass


def test_smartphone_initialization() -> None:
    smartphone = Smartphone("Телефон", "Описание", 1000.0, 2, 90.0, "Model X", 128, "Черный")

    assert smartphone.name == "Телефон"
    assert smartphone.description == "Описание"
    assert smartphone.price == 1000.0
    assert smartphone.quantity == 2
    assert smartphone.efficiency == 90.0
    assert smartphone.model == "Model X"
    assert smartphone.memory == 128
    assert smartphone.color == "Черный"


def test_lawn_grass_initialization() -> None:
    grass = LawnGrass("Трава", "Описание", 100.0, 3, "Россия", "7 дней", "Зеленый")

    assert grass.name == "Трава"
    assert grass.description == "Описание"
    assert grass.price == 100.0
    assert grass.quantity == 3
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_category_add_product_accepts_product_subclasses() -> None:
    category = Category("Смартфоны", "Описание", [])
    smartphone = Smartphone("Телефон", "Описание", 1000.0, 2, 90.0, "Model X", 128, "Черный")

    category.add_product(smartphone)

    assert category.products == "Телефон, 1000 руб. Остаток: 2 шт.\n"
    assert Category.product_count == 1


def test_category_add_product_rejects_non_product() -> None:
    category = Category("Смартфоны", "Описание", [])

    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_category_str() -> None:
    product1 = Product("Товар 1", "Описание", 100.0, 10)
    product2 = Product("Товар 2", "Описание", 200.0, 5)
    category = Category("Электроника", "Описание", [product1, product2])
    result = str(category)
    assert result == "Электроника, количество продуктов: 15 шт."


def test_category_iterator() -> None:
    product1 = Product("Товар 1", "Описание", 100.0, 10)
    product2 = Product("Товар 2", "Описание", 200.0, 5)
    product3 = Product("Товар 3", "Описание", 300.0, 3)
    category = Category("Электроника", "Описание", [product1, product2, product3])

    iterator = CategoryIterator(category)
    products_list = list(iterator)

    assert len(products_list) == 3
    assert products_list[0] == product1
    assert products_list[1] == product2
    assert products_list[2] == product3


def test_category_iterator_in_for_loop() -> None:
    product1 = Product("Товар 1", "Описание", 100.0, 10)
    product2 = Product("Товар 2", "Описание", 200.0, 5)
    category = Category("Электроника", "Описание", [product1, product2])

    products_from_loop = []
    for product in CategoryIterator(category):
        products_from_loop.append(product)

    assert len(products_from_loop) == 2
    assert products_from_loop[0] == product1
    assert products_from_loop[1] == product2
