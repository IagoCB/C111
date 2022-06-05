import numpy as np
import pandas as pd

# carregando um data-set usando pandas
dfPaises = pd.read_csv('paises.csv', delimiter=';')

#1
#a
paisesOceania = dfPaises['Country'][dfPaises['Region'].str.contains('OCEANIA')]

print('Paises que sao da Oceania')
print(paisesOceania)
print('-'*60)

#b
print('Quantidade de paises na Oceaenia: ', len(paisesOceania))
print('-'*60)
#2
taxasGlobais = dfPaises['Literacy (%)']
mediaTaxasGlobais = np.mean(taxasGlobais)
print('Media da taxa de alfabetizacao Global: ',mediaTaxasGlobais )
print('-'*60)

#3
paisMaiorPop = dfPaises[['Country','Region']][dfPaises['Population'] == max(dfPaises['Population'])]

print('Pais e Regiao com a maior populacao: ')
print(paisMaiorPop)
print('-'*60)

#4
paisesSemCosta = dfPaises['Country'][dfPaises['Coastline (coast/area ratio)'] == 0]

paisesSemCosta.to_csv('Paises_Sem_Costa.csv', sep=';', header=False)