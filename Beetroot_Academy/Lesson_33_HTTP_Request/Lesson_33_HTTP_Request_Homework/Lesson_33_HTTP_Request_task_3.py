import requests
import json
from datetime import datetime, timezone, timedelta

_API_KEY = 'fb4be141d3227cd5f949355455e38556'
city = input('Please write city: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={_API_KEY}&units=metric'

data = requests.get(url).json()


def format_time(timestamp: int, timezone_offset: int) -> str:
    return datetime.fromtimestamp(timestamp, tz=timezone.utc) + timedelta(seconds=timezone_offset)


print(
    f"\nГород: {data['name']} ({data['sys']['country']})\n"
    f"Координаты: {data['coord']['lat']}°N, {data['coord']['lon']}°E\n"
    f"Погода: {data['weather'][0]['main']} ({data['weather'][0]['description']})\n"
    f"Температура: {data['main']['temp']}°C (ощущается как {data['main']['feels_like']}°C)\n"
    f"Минимальная: {data['main']['temp_min']}°C, Максимальная: {data['main']['temp_max']}°C\n"
    f"Давление: {data['main']['pressure']} гПа (на уровне моря: {data['main']['sea_level']} гПа, на земле: {data['main']['grnd_level']} гПа)\n"
    f"Влажность: {data['main']['humidity']}%\n"
    f"Видимость: {data['visibility']} м\n"
    f"Ветер: {data['wind']['speed']} м/с, направление {data['wind']['deg']}°"
    f"Облачность: {data['clouds']['all']}%\n"
    f"Время обновления: {format_time(data['dt'], data['timezone'])}\n"
    f"Восход солнца: {format_time(data['sys']['sunrise'], data['timezone'])}\n"
    f"Закат солнца: {format_time(data['sys']['sunset'], data['timezone'])}\n"
    f"Часовой пояс: UTC{data['timezone'] // 3600:+}\n"
    f"Код ответа сервера: {data['cod']}\n"
)
