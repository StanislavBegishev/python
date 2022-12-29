from itertools import count


def two_max_sum(arg_1, arg_2, arg_3):
    my_list = sorted([float(arg_1), float(arg_2), float(arg_3)], reverse=True)
    return my_list[0] + my_list[1]




def int_func(arg):
    return arg.title()




def my_func(list_in):
    result_list = [el for el in list_in if list_in.count(el) == 1]
    return result_list




class DivisionByZero(Exception):

    def __init__(self, text):
        self.text = text


def division_1(a, b):
    try:
        if b == 0:
            raise DivisionByZero('Cannot divide by zero')
    except DivisionByZero:
        return 'Cannot divide by zero'
    else:
        return a / b


def division_2(a, b):
    if b == 0:
        raise DivisionByZero('Cannot divide by zero')
    return a / b




def my_func_count(initial_num, termination_num):
    result_list = []
    for el in count(initial_num):
        if el > termination_num:
            break
        result_list.append(el)
    return result_list




class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'cell consists of {self.quantity} partitions'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        return 'Subtraction operation is not possible for these cells'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if self.quantity >= other.quantity:
            return Cell(self.quantity // other.quantity)
        return 'Division operation is not possible for these cells'

    def make_order(self, cells_row):

        row = []
        for _ in range(self.quantity // cells_row):
            row.append('*' * cells_row)
        if self.quantity % cells_row != 0:
            row.append('*' * (self.quantity % cells_row))
        return '\\n'.join(row)
