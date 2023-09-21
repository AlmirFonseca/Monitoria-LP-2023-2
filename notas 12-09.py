# import numpy as np

a = 10

# print(isinstance(a, int))

"""
try:

    BLOCO QUE PODE DAR ERRO

except -----:

except -----:

except (-----, ------) -> exceções agrupadas (OR)

except ------ as XX: -> "apelido" pro seu erro

    print(XX.__class__)

except:

    BLOCO QUE É EXECUTADO CASO DÊ ERRO

else:

    BLOCO QUE É EXECUTADO CASO NAAAAAAAAAO DÊ ERRO

finally:

    BLOCO QUE É EXECUTADO NO FINAL (COM OU SEM ERRO)

"""

# def divisao(x, y):

#     Try

#     return x / y

# print(divisao(1, "J"))


"""

* For e while aceitam else CASO NÃO SEJA EXECUTADO O BREAK -> INDICA QUE TODAS AS ITERAÇÕES FORAM REALIZADAS

"""

# for i in range(10):
#     print(i)

#     if i == 15:
#         break
# else:
#     print("ELSE")

# i = 110
# while i < 10:
#     print(i)

#     i += 5
# else:
#     print("ELSE")

"""

try:

    ABRIR UM ARQUIVO

except:

    IMPRIMO O ERRO

else:

    IMPRIMO QUE HOUVE SUCESSO

finally:

    FECHO O ARQUIVO

"""

"""

raise -> "levanta" um erro MANUALMENTE

raise
raise ValueError
raise ValueError("não tem como dividir por zero, chefe ;-;")



Posicionamos uma assertiva pra fins de DESENVOLVIMENTO

assert -> "levanta" um erro COM BASE EM UMA CONDIÇÃO
SE A CONDIÇÃO FOR VERDADEIRA -> CONTINUA
SE A CONDIÇÃO FOR FALSE -> levanta um Assertion Error (um tipo de exceção)

* Geralmente, não colocamos assertivas dentro do try/except para facilitar o monitoramento de erros
** Alguns compiladores conseguem "ignorar" de forma automática a assertiva durante deploys

"""