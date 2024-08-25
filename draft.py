import os
os.system('cls' if os.name == 'nt' else 'clear')


import json


file_path = "contacts.json"

# Ваш список контактов
contacts = [
    {'user': 'sdfgs', 'email': 'agr'},
    {'user': 'sdfhsb', 'email': 'sdhs'},
    {'user': 'dfh', 'email': 'stfh'}
]

# Сохранение списка в файл
with open('contacts.json', 'w') as file:
    json.dump(contacts, file, indent=4)  # indent=4 для красивого форматирования



import json

# Загрузка данных из файла JSON
with open('contacts.json', 'r') as file:
    contacts = json.load(file)

# Теперь contacts содержит данные из файла
print(contacts)