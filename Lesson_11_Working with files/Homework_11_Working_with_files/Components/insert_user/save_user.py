import json

# Saving users data to Json file
def save_users(users,file_name):
    with open(file_name, 'a') as my_data_base:
        json.dump(users, my_data_base,indent=4)
