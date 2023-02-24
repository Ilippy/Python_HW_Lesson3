# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint


def findIndexOfClosestNumberInList(lst: list[int], num: int) -> int:
    """Нахождение индекса числа в списке ближашего к число"""
    min_index = 0
    min_diff = abs(lst[0] - num)
    # print(f'{0}# abs({lst[0]} - {number}) = {t}')
    for i in range(1, len(lst)):
        t = abs(lst[i] - num)
        # print(f'{i}# abs({lst[i]} - {number}) = {t}')
        if t < min_diff:
            min_diff = t
            min_index = i
        if min_diff == 0:
            break
    return lst[min_index]


size = int(input("Введите длину списка\n"))
lst = [randint(0, size) for _ in range(size)]
print(*lst)
number = int(input(f"Введите число от 1 до {size}\n"))
print(f"-> {findIndexOfClosestNumberInList(lst, number)}")
