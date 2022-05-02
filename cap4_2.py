import numpy as np

#1

np.random.seed(5)

array = np.random.rand(10)

print((array*100).astype(int))

#2

np.random.seed(10)
matriz = (np.random.randint(1,51,16)).reshape(4,4)

print(matriz)

#3

media_linha = (matriz.sum(axis=1))/4
media_coluna = (matriz.sum(axis=0))/4

print(media_linha)
print(media_coluna)
print(f"Maior valor das medias das linhas: {max(media_linha)}" )
print(f"Maior valor das medias das colunas: {max(media_coluna)}")

#4

print(np.unique(matriz,return_counts=True))

elemento, conts = np.unique(matriz, return_counts= True)

for i, e in enumerate(elemento):
    if conts[i] >= 2:
        print(f"Elemento: {e} = {conts[i]}")