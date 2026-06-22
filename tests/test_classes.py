import pytest

from src.classes import Category, Product


# ================================
# запуск тестов
# poetry run pytest tests/test_classes.py -v

# запуск всех тестов в проекте tests
# poetry run pytest tests -v
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
    product = sample_products[0]  # запускаем функцию-фикстуру и подставляем первый элемент по индексу

    assert product.name == "Samsung"  # реальное значение == ожидаемое значение
    assert product.description == "Смартфон"
    assert product.price == 60000.0
    assert product.quantity == 8


def test_category_initialization(sample_products):
    """Тест корректности инициализации объекта класса Category и работы геттера products."""
    category = Category("Смартфоны", "Мобильные телефоны", [sample_products[0], sample_products[1]])
    assert category.name == "Смартфоны"
    assert category.description == "Мобильные телефоны"

    # Исправлено: теперь геттер возвращает строку в заданном формате
    expected_output = (
        "Samsung, 60000.0 руб. Остаток: 8 шт.\n"
        "Nokia, 3999.99 руб. Остаток: 3 шт."
    )
    assert category.products == expected_output


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


def test_category_add_product(sample_products):
    """Тест добавления товара через add_product."""
    category = Category("Смартфоны", "Мобильные телефоны", [sample_products[0]])
    assert Category.product_count == 1

    # Добавляем новый продукт
    category.add_product(sample_products[1])

    # Проверяем, что общий счетчик увеличился, а товар добавился в строку вывода
    assert Category.product_count == 2
    assert "Nokia, 3999.99 руб. Остаток: 3 шт." in category.products


def test_product_new_product_creation():
    """Тест создания продукта через класс-метод new_product."""
    product_data = {
        "name": "Xiaomi",
        "description": "Бюджетный смартфон",
        "price": 15000.0,
        "quantity": 5
    }
    new_item = Product.new_product(product_data)

    assert isinstance(new_item, Product)
    assert new_item.name == "Xiaomi"
    assert new_item.price == 15000.0
    assert new_item.quantity == 5


def test_product_new_product_duplicate(sample_products):
    """Тест слияния дубликатов при создании через new_product."""
    products_list = [sample_products[0]]  # Список содержит Samsung (60000.0 руб, 8 шт)

    duplicate_data = {
        "name": "Samsung",
        "description": "Новая поставка",
        "price": 65000.0,  # Цена выше текущей
        "quantity": 2  # Количество увеличится на 2
    }

    updated_product = Product.new_product(duplicate_data, products_list)

    assert updated_product.quantity == 10  # 8 + 2
    assert updated_product.price == 65000.0  # Выбрана большая цена


def test_product_price_setter_invalid(sample_products):
    """Тест валидации цены (не должна быть нулевой или отрицательной)."""
    product = sample_products[0]

    product.price = 0
    assert product.price == 60000.0  # Цена не изменилась

    product.price = -100
    assert product.price == 60000.0  # Цена не изменилась


def test_product_price_decrease_confirm(sample_products, monkeypatch):
    """Тест успешного снижения цены при подтверждении 'y'."""
    product = sample_products[0]

    # Имитируем ввод пользователя 'y' в терминале
    monkeypatch.setattr('builtins.input', lambda _: 'y')

    product.price = 55000.0
    assert product.price == 55000.0


def test_product_price_decrease_cancel(sample_products, monkeypatch):
    """Тест отмены снижения цены при вводе 'n'."""
    product = sample_products[0]

    # Имитируем ввод пользователя 'n' в терминале
    monkeypatch.setattr('builtins.input', lambda _: 'n')

    product.price = 55000.0
    assert product.price == 60000.0  # Цена осталась прежней