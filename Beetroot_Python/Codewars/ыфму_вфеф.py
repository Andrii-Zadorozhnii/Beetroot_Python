import json
import os

# Имя файла для хранения данных
FILE_NAME = "user_data.json"

def load_data():
    """Считывает данные из файла, если он существует, иначе возвращает пустой словарь."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}  # Если файл поврежден, вернуть пустой словарь
    return {}

def save_data(data):
    """Сохраняет данные в файл."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def main():
    # Загрузка существующих данных
    data = load_data()

    # Проверка, есть ли уже сохраненные данные
    if "user_input" in data:
        print(f"Сохраненные данные: {data['user_input']}")
        use_old = input("Хотите использовать сохраненные данные? (да/нет): ").strip().lower()
        if use_old == "да":
            print("Используем сохраненные данные.")
        else:
            new_data = input("Введите новую информацию: ").strip()
            data["user_input"] = new_data
            save_data(data)
            print("Новые данные сохранены.")
    else:
        # Если данных нет, запросить их у пользователя
        user_input = input("Введите информацию для сохранения: ").strip()
        data["user_input"] = user_input
        save_data(data)
        print("Данные сохранены.")

if __name__ == "__main__":
    main()