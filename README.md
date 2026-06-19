# E-commerce Homework

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](COVERAGE.md)

**Репозиторий:** [github.com/kartonka1/internet_shop_v1](https://github.com/kartonka1/internet_shop_v1)

Учебный проект — ядро интернет-магазина на ООП (уроки 14.1–14.3). Реализованы сущности каталога без платежей: товары и категории с контролируемым доступом к данным, иерархия наследования с абстрактными классами и миксинами.

В этой работе добавлены абстрактные классы для базовой функциональности продуктов и класс-миксин для логирования создания объектов.

## Функциональность

- `src/base_product.py` — абстрактный класс `BaseProduct` с общей функциональностью для всех типов товаров.
- `src/repr_mixin.py` — миксин `ReprMixin`, выводящий информацию о создании объекта.
- `src/product.py` — класс `Product` с наследованием от `ReprMixin` и `BaseProduct`: приватная цена (`@property` / `@price.setter`), класс-метод `new_product(cls, product_dict)`.
- `src/smartphone.py` и `src/lawn_grass.py` — наследники `Product` для смартфонов и газонной травы.
- `src/category.py` — класс `Category`: приватный список товаров, `add_product()`, геттер `products` (список товаров).
- Атрибуты класса `Category`: `category_count` и `product_count` — счётчики категорий и добавленных товаров.
- `src/utils/products_loader.py` — загрузка категорий и товаров из `data/products.json`.
- `main.py` — демонстрация функциональности с вводом информации о создании объектов через миксин.

## Установка

```bash
git clone https://github.com/kartonka1/internet_shop_v1.git
cd internet_shop_v1
poetry install
```

## Запуск

```bash
poetry run python main.py
```

## Тесты и покрытие

```bash
poetry run pytest
```

Минимальное покрытие: **75%** (настроено в `pyproject.toml`, текущее — **100%**).

- [`COVERAGE.md`](COVERAGE.md) — сводный отчёт о покрытии в репозитории
- [`coverage.json`](coverage.json) — машиночитаемый отчёт (обновляется при запуске тестов)
- `htmlcov/index.html` — подробный HTML-отчёт (генерируется локально, не коммитится)

## Линтер

```bash
poetry run flake8 .
```

## Пример

```python
from src.category import Category
from src.product import Product
from src.utils.products_loader import load_categories_from_json

product = Product("Наушники", "Беспроводные", 19990.0, 8)
# Output: Product('Наушники', 'Беспроводные', 19990.0, 8)

category = Category("Аудио", "Звуковая техника", [product])
print(category.products_string())

categories = load_categories_from_json("data/products.json")
print(Category.category_count, Category.product_count)
```

## GitFlow

- `main` — стабильная ветка
- `develop` — интеграция
- `feature/homework-product-category` — ДЗ 14.1 (классы Product и Category)
- `feature/homework-14-2-access-modifiers` — ДЗ 14.2 (приватные атрибуты, property, classmethod)
- `feature/homework-14-3-abstract-classes` — ДЗ 14.3 (абстрактные классы и миксины)
