import pytest

from src.classes import Category, Product

# ================================
# запуск тестов
# poetry run pytest tests/test_classes.py -v
# ================================


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов."""
    product1 = Product("Samsung", "Смартфон", 60000.0, 8)
    product2 = Product("Nokia", "Мобильный телефон", 3999.99, 3)
    product3 = Product("sd 128Гб", "карта памяти", 1750.20, 12)
    return [product1, product2, product3]


# Когда написано @pytest.fixture(autouse=True), фреймворк pytest сканирует тестовый файл,
# видит эту метку и автоматически запускает привязанную к ней функцию перед началом выполнения каждого теста.
@pytest.fixture(autouse=True)
def reset_category_counts():
    """Фикстура для автоматического сброса счетчиков класса перед каждым тестом.
    Гарантирует, что тесты не будут влиять друг на друга.
    В тестах явно не запускается, инициализируется при каждом запуске теста
    """
    Category.category_count = 0
    Category.product_count = 0


# ================================


def test_product_initialization(sample_products):  # в аргумент передаём фикстуру
    """Тест корректности инициализации объекта класса Product."""
    product = sample_products[
        0
    ]  # запускаем функцию-фикстуру и подставляем первый элемент по индексу

    assert product.name == "Samsung"  # реальное значение == ожидаемое значение
    assert product.description == "Смартфон"
    assert product.price == 60000.0
    assert product.quantity == 8


def test_category_initialization(sample_products):
    """Тест корректности инициализации объекта класса Category."""
    category = Category(
        "Смартфоны", "Мобильные телефоны", [sample_products[0], sample_products[1]]
    )
    assert category.name == "Смартфоны"
    assert category.description == "Мобильные телефоны"
    assert category.products == [sample_products[0], sample_products[1]]


def test_category_and_product_count(sample_products):
    """Тест подсчета количества категорий и уникальных продуктов."""
    # До создания категорий счетчики должны быть равны 0
    assert Category.category_count == 0
    assert Category.product_count == 0

    # Создаем первую категорию с 2 товарами
    cat1 = Category("Электроника", "Гаджеты", [sample_products[0], sample_products[1]])

    assert Category.category_count == 1
    assert Category.product_count == 2
    assert cat1.name == "Электроника"

    # Создаем вторую категорию с 1 товаром
    cat2 = Category("Аксессуары", "Разное", [sample_products[2]])
    assert cat2.name == "Аксессуары"

    # Проверяем итоговые значения счетчиков
    assert Category.category_count == 2
    assert Category.product_count == 3
