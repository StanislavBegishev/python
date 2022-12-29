# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numbers = int(input('Введите число: '))
max_num = numbers % 10
numbers //= 10
while numbers > 0:
    if numbers % 10 > max_num:
        max_num = numbers % 10
    numbers //= 10

print(max_num)
