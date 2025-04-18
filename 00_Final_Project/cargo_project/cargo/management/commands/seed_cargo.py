from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, datetime
import random
import uuid

from cargo.models import Cargo, Company, User

class Command(BaseCommand):
    help = 'Створює фейкові вантажі для періоду з 01.02.2025 по сьогодні'

    def handle(self, *args, **kwargs):
        # Встановлюємо дати для періоду з 01.02.2025 по сьогодні
        start_date = datetime(2025, 2, 1).date()
        end_date = timezone.now().date()

        cities = [
            'Київ', 'Харків', 'Одеса', 'Дніпро', 'Львів',
            'Запоріжжя', 'Кривий Ріг', 'Миколаїв', 'Вінниця',
            'Херсон', 'Полтава', 'Чернігів', 'Черкаси', 'Житомир',
            'Суми', 'Івано-Франківськ', 'Тернопіль', 'Ужгород', 'Луцьк'
        ]

        cargo_names = [
            'Зерно', 'Вугілля', 'Металопрокат', 'Деревина', 'Цемент', 'Картопля',
            'Яблука', 'Молочні продукти', 'Побутова техніка', 'Будматеріали',
            'Сільгосптехніка', 'Газоблоки', 'Соя', 'Олія', 'Удобрення'
        ]

        # Вибір користувача та компанії
        try:
            user = User.objects.first()
            company = Company.objects.first()
        except:
            self.stdout.write(self.style.ERROR("Не знайдено користувача або компанії"))
            return

        total_inserted = 0
        current_date = start_date

        while current_date <= end_date:
            num_rows = random.randint(20, 50)  # Випадкове число вантажів

            for _ in range(num_rows):
                origin = random.choice(cities)
                destination = random.choice([c for c in cities if c != origin])
                name = random.choice(cargo_names)

                # Генерація телефону та часу
                phone = f"+380{random.randint(100000000, 999999999)}"

                # Генерація випадкової дати та часу для кожного вантажу
                created_at = datetime.combine(current_date, datetime.min.time()) + timedelta(
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59)
                )

                # Створення вантажу
                Cargo.objects.create(
                    name=name,
                    origin=origin,
                    destination=destination,
                    distance=f"{random.randint(100, 900)} км",
                    duration=f"{random.randint(1, 12)} год",
                    description=f"Перевезення {origin} → {destination}",
                    shipment_id=str(uuid.uuid4())[:12],
                    company=company,
                    phone=phone,
                    payment=round(random.uniform(300, 1000), 2),
                    user=user,
                    created_at=created_at
                )
                total_inserted += 1

            current_date += timedelta(days=1)

        self.stdout.write(self.style.SUCCESS(f"Успішно додано {total_inserted} вантажів для періоду з 01.02.2025 по сьогодні!"))