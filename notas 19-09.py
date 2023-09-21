"""
O que é NumPy?
"Numerical Python"; é um módulo feito em C/C++ voltado pra computação matemática


Pra que serve isso? Porque não podemos só usar listas?
- Mais eficiente (mais rápido, mais leve)
    -> de 50 a 100 vezes mais rápido q python
    -> Em python, um inteiro "pesa" 23 Bytes, e em numpy, apenas 4 Bytes (podendo escolher outras opções, como 1, 2, 8, 16...)
    -> Alocação Contínua de memória
- Broadcasting*
- Operadores puramente matemáticos (ex: multiplicação de matrizes) e matriciais
- Possui funções para Álgebra Linear (np.linalg)
- É base pra várias bibliotecas de Data Science (Pandas, Matplotlib, Seaborn)

O que é broadcasting?
"Operação aplicada element-wise (elemento a elemento)"
Ex:
Python "puro": [1, 2, 3] * 2 -> [1, 2, 3, 1, 2, 3]
numpy: np.array([1, 2, 3]) * 2 -> np.array([2, 4, 6])
Ex:
Python "puro": [1, 2, 3] / 2 -> ERRO
numpy: np.array([1, 2, 3]) / 2 -> np.array([0.5, 1, 1.5])
"""

import numpy as np

lista = [1, 2, 3, 4, 5]

# Definindo um np.array a partir de uma lista
array = np.array(lista)

print(array)

# Propriedades ######################################################################
"""
- Todos os elementos devem ter um mesmo tipo
- É iterável
- Não é possível adicionar ou remover elementos de um array
"""

# Atributos ######################################################################

print("Atributos (características)", "-="*10)

print("shape:", array.shape, sep="\n", end="\n\n") # formato do array
print("ndim:", array.ndim, sep="\n", end="\n\n") # número de dimensões
print("size:", array.size, sep="\n", end="\n\n") # número de elementos
print("dtype:", array.dtype, sep="\n", end="\n\n") # tipo de cada elemento
print("itemsize:", array.itemsize, sep="\n", end="\n\n") # tamanho, em bytes, de cada elemento

# Geradores automáticos ######################################################################

"""
np.zeros() -> matriz repleta de 0s
np.ones() -> matriz repleta de 1s
np.identity() -> matriz identidade nxn
np.eye() -> matriz com 1 na diagonal (a identidade, por padrão)
np.arange() -> array igualmente espaçados dado um intervalo (min, max) e pode escolher um stepsize
np.linspace() -> array igualmente espaçados dado um intervalo (min, max) e uma quantidade de elementos
"""

# Métodos e funções ######################################################################

array = np.array([[1, 2, 3], [4, 5, 6]])

print(array)

print("reshape:", array.reshape(3, 2), sep="\n", end="\n\n") # remodela o array
print("transpose:", array.transpose(), sep="\n", end="\n\n") # transpõe o array
print("min:", array.min(), sep="\n", end="\n\n") # o menor elemento do array
print("argmin:", array.argmin(), sep="\n", end="\n\n") # o menor elemento do array
print("max:", array.max(), sep="\n", end="\n\n") # o maior elemento do array
print("argmax:", array.argmax(), sep="\n", end="\n\n") # o maior elemento do array
print("ptp:", array.ptp(), sep="\n", end="\n\n") # range, a diferença entre o max e o min
print("sum:", array.sum(), sep="\n", end="\n\n") # a soma dos elementos do array
print("tolist:", array.tolist(), sep="\n", end="\n\n") # retorna uma cópia do array, transformando-a numa lista
print("copy:", array.copy(), sep="\n", end="\n\n") # cria uma "deep copy" do array

print("mean:", np.mean(array), sep="\n", end="\n\n") # media do array
print("median:", np.median(array), sep="\n", end="\n\n") # mediana do array
print("std:", np.std(array), sep="\n", end="\n\n") # desvio padrão do array
print("var:", np.var(array), sep="\n", end="\n\n") # variância do array
print("sort:", np.sort(array), sep="\n", end="\n\n") # ordena o array
print("unique:", np.unique(array), sep="\n", end="\n\n") # os elementos únicos do array

array2 = np.array([[7, 8, 9], [10, 11, 12]])

print("hstack:", np.hstack((array, array2)), sep="\n", end="\n\n") # concatena horizontalmente os arrays
print("hstack:", np.vstack((array, array2)), sep="\n", end="\n\n") # concatena verticaalmente os arrays
print("union1d:", np.union1d(array, array2), sep="\n", end="\n\n") # a união dos elementos dos arrays
print("intersect1d:", np.intersect1d(array, array2), sep="\n", end="\n\n") # a intersecção dos elementos dos arrays
print("setdiff1d:", np.setdiff1d(array, array2), sep="\n", end="\n\n") # os elementos de (1) que não estão em (2)

# Operadores ######################################################################

array1 = np.array([1, 2, 3])
array2 = np.array([[4], [5], [6]])

print(array1 * array2) # = np.multiply() (element-wise)

# Máscara ######################################################################
# "a boolean array of the same shape as array"

# mask <- vetor de booleanos (broadcasting)
mask = array > 2

print("ARRAY:", array)
print("MASK:", mask)
print("ARRAY[MASK]:", array[mask]) # Retorna só os elementos onde a máscara é verdadeira

array[array > 2]

# Usamos "~" para inverter uma máscara
array[~mask] # é igual a array[array <= 2]


print("isin:", np.isin(array, array2), sep="\n", end="\n\n")

