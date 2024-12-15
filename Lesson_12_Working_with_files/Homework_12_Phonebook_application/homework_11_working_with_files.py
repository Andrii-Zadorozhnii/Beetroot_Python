import json

from Components.insert_user.add_user import add_user
from Components.show_users import show_users
from Components.update_user.update_users import update_user
from Lesson_12_Working_with_files.Homework_12_Phonebook_application.Components.delete_user.delete_user import \
    delete_user
from Lesson_12_Working_with_files.Homework_12_Phonebook_application.Components.load_users import load_user

file_name = 'Components/insert_user/phones.json'

users = load_user(file_name)
working = True
while working:

    action = input(
        'What do you want to do: Insert User(1)/Update User(2)/Delete User(3)/Search(4)/Show Users(5) or Exit?(e): ')

    if action == '1':

        add_user(users, file_name)

    elif action == '2':

        update_user(users, file_name)

    elif action == '3':

        delete_user(users, file_name)

    elif action == '4':

        def search_user(variable, filename):
            input_key = input(
                'Please write what do you want to use for search |(1)Phone Number|(2)Name|(3)Family name|(4)City|(5)Country: ')
            search_key = ''
            counter = 0

            if input_key == '1':
                search_key = 'name'
            elif input_key == '2':
                search_key = 'family name'
            elif input_key == '3':
                search_key = 'full name'
            elif input_key == '4':
                search_key = 'city'
            elif input_key == '5':
                search_key = 'country'
            else:
                print('Wrong input')

            print(search_key)

            with open(filename, 'r+', encoding='utf-8') as file:
                variable = json.load(file)

            while counter == len(variable):

                for user_number, details in variable.items():
                    a = []
                    for key, value in details.items():
                        if key == search_key:
                            a.append(f'{key.capitalize()}: {value:18}')
                    print(" | ".join(a))

                counter += 1


        search_user(users, file_name)
        print()

    elif action == '5':

        show_users(file_name, users)

    elif action == 'e':
        working = False
        print('Exiting the program.')
    else:
        print("Invalid option, please choose again.")
