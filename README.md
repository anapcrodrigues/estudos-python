# Material de estudos sobre python

<img src="Savings-bro.png">

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

## 📫 Contribuindo para o projeto

Para contribuir, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
