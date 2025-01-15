#
# Задание 1
#
# Школа
#
# Создайте структуру классов в Python, представляющую людей в школе.
# Создайте базовый класс с именем Person, класс с именем Student и еще один с именем Teacher.
# Постарайтесь найти как можно больше методов и атрибутов, которые принадлежат разным классам, и помните, какие из них являются общими, а какие нет.
# Например, name должно быть атрибутом Person, а salary должен быть доступен только учителю.


print(
    '''
Task 1
School
    '''
)


class Person:
    def __init__(self, name, family_name, age, gender):
        self.family_name = family_name
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Name: {self.name} {self.family_name}\nAge: {self.age}\nGender: {self.gender}\n"


class Student(Person):
    def __init__(self, name, family_name, age, gender, class_number, learning_period='morning'):
        super().__init__(name, family_name, age, gender)
        self.class_number = class_number
        self.learning_period = learning_period

    def introduce(self):
        return (super().introduce() +
                f"Class Number: {self.class_number}\nLearning Period: {self.learning_period}\n")


class Teacher(Person):
    def __init__(self, name, family_name, age, gender, studying, experience, salary):
        super().__init__(name, family_name, age, gender)
        self.salary = salary
        self.experience = experience
        self.studying = studying

    def introduce(self):
        return (super().introduce() +
                f"Studying: {self.studying}\nExperience: {self.experience} y.o.\nSalary: {self.salary} UAH\n")

    def increase_salary(self, increase_salary):
        self.salary += increase_salary
        return f'New teacher salary: {self.salary}'


student = Student('Andrii', 'Zadorozhnii', 32, 'Male', '10-A', 'evening')
teacher = Teacher('Olga', 'Petrovna', 55, 'Female', 'Geometry', '12', 5500)

print("\nStudent Info:")
print(student.introduce())

print("\nTeacher Info:")
print(teacher.introduce())
print(teacher.increase_salary(500))

# Задание 2
#
# Математик
# Реализовать класс Mathematician, который является вспомогательным классом для выполнения математических операций со списками.
#
# Класс не принимает никаких атрибутов и имеет только методы:
#
# square_nums (принимает список целых чисел и возвращает список квадратов)
# remove_positives (принимает список целых чисел и возвращает его без положительных чисел)
# filter_leaps (берет список дат (целых чисел) и удаляет те, которые не являются «високосными годами»
print(
    '''
Task 2
Mathematician
    '''
)


class Mathematician:

    def square_nums(self, number_list: list):
        for index in range(len(number_list)):
            number_list[index] = number_list[index] ** 2
        print(number_list)
        return number_list

    def remove_positives(self, number_list: list):
        new_list = []
        for index in range(len(number_list)):
            if number_list[index] < 0:
                new_list.append(number_list[index])
        print(new_list)
        return new_list

    def filter_leaps(self, years_list: list):
        leaps_years = []
        for index in range(len(years_list)):
            if (years_list[index] % 4 == 0 and years_list[index] % 100 != 0) or (years_list[index] % 400 == 0):
                leaps_years.append(years_list[index])
        print(leaps_years)
        return leaps_years


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# Задание 3
#
# Магазин продуктов
#
# Напишите класс Product, который имеет три атрибута:
#
# тип
# имя
# цена

# Затем создайте класс ProductStore, который будет иметь некоторые Products и будет работать со всеми продуктами в магазине. Все методы, в случае если они не могут выполнить свое действие, должны вызывать ValueError с соответствующей информацией об ошибке.
#
# Советы: Используйте концепции агрегации/композиции при реализации класса ProductStore. Вы также можете реализовать дополнительные классы для работы с определенным типом продукта и т. д.

# Также класс ProductStore должен иметь следующие методы:
#
# add(product, amount) - добавляет указанное количество одного товара с предопределенной ценовой надбавкой для вашего магазина (30 процентов)
# set_discount(identifier, percent, identifier_type='name') - добавляет скидку для всех продуктов, указанных входными идентификаторами (type или name). Скидка должна быть указана в процентах
# sell_product(product_name, amount) - удаляет определенное количество товаров из магазина, если они доступны, в противном случае выдает ошибку. Также увеличивает доход, если метод sell_product успешен.
# get_income() - возвращает сумму дохода, заработанную экземпляром ProductStore.
# get_all_products() - возвращает информацию обо всех доступных товарах в магазине.
# get_product_info(product_name) — возвращает кортеж с названием товара и количеством товаров в магазине.
print(
    '''
Task 3
Product store
    '''
)

cash = 0


class Product:
    def __init__(self, product_type, product_name, product_price):
        self.product_type = product_type
        self.product_name = product_name
        if product_price <= 0:
            raise ValueError("Price should be more than 0")
        self.product_price = product_price


class ProductStore:
    def __init__(self):
        self.products = {}  # Хранит товары в формате {имя: {'product': product, 'amount': количество, 'price_with_markup': цена}}
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Unknown object, expected Product")
        if amount <= 0:
            raise ValueError("Quantity should be more than 0")

        if product.product_name in self.products:
            self.products[product.product_name]['amount'] += amount
        else:
            price_with_markup = product.product_price * 1.3
            self.products[product.product_name] = {
                'product': product,
                'amount': amount,
                'price_with_markup': price_with_markup
            }

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent <= 0 or percent >= 100:
            raise ValueError("Discount should be between 0% and 100%")
        for product_info in self.products.values():
            product = product_info['product']
            if (identifier_type == 'name' and product.product_name == identifier) or \
                    (identifier_type == 'type' and product.product_type == identifier):
                product_info['price_with_markup'] *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError(f"Item '{product_name}' not in stock")
        if amount <= 0:
            raise ValueError("Quantity to sell should be more than 0")

        product_info = self.products[product_name]
        if product_info['amount'] < amount:
            raise ValueError(f"Not enough '{product_name}' in stock to sell")

        product_info['amount'] -= amount
        self.income += product_info['price_with_markup'] * amount

        if product_info['amount'] == 0:
            del self.products[product_name]  # Удаляем товар, если его больше нет в наличии

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [
            {
                'name': product_info['product'].product_name,
                'type': product_info['product'].product_type,
                'price': product_info['price_with_markup'],
                'amount': product_info['amount']
            }
            for product_info in self.products.values()
        ]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError(f"Item '{product_name}' not found in stock")
        product_info = self.products[product_name]
        return product_name, product_info['amount']


# Пример использования
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)

print("Income:", s.get_income())
print("All items:", s.get_all_products())

# Этот вызов вызовет ошибку, так как 'Milk' нет в магазине
try:
    print("Information regarding Food:", s.get_product_info("Milk"))
except ValueError as e:
    print(e)

# Задание 4
#
# Пользовательское исключение
#
# Создайте свое собственное исключение с именем 'CustomException', вы можете унаследовать его от базового класса Exception, но расширить его функциональность для регистрации каждого сообщения об ошибке в файле с именем 'logs.txt'. Советы: используйте метод __init__ для расширения функциональности сохранения сообщений в файл

print(
    '''
Task 4
Custom exception
    '''
)


class CustomException(Exception):

    def __init__(self, msg):
        super().__init__(msg)
        self.log_message(msg)

    def log_message(self, msg):
        with open('logs.txt', 'a') as file:
            file.write(f"{msg}\n")


try:
    raise CustomException("Это пользовательское исключение")
except CustomException as e:
    print(f"Исключение перехвачено: {e}")
