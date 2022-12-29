# Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
# оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали
# и чего удалось добиться

def update_rating(r_list, number):
    for i in range(len(r_list)):
        if r_list[i] == number:
            r_list.insert(i + 1, number)
            break
        if r_list[0] < number:
            r_list.insert(0, number)
        elif r_list[-1] > number:
            r_list.append(number)
        elif r_list[i + 1] < number < r_list[i]:
            r_list.insert(i + 1, number)
            break
    return r_list


"""
Длинный код с циклом, вычисления проходят довольно быстро
"""


def update_rating_2(r_list, number):
    r_list.append(number)
    r_list.sort(reverse=True)
    return r_list


"""
Короткий код со встроенными методами, выдает худший результат времени
update_rating   - 0.0006591999990632758 seconds
update_rating_2 - 0.0035521000008884585 seconds 
"""


def my_func_1(x, y):
    try:
        if int(y) < 0 < float(x):
            return float(x) ** float(y)
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


"""
Код с оператором, вычисления проходят довольно быстро
"""


def my_func_2(x, y):
    return pow(x, y)


"""
код со встроенной функцией, вычисления проходят раза в два быстрее
my_func_1 - 0.0008189999989554053 seconds
my_func_2 - 0.0003113999991910532 seconds
"""
