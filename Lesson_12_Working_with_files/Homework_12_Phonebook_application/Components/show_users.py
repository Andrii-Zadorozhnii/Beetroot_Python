from .load_users import load_user


# Showing all users to
def show_users(file_name, variable):
    variable = load_user(file_name)
    if variable == {}:
        print(
            "No users found."
        )
    else:
        print('\n')
        count = 1
        for user_number, details in variable.items():
            a = []
            a.append(f'{count:3}.| Phone number: {user_number:18}')
            count += 1
            for key, value in details.items():
                a.append(f'{key.capitalize()}: {value:18}')
            print(" | ".join(a))

        print('\n')
