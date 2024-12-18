# módulo datetime
from datetime import date, datetime, time, timedelta

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

# timedelta
print('-> timedelta')

# from datetime import timedelta 

# criando data e hora
d = datetime(2023, 7, 19, 13, 45)
print(d) # 2023-7-19 13:45:00

# adicionando uma semana
d = d + timedelta(weeks=1)
print(d)

tipo_carro = "M"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())


# Conversão e formatação
print('-> Conversão e formatação')
# from datetime import datetime

# strftime
d = datetime.now()

# formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M")) # dd/mm/aaaa hh:mm

# strptime
# from datetime import datetime
d = datetime.now()
# convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d) # 2023-07-20 15:30:00


# from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))