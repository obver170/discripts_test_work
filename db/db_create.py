from db.db_work import WorkDB


# Класс-потомок WorkDB, вызывается 1 раз для создания БД и структуры таблиц в ней
class CreateDB(WorkDB):

    def __init__(self, path_db):
        # Создать базу
        super().__init__(path_db)
        # Получить код для создания таблиц
        self.tables = self.get_structure()
        # Создать таблицы
        for table in self.tables:
            self.execute_query(table)

    # Получить структуру таблиц БД
    def get_structure(self):
        queries = []
        # Таблица для типа станка
        create_types_machines = """
            CREATE TABLE IF NOT EXISTS types_machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        );
        """
        queries.append(create_types_machines)

        # Таблица для фонда времени станка
        create_times_machines = """
            CREATE TABLE IF NOT EXISTS times_machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER UNIQUE
        );
        """
        queries.append(create_times_machines)

        # Таблица для станка
        create_machines = """
            CREATE TABLE IF NOT EXISTS machines (
            id INTEGER PRIMARY KEY NOT NULL UNIQUE,
            number INTEGER NOT NULL UNIQUE,
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
            value INTEGER UNIQUE
        );
        """
        queries.append(create_priority)

        # Таблица для частей задачи
        create_parts = """
            CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER UNIQUE
        );
        """
        queries.append(create_parts)

        # Таблица для операций
        create_operations = """
            CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
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
