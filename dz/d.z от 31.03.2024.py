file = "text11.txt"
f = open(file, "w")
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
f.close()

pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))

f = open(file, "r")
read_line = f.readlines()
if pos1 not in range(len(read_line)) or pos2 not in range(len(read_line)):
    print("Не верно введены данные")
else:
    print(read_line)
    read_line[pos1] = "записать список в файл\n"
    read_line[pos2] = "изменить строку в списке\n"
    print(read_line)
    f.close()

f = open(file, "w")
f.writelines(read_line)
f.close()


