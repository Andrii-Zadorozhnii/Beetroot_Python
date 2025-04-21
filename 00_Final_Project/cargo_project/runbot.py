import os
import django
import asyncio
import sys

# Добавляем путь к проекту в PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cargo_project.settings')
django.setup()

from bot.main import main

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually")
    except Exception as e:
        print(f"Critical error: {e}")