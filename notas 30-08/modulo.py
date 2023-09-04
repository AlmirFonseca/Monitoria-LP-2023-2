# Definição de funções

"""
def NOME_DA_FUNCAO (ARGUMENTOS):
    
    CODIGO_DA_FUNCAO

    return VALOR_A_SER_RETORNADO
"""

def soma(a, b):

    s = a + b

    return a + b

# Soma a partir de valores inteiros
# soma1 = soma(1, 2)
# print(soma1) # print(soma(1, 2))

# Soma a partir de variáveis
a = 2
b = 4
# print(soma(a, b))

# print(soma(1)) # TypeError: soma() missing 1 required positional argument: 'b'

# print(soma(1, 2, 3)) # TypeError: soma() takes 2 positional arguments but 3 were given

# print(soma(b=10, a=20)) # Posso colocar os argumentos fora da ordem, desde que eu os especifique

# def multiplicacao(a, b): # Definição com argumentos posicionais OBRIGATÓRIOS
# def multiplicacao(a=0, b=0): # Definição com argumentos posicionais FACULTATIVOS (argumentos padrão)
# def multiplicacao(param1, param2, param3=1, param4=1): # Os argumentos posicionais sempre vêm primeiro 
def multiplicacao(elemento1, elemento2, *outros_elementos): # Args (*) (opcionais) -> receber um número extra de parâmetros no formato de uma tupla acessível dentro da função
    print(type(elemento1))
    print(type(elemento2))
    print(type(outros_elementos))
    print("outros elementos:", outros_elementos)

    if len(outros_elementos) == 0: # Se não foram passados argumentos extras
        return elemento1*elemento2 # RETURN: para imediatamente uma função e retorna o seu valor 
    else: # Se forem passados argumentos extras
        resultado = elemento1*elemento2

        for elemento in outros_elementos:
            resultado = resultado * elemento

        return resultado

# print(multiplicacao(1,2)) # Funciona
# print(multiplicacao(1,2,3,4,5,6,7,8,9)) # Funciona

# def multiplicacao(elemento1, elemento2, **outros_elementos): # Kwargs