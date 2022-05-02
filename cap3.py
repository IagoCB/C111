#1
print("EXERCÍCIO 01")
lista = ['Barcelona', 'Manchester United', 'Bayern Munchen', 'Santos', 'Real Madrid']

#a
print('Os 3 primeiros')
for x in range(0, 3):
    print(lista[x])

#b
print('Os 2 ultimos')
for y in range(4, 2, -1):
    print(lista[y])

#c
lista_ordenada = sorted(lista)
print(lista_ordenada)

#d
for z in range(0, 5):
    if( lista[z] == 'Barcelona'):
        print(z+1)
        break

#2
print("\nEXERCÍCIO 02")
Loja1 = {'Motorola'}
Loja2 = {'Xiaomi', 'iPhone', 'Motorola'}
modelos = Loja1 | Loja2
print(Loja1)
print(Loja2)
print(modelos)
print(Loja1 & Loja2)

#3
print("\nEXERCÍCIO 03")
nome = input("Nome do Aluno: ")
media = int(input("Média: "))

boletim = {
    'Nome': nome, 
    'Média': media
}

if media >= 60:
    print('AP')
    boletim['Situação'] = 'AP'
else:
    print('RP')
    boletim['Situação'] = 'RP'

print(boletim)