import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = response.json()

with open("dict_new.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\n", fieldnames=list(data[0].keys()))
    writer.writeheader()
    for d in data:
        writer.writerow(d)




