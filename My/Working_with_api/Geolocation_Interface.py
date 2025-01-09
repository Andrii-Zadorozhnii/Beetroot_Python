
import requests
import tkinter as tk

# Функция для получения геолокации
def get_location():
    api_url = "http://ip-api.com/json/"

    try:
        # Отправляем запрос к API
        response = requests.get(api_url)
        response.raise_for_status()  # Проверяем статус ответа

        # Разбираем ответ
        data = response.json()
        if data["status"] == "success":
            latitude = data["lat"]
            longitude = data["lon"]
            city = data["city"]
            country = data["country"]
            location_info = f"Город: {city}\nСтрана: {country}\nШирота: {latitude}\nДолгота: {longitude}"
        else:
            location_info = "Не удалось определить местоположение."
    except requests.exceptions.RequestException as e:
        location_info = f"Ошибка при запросе: {e}"

    # Обновляем текст в поле
    location_label.config(text=location_info)

# Создаем основное окно
root = tk.Tk()
root.title("Геолокация пользователя")

# Размеры окна
root.geometry("400x300")

# Кнопка для получения геолокации
location_button = tk.Button(root, text="Получить Геолокацию", command=get_location)
location_button.pack(pady=20)

# Место для отображения результата
location_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
location_label.pack(pady=20)

# Запуск интерфейса
root.mainloop()
