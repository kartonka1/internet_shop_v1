# E-commerce Homework

Учебный проект — ядро интернет-магазина на ООП (урок 14.1). Реализованы сущности каталога без платежей: товары и категории.

## Функциональность

- `src/product.py` — класс `Product` с полями `name`, `description`, `price`, `quantity`.
- `src/category.py` — класс `Category` с полями `name`, `description`, `products` (список объектов `Product`).
- Атрибуты класса `Category`: `category_count` и `product_count` — увеличиваются при каждом создании категории (товары считаются по длине списка `products`).
- `src/utils/products_loader.py` — загрузка категорий и товаров из `data/products.json`.
- `main.py` — демонстрация из задания (`14.1_main.py`).

## Установка

```bash
cd ecommerce-homework
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

Отчёт о покрытии сохраняется в каталог `htmlcov/` (откройте `htmlcov/index.html` в браузере).

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
category = Category("Аудио", "Звуковая техника", [product])

categories = load_categories_from_json("data/products.json")
print(Category.category_count, Category.product_count)
```

## GitFlow

- `main` — стабильная ветка
- `develop` — интеграция
- `feature/homework-product-category` — ветка с домашним заданием
