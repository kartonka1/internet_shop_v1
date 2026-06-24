# Отчёт о покрытии тестами

Минимально допустимое покрытие: **75%**.

Текущее покрытие по результатам последнего запуска тестов: **97.18%**.

| Модуль | Строк | Пропущено | Покрытие |
|--------|------:|----------:|---------:|
| `src/category.py` | 34 | 0 | 100% |
| `src/product.py` | 39 | 0 | 100% |
| `src/lawn_grass.py` | 7 | 0 | 100% |
| `src/smartphone.py` | 8 | 0 | 100% |
| `src/utils/products_loader.py` | 13 | 0 | 100% |
| `src/repr_mixin.py` | 11 | 0 | 100% |
| `src/category_iterator.py` | 15 | 0 | 100% |
| `src/base_product.py` | 15 | 4 | 73% |
| **Итого** | **142** | **4** | **97.18%** |

Подробный HTML-отчёт доступен в каталоге `htmlcov/` (файл `htmlcov/index.html`).

Машиночитаемый отчёт: [`coverage.json`](coverage.json).

Обновление отчёта:

```bash
poetry run pytest
```
