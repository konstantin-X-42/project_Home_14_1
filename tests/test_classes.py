import pytest

from src.classes import Category, CategoryIterator, Product, Smartphone, LawnGrass

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


@pytest.fixture
def sample_smartphone():
    """Фикстура для создания смартфона."""
    return Smartphone(
        name="iPhone 15",
        description="Флагман",
        price=100000.0,
        quantity=2,
        efficiency=4.5,
        model="15 Pro",
        memory=256,
        color="Торнадо",
    )


@pytest.fixture
def sample_lawn_grass():
    """Фикстура для создания газонной травы."""
    return LawnGrass(
        name="Газон Канада",
        description="Быстрорастущий",
        price=500.0,
        quantity=10,
        country="Канада",
        germination_period="14 дней",
        color="Зеленый",
    )


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

# ========================================================

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
    expected_output = "Samsung, 60000.0 руб. Остаток: 8 шт.\n" "Nokia, 3999.99 руб. Остаток: 3 шт."
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
    product_data = {"name": "Xiaomi", "description": "Бюджетный смартфон", "price": 15000.0, "quantity": 5}
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
        "quantity": 2,  # Количество увеличится на 2
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
    monkeypatch.setattr("builtins.input", lambda _: "y")

    product.price = 55000.0
    assert product.price == 55000.0


def test_product_price_decrease_cancel(sample_products, monkeypatch):
    """Тест отмены снижения цены при вводе 'n'."""
    product = sample_products[0]

    # Имитируем ввод пользователя 'n' в терминале
    monkeypatch.setattr("builtins.input", lambda _: "n")

    product.price = 55000.0
    assert product.price == 60000.0  # Цена осталась прежней


# ======================================================
# ТЕСТЫ 15.1 для строкового представления и итераторов
# ======================================================


def test_product_str(sample_products):
    """Тест строкового представления объекта класса Product (__str__)."""
    product = sample_products[0]
    assert str(product) == "Samsung, 60000.0 руб. Остаток: 8 шт."


def test_category_str(sample_products):
    """Тест строкового представления объекта класса Category (__str__)."""
    category = Category("Смартфоны", "Мобильные телефоны", [sample_products[0], sample_products[1]])
    # 8 шт (Samsung) + 3 шт (Nokia) = 11 шт всего на складе
    assert str(category) == "Смартфоны, количество продуктов: 11 шт."


def test_category_iterator(sample_products):
    """Тест работы класса-итератора CategoryIterator в цикле for."""
    category = Category("Смартфоны", "Мобильные телефоны", [sample_products[0], sample_products[1]])

    iterator = CategoryIterator(category)
    iterated_products = []

    # Проверяем, что итератор корректно работает в цикле for
    for product in iterator:
        iterated_products.append(product)

    assert len(iterated_products) == 2
    assert iterated_products[0].name == "Samsung"
    assert iterated_products[1].name == "Nokia"


def test_category_iterator_stop_iteration(sample_products):
    """Тест генерации исключения StopIteration при выходе за пределы списка."""
    category = Category("Аксессуары", "Разное", [sample_products[2]])
    iterator = CategoryIterator(category)

    # Первый вызов возвращает карту памяти
    assert next(iterator).name == "sd 128Гб"

    # Второй вызов должен вызвать StopIteration, так как товаров больше нет
    with pytest.raises(StopIteration):
        next(iterator)


# ======================================================
# ТЕСТЫ 16.1
# ======================================================


def test_smartphone_initialization(sample_smartphone):
    """Задание 1. Тест инициализации подкласса Смартфон."""
    assert sample_smartphone.name == "iPhone 15"
    assert sample_smartphone.efficiency == 4.5
    assert sample_smartphone.model == "15 Pro"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Торнадо"


def test_lawn_grass_initialization(sample_lawn_grass):
    """Задание 1. Тест инициализации подкласса Газонная Трава."""
    assert sample_lawn_grass.name == "Газон Канада"
    assert sample_lawn_grass.country == "Канада"
    assert sample_lawn_grass.germination_period == "14 дней"
    assert sample_lawn_grass.color == "Зеленый"


def test_product_add_assignment_example():
    """Задание 2. Тест сложения двух продуктов (__add__) одного класса."""
    product_a = Product("Товар A", "Описание A", 100.0, 10)
    product_b = Product("Товар B", "Описание B", 200.0, 2)
    assert product_a + product_b == 1400.0


def test_product_add_type_error(sample_products, sample_smartphone, sample_lawn_grass):
    """Задание 2. Тест запрета сложения объектов разных классов через type()."""
    # Базовый продукт + число -> TypeError
    with pytest.raises(TypeError):
        _ = sample_products[0] + 12345

    # Смартфон + Газонная трава -> TypeError
    with pytest.raises(TypeError):
        _ = sample_smartphone + sample_lawn_grass

    # Смартфон + Базовый продукт -> TypeError
    with pytest.raises(TypeError):
        _ = sample_smartphone + sample_products[0]


def test_category_add_invalid_product_type_raises_error():
    """Задание 3. Тест запрета добавления некорректных типов в категорию через isinstance()."""
    category = Category("Тест", "Описание", [])
    with pytest.raises(TypeError):
        category.add_product("Не объект продукта, а просто строка")


def test_category_accepts_subclasses(sample_smartphone, sample_lawn_grass):
    """Задание 3. Тест успешного добавления наследников Product в категорию."""
    category = Category("Микс", "Описание", [sample_smartphone])
    assert Category.product_count == 1

    category.add_product(sample_lawn_grass)
    assert Category.product_count == 2
