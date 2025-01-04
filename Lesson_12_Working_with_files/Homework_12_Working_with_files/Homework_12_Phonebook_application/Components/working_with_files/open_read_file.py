import json


def open_read_file(file_name):
    try:
        with open(file_name, 'r+', encoding='utf-8') as file:
            variable = json.load(file)
            return variable
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
