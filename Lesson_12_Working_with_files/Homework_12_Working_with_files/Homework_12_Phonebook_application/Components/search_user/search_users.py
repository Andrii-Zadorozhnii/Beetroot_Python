from Lesson_12_Working_with_files.Homework_12_Working_with_files.Homework_12_Phonebook_application.Components.working_with_files.open_read_file import \
    open_read_file


def search_user(variable, filename):
    input_key = input(
        'Please write what do you want to use for search |(1)Phone Number|(2)Name|(3)Family name|(4)Full Name|(5)City|(6)Country: ')

    search_data = input('Please write what do you search: ')

    if input_key == '1':

        try:
            open_read_file(filename)

            # with open(filename, 'r+', encoding='utf-8') as file:
            #     variable = json.load(file)
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
            open_read_file(filename)
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
            open_read_file(filename)
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
            open_read_file(filename)
            for user_number, details in variable.items():
                family_name = f'{details['name'].lower()} {details['family name'].lower()}'
                if family_name == search_data.lower():
                    a = []
                    a.append(f'Phone number: {user_number:15}')
                    for key, value in details.items():
                        a.append(f'{key:8}: {value:15}')

                    print(' | '.join(a))
        except Exception:
            print('Some Error')
    elif input_key == '5':
        try:
            open_read_file(filename)
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
            open_read_file(filename)
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
