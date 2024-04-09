
import os

dir_name = "nested1"

objs = os.listdir(dir_name)
print(objs)

for obj in objs:
    p = os.path.join(dir_name, obj)
    if os.path.isfile(p):
        print(f"{obj} - file - {os.path.getsize(p)} bytes")

    elif os.path.isdir(p):
        print(f"{obj} - dir")
