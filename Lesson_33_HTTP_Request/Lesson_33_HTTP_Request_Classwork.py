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

response = requests.get(
    'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20220115&end=20220131&valcode=usd&sort=exchangedate&order=desc&json')

print('Status-cod', response.status_code)
print('Response', response.json())

engine = create_engine('sqllite:///hr.db')
SessionLocal = sessionmaker(bing=engine)
session = SessionLocal()
