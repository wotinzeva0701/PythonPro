import re


def check(password):
    return re.findall(r"[A-Za-z0-9_@-]{6,18}$", password)


print(check("Pas_12@"))
print(check("Pasw!#3"))
