import json
from importlib.resources import files

from Components.load_users import load_user
from Components.insert_user.add_user import add_user
from Components.show_users import show_users



file_name = 'Components/insert_user/phones.json'

users = load_user(file_name)
working = True

print(users)





while working:

    action = input('What do you want to do: Insert User(1)/Update User(2)/Delete User(3)/Search(4)/Show Users(5) or Exit?(e): ')
    phone_number = input('Please write a phone number for change data: ')
    if action == '1':
        try:
            add_user(users,file_name)
        except Exception:
            print('Input User Error')


    elif action == '2':
        key = input('Please write a data(name/family name/city/country) that you want change data: ')
        new_data = input(f'Please write a new data for {key}: ')
        def update_user(file_name, phone_number,key,new_data):
            global users
            with open(file_name, 'r+', encoding='utf-8') as file:
                users = dict(json.load(file_name))

            if phone_number in users:

                users[phone_number][key] = new_data
                file.seek(0)
                json.dump(users,file, indent=4)

                update_user(file_name, phone_number, key, new_data)

                print('User data updated successfully')
            else:
                answer = input('No current user in list, do you want to add? (y/n)')
                if answer == 'y':
                    try:
                        add_user(users, file_name)
                    except Exception:
                        print('Input User Error')
                else:
                    print("We will come back you to main menu...")

        update_user(file_name, phone_number,key,new_data)


    elif action == '3':
        print('')
    elif action == '4':
        print('')
    elif action == '5':
        show_users(file_name,users)
    elif action == 'e':
        working = False
        print('Exiting the program.')
    else:
        print("Invalid option, please choose again.")