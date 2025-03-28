
def user_data(variable,user_number, user_name, user_family_name, user_city, user_country):

    try:
        variable[user_number] = {'name': user_name,
                          'family name': user_family_name,
                          'user city': user_city,
                          'user country': user_country}
    except Exception:
        print('Some Error')