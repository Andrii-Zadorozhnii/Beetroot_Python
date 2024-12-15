import json


def load_user(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as my_data_base:
            return json.load(my_data_base)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return {}
