import json


def open_write_file(variable, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(variable, file, indent=4)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
