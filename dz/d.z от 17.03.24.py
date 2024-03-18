def replace(row, old_sym, new_sym):
    res = " "
    for s in row:
        if s == old_sym:
            res += new_sym
        else:
            res += s

    return res


str1 = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'
old_sym = 'N'
new_sym = 'P'


res = replace(str1, old_sym, new_sym)
print(res)
