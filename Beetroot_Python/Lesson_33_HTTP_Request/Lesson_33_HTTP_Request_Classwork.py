# Через API сайту Нацбанку України потрібно отримати курси іноземних валют (долар, євро, фунт) до гривні з початку поточного року.
# Деталі:
# - для доступу до API використовуйте бібліотеку requests
# - для збереження результатів створіть в базі даних hr (додатковий матеріал до уроків з SQL) дві таблиці. Одна — з полями
# ’code’ (integer(3),
# primary key),
# ’currency’ (varchar(20))
# , де в першому полі знаходиться код валюти (для долара — 840 і т.д), в другому — назва валюти.
# В другій таблиці поля id (integer(3), primary key), date (date), value (тип вибрати відповідно до того, як зберігаються дані на сайті Нацбанку), код валюти. Перша таблиця з другою з’єднана відношенням один-до-багатьох по полю code.
# - збережіть дані з сайту в новостворені таблиці в БД
# - виведіть середнє значення курсу по кожній валюті, використовуючи group by
# - виведіть графік курсу валют (використовуючи відповідну бібліотеку, з допомогою якої раніше малювали фігури)
# - постарайтесь всі завдання виконати суто з python (в т.ч. операції з БД)

import requests
from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timedelta
import time

engine = create_engine(
    'sqlite:////Users/andriizadorozhnii/Documents/Beetroot_Python/Lesson_29_SQL/Lesson_29_Homework/hr.db')
Base = declarative_base()


class Currency(Base):
    __tablename__ = 'currencies'
    code = Column(Integer, primary_key=True)
    currency = Column(String, nullable=False)


class CurrencyRate(Base):
    __tablename__ = 'currency_rates'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)
    currency_code = Column(Integer, nullable=False)


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

currencies_data = [
    {"code": 840, "currency": "USD"},
    {"code": 978, "currency": "EUR"},
    {"code": 826, "currency": "GBP"}
]

for currency in currencies_data:
    existing_currency = session.query(Currency).filter(Currency.code == currency['code']).first()
    if not existing_currency:
        new_currency = Currency(code=currency['code'], currency=currency['currency'])
        session.add(new_currency)

try:
    session.commit()
except Exception as e:
    print(f"Ошибка при сохранении данных: {e}")
    session.rollback()


def fetch_currency_rates(start_date, end_date, valcode):
    all_rates = []
    current_date = start_date
    while current_date <= end_date:
        url = f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={current_date.strftime("%Y%m%d")}&end={current_date.strftime("%Y%m%d")}&valcode={valcode}&sort=exchangedate&order=desc&json'

        retries = 3
        for _ in range(retries):
            try:
                response = requests.get(url, timeout=10)
                print(f"Запит до API для {current_date}: Статус код: {response.status_code}")  # Перевіряємо статус код
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        print(f"Отримані дані для {current_date}: {data}")  # Перевіряємо отримані дані
                        for rate in data:
                            rate_date = datetime.strptime(rate['exchangedate'], "%Y%m%d")
                            rate_value = rate['rate']
                            all_rates.append({
                                'date': rate_date,
                                'value': rate_value,
                                'currency_code': valcode
                            })
                    else:
                        print(f"Немає даних для {current_date}")
                    break  # Если запрос успешный, выходим из цикла
            except (requests.exceptions.RequestException, requests.exceptions.JSONDecodeError) as e:
                print(f"Ошибка при запросе для {current_date}: {e}")
                time.sleep(5)  # Задержка перед повторной попыткой

        current_date += timedelta(days=1)

    return all_rates


start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 1, 26)

for currency in currencies_data:
    rates = fetch_currency_rates(start_date, end_date, currency['code'])

    for rate in rates:
        new_rate = CurrencyRate(
            date=rate['date'],
            value=rate['value'],
            currency_code=rate['currency_code']
        )
        session.add(new_rate)

try:
    session.commit()
except Exception as e:
    print(f"Ошибка при сохранении данных: {e}")
    session.rollback()

print("Данные о курсах валют успешно сохранены в БД!")

session.close()
