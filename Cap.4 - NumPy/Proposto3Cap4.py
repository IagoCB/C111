import numpy as np

arr = np.loadtxt('./space.csv', delimiter=';', dtype=str, encoding='utf-8')

#1
arr2= arr[1:,7].copy()

success= arr2[arr2 == 'Success'].size / arr2.size

print(f'Missoes bem sucedidas:{success: .2%}')

#2

arr3= arr[1:,6].copy()

print(f'Media de gastos {round(sum(map(float, arr3))/ arr3.size, 2)}')

#3

arr4= arr[1:,2].copy()

usa = arr4[np.char.find(arr4,'USA') != -1].size

print(f'{usa} missoes foram realizadas pelos EUA')

#4

arr5 = arr[1:].copy()

arr5 = arr5[np.char.startswith(arr5[:,1],'SpaceX')].copy()

arr6 = arr5[:,6].copy()

max_value = np.max(list(map(float, arr6)))

print('Essas foram as missoes mais caras realizadas pela SpaceX:')
print(arr5[np.char.startswith(arr5[:,6],str(max_value))])


#5
arr5 = arr[1:].copy()
arr7 = arr[1:,1].copy()

tamanho = np.unique(arr7)

for i in tamanho:  
    print(f'A {i} realizou {arr5[np.char.startswith(arr5[:,1],i)].size} missoes') 