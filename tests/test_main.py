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
    """main.py (14.2) запрашивает подтверждение при понижении цены."""
    monkeypatch.setattr("builtins.input", lambda _: "y")
    main_path = Path(__file__).resolve().parents[1] / "main.py"
    runpy.run_path(str(main_path), run_name="__main__")
    out = capsys.readouterr().out

    assert "Samsung Galaxy S23 Ultra" in out
    assert "Остаток: 5 шт." in out
    assert '55" QLED 4K' in out
    assert "4\n" in out or out.strip().endswith("4")
    assert "800" in out
    assert "Цена не должна быть нулевая или отрицательная" in out
