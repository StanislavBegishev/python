class GrammarError(Exception):
    def __init__(self, text):
        self.text = text


class NameValidation:

    def __set__(self, instance, name):
        if not name.isalpha():
            raise GrammarError(
                'Name & surname must be written in letters only')
        instance.__dict__[self.name] = name.capitalize()

    def __set_name__(self, owner, name):
        self.name = name


class Worker:
    name = NameValidation()
    surname = NameValidation()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Worker name is {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Worker salary is {sum(self._income.values())}')


employee = Position('dAvide', 'PAp3To', 'manager', 5000, 1700)
employee.get_full_name()
print(employee.position)
employee.get_total_income()
