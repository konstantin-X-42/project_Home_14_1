import json

from src.classes import Category, Product


def load_data(file_path: str) -> list[Category]:
    """Читает JSON-файл и возвращает список объектов класса Category."""
    categories_list = []

    # Открываем файл с явным указанием кодировки UTF-8 (чтобы не было проблем с кириллицей)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        # Перебираем категории в JSON
        for category_data in data:
            # 1. Создаем пустой список для объектов Product
            products_list = []

            # 2. Проходим циклом по словарям товаров из JSON
            for product_data in category_data.get("products", []):
                # Создаем объект Product из данных словаря
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )

                # записываем данные product в конец списка product_list
                products_list.append(product)

            # 3. Создаем объект category и передаем список готовых ОБЪЕКТОВ Product в конструктор Category
            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products_list,  # Передаем объекты, а не словари!
            )
            # записываем данные category в конец списка categories_list
            categories_list.append(category)

    return categories_list


# ================================
# print
# ================================

# import os

# if __name__ == "__main__":
#     # Сбрасываем счетчики перед загрузкой (на всякий случай)
#     Category.category_count = 0
#     Category.product_count = 0
#
#
#     # Определяем путь к текущему файлу utils.py, поднимаемся на уровень выше в src, затем в корень OOP_practica
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     root_dir = os.path.dirname(current_dir)  # это папка OOP_practica
#     json_path = os.path.join(root_dir, "data", "products.json")
#
#     # Загружаем данные из файла json
#     categories = load_data(json_path)
#
#     print(f"--- Успешно загружено ---")
#     print(f"Всего категорий создано: {Category.category_count}")
#     print(f"Всего уникальных товаров создано: {Category.product_count}\n")
#
#     # Выведем информацию для проверки структуры
#     for cat in categories:
#         print(f"Категория: {cat.name} ({cat.description})")
#         print("Товары:")
#         for prod in cat.products:
#             print(
#                 f"  - {prod.name}: {prod.price} руб. (в наличии: {prod.quantity} шт.)"
#             )
#         print("-" * 30)

# ================================
# Возвращает в консоль
# ================================

# --- Успешно загружено ---
# Всего категорий создано: 2
# Всего уникальных товаров создано: 4
#
# Категория: Смартфоны (Смартфоны, как средство не только коммуникации,
# но и получение дополнительных функций для удобства жизни)
# Товары:
#   - Samsung Galaxy C23 Ultra: 180000.0 руб. (в наличии: 5 шт.)
#   - Iphone 15: 210000.0 руб. (в наличии: 8 шт.)
#   - Xiaomi Redmi Note 11: 31000.0 руб. (в наличии: 14 шт.)
# ------------------------------
# Категория: Телевизоры (Современный телевизор, который позволяет
# наслаждаться просмотром, станет вашим другом и помощником)
# Товары:
#   - 55" QLED 4K: 123000.0 руб. (в наличии: 7 шт.)
# ------------------------------
