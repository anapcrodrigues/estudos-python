# Lidando com date, datetime e time

## Módulo datetime

[Documentação](https://docs.python.org/pt-br/3.13/library/datetime.html#)

O módulo 'datetime' é usado para lidar com datas e horas.

```python
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
```

## timedelta

[Documentação](https://docs.python.org/pt-br/3.13/library/datetime.html#timedelta-objects)

Classe utilizada para criar e manipular objetos date, time e datetime de várias maneiras. Por exemplo, podemos adicionar e subtrair datas, verificar a diferença entre datas e muito mais.

As operações suportadas envolvem apenas objetos com tipo datetime.

```python
 from datetime import timedelta, datetime, date

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
```

## Conversão e formatação de datas e horas

[Documentação](https://docs.python.org/pt-br/3.13/library/datetime.html#strftime-and-strptime-behavior)

Python permite converter e formatar datas e horas atravé dos métodos 'strftime' (string format time) e 'strptime' (string parse time).

### strftime
É o método utilizado para alterar o formato de um objeto tipo datetime.

```python
from datetime import datetime
# strftime
d = datetime.now()
# formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M")) # dd/mm/aaaa hh:mm
```

### strptime
É o método utilizado para converter um objeto tipo string para datetime.

```python
from datetime import datetime
d = datetime.now()
# convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d) # 2023-07-20 15:30:00
```

## Timezone

Quando trabalhamos com data e hora precisamos lidar com fusos horários. Python facilita isso através do módulo 'pytz'.


