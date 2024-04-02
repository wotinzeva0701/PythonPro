def count_list(lst):
    if lst == []:
        return 0
    if lst[0] < 0:
        return 1 + count_list(lst[1:])
    else:
        return count_list(lst[1:])


print("Количество отрицательных чисел в списке:", count_list([-2, 3, 8, -11, -4, 6]))
