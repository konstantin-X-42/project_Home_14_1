from typing import Any, List, Optional


class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация и сохранение параметров каждого объекта"""

        # Название товара
        self.name = name

        # Описание товара
        self.description = description

        # Цена товара через приватный атрибут
        self.__price = price

        # Количество в наличии
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict[str, Any], products_list: Optional[list["Product"]] = None) -> "Product":
        """
        Класс-метод для создания нового товара или обновления существующего дубликата.
        """
        name = str(product_data.get("name", ""))
        description = str(product_data.get("description", ""))
        price = float(product_data.get("price", 0.0))
        quantity = int(product_data.get("quantity", 0))

        # Если передан список существующих товаров, проверяем на дубликаты
        if products_list:
            for existing_product in products_list:
                if existing_product.name == name:
                    # 1. Складываем количество в наличии
                    existing_product.quantity += quantity

                    # 2. Выбираем более высокую цену, используем СЕТТЕР для сравнения и изменения цены
                    if price > existing_product.price:
                        existing_product.price = price

                    # Возвращаем обновленный существующий товар
                    return existing_product

        # Если дубликат не найден или список не передан, создаем новый объект
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для получения приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для изменения цены с проверкой корректности."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Если цена понижается, запрашиваем подтверждение пользователя
        if new_price < self.__price:
            user_answer = input("Вы уверены, что хотите понизить цену? (y/n): ").strip().lower()
            if user_answer == "y":
                self.__price = new_price
                print("Цена успешно понижена.")
            else:
                print("Действие отменено. Цена осталась прежней.")
        else:
            # Если цена повышается или не меняется, обновляем без вопросов
            self.__price = new_price


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

        # Приватный список объектов класса Product
        self.__products = products

        # Автоматическое увеличение счетчиков при создании новой категории (Класс.атрибут)
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления товара в приватный список категории."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров в виде строки."""
        product_strings = []
        for product in self.__products:
            product_strings.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_strings)
