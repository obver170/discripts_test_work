class Machine:

    def __init__(self, machine_dict):
        self.id = machine_dict.get('id')
        self.number = machine_dict.get('number')
        self.types_machines = machine_dict.get('types_machines')
        self.times_machines = machine_dict.get('times_machines')

    def set_times_machines(self, times_machines):
        self.times_machines = times_machines
