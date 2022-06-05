from re import A
import numpy as np

# #1 
lista = []

cadastrar = bool

cadastrar = True

while(cadastrar): 
    nome = input("Nome da Musica: ")
    ano = input("Ano da Musica: ")
    dicionario = {"nome": nome, "ano": ano}
    lista.append(dicionario)  
    cadastrar = input("Deseja continuar cadastrando?(Sim/Não): ")
    if( cadastrar == 'Sim'):
        cadastrar = True
    else:
        cadastrar = False  

print(len(lista))

min_year = 9999
temp_year = 0
index = int
for i in range(len(lista)):
    temp_year = int(lista[i]['ano'])
    if min_year > temp_year:
        min_year = temp_year
        index = i

print(lista[index])

#2
nomes1 = np.array(['Iago', 'Luiz', 'Carlos', 'Juan'])
nomes2 = np.array(['Rafaela', 'Celeucia', 'Jão', 'Maria'])

nomes = np.concatenate((nomes1,nomes2))

nomes = nomes.reshape(2,4)

print(np.flip(np.sort(nomes)))

#3

colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1],"hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1],"hex": "#0F0"}},
    {"color": "yellow", "type": "primary","code": {"rgba": [255,255,0,0.7],"hex": "#FF0"}},
    {"color": "blue", "type": "primary","code": {"rgba": [0,0,255,1],"hex": "#00F"}}
]

#a

for i in range(len(colors)):
    if colors[i]["type"] == "primary":
        print(colors[i]["color"])

#b

for i in range(len(colors)):
    if colors[i]["code"]["rgba"][2] == 255:
        print(colors[i]["code"]["hex"])

#c
aux = []

for i in range(len(colors)):    
    aux.append(colors[i]["color"])
    aux.append(colors[i]["code"]["hex"])

lista = np.array(aux)
print(lista)

#d

lista = lista.reshape(4,2)
print(lista)

#e

new = lista

new[new[:,0:] == 'black'] = 'preto'  
new[new[:,0:] == 'green'] = 'verde'    
new[new[:,0:] == 'yellow'] = 'amarelo'    
new[new[:,0:] == 'blue'] = 'azul'

print(new)