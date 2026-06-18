from typing import List


class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация и сохранение параметров каждого объекта"""

        # Название товара
        self.name = name

        # Описание товара
        self.description = description

        # Цена товара
        self.price = price

        # Количество в наличии
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса для хранения общей информации
    category_count: int = 0  # Количество категорий
    product_count: int = 0  # Количество уникальных товаров

    def __init__(self, name: str, description: str, products: List[Product]):
        """Инициализация и сохранение параметров каждого объекта"""

        # Название категории
        self.name = name

        # Описание категории
        self.description = description

        # Список объектов класса Product
        self.products = products

        # Автоматическое увеличение счетчиков при создании новой категории (Класс.атрибут)
        Category.category_count += 1
        Category.product_count += len(products)
