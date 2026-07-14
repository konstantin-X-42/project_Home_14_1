from abc import ABC, abstractmethod
from typing import Any, List, Optional


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов проекта."""

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict[str, Any], products_list: Optional[list[Any]] = None) -> Any:
        """Абстрактный класс-метод для создания нового товара."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Абстрактный сеттер для цены."""
        pass


# 16.2 задание 1, 2
class PrintMixin:
    """Класс миксин для логирования создания объектов."""
#####
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Конструктор миксина, печатающий информацию об объекте в консоль."""
        # Выводим строковое представление объекта в консоль
        print(self.__repr__())
        # Передаем управление дальше по цепочке MRO для инициализации объекта
        super().__init__(*args, **kwargs)
#####
    # 17.1 задание 2 изменил метод
    def __repr__(self) -> str:
        """Магический метод для детального текстового представления объекта."""
        class_name = self.__class__.__name__
        attrs_list = []
        for k, v in self.__dict__.items():
            clean_key = k.split("__")[-1]
            val = f"'{v}'" if isinstance(v, str) else str(v)
            attrs_list.append(f"{clean_key}={val}")

        return f"{class_name}({', '.join(attrs_list)})"

    # def __repr__(self) -> str:
    #     """Магический метод для детального текстового представления объекта."""
    #     # Получаем имя текущего класса динамически
    #     class_name = self.__class__.__name__
    #     # Динамически собираем все значения атрибутов через __dict__
    #     attrs = ", ".join(f"'{v}'" if isinstance(v, str) else str(v) for v in self.__dict__.values())
    #     return f"{class_name}({attrs})"


# 16.2 задание 2. Добавляем миксин в цепочку наследования класса Product (справа)
# class Product(BaseProduct, PrintMixin):
# 17.1 задание 2. Добавляем миксин в цепочку наследования класса Product (слева)
class Product(PrintMixin, BaseProduct):
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация и сохранение параметров каждого объекта"""
        # 17.1 задание 1. Вызываем исключение, если количество нулевое или отрицательное
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        # Название товара
        self.name = name
        # Описание товара
        self.description = description
        # Цена товара через приватный атрибут
        self.__price = price
        # Количество в наличии
        self.quantity = quantity
        # вызываем super().__init__() без аргументов, чтобы отработал конструктор миксина и распечатал готовый объект!
######17.1-2
        # super().__init__()

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """
        Сложение двух продуктов, сумма произведений цены на количество.
        Разрешено сложение товаров только одинаковых классов.
        """
        # 16.1 задание 2. Строгая проверка на совпадение классов с помощью type()
        if type(self) is not type(other):
            raise TypeError("Можно складывать товары только одинаковых классов продуктов")
        # Перемножаем цену на количество для обоих товаров и складываем
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict[str, Any], products_list: Optional[list["Product"]] = None) -> "Product":
        """
        Класс-метод для создания нового товара или обновления существующего дубликата.
        """
        name = str(product_data.get("name", ""))
        description = str(product_data.get("description", ""))
        price = float(product_data.get("price", 0.0))
        quantity = int(product_data.get("quantity", 0))

        if products_list:
            for existing_product in products_list:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product
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
        if new_price < self.__price:
            user_answer = input("Вы уверены, что хотите понизить цену? (y/n): ").strip().lower()
            if user_answer == "y":
                self.__price = new_price
                print("Цена успешно понижена.")
            else:
                print("Действие отменено. Цена осталась прежней.")
        else:
            self.__price = new_price


########################################################################################################


class Smartphone(Product):
    """16.1 Класс для представления смартфона."""
#####
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализация смартфона.
        Использует конструктор базового класса Product для общих атрибутов
        и расширяется специфичными для смартфона свойствами.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет

#####
class LawnGrass(Product):
    """16.1 Класс для представления газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализация газонной травы.
        Использует конструктор базового класса Product для общих атрибутов
        и расширяется специфичными для травы свойствами.
        """
        super().__init__(name, description, price, quantity)
        self.country = country  # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет


# 17.1 задание2
class BaseOrderCategory(ABC):
    """Абстрактный базовый класс для Категорий и Заказов."""

    @abstractmethod
    def __str__(self) -> str:
        """Обязательное строковое представление для наследников."""
        pass

# 17.1 задание2
class Category(BaseOrderCategory):
    """Класс для представления категории товаров."""

    # Атрибуты класса для хранения общей информации
    category_count: int = 0  # Количество категорий
    product_count: int = 0  # Количество уникальных товаров

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """Инициализация и сохранение параметров каждого объекта"""
        # Название категории
        self.name = name
        # Описание категории
        self.description = description
        self.__products: List[Product] = []  # Изначально создаем пустой приватный список

        # Запускаем все переданные продукты через метод add_product с проверкой типа
        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def __str__(self) -> str:
        """Строковое представление категории"""
        # for берет каждый товар из приватного списка,
        # product.quantity - на каждом шаге цикла, забираем у текущего товара его количество и суммируем
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления товара в приватный список категории.
        Принимает только объекты класса Product или его наследников.
        """
        # 16.1.задание 3. Проверка типа с помощью isinstance
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только продукты или их наследников")
        # 17.1 задание 2 Проверка товара в списке, если такой товар уже существует, добавляет его копию еще раз
        if any(p.name == product.name for p in self.__products):
            self.__products.append(product)
        else:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров в виде строки с использованием __str__ продуктов"""
        # Оптимизация: преобразуем каждый объект продукта в строку через str(product)
        # ----------------------------
        # 1. Создаем пустой список, куда будем складывать готовые текстовые строки
        product_strings = []

        # 2. Запускаем цикл: берем по очереди каждый объект-продукт из приватного списка
        for product in self.__products:
            # Переводим объект продукта в строку. В этот момент автоматически
            # вызывается метод __str__ внутри класса Product.
            product_text = str(product)

            # Складываем получившуюся текстовую строку в наш список product_strings
            product_strings.append(product_text)

        # 3. Объединяем все элементы списка в один большой текст.
        # На месте стыков между строками вставляем перенос строки (\n).
        result_text = "\n".join(product_strings)

        # 4. Возвращаем готовый текст из метода наружу
        return result_text

    # ----------------------------
    # запись коротко
    # return "\n".join(str(product) for product in self.__products)

    @property
    def get_products_list(self) -> list[Product]:
        """Дополнительный геттер для получения списка объектов (для итератора)"""
        return self.__products

    # 17.1 задание 2. Расчет средней цены товаров
    def middle_price(self) -> float:
        """Метод подсчета среднего ценника всех товаров в категории.
        Если в категории нет товаров, возвращает 0."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            # Если в категории нет товаров (деление на ноль), возвращаем 0
            return 0.0

class CategoryIterator:
    """Класс для итерации по товарам конкретной категории."""

    def __init__(self, category: Category) -> None:
        self.products = category.get_products_list
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        self.index = 0  # Сбрасываем индекс при начале новой итерации
        return self

    def __next__(self) -> Product:
        # Проверяем не закончились ли товары, меньше ли текущий индекс, чем общее число товаров
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            # товары закончились
            raise StopIteration


# 16.2 доп.задание
class BaseOrderCategory(ABC):
    """Абстрактный базовый класс для Категорий и Заказов."""

    @abstractmethod
    def __str__(self) -> str:
        """Обязательное строковое представление для наследников."""
        pass


class Order(BaseOrderCategory):
    """Класс для представления заказа одного товара."""

    def __init__(self, product: Product, quantity: int):
        """Инициализация заказа."""
        # 16.1 проверка типа. Заказ может принимать только продукты или их наследников
        if not isinstance(product, Product):
            raise TypeError("В заказ можно добавить только продукт или его наследника")

        # 17.1 задание 2
        if quantity <= 0:
            raise ValueError("Количество товара в заказе должно быть больше нуля")

        self.product = product
        self.quantity = quantity


    @property
    def total_cost(self) -> float:
        """Динамический расчет итоговой стоимости заказа."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Строковое представление заказа."""
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итоговая стоимость: {self.total_cost} руб."
