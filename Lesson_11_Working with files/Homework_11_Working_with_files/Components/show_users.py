from .load_users import load_user

# Showing all users to
def show_users(file_name,variable):
    variable = load_user(file_name)
    if variable == {}:
           print(
               "No users found."
           )
    else:
            for user_number, details in variable.items():
                print(
                    f'Phone number: {user_number}'
                )
                for key, value in details.items():
                    print(
                        f'{key.capitalize()}: {value}'
                    )
                print('\n')

