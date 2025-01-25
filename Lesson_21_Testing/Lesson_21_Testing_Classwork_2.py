import unittest
from Lesson_21_Testing_Classwork import *


class BankClientTestCase(unittest.TestCase):

    def setUp(self):
        self.client = BankClient('Petrenko', 'Ivan', 'Ivanovych', 35, 36000)
        self.another_client = BankClient('Shevchenko', 'Taras', 'Hryhorovych', 45, 50000, current_debt=15000)

    def test_initialization(self):
        self.assertEqual(self.client.last_name, 'Petrenko')
        self.assertEqual(self.client.name, 'Ivan')
        self.assertEqual(self.client.middle_name, 'Ivanovych')
        self.assertEqual(self.client.age, 35)
        self.assertEqual(self.client.avg_salary, 36000)
        self.assertEqual(self.client.location, 'Київ')
        self.assertEqual(self.client.current_debt, 0)
        self.assertEqual(BankClient.clients_number, 2)

    def test_change_salary(self):
        self.client.change_salary(40000)
        self.assertEqual(self.client.avg_salary, 40000)

    def test_change_debt(self):
        self.client.change_debt(5000)
        self.assertEqual(self.client.current_debt, 5000)

    def test_compare_clients(self):
        self.another_client.last_name = 'Petrenko'
        self.another_client.name = 'Ivan'
        self.another_client.middle_name = 'Ivanovych'
        self.another_client.age = 35
        self.another_client.avg_salary = 36000
        self.another_client.current_debt = 0
        self.another_client.location = 'Київ'
        self.assertTrue(self.client.compare(self.another_client))

        self.another_client.change_salary(50000)
        self.assertFalse(self.client.compare(self.another_client))

    def test_clients_number(self):
        initial_clients = BankClient.clients_number
        new_client = BankClient('Petrenko', 'Ivan', 'Ivanovych', 35, 36000)
        self.assertEqual(BankClient.clients_number, initial_clients + 1)

    def test_print_clients_number(self):
        with self.assertLogs(level='INFO') as log:
            self.client.print_clients_number()
            self.assertIn('clients_number = 2', log.output[0])

    def test_print_type_id(self):
        with self.assertLogs(level='INFO') as log:
            self.client.print_type_id()
            self.assertIn(f'type_id <class', log.output[0])

    #     Крайний сценарий

    def test_min_value(self):
        client = BankClient('', '', '', 0, 0, current_debt=0)
        self.assertEqual(client.last_name, '')
        self.assertEqual(client.name, '')
        self.assertEqual(client.middle_name, '')
        self.assertEqual(client.age, 0)
        self.assertEqual(client.avg_salary, 0)
        self.assertEqual(client.current_debt, 0)

    def test_max_value(self):
        client = BankClient("A" * 1000, "B" * 1000, "C" * 1000, 1e9, 1e9, current_debt=1e9)
        self.assertEqual(client.age, 1e9)
        self.assertEqual(client.avg_salary, 1e9)
        self.assertEqual(client.current_debt, 1e9)


if __name__ == "__main__":
    unittest.main()
