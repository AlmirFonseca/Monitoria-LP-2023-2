import numpy as np

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

print("Tipo da lista1:", type(lista1))

arr1 = np.array(lista1)
arr2 = np.array(lista2).reshape(5, 1)

print("Tipo da arr1:", type(arr1))
print("Shape da arr1:", arr1.shape)
print("arr1:", arr1)

print("Tipo da arr2:", type(arr2))
print("Shape da arr2:", arr2.shape)
print("arr2:", arr2)

arr3 = arr1 * arr2

print("Tipo da arr3:", type(arr3))
print("Shape da arr3:", arr3.shape)
print("arr3:", arr3)

arr3 = arr3.reshape(1, 25)

print("Tipo da arr3:", type(arr3))
print("Shape da arr3:", arr3.shape)
print("arr3:", arr3)

arr4 = arr1 @ arr2

print("Tipo da arr4:", type(arr4))
print("Shape da arr4:", arr4.shape)
print("arr4:", arr4)

arr4 = arr4.reshape(1, 1)

print("Tipo da arr4:", type(arr4))
print("Shape da arr4:", arr4.shape)
print("arr4:", arr4)

arr4 = arr4.reshape(1, 1, 1)

print("Tipo da arr4:", type(arr4))
print("Shape da arr4:", arr4.shape)
print("arr4:", arr4)




# arr4 = arr5 = np.array(lista1 + lista2)

# print("Tipo da arr4:", type(arr4))
# print("arr4:", arr4)
# print("Tipo da arr5:", type(arr5))
# print("arr5:", arr5)


"""
import os -> os.ndarray           #
import numpy as np -> np.ndarray  #
from numpy import array -> array
from numpy import * -> array

"""
