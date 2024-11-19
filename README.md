# Material de estudos sobre python

<img src="https://img.freepik.com/free-photo/rear-view-programmer-working-all-night-long_1098-18697.jpg?t=st=1731702342~exp=1731705942~hmac=452a071b75b852b11e07d2877d91a8485b27a31c54e2298821bda15091593c41&w=740" >

> Material criado a partir das aulas de Python presentes no bootcamp NTT DATA - Engenharia de Dados com Python disponível na plataforma [DIO](https://web.dio.me/home).

## 🎯 Objetivo geral
Criar um local para armazenar comandos e lembretes sobre a linguagem `python`.

## 💻 Pré-requisitos
Antes de começar, verifique se você atendeu aos seguintes requisitos:
- Você instalou a versão mais recente de `python`
  
## ⚠️ Premissas
Não se aplica.

## 📝 Estrutura de dados

### Listas

Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. 
Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação

#### Criando listas
- Utilizando o construtor **list()**
- Utilizando uma declaração colocando valores separados por vírgulo dentro de colchetes

```python
frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)
```

#### Acesso direto
Por a lista ser uma sequência, podemos acessar seus dados utilizando índices.
Contamos o índice de uma sequência a partir do zero.

```python
frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[0])  # maçã
print(frutas[2])  # uva
print(frutas[-1])  # pera
print(frutas[-3])  # laranja
```

#### Listas aninhadas
Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas.
Assim, podemos criar estruturas bidimensionais (matrizes), e acessar informações passando os índices de linha e coluna.

```python
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
```

#### Fatiamento
Além de acessar os itens em uma lista, podemos extrair um subconjunto de valores. Para isso devemos passar o índice inicial e/ou final para acessar o conjunto. Podemos também informar quantas posições o cursor deve "pular" no acesso.

```python
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
```

#### Iterar listas
A forma mais comum para percorrer os dados de uma lista é utilizando o comando **for**.

```python
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

#### Compreensão de listas
A compreensão oferece uma sintaxe mais curta quando se deseja:
- criar uma nova lista a partir de uma lista já existente (filtro);
- gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

```python
# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
```

#### [].append
Método utilizado para adicionar um item ao fim da lista.

```python
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]
```

#### [].clear
Método utilizado para limpar uma lista.

```python
lista = [1, "Python", [40, 30, 20]]

print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista)  # []
```

#### [].copy
Método utilizado para copiar uma lista conforme ela estava no momento da cópia. Ele retorna uma nova lista igual a lista da qual foi copiado.
O que é feito na lista após a cópia não reflete na cópia e a recíproca também é verdadeira, o que é feito sobre a cópia da lista não reflete na lista original.

```python
lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(l2)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista)) # ids diferentes. São objetos distintos.
```

#### [].count
Método utilizado para contar quantas vezes um determinado item aparece dentro de uma lista.

```python
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
```

#### [].extend
Método utilizado para juntar duas listas. Não elimina valores duplicados.

```python
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp", "c"])

print(linguagens)  # ["python", "js", "c", "java", "csharp", "c"]
```

#### [].index
Método utilizado para localizar a primeira ocorrência de um item.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
```

#### [].pop
Uma lista vem organizada como uma pilha de elementos. O pop é um método utilizado para remover um item da lista a partir da sua posição na sequência. Por padrão, ele irá remover o último item da lista a menos que seja indicada uma posição na sequência a ser removida (índice).


```python
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python
```

#### [].remove
Método utilizado para remover um item da lista. Diferente do método pop, deve ser passado como parâmetro o item a ser removido. Ele remove apenas a primeira ocorrência do item por vez.

```python
linguagens = ["python", "js", "c", "java", "csharp", "c"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp", "c"]
```

#### [].reverse
Método utilizado para espelhar uma lista. Inverter a ordem dos itens.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]
```

#### [].sort
Método utilizado para classificar os itens de uma lista.

``` python
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
```

#### len()
Método utilizado para contar o tamanho das coisas.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5
```

#### sorted()
É uma função buit-in do python que é utilizado para classificar os itens de uma lista.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
```

### Tuplas

São estruturas de dados muito parecida com as listas, a diferença é que tuplas são imutáveis enquanto listas são mutáveis. Não é possível alterar itens dentro de uma tupla.

#### Criando tuplas
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

#### Acesso direto
A tupla é uma sequência, sendo assim podemos acessar seus dados utilizando índices.
O índice é contado em sequência a partir do zero.

```python
frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0])  # maçã
print(frutas[2])  # uva
print(frutas[-1])  # pera
print(frutas[-3])  # laranja
```

#### Tuplas aninhadas
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

#### Fatiamento
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

#### Iterar tuplas
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

#### ().count
Método utilizado para contar quantas vezes um determinado item aparece dentro de uma tupla.

```python
cores = ("vermelho", "azul", "verde", "azul")

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
```

#### ().index
Método utilizado para localizar a primeira ocorrência de um item.

```python
linguagens = ("python", "js", "c", "java", "csharp")

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
```

#### len()
Método utilizado para contar o tamanho das coisas.

```python
linguagens = ("python", "js", "c", "java", "csharp")

print(len(linguagens))  # 5
```

## 📫 Contribuindo para o projeto

Para contribuir, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
