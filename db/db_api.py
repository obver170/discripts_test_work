from db.db_work import WorkDB


# Класс для работы с конкретной БД, CRUD операции с таблицей
class DB_API(WorkDB):

    def __init__(self, path_db):
        super().__init__(path_db)

    # Общий метод для вставки данных для таблиц times_machines, priority, parts
    def insert_simple_data(self, table, value, column='value'):
        insert = f"""
            INSERT INTO
              {table} ({column})
            VALUES
              ({value});
            """
        self.execute_query(insert)

    # Общий метод для выборки данных для таблиц times_machines, priority, parts
    def select_simple_data(self, table):
        insert = f"""SELECT * FROM {table}"""
        res = self.execute_read_query(insert)
        return res

    # Запрос на добавление фонда времени
    def insert_times_machines(self, value):
        table = 'times_machines'
        self.insert_simple_data(table, value)

    # Запрос на добавление приоритета
    def insert_priority(self, value):
        table = 'priority'
        self.insert_simple_data(table, value)

    # Запрос на добавление количества частей задачи
    def insert_parts(self, value):
        table = 'parts'
        self.insert_simple_data(table, value)

    # Запрос на добавление типа станка
    def insert_types_machines(self, name):
        table = 'types_machines'
        column = 'name'
        name = '"' + name + '"'
        self.insert_simple_data(table, name, column)

    # Запрос на добавление станка
    def insert_machines(self, number, types_machines_id, times_machines_id):
        insert = f"""
            INSERT INTO
              machines (number, types_machines_id, times_machines_id)
            VALUES
              ({number}, {types_machines_id}, {times_machines_id} );
            """
        self.execute_query(insert)

    # Запрос на добавление операции
    def insert_operations(self, name, weight_all, weight_part, types_machines_id, priority_id, parts_id):
        name = '"' + name + '"'
        insert = f"""
            INSERT INTO
              operations (name, weight_all, weight_part, types_machines_id, priority_id, parts_id)
            VALUES
              ({name}, {weight_all}, {weight_part}, {types_machines_id}, {priority_id}, {parts_id} );
            """
        self.execute_query(insert)