import csv

from db.db_api import DB_API


class Parser_csv:

    def __init__(self):
        self.api = DB_API('discripts_operations.sqlite')

    # Сохранить данные из csv станков
    def parser_machines(self):
        with open('in/machines.csv', 'r', newline='') as csvfile:
            machines = csv.reader(csvfile, delimiter=',')
            for row in machines:
                self.api.insert_machines_lazy(
                    number=row[0],
                    types_machines_value=row[1],
                    times_machines_value=row[3]
                )

    # Сохранить данные из csv операций
    def parser_operations(self):
        with open('in/operations.csv', 'r', newline='') as csvfile:
            operations = csv.reader(csvfile, delimiter=',')
            for row in operations:
                self.api.insert_operations_lazy(
                    name=row[0],
                    priority_value=row[1],
                    types_machines_value=row[2],
                    parts_value=row[3],
                    weight_all=row[4],
                    weight_part=row[5]
                )

    # Сохранить данные из csv операций
    def parser_print_operations(self):
        with open('in/operations.csv', 'r', newline='') as csvfile:
            operations = csv.reader(csvfile, delimiter=',')
            for row in operations:
                print(row)
