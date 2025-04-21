from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, datetime
import random
import uuid

from cargo.models import Cargo, Company, User, Manager


class Command(BaseCommand):
    help = 'Створює фейкові вантажі для періоду з 01.02.2025 по сьогодні'

    def handle(self, *args, **kwargs):
        start_date = datetime(2025, 2, 1).date()
        end_date = timezone.now().date()

        cities = [
            'Київ, Київська область, Україна',
            'Харків, Харківська область, Україна',
            'Одеса, Одеська область, Україна',
            'Дніпро, Дніпропетровська область, Україна',
            'Львів, Львівська область, Україна',
            'Запоріжжя, Запорізька область, Україна',
            'Кривий Ріг, Дніпропетровська область, Україна',
            'Миколаїв, Миколаївська область, Україна',
            'Вінниця, Вінницька область, Україна',
            'Херсон, Херсонська область, Україна',
            'Полтава, Полтавська область, Україна',
            'Чернігів, Чернігівська область, Україна',
            'Черкаси, Черкаська область, Україна',
            'Житомир, Житомирська область, Україна',
            'Суми, Сумська область, Україна',
            'Івано-Франківськ, Івано-Франківська область, Україна',
            'Тернопіль, Тернопільська область, Україна',
            'Ужгород, Закарпатська область, Україна',
            'Луцьк, Волинська область, Україна'
        ]

        cargo_names = [
            'Зерно', 'Вугілля', 'Металопрокат', 'Деревина', 'Цемент', 'Картопля',
            'Яблука', 'Молочні продукти', 'Побутова техніка', 'Будматеріали',
            'Сільгосптехніка', 'Газоблоки', 'Соя', 'Олія', 'Удобрення'
        ]

        trucks = [
            'Тентований',
            'Мега_трейлер',
            'Jumbo',
            'Рефрижератор',
            'Ізотермічний',
            'Відкритий',
            'Низькорамний',
            'Контейнеровоз (20 футів)',
            'Контейнеровоз (40 футів)',
            'Контейнерна платформа',
            'Зерновоз',
            'Самоскид',
            'Рухома_підлога',
            'Цистерна',
            'Цистерна для хімікатів',
            'Цистерна для пального',
            'Цистерна харчова',
            'Причіп для тварин',
            'Лісовоз',
            'Автовоз',
            'Караван',
            'Платформа',
            'Модульний трал'
        ]

        currencies = [
            'UAH', 'USD', 'EUR', 'PLN', 'GBP', 'CHF', 'CZK',
            'HUF', 'RON', 'TRY', 'CNY', 'JPY', 'CAD', 'AUD',
            'MDL', 'RSD', 'NOK', 'SEK', 'DKK'
        ]

        payment_methods = [
            'На картку',
            'Готівкою',
            'Банківський переказ',
            'Післяплата',
            'По рахунку',
            'Онлайн_гаманець',
            'Криптовалюта',
            'Термінал',
            'Акредитив',
            'Бартер',
            'Банківський чек',
            'Мобільна оплата'
        ]

        try:
            user = User.objects.first()
            company = Company.objects.first()
            # Try to get manager data if exists
            try:
                manager = Manager.objects.get(user=user)
                manager_phone = manager.manager_phone
            except Manager.DoesNotExist:
                manager_phone = f"+380{random.randint(100000000, 999999999)}"
        except:
            self.stdout.write(self.style.ERROR("Не знайдено користувача або компанії"))
            return

        total_inserted = 0
        current_date = start_date

        while current_date <= end_date:
            num_rows = random.randint(20, 50)

            for _ in range(num_rows):
                origin = random.choice(cities)
                destination = random.choice([c for c in cities if c != origin])
                name = random.choice(cargo_names)

                created_at = datetime.combine(current_date, datetime.min.time()) + timedelta(
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59)
                )

                cargo = Cargo(
                    name=name,
                    origin=origin,
                    destination=destination,
                    distance=f"{random.randint(100, 900)} км",
                    duration=f"{random.randint(1, 12)} год",
                    description=f"Перевезення {origin} → {destination}",
                    company=company,
                    phone=manager_phone,
                    payment=round(random.uniform(300, 1000), 2),
                    truck=random.choice(trucks),
                    currency=random.choice(currencies),
                    payment_method=random.choice(payment_methods),
                    user=user,
                    created_at=created_at
                )

                # Let the model handle shipment_id generation in save()
                cargo.save()
                total_inserted += 1

            current_date += timedelta(days=1)

        self.stdout.write(self.style.SUCCESS(
            f"Успішно додано {total_inserted} вантажів для періоду з 01.02.2025 по {end_date.strftime('%d.%m.%Y')}!"
        ))