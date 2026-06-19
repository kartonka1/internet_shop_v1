"""Тесты для демонстрации Product/Category в main.py."""

import runpy
from pathlib import Path

import pytest

from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Сбрасывает счётчики класса перед запуском main.py."""
    Category.category_count = 0
    Category.product_count = 0


def test_main_runs_without_error(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """main.py запускается без ошибок и выводит информацию о создании объектов."""
    monkeypatch.setattr("builtins.input", lambda _: "y")
    main_path = Path(__file__).resolve().parents[1] / "main.py"
    runpy.run_path(str(main_path), run_name="__main__")
    out = capsys.readouterr().out

    # Проверяем информацию о создании объектов от миксина
    assert "Product('Samsung Galaxy S23 Ultra'" in out
    assert "Product('Iphone 15'" in out
    assert "Product('Xiaomi Redmi Note 11'" in out
    assert "Product('55\" QLED 4K'" in out
    
    # Проверяем вывод информации о товарах
    assert "Samsung Galaxy S23 Ultra" in out
    assert "шт." in out  # Проверяем что есть информация о количестве товаров
    assert '55" QLED 4K' in out
    assert "4" in out  # 4 товара всего
