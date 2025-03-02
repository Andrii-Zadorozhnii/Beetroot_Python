# Импортируем необходимые модули
from typing import Annotated  # Используется для аннотации зависимостей FastAPI

from fastapi import FastAPI, Depends  # FastAPI - основной фреймворк, Depends - для внедрения зависимостей
import uvicorn  # Запускает сервер ASGI
from sqlalchemy.ext.asyncio import (  # Импортируем модули для работы с асинхронной БД
    create_async_engine,  # Создаёт асинхронный движок SQLAlchemy
    async_sessionmaker,  # Фабрика для создания асинхронных сессий
    AsyncSession,  # Тип асинхронной сессии
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # Импорты для описания моделей
from pydantic import BaseModel  # Базовая модель для валидации входных данных
from sqlalchemy import select  # Функция для выполнения SQL-запросов

# Создаём экземпляр FastAPI
app = FastAPI()

# 1. Настройка базы данных

# Создаём асинхронный движок для работы с SQLite
# SQLite поддерживает асинхронные операции через `aiosqlite`
engine = create_async_engine('sqlite+aiosqlite:///books.db')

# Создаём фабрику сессий
# `expire_on_commit=False` означает, что объекты не будут "протухать" после коммита
new_session = async_sessionmaker(engine, expire_on_commit=False)

# Функция получения сессии, используется в качестве зависимости
async def get_session():
    async with new_session() as session:  # Создаём новую сессию
        yield session  # Передаём сессию в зависимость
        # Сессия автоматически закрывается после использования

# Аннотация зависимости для передачи в эндпоинты FastAPI
SessionDep = Annotated[AsyncSession, Depends(get_session)]


# 2. Определение моделей базы данных

# Базовый класс для моделей SQLAlchemy
class Base(DeclarativeBase):
    pass  # Нужен только как основа для наследования

# Модель книги, соответствующая таблице `books`
class BookModel(Base):
    __tablename__ = 'books'  # Имя таблицы в базе данных

    # Поле `id` - первичный ключ
    id: Mapped[int] = mapped_column(primary_key=True)

    # Поле `title` - название книги
    title: Mapped[str] = mapped_column()

    # Поле `author` - автор книги
    author: Mapped[str] = mapped_column()


# 3. Инициализация базы данных

# Эндпоинт для создания таблиц в базе данных
@app.post('/setup_database')
async def setup_database():
    async with engine.begin() as conn:  # Открываем соединение
        await conn.run_sync(Base.metadata.drop_all)  # Удаляем все таблицы (если они есть)
        await conn.run_sync(Base.metadata.create_all)  # Создаём новые таблицы
    return {'status': True, 'message': 'Completed with positive result'}  # Возвращаем результат


# 4. Определение схем Pydantic для валидации входных данных

# Схема для добавления книги (без ID)
class BookAddSchema(BaseModel):
    title: str  # Название книги (обязательно)
    author: str  # Автор книги (обязательно)

# Схема для отображения книги (с ID)
class BookSchema(BookAddSchema):
    id: int  # ID книги


# 5. Реализация API-эндпоинтов

# Эндпоинт для добавления книги в базу данных
@app.post('/books', response_model=BookSchema)
async def add_books(data: BookAddSchema, session: SessionDep):
    # Создаём новый объект книги
    new_book = BookModel(
        title=data.title,
        author=data.author,
    )
    session.add(new_book)  # Добавляем книгу в сессию
    await session.commit()  # Сохраняем изменения в базе
    await session.refresh(new_book)  # Обновляем объект после коммита (чтобы получить ID)
    return new_book  # Возвращаем добавленную книгу


# Эндпоинт для получения списка всех книг
@app.get('/books', response_model=list[BookSchema])
async def get_books(session: SessionDep):
    query = select(BookModel)  # Создаём SQL-запрос на выбор всех книг
    result = await session.execute(query)  # Выполняем запрос асинхронно
    return result.scalars().all()  # Извлекаем список объектов `BookModel`


# 6. Запуск приложения

# Если этот файл запускается напрямую, то стартуем сервер Uvicorn
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)  # `reload=True` включает автообновление при изменении кода