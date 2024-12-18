import json

from Lesson_12_Working_with_files.Homework_12_Phonebook_application.Components.insert_user.add_user import add_user
from Lesson_12_Working_with_files.Homework_12_Phonebook_application.Components.show_users import show_users
from Lesson_12_Working_with_files.Homework_12_Phonebook_application.Components.update_user.update_users import \
    update_user
from Lesson_12_Working_with_files.Homework_12_Phonebook_application.Components.delete_user.delete_user import \
    delete_user
from Lesson_12_Working_with_files.Homework_12_Phonebook_application.Components.load_users import load_user

file_name = 'Data_base/data_base.json'

users = load_user(file_name)
working = True
while working:

    action = input(
        'What do you want to do: (1)Insert User/(2)Update User/(3)Delete User/(4)Search/(5)Show Users or (e)Exit?: ')

    if action == '1':

        add_user(users, file_name)

    elif action == '2':

        update_user(users, file_name)

    elif action == '3':

        delete_user(users, file_name)

    elif action == '4':

        def search_user(variable, filename):
            input_key = input(
                'Please write what do you want to use for search |(1)Phone Number|(2)Name|(3)Family name|(4)Full Name|(5)City|(6)Country: ')

            search_data = input('Please write what do you search: ')

            if input_key == '1':

                try:
                    with open(filename, 'r+', encoding='utf-8') as file:
                        variable = json.load(file)
                        for user_number, details in variable.items():
                            if user_number == search_data:
                                a = []
                                a.append(f'{user_number}{details}')
                                print(' | '.join(a))  # need to make better looking
                            else:
                                print('No current phone number in data base')
                except Exception:
                    print('some Error')

            elif input_key == '2':

                try:
                    with open(filename, 'r+', encoding='utf-8') as file:
                        variable = json.load(file)
                        for user_number, details in variable.items():
                            if details['name'].lower() == search_data.lower():
                                a = []
                                a.append(f'Phone number: {user_number:15}')
                                for key, value in details.items():
                                    a.append(f'{key:8}: {value:15}')

                                print(' | '.join(a))
                except Exception:
                    print('Some Error')

            elif input_key == '3':

                try:
                    with open(filename, 'r+', encoding='utf-8') as file:
                        variable = json.load(file)
                        for user_number, details in variable.items():
                            if details['family name'].lower() == search_data.lower():
                                a = []
                                a.append(f'Phone number: {user_number:15}')
                                for key, value in details.items():
                                    a.append(f'{key:8}: {value:15}')
                                print(' | '.join(a))
                except Exception:
                    print('Some Error')

            elif input_key == '4':
                try:
                    with open(filename, 'r+', encoding='utf-8') as file:
                        variable = json.load(file)
                        for user_number, details in variable.items():
                            if (
                            f'{details['name'].lower()}+" "+ {details['family name'].lower()}') == search_data.lower():
                                a = []
                                a.append(f'Phone number: {user_number:15}')
                                for key, value in details.items():
                                    a.append(f'{key:8}: {value:15}')

                                print(' | '.join(a))
                except Exception:
                    print('Some Error')
            elif input_key == '5':
                try:
                    with open(filename, 'r+', encoding='utf-8') as file:
                        variable = json.load(file)
                        for user_number, details in variable.items():
                            if details['user city'].lower() == search_data.lower():
                                a = []
                                a.append(f'Phone number: {user_number:15}')
                                for key, value in details.items():
                                    a.append(f'{key:8}: {value:15}')

                                print(' | '.join(a))
                except Exception:
                    print('Some Error')
            elif input_key == '6':

                try:
                    with open(filename, 'r+', encoding='utf-8') as file:
                        variable = json.load(file)
                        counter = 1
                        for user_number, details in variable.items():
                            if details['user country'].lower() == search_data.lower():
                                a = []

                                a.append(f'{counter}.Phone number: {user_number:15}')
                                for key, value in details.items():
                                    a.append(f'{key:8}: {value:15}')

                                print(' | '.join(a))
                        counter += 1
                except Exception:
                    print('Some Error')
                search_key = 'country'
            else:
                print('Wrong input')


        search_user(users, file_name)
        print()

    elif action == '5':

        show_users(file_name, users)

    elif action == 'e':
        working = False
        print('Exiting the program.')
    else:
        print("Invalid option, please choose again.")
