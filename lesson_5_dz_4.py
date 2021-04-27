# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]


# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
from random import randint

my_list = [randint(-10, 10) for _ in range(20)]  # границы включаются
uniq_list = [el for el in my_list if my_list.count(el) == 1]  # O(n ** 2) !!!
print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}")
#ujnjdj
#ddf2