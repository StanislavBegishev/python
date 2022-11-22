# 2) Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input('Введите время в секундах: '))
hours = time_in_seconds // 3600
residue = time_in_seconds % 3600
minutes = residue // 60
seconds = residue % 60

print(f"{hours}:{minutes}:{seconds}")
