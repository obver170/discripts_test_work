import sqlite3
from sqlite3 import Error


class CreateDB:

    def __init__(self, path_db):
        # Создать базу
        self.connection = self.get_connection(path_db)
        # Получить код для создания таблиц
        self.tables = self.get_structure()
        # Создать таблицы
        for table in self.tables:
            self.execute_query(table)

    def get_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print(f"Ошибка при создании подключения-  '{e}' ")
        return connection

    # Получить структуру таблиц БД
    def get_structure(self):

        queries = []
        # Таблица для типа станка
        create_types_machines = """
            CREATE TABLE IF NOT EXISTS types_machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
        """
        queries.append(create_types_machines)

        # Таблица для фонда времени станка
        create_times_machines = """
            CREATE TABLE IF NOT EXISTS times_machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER
        );
        """
        queries.append(create_times_machines)

        # Таблица для станка
        create_machines = """
            CREATE TABLE IF NOT EXISTS machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number INTEGER NOT NULL,
            types_machines_id INTEGER NOT NULL,
            times_machines_id INTEGER NOT NULL,
            FOREIGN KEY (types_machines_id) REFERENCES types_machines (id),
            FOREIGN KEY (times_machines_id) REFERENCES times_machines (id)
        );
        """
        queries.append(create_machines)

        # Таблица для приоритета
        create_priority = """
            CREATE TABLE IF NOT EXISTS priority (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER
        );
        """
        queries.append(create_priority)

        # Таблица для частей задачи
        create_parts = """
            CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER
        );
        """
        queries.append(create_parts)

        # Таблица для операций
        create_operations = """
            CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight_all REAL NOT NULL,
            weight_part REAL NOT NULL,
            types_machines_id INTEGER NOT NULL,
            priority_id INTEGER NOT NULL,
            parts_id INTEGER NOT NULL,
            FOREIGN KEY (types_machines_id) REFERENCES types_machines (id),
            FOREIGN KEY (priority_id) REFERENCES priority (id),
            FOREIGN KEY (parts_id) REFERENCES parts (id)
        );
        """
        queries.append(create_operations)

        return queries

    # Выполнить запрос к БД
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Таблица создана")
        except Error as e:
            print(f"Ошибка при создании таблицы '{e}' ")
