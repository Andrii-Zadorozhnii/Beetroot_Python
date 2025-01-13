# Задача 1.
#  Створити клас клієнта, з атрибутами:
# ПІБ
# рік народження
# залишок на рахунку
# місто проживання
# Створити підклас VIP-клієнта, додати дані:
# дата народження (тип str, значення по замовчуванню None)
# рівень VIP (можливі значення від 1 до 5)

# Для VIP – клієнта створити методи:
# __repr__ та __str__, в яких виведіть всі поля, але для __repr__ виведіть ще тип поля. Потестуйте ці методи після кожного з 2-х варіантів ініціалізації, що вказані нижче.
# 1-ий варіант ініціалізації, з використанням аналогічного методу батьківського класу
# 2-ий варіант ініціалізації, написати свій метод (і зрозуміти, чому зручніше використовувати батьківський :) )


class Client:
    def __init__(self, client_full_name, client_year_of_birth, client_remain_balance, client_place_of_birth):
        self.client_full_name = client_full_name
        self.client_year_of_birth = client_year_of_birth
        self.client_remain_balance = client_remain_balance
        self.client_place_of_birth = client_place_of_birth


class Vip(Client):
    def __init__(self, client_full_name, client_year_of_birth, client_remain_balance, client_place_of_birth,
                 vip_date_of_birth, vip_level):
        super().__init__(client_full_name, client_year_of_birth, client_remain_balance, client_place_of_birth)
        self.vip_date_of_birth = vip_date_of_birth
        self.vip_level = vip_level

    def __repl__(self):
        return f'Client full name is: {type(self.client_full_name)}\nClient birth date: {type(self.vip_date_of_birth)}.{type(self.client_year_of_birth)}\nClient balance {type(self.client_remain_balance)}\nClient place of birth {type(self.client_place_of_birth)}\nClient Vip level {type(self.vip_level)}\n'

    def __str__(self):
        return f'Client full name is: {self.client_full_name}\nClient birth date: {self.vip_date_of_birth}.{self.client_year_of_birth}\nClient balance {self.client_remain_balance}\nClient place of birth {self.client_place_of_birth}\nClient Vip level {self.vip_level}\n'


vip_1 = Vip('Igor Petrov Petrovich', 1992, 500, 'Kiev', 1992, 3)

print(vip_1.__repl__())
print(vip_1.__str__())


#
# Задача 1а.

# ( Розказати коротко про другий варіант ініціалізації
#         super().__init__(arg1, arg2)
#         Class_2.__init__(self, arg3, arg4)
# )


# Створіть базовий клас Person, у якого є:
#     метод __init__, що приймає ім'я та вік людини. Їх необхідно зберегти в атрибути name і age відповідно
#     метод display_person_info , який друкує інформацію в такому вигляді:
#     Person: {name}, {age}
# Потім створіть клас Company , у якого є:
#     метод __init__, що приймає назву компанії та місто її заснування. Їх необхідно зберегти в атрибути екземпляра company_name і location відповідно
#     метод display_company_info , який друкує інформацію в такому вигляді:
#     Company: {company_name}, {location}
# І наприкінці створіть клас Employee , який:
#     успадкований від класів Person і Company
#     має метод __init__, що приймає назву ім'я людини, її вік, назву компанії та місто заснування. Необхідно делегувати створення атрибутів name і age класу Person , а атрибути company_name і location має створити клас Company
# Після множинного успадкування у екземплярів класу Employee будуть доступні методи батьківських класів. Перевірте це.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        return f'Person: {self.name}, {self.age}'


class Company:
    def __init__(self, company_name, company_location):
        self.company_name = company_name
        self.company_location = company_location

    def display_company_info(self):
        return f'Company: {self.company_name}, {self.company_location}'


class Employee(Person, Company):
    def __init__(self, name, age, company_name, company_location):
        Person.__init__(self, name, age)
        Company.__init__(self, company_name, company_location)


employee_1 = Employee('Igor', 34, 'Beetroot', 'Kiev')

print(employee_1.display_person_info())
print(employee_1.display_company_info())


# Задача 2.
# Створіть класи, з одним методом, що виводить ім“я цього класу.
# Нехай клас Class_2 наслідується від класу Class_1.
# Клас 3 – від 4.
# Клас 5 – від 6 , а той в свою чергу – від 7 (додайте інший метод).
# Клас 8 наслідується від класів 2, 3, 6.
# Створіть екземпляр класу 2, запустіть його метод, чи коректно відпрацював ?
# Поміняйте порядок наслідування класу 8 на 6, 2, 3 , що змінилось.
# Викличте інший метод, з класу 7, відпрацював ? Зрозуміло чому ?
# Яка функція виводить порядок виконання класів ? (Не було в матеріалах уроку ? А загуглити ? ;) ) class.__mro__


class Class_1:

    def class_name(self):
        print(f'{self.__class__.__name__}')


class Class_2(Class_1):
    def class_name(self):
        print(f'{self.__class__.__name__}')


class Class_4:
    def class_name(self):
        print(f'{self.__class__.__name__}')


class Class_3(Class_4):
    def class_name(self):
        print(f'{self.__class__.__name__}')


class Class_7:
    def class_name(self):
        print(f'{self.__class__.__name__}')


class Class_6(Class_7):
    def class_name(self):
        print(f'{self.__class__.__name__}')


class Class_5(Class_6):
    def class_name(self):
        print(f'{self.__class__.__name__}')


class Class_8(Class_2, Class_3, Class_6):
    pass


name = Class_1()
name.class_name()
name_2 = Class_2()
name_2.class_name()
name_8 = Class_8()
print(Class_8.__mro__)
name_8.class_name()


class Class_8(Class_6, Class_2, Class_3):
    pass


print(Class_8.__mro__)


# Задача 3.
# Реалізуйте функцію, щоб виводила mro у форматі:
# A -> C -> D -> ...
class H:
    description_attr = "class H"


class G(H):
    description_attr = "class G"


class F(H):
    description_attr = "class F"


class E(H):
    description_attr = "class E"


class D(H):
    description_attr = "class D"


class C(F, G):
    description_attr = "class C"


class B(D, E):
    description_attr = "class B"


class A(B, C):
    description_attr = "class A"


def display_mro(clas):
    list_1 = [base.__name__ for base in clas.__mro__]
    list_1 = '->'.join(list_1)
    print(list_1)


display_mro(C)

# Задача 4.
# Розсташуйте класи в порядку mro вручну, потім перевірте з допомогою функції mro.

display_mro(A)

display_mro(D)

print(A().description_attr)
print(B().description_attr)
print(C().description_attr)
print(D().description_attr)
print(E().description_attr)
print(F().description_attr)
print(G().description_attr)
