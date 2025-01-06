# Фильтрация списка товаров:
# Напишите функцию filter_products(products, category, *, min_price=0,# max_price=10000),
# которая принимает список товаров (список словарей с ключами name, category, price),
# категорию и опциональные параметры минимальной и максимальной цены.
# Функция должна возвращать только те товары, которые соответствуют категории и
# находятся в указанном ценовом диапазоне.

products = [
    {"name": "Ноутбук Lenovo IdeaPad", "category": "Электроника", "price": 65000},
    {"name": "Беспроводные наушники Sony", "category": "Аксессуары", "price": 12000},
    {"name": "Смартфон Samsung Galaxy S21", "category": "Электроника", "price": 85000},
    {"name": "Микроволновая печь Panasonic", "category": "Бытовая техника", "price": 14500},
    {"name": "Электрочайник Philips", "category": "Бытовая техника", "price": 3000},
    {"name": "Гитара Fender Stratocaster", "category": "Музыкальные инструменты", "price": 120000},
    {"name": "Спортивный рюкзак Nike", "category": "Одежда и аксессуары", "price": 4000},
    {"name": "Книга 'Властелин колец'", "category": "Книги", "price": 1500},
    {"name": "Игровая приставка PlayStation 5", "category": "Электроника", "price": 55000},
    {"name": "Стол письменный", "category": "Мебель", "price": 8000},
]

def filter_products(products, category, *, min_price=0, max_price=10000):
