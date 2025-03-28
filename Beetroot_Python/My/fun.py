import asyncio
import aiohttp
import random


async def fetch_exchange_rate() -> float:
    """
    Получает курс обмена RON -> UAH из API.

    :return: Курс обмена (сколько UAH за 1 RON)
    """
    url = "https://api.exchangerate-api.com/v4/latest/RON"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data["rates"]["UAH"]  # Достаём курс RON -> UAH


async def calculate_price() -> float:
    """
    Вычисляет цену колес самоката в гривнах.

    :return: Цена колес в UAH
    """
    price_ron = 175  # Цена в леях

    exchange_rate = await fetch_exchange_rate()
    price_uah = price_ron * exchange_rate

    print(
        "Цена колес самоката в гривнах:", round(price_uah, 2)
    )

    return price_uah


async def calculate_wear_rate() -> None:
    """
    Рассчитывает износостойкость колес самоката.
    """
    total_distance = 5000  # Замена каждые 5000 км
    avg_speed = random.randint(40, 50)  # Случайная скорость в диапазоне 40-50 км/ч

    hours_until_replacement = total_distance / avg_speed  # Часы до замены

    print(
        "📌 Средняя скорость:", avg_speed, "км/ч"
    )
    print(
        "⌛ Можно кататься примерно", round(hours_until_replacement, 2), "часов до замены колес."
    )
    print(
        "🚲 Максимальный пробег без замены:", total_distance, "км"
    )


async def main():
    """
    Главная асинхронная функция: рассчитывает цену и износостойкость.
    """
    await calculate_price()
    await calculate_wear_rate()


# Запуск асинхронной задачи
asyncio.run(main())
