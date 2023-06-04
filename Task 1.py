def merge_arrays(arr_1, arr_2):
    unique_arr = list(set(arr_1) & set(arr_2))
    return unique_arr


arr1 = input("Введите первый массив через пробел: ").split()
arr2 = input("Введите второй массив через пробел: ").split()
print(merge_arrays(arr1, arr2))
