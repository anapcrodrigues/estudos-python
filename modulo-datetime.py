# módulo datetime
from datetime import date, datetime, time

d = date(2024, 11, 1)
print(d)

print(date.today())

data_hora = datetime(2024, 11, 1, 16, 40, 0)
print(data_hora)

data_hora = datetime(2024, 11, 1)
print(data_hora)

print(datetime.today())

hora = time(10, 20, 0)
print(hora)