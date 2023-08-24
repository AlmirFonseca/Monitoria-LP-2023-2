"""
Estruturas de dados
"""

# Lista (List): []

lista = [1, 2, 3]

# Listas podem conter elementos de tipos diferentes
lista = [1, "A", False]

# Listas podem conter outras listas
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_interior = lista[0]

# Listas podem conter duplicatas
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3]

# Tamanho da lista
print("Tamanho da lista:", len(lista))

# Acesso a item de uma lista
print("Primeiro elemento da lista:", lista[0]) # Primeiro elemento

# É uma estrutura mutável
lista[0] = 10
print("Primeiro elemento da lista:", lista[0]) # Primeiro elemento

# Adicionar elemento ao final da lista
lista.append(4)
print("Lista:", lista)

# Adicionar elemento no início da lista
lista.insert(0, 0)
print("Lista:", lista)

# Remover elemento da lista
lista.remove(10) # Remove o primeiro elemento com valor 10
print("Lista:", lista)

# Slices [a:b) -> (start, stop, step)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista:", lista) # Lista completa
print("Lista[0]:", lista[0]) # Primeiro elemento
print("Lista[0:3]:", lista[0:3]) # Primeiros 3 elementos
print("Lista[::-1]:", lista[::-1]) # Lista invertida
print("Lista[::2]:", lista[::2]) # Elementos de 2 em 2
print("Lista[1::2]:", lista[1::2]) # Elementos de 2 em 2 a partir do segundo elemento
# Indices negativas
print("Lista[-1]:", lista[-1]) # Último elemento
print("Lista[-3]:", lista[-3]) # Terceiro elemento a partir do final

# Operações com listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Concatenação
lista3 = lista1 + lista2
print("Lista concatenada:", lista3)

# Repetição
lista4 = lista1 * 3
print("Lista repetida:", lista4)

# Ordenação
lista5 = [5, 4, 3, 2, 1]
# Ordenação inplace (modifica a lista original)
lista5.sort() 
print("Lista ordenada (inplace):", lista5) 
# Ordenação não inplace (não modifica a lista original)
lista5 = [5, 4, 3, 2, 1]
lista5_ordenada = sorted(lista5)
print("Lista ordenada (não inplace):", lista5_ordenada)
print("Lista original:", lista5)

# Tupla (Tuple): ()

# Diferente de listas, tuplas são imutáveis
tupla = (1, 2, 3)
print("Tupla:", tupla)
# tupla[0] = 10 # Erro

# Tuplas podem conter elementos de tipos diferentes
tupla = (1, "A", False)
print("Tupla:", tupla)

# Tuplas podem conter outras tuplas
tupla = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Tamanho da tupla
print("Tamanho da tupla:", len(tupla))

# Acesso a item de uma tupla
print("Primeiro elemento da tupla:", tupla[0]) # Primeiro elemento

# Slices [a:b) -> (start, stop, step)
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Tupla:", tupla) # Tupla completa
print("Tupla[0]:", tupla[0]) # Primeiro elemento
print("Tupla[0:3]:", tupla[0:3]) # Primeiros 3 elementos

# Empacotar tupla (packing)
tupla = (1, 2, 3)
print("Tupla:", tupla)

# Desempacotar tupla (unpacking)
a, b, c = tupla
print("a:", a)
print("b:", b)
print("c:", c)

# Dicicionario (Dict): {}

# Dicionários são estruturas de dados que armazenam pares chave-valor
dicionario = {"chave1": "valor1", "chave2": "valor2"}
print("Dicionário:", dicionario)

# Tamanho do dicionário
print("Tamanho do dicionário:", len(dicionario))

# Métricas do dicionário
print("Chaves do dicionário:", dicionario.keys()) # Chaves
print("Valores do dicionário:", dicionario.values()) # Valores
print("Itens do dicionário:", dicionario.items()) # Itens, que são tuplas (chave-valor)

# Conversão de dicionário para lista
lista = list(dicionario.items())

# Dicionários são mutáveis
dicionario["chave1"] = "novo_valor"
print("Dicionário:", dicionario)

# Dicionarios também podem conter dicionários
dicionario = {"chave1": {"chave2": "valor2"}}
print("Dicionário:", dicionario)

# Acesso a item de um dicionário
print("Valor da chave1:", dicionario["chave1"]) # Acesso "fraco"
# print("Valor da chave_inexistente:", dicionario["chave_inexistente"]) # Erro (chave não existe)
print("Valor da chave1:", dicionario.get("chave1")) # Acesso "forte"
# Em caso de chave inexistente, retorna None (esse comportamento pode ser alterado)
print("Valor da chave_inexistente:", dicionario.get("chave_inexistente", "ainda não existe"))

# Adicionar novo par chave-valor
dicionario["chave3"] = "valor3" # Maneira mais simples
print("Dicionário:", dicionario)
dicionario.update({"chave4": "valor4"}) # Maneira mais completa
print("Dicionário:", dicionario)

# Remover par chave-valor
del dicionario["chave1"]
print("Dicionário:", dicionario)

# Conjunto (Set): {}

# Tendo visto uma {}, não é possível afirmar de que se trata um dicionário ou um conjunto, a menos que sejam adicionados elementos
conjunto = {1, 2, 3}

# Conjuntos não podem conter elementos duplicados
conjunto = {1, 1, 1, 2, 2, 3, 3, 3, 3}
print("Conjunto:", conjunto)

# Tamanho do conjunto
print("Tamanho do conjunto:", len(conjunto))

# Operações com conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# União
conjunto3 = conjunto1 | conjunto2

# Interseção
conjunto4 = conjunto1 & conjunto2

# Ordenar lista usando conjunto (remove duplicatas)
lista = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]
lista_ordenada = sorted(set(lista))
print("Lista ordenada:", lista_ordenada)