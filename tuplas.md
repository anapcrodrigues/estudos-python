# Tuplas

São estruturas de dados muito parecida com as listas, a diferença é que tuplas são imutáveis enquanto listas são mutáveis. Não é possível alterar itens dentro de uma tupla.

## Criando tuplas
- Criada através da classe **tuple**;
- Criada através da declaração de valores separados por vírgula dentro de parênteses.

```python
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
```

> Uma boa prática em declação de tuplas é deixar sempre uma virgula após o último item, vide exemplos acima.

## Acesso direto
A tupla é uma sequência, sendo assim podemos acessar seus dados utilizando índices.
O índice é contado em sequência a partir do zero.

```python
frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0])  # maçã
print(frutas[2])  # uva
print(frutas[-1])  # pera
print(frutas[-3])  # laranja
```

## Tuplas aninhadas
Tuplas podem armazenar todos os tipos de objetos Python, portanto podem armazenar outras tuplas. Com isso é possível criar estruturas bidimensionais (matrizes), e acessar informando os índices de linha e coluna.

```python
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
```

## Fatiamento
Além de acessar os itens em uma tupla, podemos extrair um subconjunto de valores. Para isso devemos passar o índice inicial e/ou final para acessar o conjunto. Podemos também informar quantas posições o cursor deve "pular" no acesso.

```python
tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")
```

## Iterar tuplas
A forma mais comum para percorrer os dados de uma lista é utilizando o comando **for**.

```python
carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

## ().count
Método utilizado para contar quantas vezes um determinado item aparece dentro de uma tupla.

```python
cores = ("vermelho", "azul", "verde", "azul")

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
```

## ().index
Método utilizado para localizar a primeira ocorrência de um item.

```python
linguagens = ("python", "js", "c", "java", "csharp")

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
```

## len()
Método utilizado para contar o tamanho das coisas.

```python
linguagens = ("python", "js", "c", "java", "csharp")

print(len(linguagens))  # 5
```