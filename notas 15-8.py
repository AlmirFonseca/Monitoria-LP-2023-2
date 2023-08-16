"""
Monitoria de Linguagem de Programação
15/08/2023 - 18hrs
"""

###################################################################################

# Comentários (linha única)

"""
Comentários
em
bloco
"""

###################################################################################

# Definição de variáveis (a variável 'a' recebe o valor 10)
# Não é necessário definir o tipo da variável

a = 10

# Aqui, imprimimos o tipo e o valor da variável 'a' (<class 'int'> 10)
print(type(a), a)

# Sobrescrevendo o valor da variável 'a' para 20
a = 20

print(type(a), a)

# Sobrescrevendo o valor da variável 'a' para "F"
# Nesse caso, o tipo da variável 'a' é alterado para <class 'str'>
a = "F"

print(type(a), a)

###################################################################################

b = 20

# Estruturas de decisão

# Exemplo de estrutura de decisão em C/C++:

# if (a == 10){
#     ...
# }

# Já em python, não é necessário utilizar parênteses e chaves, mas é necessário utilizar ":" e a identação

if a == 10:
    print("A é igual a 10")

# Os operadores lógicos também são diferentes:

#============================================

# C/C++                          Python
# &&                             and

# if (a == 10 && b == 20){
#     ...
# }

if a == 10 and b == 20:
    print("A é igual a 10 e B é igual a 20")

#============================================

# C/C++                          Python
# ||                             or

# if (a == 10 || b == 20){
#     ...
# }

if a == 10 or b == 20:
    print("A é igual a 10 ou B é igual a 20")

#============================================

# C/C++                          Python
# !                              not

# if !(a == 10){
#     ...
# }

if not a == 10:
    print("A não é igual a 10")

# Estruturas de decisão aninhadas

a = 12
b = 15

# Em C/C++, usamos "if", "else if" e "else"

# if (a == 10){
#     ...
# } else if (a < 10){
#     ...
# } else {
#     ...
# }

# Já em python, usamos "if", "elif" e "else"
# Ou seja, "elif" é a junção de "else" e "if"

# if a == 10:
#     ...
# elif a < 10:
#     ...
# elif a > 10 and a < 20:
    
#     if (b == 15):
        
#         print("CD >> MAp")
#         print()
# elif a < -1 or a > 100:
#     ...
# else:
#     ...

# Exemplo de estrutura de decisão aninhada

# Definindo variáveis
aluno = "Almir" 
semestre = 4

# Se o aluno não for o Almir, imprime "Ih, aluno diferente"
if aluno != "Almir":
    print("Ih, aluno diferente")

# Caso contrário (se o aluno for o Almir), verifica o semestre
else:

    # Se o semestre for maior que 7, imprime "TAMO QUASE FORMANDO"
    if (semestre > 7):
        print("TAMO QUASE FORMANDO")

    # Se o semestre for menor que 7, imprime "Poxa, tem muito tabalho a fazer"
    else:
        print("Poxa, tem muito tabalho a fazer")


###################################################################################

# Print e print formatado

# Imprime o valor das variáveis 'aluno' e 'semestre' separados por um espaço (padrão)
print(aluno, semestre)

# Imprime o valor das variáveis 'aluno' e 'semestre' separados por um traço
print(aluno, semestre, sep="-")

# Imprime o valor das variáveis 'aluno' e 'semestre' separados por um traço e com um ponto no final
print(aluno, semestre, sep="-", end=".")

# Imprime o valor das variáveis 'aluno' e 'semestre', além de outras strings
print("O aluno", aluno, "está matriculado na", semestre, "° série")

# Formata a string com os valores das variáveis 'aluno' e 'semestre' e imprime o resultado já formatado
print(f"O aluno {aluno} está matriculado na {semestre}° série")