# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

origin_file = "text_4.txt"
new_file = "text_4_RU.txt"
ru_num = ('Один', 'Два', 'Три', 'Четыре')

try:
    with open(origin_file, encoding='utf-8') as fhs:
        lines = fhs.readlines()

    numbers = [int(line[-2]) for line in lines if line != '\n']
    content = "\n".join(f'{ru_num[n - 1]} - {n}' for n in numbers)

    with open(new_file, 'w', encoding='utf-8') as fhd:
        fhd.write(content)
except IOError as e:
    print(e)
except (ValueError, IndexError):
    print("Неконсистентные данные")
