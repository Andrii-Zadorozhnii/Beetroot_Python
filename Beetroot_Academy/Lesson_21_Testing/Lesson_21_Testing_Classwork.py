class BankClient:
    clients_number = 0

    def __init__(self, last_name, name, middle_name, age, avg_salary, location='Київ', current_debt=0):
        self.last_name = last_name
        self.name = name
        self.middle_name = middle_name
        self.age = age
        self.avg_salary = avg_salary
        self.location = location
        self.current_debt = current_debt
        BankClient.clients_number += 1

    def change_salary(self, salary):
        self.avg_salary = salary

    def change_debt(self, debt):
        self.current_debt = debt

    def print_clients_number(self):
        print(f'clients_number = {BankClient.clients_number}')

    def print_type_id(self):
        print(f'type_id {type(self)} {id(self)}')

    def compare(self, another_object):
        return self.__dict__ == another_object.__dict__
