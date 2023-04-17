# Задача 18: Требуется найти в массиве A[1..N] самый 
# близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве. В последующих строках 
# записаны N целых чисел Ai. Последняя строка содержит 
# число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Enter the number of elements in the array N: "))
list_1 = []
for i in range(n):
    m = int(input("Enter the element of array: "))
    list_1.append(m)
print(list_1)

x = int(input("Enter X: "))
for m in list_1:
    if x == m + 1:
        print("Number to the left of X: ", m)