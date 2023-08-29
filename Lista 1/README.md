# Manipulação e análise de dados com python

## Objetivos

- Manipular listas, dicionários, tuplas e conjuntos
- Utilizar funções, classes e módulos
- Utilizar estruturas condicionais e de repetição
- Praticar tratamento de exceções
- Praticar documentação de código

## Descrição

O trabalho consiste em construir módulos e funções para manipulação e análise de um conjunto de dados.

Durante o desenvolvimento, vocês terão um conjunto de dados disponível, o qual serve como exemplo. Contudo, durante a correção, um novo conjunto de dados será utilizado, com o mesmo formato, mas com dados diferentes. Portanto, é importante que o código seja genérico, ou seja, que funcione para qualquer conjunto de dados que tenha o mesmo formato. Além disso, é de extrema importância que o código siga com exatidão as especificações (nome de arquivos, nome de funções e parâmetros) e também seja bem documentado, para que a correção seja facilitada.

## Conjunto de dados

Abaixo, segue o conjunto de dados de exemplo, que também está disponível no arquivo `data.py`:

```python
people_data = [
    {"name": "Alice", "age": 25, "city": "New York", "hobbies": ["hiking", "reading"]},
    {"name": "Bob", "age": 30, "city": "San Francisco", "hobbies": ["gardening", "painting"]},
    {"name": "Charlie", "age": 22, "city": "Los Angeles", "hobbies": ["photography", "dancing"]},
    {"name": "David", "age": 27, "city": "Chicago", "hobbies": ["cooking", "hiking"]},
    {"name": "Eve", "age": 29, "city": "Boston", "hobbies": ["reading", "gardening"]},
]
```

Para testar, vocês podem importar o conjunto de dados no arquivo `main.py` da seguinte forma:

```python
import data

people_data = data.people_data
```

## Especificações 

### 1. Módulo `data`

O módulo `data` apenas contém o conjunto de dados de exemplo, que deve ser utilizado para testar o código. O módulo pode ser alterado, para que o conjunto de dados seja modificado, mas a estrutura do conjunto de dados deve ser mantida.

### 2. Módulo `utils`

As funções para manipular o conjunto de dados devem ser desenvolvidas dentro desse módulo. 

As funções devem ser genéricas, ou seja, devem funcionar para qualquer conjunto de dados que tenha o mesmo formato. As variáveis devem possuir nomes significativos e as funções devem ser comentadas e documentadas, da forma que desejarem. (Aqui, o intuito é que vocês pratiquem a documentação de código, não necessariamente seguir um padrão específico.)

Cada questão deve ser resolvida em uma função diferente, seguindo à risca as especificações fornecidas. As funções deverão ser chamadas no arquivo `main.py` e suas funcionalidades devem ser demonstradas através de prints organizados.

### 3. Main

O arquivo `main.py` deve ser utilizado para testar as funções desenvolvidas no módulo `utils`.

## Questões

### 1. `add_person(data, name, age, city, hobbies)`

Escreva uma função que recebe o conjunto de dados, uma string (representando o nome de uma pessoa), um inteiro (representando a idade), uma string (representando a cidade de uma pessoa) e uma lista de strings (representando os hobbies dessa pessoa) e retorne o conjunto de dados com essa pessoa adicionada.

Nessa questão, se atentem ao fato de que o nome dessa pessoa pode já existir no conjunto de dados. Nesse caso, a função deve informar o usuário que já existe uma pessoa listada com esse nome e retornar o conjunto de dados sem alterações.

Caso a idade seja menor que 0 ou maior que 100, a função deve lançar uma exceção do tipo `ValueError`, que deve ser tratada e informar o usuário que a idade deve ser um inteiro entre 0 e 100. Nesse caso, a função deve retornar o conjunto de dados sem alterações.

Caso o valor passado para o argumento city não seja uma string, a função deve lançar uma exceção do tipo `TypeError`, que deve ser tratada e informar o usuário que o tipo do valor passado para o argumento city não é uma string.

Caso a lista de hobbies seja vazia, a função deve lançar uma exceção do tipo `ValueError`, que deve ser tratada e informar o usuário que a lista de hobbies não pode ser vazia. Nesse caso, a função deve retornar o conjunto de dados sem alterações.

### 2. `remove_person(data, name)`

Escreva uma função que recebe o conjunto de dados e uma string (representando o nome de uma pessoa) e retorne o conjunto de dados com essa pessoa removida.

Nessa questão, se atentem ao fato dessa pessoa poder não existir no conjunto de dados. Nesse caso, a função deve informar o usuário que não existe nenhuma pessoa listada com esse nome e retornar o conjunto de dados sem alterações.

### 3. `get_ages(data)`

Escreva uma função que recebe o conjunto de dados e retorne uma tupla contendo 3 inteiros, nessa ordem: a idade da pessoa mais nova, a média de idade das pessoas e a idade da pessoa mais velha.

Nessa questão, não há tratamento de exceções, apenas notem que eu quero que a função retorne uma tupla de **inteiros**. Para isso, certifiquem-se de truncar a média, para que ela seja um inteiro.

### 4. `get_hobbies(data)`

Escreva uma função que recebe o conjunto de dados e retorne um conjunto contendo todos os hobbies das pessoas.

Nessa questão, não há tratamento de exceções, apenas notem que eu quero que a função retorne um **conjunto**.

### 5. `get_people_by_hobbies(data, hobbies)`

Escreva uma função que recebe o conjunto de dados e um conjunto de strings (representando hobbies) e retorne uma lista contendo os nomes das pessoas que possuem pelo menos um desses hobbies, ordenados por idade (do mais novo para o mais velho).

Nessa questão, se atentem ao fato de que o conjunto de hobbies pode ser vazio. Nesse caso, a função deve retornar uma lista vazia.

Além disso, se atentem ao fato de que você deve listar as pessoas que possuem pelo menos um dos hobbies passados, ou seja, se uma pessoa possui dois hobbies e apenas um deles está na lista de hobbies passada, essa pessoa deve ser listada.

### 6. `match_people(data, name=None, min_age=None, max_age=None, city=None, hobbies=[])`

Escreva uma função que recebe o conjunto de dados e pode receber alguns parâmetros opcionais: um nome, uma idade mínima, uma idade máxima, uma cidade ou um conjunto de hobbies (representado por uma lista de strings). A função deve retornar uma lista contendo os nomes das pessoas que atendem simultaneamente a todos os critérios passados, ordenados por idade (do mais novo para o mais velho). Caso nenhuma pessoa atenda aos critérios, a função deve retornar uma lista vazia. Caso nenhum critério seja passado, a função deve retornar uma lista contendo os nomes de todas as pessoas.

Nessa questão, se atentem ao fato de que, além do conjunto de dados, os parâmetros são opcionais, ou seja, a função pode ser chamada sem nenhum desses parâmetros extras, apenas com alguns deles ou com todos eles. Os parâmetros serão inicializados com valores nulos, ou seja, `name=None`, `min_age=None`, `max_age=None`, `city=None` e `hobbies=[]`. Dessa forma, é possível verificar se o parâmetro foi passado ou não, apenas verificando se ele é igual ao seu valor padrão.

Além disso, se atentem ao fato de que os parâmetros `min_age` e `max_age` são inteiros, ou seja, a função deve verificar se a idade da pessoa está nesse intervalo. Caso `min_age` seja maior que `max_age`, a função deve lançar uma exceção do tipo `ValueError`, que deve ser tratada e informar o usuário que `min_age` deve ser menor ou igual a `max_age`. Nesse caso, a função deve retornar uma lista vazia.

Por fim, não se esqueçam que, nessa questão, só deverão ser listados os nomes das pessoas que atendem **simultaneamente** a todos os critérios passados, ou seja, se uma pessoa possui dois hobbies e apenas um deles está na lista de hobbies passada, essa pessoa não deve ser listada.
