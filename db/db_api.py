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

    # Запрос на добавление станка с указанием id типа станка и фонда времени
    def insert_machines(self, number, types_machines_id, times_machines_id):
        insert = f"""
            INSERT INTO
              machines (number, types_machines_id, times_machines_id)
            VALUES
              ({number}, {types_machines_id}, {times_machines_id} );
            """
        self.execute_query(insert)

    # Запрос на добавление станка с указанием значений типа станка и фонда времени
    # Если такой тип станков и значение фонда времени еще не хранится в БД - будут созданы соответствующие записи
    def insert_machines_lazy(self, number, types_machines_value, times_machines_value):
        types_machines_id = self.select_id_types_machines_or_insert(types_machines_value)
        times_machines_id = self.select_id_times_machines_or_insert(times_machines_value)
        self.insert_machines(number, types_machines_id, times_machines_id)

    # Запрос на добавление операции с указанием id типа станка и приоритета и количества частей
    def insert_operations(self, name, weight_all, weight_part, types_machines_id, priority_id, parts_id):
        weight_all = weight_all.replace(',', '.')
        weight_part = weight_part.replace(',', '.')
        name = '"' + name + '"'
        insert = f"""
            INSERT INTO
              operations (name, weight_all, weight_part, types_machines_id, priority_id, parts_id)
            VALUES
              ({name}, {weight_all}, {weight_part}, {types_machines_id}, {priority_id}, {parts_id} );
            """
        self.execute_query(insert)

    # Запрос на добавление операции с указанием значений типа станка, приоритета, частей задачи
    # Если значения типа станка, приоритета, частей задачи еще не хранится в БД - будут созданы соответствующие записи
    def insert_operations_lazy(self, name, weight_all, weight_part, types_machines_value, priority_value, parts_value):
        types_machines_id = self.select_id_types_machines_or_insert(types_machines_value)
        priority_id = self.select_id_priority_or_insert(priority_value)
        parts_id = self.select_id_parts_or_insert(parts_value)
        self.insert_operations(name, weight_all, weight_part, types_machines_id, priority_id, parts_id)

    # Общий метод для получения значения (target) по значению (value) колонки (column) из таблицы (table)
    def select_simple_data(self, table, column, value, target):
        insert = f"""SELECT {target} FROM {table} WHERE {column} = {value}"""
        res = self.execute_read_query(insert)
        res = res if not res else res[0][0]
        return res

    # Получить id типа станка по значению поля name
    def select_id_types_machines(self, name):
        name = '"' + name + '"'
        types_machines_id = self.select_simple_data('types_machines', 'name', name, 'id')
        return types_machines_id

    # Получить id типа станка по значению поля name, если такого поля нет, создать запись и вернуть id
    def select_id_types_machines_or_insert(self, name):
        types_machines_id = self.select_id_types_machines(name)
        if not types_machines_id:
            self.insert_types_machines(name)
            types_machines_id = self.select_id_types_machines(name)

        return types_machines_id

    # Получить id фонда времени станка по значению поля value
    def select_id_times_machines(self, value):
        times_machines_id = self.select_simple_data('times_machines', 'value', value, 'id')
        return times_machines_id

    # Получить id фонда времени типа станка по значению поля value, если такого поля нет, создать запись и вернуть id
    def select_id_times_machines_or_insert(self, value):
        times_machines_id = self.select_id_times_machines(value)
        if not times_machines_id:
            self.insert_times_machines(value)
            times_machines_id = self.select_id_times_machines(value)

        return times_machines_id

    # Получить id приоритета по значению поля value
    def select_id_priority(self, value):
        priority_id = self.select_simple_data('priority', 'value', value, 'id')
        return priority_id

    # Получить id приоритета по значению поля value, если такого поля нет, создать запись и вернуть id
    def select_id_priority_or_insert(self, value):
        priority_id = self.select_id_priority(value)
        if not priority_id:
            self.insert_priority(value)
            priority_id = self.select_id_priority(value)

        return priority_id

    # Получить id количества частей задач по значению поля value
    def select_id_parts(self, value):
        parts_id = self.select_simple_data('parts', 'value', value, 'id')
        return parts_id

    # Получить id приоритета по значению поля value, если такого поля нет, создать запись и вернуть id
    def select_id_parts_or_insert(self, value):
        parts_id = self.select_id_parts(value)
        if not parts_id:
            self.insert_parts(value)
            parts_id = self.select_id_parts(value)

        return parts_id
