import sqlite3
from sqlite3 import Error

# Класс для работы с общими методами для взаимодействия с БД
class WorkDB:

    def __init__(self, path_db):
        self.connection = self.get_connection(path_db)

    # Получить соединение с БД
    def get_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print(f"Ошибка при создании подключения -  '{e}' ")
        return connection

    # Выполнить запрос к БД (создание, вставка)
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Запрос выполнен")
        except Error as e:
            print(f"Ошибка при выполнении запроса '{e}' ")

    # Выполнить запрос к БД (выборка)
    def execute_read_query(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Ошибка при попытке получить данные '{e}' ")
