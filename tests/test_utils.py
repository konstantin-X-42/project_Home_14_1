import json

import pytest

from src.classes import Category, Product
from src.utils import load_data


# ================================
# запуск тестов
# poetry run pytest tests/test_utils.py -v
# ================================


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Фикстура для автоматического сброса счетчиков класса перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


# ================================


def test_load_data_success(tmp_path):
    """Тест успешной загрузки корректных данных из JSON-файла."""
    # Тестовые данные в формате JSON
    test_data = [
        {
            "name": "Электроника",
            "description": "Техника и гаджеты",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Флагман",
                    "price": 50000.0,
                    "quantity": 10,
                },
                {
                    "name": "Наушники",
                    "description": "Беспроводные",
                    "price": 5000.0,
                    "quantity": 2,
                },
            ],
        },
        {"name": "Книги", "description": "Художественная literature", "products": []},
    ]

    # Создаем временный файл во временной папке pytest
    test_file = tmp_path / "test_products.json"

    # Записываем тестовый JSON в файл с кодировкой UTF-8
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(test_data, f)

    # Вызываем тестируемую функцию
    result = load_data(str(test_file))

    # 1. Проверяем длину возвращаемого списка категорий
    assert len(result) == 2

    # 2. Проверяем первую категорию и её товары
    cat_1 = result[0]
    assert isinstance(cat_1, Category)
    assert cat_1.name == "Электроника"
    assert cat_1.description == "Техника и гаджеты"

    # ИСПРАВЛЕНО: Обращаемся к приватному списку через name mangling для проверки его длины
    assert len(cat_1._Category__products) == 2

    # ИСПРАВЛЕНО: Извлекаем объект Product из приватного списка
    prod_1 = cat_1._Category__products[0]
    assert isinstance(prod_1, Product)
    assert prod_1.name == "Смартфон"
    assert prod_1.price == 50000.0
    assert prod_1.quantity == 10

    # 3. Проверяем вторую категорию (пустую)
    cat_2 = result[1]
    assert cat_2.name == "Книги"

    # ИСПРАВЛЕНО: Проверяем пустой приватный список
    assert len(cat_2._Category__products) == 0

    # 4. Проверяем, что глобальные атрибуты классов тоже корректно посчитались
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_load_data_file_not_found():
    """Тест поведения функции при отсутствии файла.
    Ожидается стандартная ошибка FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file_12345.json")
