# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# 12345 - 0
# 51234 - 1
# 45123 - 2
# 34512 - 3
# 23451 - 4

def shiftListToTheLeft(lst: list, shift: int) -> list:
    for _ in range(k):
        l.insert(0, l.pop())
    return lst

l = [1, 2, 3, 4, 5]
k = 34


k %= len(l)

size = len(l)
print(l[-k:] + l[:size-k])

shiftListToTheLeft(l, k)
print(l)



