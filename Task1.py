# Создать 2 массива NumPy
# Один из случайных чисел, второй - использую arange Или linspace
# После этого выполнить математические операции- сложить, перемножить, делить
# Найти максимальный элемент в каждой строчке и столбце первого массива (из случайных чисел_
# Найти максимальный элемент в из 2 массивов
# Изменить форму массива
import numpy as np

arr1 = np.random.randint(0, 10, 4, dtype=int)
arr2 = np.arange(1,5)
sum_arr = arr1 + arr2
print(f'{arr1} + {arr2} = {sum_arr}')
mult_arr = arr1 * arr2
print(f'{arr1} * {arr2} = {mult_arr}')
div_arr = arr2 / arr1 
print(f'{arr2} / {arr1} = {div_arr}')

reshape_arr1 = arr1.reshape(2, -1)
reshape_arr2 = arr2.reshape(2, -1)
print(f'reshape array: {reshape_arr1}')
max_arr1_column = reshape_arr1.max(axis=0)
print(f'max in column: {max_arr1_column}')
max_arr1_row = reshape_arr1.max(axis=1)
print(f'max in row: {max_arr1_row}')

max_element = np.vstack([reshape_arr1, reshape_arr2]).max()
print(f'max_element in {reshape_arr1} and {reshape_arr2}: {max_element}')