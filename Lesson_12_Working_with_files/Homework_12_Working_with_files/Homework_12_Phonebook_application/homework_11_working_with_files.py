import json
# import sys
# import os

from Components.insert_user.add_user import add_user
from Components.search_user.search_users import search_user
from Components.show_users import show_users
from Components.update_user.update_users import update_user
from Components.delete_user.delete_user import delete_user
from Components.load_users import load_user

# Extend Phonebook application
#
# Functionality of Phonebook application:
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
#
# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application, else raise an error.
# After the user exits, all data should be saved to loaded JSON.

print(
    '\t_____Task 2 Phonebook_____\n'
)

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# if len(sys.argv) != 2:
#     print("Usage: python my_script_file.py my_data_base.json")
#     sys.exit(1)

file_name = 'Data_base/data_base.json'
# file_name = sys.argv[1]

users = load_user(file_name)
working = True
while working:
    try:
        action = input(
            'What do you want to do: (1)Insert User/(2)Update User/(3)Delete User/(4)Search/(5)Show Users or (e)Exit?: ')

        if action == '1':

            add_user(users, file_name)

        elif action == '2':

            update_user(users, file_name)

        elif action == '3':

            delete_user(users, file_name)

        elif action == '4':

            search_user(users, file_name)

        elif action == '5':

            show_users(file_name, users)

        elif action == 'e':
            working = False
            print('Exiting the program.')
        else:
            print("Invalid option, please choose again.")
    except Exception:
        print('Some Error, try again...')
