
def avg(fn):
    def wrap(*args):
        return fn(*args), sum(args) / len(args)

    return wrap


@avg
def summa(*args):
    return sum(args)


res_sum, res_avg = summa(2, 3, 3, 4)


print("Сумма чисел 2, 3, 3, 4 =", res_sum)
print("Среднее арифметическое чисел 2, 3, 3, 4 =", res_avg)