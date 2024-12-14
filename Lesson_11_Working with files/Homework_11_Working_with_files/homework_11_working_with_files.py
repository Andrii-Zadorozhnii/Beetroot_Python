import json

users = {}
working = True

def user_data(user_number, user_name, user_family_name, user_city, user_country):
    users[user_number] = {'name': user_name, 'family name': user_family_name, 'user_city': user_city,
                          'user_country': user_country}



def save_users():
    with open('phones.json', 'w') as my_data_base:
        json.dump(users, my_data_base,indent=4)

while working:
    action = input('What do you want to do: Insert User(1)/Update User(2)/Delete User(3)/Search(4) or Exit?(e): ')

    if action == '1':
        number = input("Enter the user's number: ")
        user_name = input("Enter the user's first name: ")
        family_name = input("Enter the user's last name: ")
        user_city = input("Enter the user's city: ")
        user_country = input("Enter the user's country: ")

        user_data(number,user_name,family_name,user_city,user_country)

        save_users()

        print("User inserted and data saved.")

    elif action == '2':
        print('Update functionality goes here.')
    elif action == '3':
        print('Delete functionality goes here.')
    elif action == '4':
        print('Search functionality goes here.')
    elif action == 'e':
        working = False
        print('Exiting the program.')
    else:
        print("Invalid option, please choose again.")