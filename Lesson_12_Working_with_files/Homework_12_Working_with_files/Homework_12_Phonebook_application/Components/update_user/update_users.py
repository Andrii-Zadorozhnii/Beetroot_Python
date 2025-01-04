import json
from ..insert_user.add_user import add_user


def update_user(variable, file_name):
    phone_number = input('Please write a phone number for change data: ')
    key = (input('Please write a data(name/family name/city/country) that you want change data: ')).lower()
    new_data = input(f'Please write a new data for {key}: ')
    # Open file for reading
    with open(file_name, 'r+', encoding='utf-8') as file:
        variable = json.load(file)

    if phone_number in variable:
        variable[phone_number][key] = new_data

        # Open the file again for writing
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(variable, file, indent=4)

        print('User data updated successfully')
    else:
        answer = input('No current user in list, do you want to add? (y/n)')
        if answer == 'y':
            try:
                add_user(variable, file_name)
            except Exception:
                print('Input User Error')
        else:
            print("We will come back to the main menu...")
