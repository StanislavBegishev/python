# Задание 3.
#
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.



class division_by_zero(Exception):


    def __init__(self, text):
        self.text = text


def div(a, b):

    try:
        if b == 0:
            raise division_by_zero("Can't divide by zero")
    except division_by_zero as err:
        print(err)
    else:
        print(f'All right: {a} / {b} = {int(a) / int(b)}')


div(2, 2)
div(2, 0)