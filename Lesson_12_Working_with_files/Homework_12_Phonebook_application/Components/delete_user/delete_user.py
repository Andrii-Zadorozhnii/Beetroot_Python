import json


def delete_user(variable, filename):
    deleting_number = input('Please write here phone number for delete it from data base: ')

    with open(filename, 'r+', encoding='utf-8') as file:
        variable = json.load(file)
    if deleting_number in variable:
        del variable[deleting_number]

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(variable, file, indent=4)

        print('User deleted successfully')
    else:
        print('No current user in the data base')
