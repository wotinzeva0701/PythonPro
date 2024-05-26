import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
print(response.text)
print(type(response.text))
todos = json.loads(response.text)
print(type(todos[0]))

todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1

print(todos_by_user)