from task_1 import update_rating, update_rating_2
from task_1 import my_func_1, my_func_2
from timeit import timeit

# first competition
rating_list = [7, 5, 3, 3, 2]
rating_lst = [7, 5, 3, 3, 2]
rating = 8

rating_1 = timeit("update_rating(rating_list, rating)", globals=globals(),
                  number=1000)
rating_2 = timeit("update_rating_2(rating_lst, rating)", globals=globals(),
                  number=1000)
print(f'Rating_1 - {rating_1} seconds')
print(f'Rating_2 - {rating_2} seconds')

# second competition
number_1, number_2 = 7, -2

pow_1 = timeit("my_func_1(number_1, number_2)", globals=globals(),
               number=1000)
pow_2 = timeit("my_func_2(number_1, number_2)", globals=globals(),
               number=1000)

print(f'Pow_1 - {pow_1} seconds')
print(f'Pow_2 - {pow_2} seconds')
