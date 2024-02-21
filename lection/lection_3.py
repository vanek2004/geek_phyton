print("EXAMPLE_1")
def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
    print('stop')

print(sum_numbers(5))


# #\------------------------------------------------------
print("EXAMPLE_2")
def sum_str(*args):                          # * -указываем неограниченное колличество аргументов 
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'o', 'e'))

# #\------------------------------------------------------
print("EXAMPLE_3")

from module import max1        # - импорт модуля # from module import * - вывод всех функций из модуля

print(max1(5, 9))              # - вызов модуля
 

import module as m
print(m.max1(10, 9))

#\------------------------------------------------------
print("EXAMPLE_4")
#Рекурсия - функция которая вызывает сама себя

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

#\------------------------------------------------------
print("EXAMPLE_5")
#Алгоритмы - набор инструкций для выполнения задачи

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([13,5,7,6,3,2,1,9]))

#\------------------------------------------------------
print("EXAMPLE_6")

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1,6,7,9,4,6,6,4,2,9]
merge_sort(list_1)
print(list_1)