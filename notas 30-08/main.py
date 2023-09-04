# import modulo # Importação simples
# -> modulo.soma(a, b)

# import modulo as mo # Importação com alias ("apelido")
# -> mo.soma(a, b)

# from modulo import soma # Importação de funções específicas
# -> soma(a, b)

# from modulo import * # Importação com "wild card" (*) -> NÃO É UMA BOA PRÁTICA
# -> soma(a, b)

# Estruturas de repetição

# lista = list(range(10))

# print("Imprimindo uma lista:", lista)

"""
for ELEMENTO in ITERAVEL:
    FAÇA ISSO
"""

# for elemento in lista:
#     print(elemento)

"""
while CONDIÇÃO (booleano) FOR VERDADE:
    FAÇA ISSO
"""

# i = 1

# while i < 10:
#     print(i)
#     i += 1 # i = i + 1 ou i++

# while i: # Sem condição de parada -> PROBLEMA (loop infinito)
#     print(i)
#     i += 1 # i = i + 1 ou i++

# while i == "PROGRAMACAO": # Condição de parada inicialmente falsa -> PROBLEMA (ele nunca "entra" no loop)
#     print(i) 
#     i += 1 # i = i + 1 ou i++

# while True:
#     print(i)
#     i += 1 # i = i + 1 ou i++

#     if i > 10:
#         break # interrompe instantenamente o loop, e "pula" pra fora do loop

#     print("após o if")

# print("fora do while")

# print(modulo.a) # Imprimindo variavel de outro modulo

# print(modulo.soma(1, 2)) # Executando função de outro modulo



