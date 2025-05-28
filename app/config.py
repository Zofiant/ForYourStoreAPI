from dotenv import load_dotenv
import os


# Загрузка переменных из .env файла
load_dotenv(override=True)


# Получение значений переменных
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


# Использование загруженных значений
print(f"Database configuration:")
print(f"Host: {DB_HOST}")
print(f"Port: {DB_PORT}")
print(f"User: {DB_USER}")
print(f"Password: {DB_PASS}")
print(f"Database name: {DB_NAME}")
print(f"Password: {SECRET_KEY}")
print(f"Database name: {ALGORITHM}")