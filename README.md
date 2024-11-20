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

Conteúdo abordado:
- Listas
- Tuplas
- Conjuntos
- Dicionários
- Objetos *date*, *datetime* e *time*

### Listas

Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. 
Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação

#### Criando listas
- Utilizando o construtor **list()**
- Utilizando uma declaração colocando valores separados por vírgula dentro de colchetes.

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

### Conjuntos

Estrutura de dados *set*.

#### Criando sets
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

#### Acessando os dados
Conjuntos em Python não suportam indexação e nem fatiamento. Para acessar os valores é necessário converter o conjunto para lista.

```python
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
```

#### Iterar conjuntos
A forma mais comum para percorrer os dados de um conjunto é utilizando o comando **for**.

```python
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

#### {}.union
Resulta na união entre dois conjuntos.

<img src="https://static.todamateria.com.br/upload/un/ia/uniao.jpg" hight=100 width=100 >

> O *set* lembra conjuntos referentes a operações matemáticas. Com o *set* é possível realizar operações similares às matemática.

```python
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)
```

#### {}.intersection
Retorna a parte igual entre dois conjuntos.

<img src="https://static.todamateria.com.br/upload/in/te/interseca_ao.jpg" hight=100 width=100 >

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)
```

#### {}.difference
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

#### {}.symmetric_difference
Retorna todos os elementos que os conjuntos não tem em comum, retorna tudo menos a intersecção.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Venn0110.svg/220px-Venn0110.svg.png" hight=100 width=100 >

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado) # {1, 4}
```

#### {}.issubset
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

#### {}.issuperset
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

#### {}.isdisjoint
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

#### {}.add
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

#### {}.clear
Limpa o set.

```python
sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}
```

#### {}.copy
Gera uma cópia do set.

```python
sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio_copia = sorteio.copy()

print(sorteio_copia)  # {1, 23}
```

#### {}.discard
Descarta o valor do set. Não apresenta erro se o valor a ser descartado não estiver no set.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
```

#### {}.pop
Retorna e elimina o primeiro item do set.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}
```

#### {}.remove
Descarta o valor do set. Apresenta erro se o valor a ser descartado não estiver no set.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

#### len()
Retorna o tamanho do conjunto.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10
```

#### in
Verifica se um elemento está dentro de um conjunto. Retorna *True* ou *False*.

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False
```

### Dicionários

É um conjunto não-ordenado de pares chave-valor, onde as chaves são únicas em uma dada instância do dicionário e devem ser valores imutáveis, inclusive tuplas.
Dicionários são delimitados por chaves {} e contém uma lista de pares chave:valor separada por vírgulas.

#### Declarando dicionários
- Utilizando o construtor **dict()**
- Utilizando uma declaração colocando conjuntos chave:valores separados por vírgula dentro de chaves {}.
  
```python
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
```

#### Acessando os dados
Os dados são acessados e modificados através da chave.

```python
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
```

#### Dicionários aninhados
Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como strings, números, tuplas.

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)
```

#### Iterar dicionários
A forma mais comum para percorrer os dados de um dicionário é utilizando o comando **for**.

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items(): # items retorna uma lista de tuplas
    print(chave, valor)
```

#### {}.clear
Limpa o dicionário.

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
print(contatos)
contatos.clear()
print(contatos)  # {}
```

#### {}.copy
Gera uma cópia do dicionário.

```python
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
```

#### {}.fromkeys
Método utilizado para criar chaves do dicionário. Pode ser um dicionário novo ou um dicionário já existente.

```python
# cria as chaves e deixa os valores vazios.
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# cria as chaves e preenche com o valor padrão, a palavra 'vazio'.
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
```

#### {}.get
Outra forma de acessar valores dentro de um dicionário. Não dá erro ao tentar acessar uma chave que não existe dentro do dicionário.

```python
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

# caso não encontre a chave, retorna valor padrão 'None'
resultado = contatos.get("chave")  # None
print(resultado)

# caso não encontre a chave, retorna o valor dado. Nesse caso '{}'.
resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
```

#### {}.items
Retorna uma lista de tuplas.

```python
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)
```

#### {}.keys
Retorna somente as chaves de um dicionário.

```python
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)
```

#### {}.pop
Remove e retorna o valor removido do dicionário.

```python
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# segundo argumento informa o valor a ser retornado se não encontrar o item a ser removido. Sem o segundo argumento, será retornado um erro.
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
```

#### {}.popitem
Remove e retorna o valor removido do dicionário. Remove os itens a partir do primeiro.

```python
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
            , "ana@gmail.com": {"nome": "Ana", "telefone": "3333-5689"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
```

#### {}.setdefault
Adiciona o atributo no dicionario se o atributo ainda não existir, se o atributo existir ele não faz a alteração.

```python
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
```

#### {}.update
Atualiza o dicionário atual com outro dicionário. Caso a chave ainda não exista, ela é adicionada. Caso a chave exista, ela é atualizada.

```python
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
```

#### {}.values
Retorna todas os valores de um dicionário.

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)
```

#### in
Verifica se a chave existe dentro do dicionário. Retorna *True* ou *False*.

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)
```

#### del
Deleta o item de um dicionário ou o dicionário inteiro.

```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)
```

### Lidando com date, datetime e time

#### Módulo datetime
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

## 📫 Contribuindo para o projeto

Para contribuir, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
