# Conjuntos

Estrutura de dados *set*.

## Criando sets
Set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

```python
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)
```

## Acessando os dados
Conjuntos em Python não suportam indexação e nem fatiamento. Para acessar os valores é necessário converter o conjunto para lista.

```python
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
```

## Iterar conjuntos
A forma mais comum para percorrer os dados de um conjunto é utilizando o comando **for**.

```python
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

## {}.union
Resulta na união entre dois conjuntos.

<img src="https://static.todamateria.com.br/upload/un/ia/uniao.jpg" hight=100 width=100 >

> O *set* lembra conjuntos referentes a operações matemáticas. Com o *set* é possível realizar operações similares às matemática.

```python
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)
```

## {}.intersection
Retorna a parte igual entre dois conjuntos.

<img src="https://static.todamateria.com.br/upload/in/te/interseca_ao.jpg" hight=100 width=100 >

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)
```

## {}.difference
Retorna tudo que tem em um conjunto que não está no outro.

<img src="https://static.todamateria.com.br/upload/di/fe/diferena_a.jpg" hight=100 width=100 >

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado) # {1}

resultado = conjunto_b.difference(conjunto_a)
print(resultado) # {4}
```

## {}.symmetric_difference
Retorna todos os elementos que os conjuntos não tem em comum, retorna tudo menos a intersecção.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Venn0110.svg/220px-Venn0110.svg.png" hight=100 width=100 >

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado) # {1, 4}
```

## {}.issubset
Verifica se um conjunto é subconjunto de outro. Retorna *True* ou *False*.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKRb1QGYOIj1kv5IXU3yjp8yfE7JMCONeyRQ&s" hight=100 width=100 >

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)
```

## {}.issuperset
Contrário do subset. Verifica se um conjunto contém um subconjunto. Retorna *True* ou *False*.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKRb1QGYOIj1kv5IXU3yjp8yfE7JMCONeyRQ&s" hight=100 width=100 >

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
```

## {}.isdisjoint
Verifica se os conjuntos são disjuntos, ou seja, os conjuntos não possuem nenhum elemento em comum. Retorna *True* ou *False*.

<img src="https://s4.static.brasilescola.uol.com.br/be/2020/06/4.jpg" hight=100 width=100 >

```python
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
```

## {}.add
Adiciona um elemento ao final do set, somente adiciona se o elemento não existir no set.

```python
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)
```

## {}.clear
Limpa o set.

```python
sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}
```

## {}.copy
Gera uma cópia do set.

```python
sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio_copia = sorteio.copy()

print(sorteio_copia)  # {1, 23}
```

## {}.discard
Descarta o valor do set. Não apresenta erro se o valor a ser descartado não estiver no set.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
```

## {}.pop
Retorna e elimina o primeiro item do set.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}
```

## {}.remove
Descarta o valor do set. Apresenta erro se o valor a ser descartado não estiver no set.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

## len()
Retorna o tamanho do conjunto.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10
```

## in
Verifica se um elemento está dentro de um conjunto. Retorna *True* ou *False*.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False
```
