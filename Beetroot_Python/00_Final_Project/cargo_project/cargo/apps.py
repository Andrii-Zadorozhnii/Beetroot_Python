from django.apps import AppConfig
import threading
# from cargo.runbot import run_bot


class CargoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cargo'

    # def ready(self):
    #     """Запускаем бота в отдельном потоке при старте Django"""
    #     from django.conf import settings
    #     if settings.DEBUG:  # Только в режиме разработки, убери при деплое
    #         threading.Thread(target=run_bot, daemon=True).start()
