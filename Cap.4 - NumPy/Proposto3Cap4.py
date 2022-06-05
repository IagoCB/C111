import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

#1 Apresente a porcentagem de quantas missões deram certo
arr2= arr[1:,7].copy()

success= arr2[arr2 == 'Success'].size / arr2.size

print(f'Missoes bem sucedidas:{success: .2%}')

#2 Qual a média de gastos de uma missão espacial se baseando em missões que possuam valores disponíveis (>0)
arr3= arr[1:,6].copy()

print(f'Media de gastos {round(sum(map(float, arr3))/ arr3.size, 2)}')

#3 Encontre quantas missões espaciasis neste DataSet foram realizadas pelos EUA
arr4= arr[1:,2].copy()

usa = arr4[np.char.find(arr4,'USA') != -1].size

print(f'{usa} missoes foram realizadas pelos EUA')

#4 Encontre qual foi a missão mais cara realizada pela "SpaceX"

arr5 = arr[1:].copy()

arr5 = arr5[np.char.startswith(arr5[:,1],'SpaceX')].copy()

arr6 = arr5[:,6].copy()

max_value = np.max(list(map(float, arr6)))

print('Essas foram as missoes mais caras realizadas pela SpaceX:')
print(arr5[np.char.startswith(arr5[:,6],str(max_value))])


#5 Mostre o nome das empresas que já realizaram Missões Espaciais juntamente com sua respectivas quantidades de missões
arr5 = arr[1:].copy()
arr7 = arr[1:,1].copy()

tamanho = np.unique(arr7)

for i in tamanho:  
    print(f'A {i} realizou {arr5[np.char.startswith(arr5[:,1],i)].size} missoes') 