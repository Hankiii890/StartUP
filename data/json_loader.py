import json

from src.models import Defects, Employees, session
from src.main import create_defects, create_employees

# Открытие Json файла и загрузки данных
with open('data.json', 'r') as f:
    data = f.read()
    result = json.loads(data)


# Добавление данных в таблицы
for defect_data in result["defects"]:
    print(defect_data)
    """Создание записей"""
    create_defects(**defect_data)

for employees_data in result["employees"]:
    create_employees(**employees_data)
