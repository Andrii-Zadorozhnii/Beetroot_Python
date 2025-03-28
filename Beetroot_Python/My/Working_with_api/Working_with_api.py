import requests
import pytz
import tkinter as tk
from datetime import datetime

from Api import open_weather_api as API
from Api import open_weather_base_url as BASE_URL

# Переменная для отслеживания количества запросов
request_count = 0


# Функция для преобразования метки времени в формат hh:mm
def convert_time(timestamp, timezone_offset):
    # Используем часовой пояс UTC
    utc_zone = pytz.utc
    # Создаем объект времени в UTC
    utc_time = datetime.fromtimestamp(timestamp, utc_zone)

    # Применяем сдвиг по часовому поясу
    local_time = utc_time.astimezone(
        pytz.FixedOffset(timezone_offset // 60))  # Переводим в местный часовой пояс

    return local_time.strftime('%H:%M')


# Функция для получения геолокации
def get_location():
    global city, request_count
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
            # Увеличиваем счетчик запросов
            request_count += 1
            update_request_count()
        else:
            location_label.config(text="Не удалось определить местоположение.")
    except requests.exceptions.RequestException as e:
        location_label.config(text=f"Ошибка при запросе: {e}")


# Функция для получения данных о погоде
def get_weather():
    global city, request_count
    if city:
        params = {
            'q': city,
            'appid': API,
            'units': 'metric',
            'lang': 'ru'
        }

        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            weather_data = response.json()

            sunrise_time = convert_time(weather_data['sys']['sunrise'], weather_data['timezone'])
            sunset_time = convert_time(weather_data['sys']['sunset'], weather_data['timezone'])
            real_feeling = (
                f"{(weather_data['main']['feels_like']):.1f}°C"
            )
            real_feeling_label.config(text=real_feeling)
            weather_info = (
                f"Город: {weather_data['name']}\n"
                f"Координаты: {weather_data['coord']['lat']:.2f} / {weather_data['coord']['lon']:.2f}\n"
                f"Погода: {weather_data['weather'][0]['main']}\n"
                f"Облачность: {weather_data['clouds']['all']}%\n"
                f"Максимальная температура: {weather_data['main']['temp_max']}°C\n"
                f"Минимальная температура: {weather_data['main']['temp_min']}°C\n"
                f"Текущая температура: {weather_data['main']['temp']}°C\n"
                f"Давление: {weather_data['main']['pressure']} hPa\n"
                f"Влажность: {weather_data['main']['humidity']}%\n"
                f"Видимость: {weather_data['visibility'] / 1000:.2f} км\n"
                f"Скорость ветра: {weather_data['wind']['speed']} м/с\n"
                f"Скорость ветра: {weather_data['wind']['deg']}°\n"
                f"Восход солнца: {sunrise_time}\n"
                f"Закат солнца: {sunset_time}\n"
                f"Часовой пояс: {weather_data['timezone'] / 3600:.0f} часов от UTC"
            )
            weather_label.config(text=weather_info)

            # Увеличиваем счетчик запросов
            request_count += 1
            update_request_count()
        except requests.exceptions.RequestException as e:
            weather_label.config(text=f"Ошибка при запросе погоды: {e}")
    else:
        weather_label.config(text="Город не определён, запрос погоды невозможен.")


# Функция для обновления времени в реальном времени
def update_clock():
    current_time = datetime.now().strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)  # Обновляем время каждую секунду


# Функция для обновления данных
def update_data():
    get_location()  # Получаем геолокацию
    get_weather()  # Получаем погоду
    root.after(300000, update_data)  # Обновляем данные каждые 5 минут (300000 миллисекунд)


# Функция для обновления информации о количестве запросов
def update_request_count():
    request_count_label.config(text=f"Количество запросов: {request_count}")


# Создаем основное окно
root = tk.Tk()
root.title("Погода и Геолокация")

# Размеры окна
root.geometry("400x500")

root.attributes("-fullscreen", True)

# Место для отображения времени
clock_label = tk.Label(root, text="", font=("Arial", 160), fg="Green")
clock_label.pack(pady=10)

# Место для отображения информации о запросах
request_count_label = tk.Label(root, text="Количество запросов: 0", font=("Arial", 20))
request_count_label.pack(pady=10)

# Место для отображения информации о погоде

real_feeling_label = tk.Label(root, text="", justify="left", font=("Arial", 200))
real_feeling_label.pack(pady=0)

weather_label = tk.Label(root, text="", justify="left", font=("Arial", 25))
weather_label.pack(pady=10)

# Запуск обновления данных и времени
update_clock()
update_data()

# Запуск интерфейса
root.mainloop()
