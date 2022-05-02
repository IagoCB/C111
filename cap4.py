from random import randint
import numpy as np

#1
arry = np.linspace(0,1,21,retstep = True)

print (arry)

#2
array1 = np.arange(0,51,2)
array2 = np.arange(100,50,-2)

array3 = np.sort(np.concatenate((array1,array2)))

print(array3)

#3

print(np.flip(array3))

#4
matriz = np.ones((3,4))

print(matriz)

print(matriz.reshape(1,12))

#5

num1 = randint(1,6)
num2 = randint(1,6)

matriz = np.ones((num1,num2))

x,y = matriz.shape

if((x * y) % 2 == 0):
    print('E um vetor com numero par de elementos')
else:
    print('E um vetor com numero impar de elementos')