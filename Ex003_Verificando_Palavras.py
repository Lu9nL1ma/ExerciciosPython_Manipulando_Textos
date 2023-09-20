# Exercício Python 03: Crie um programa que leia o nome de uma cidade
# E diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Qual o nome da cidade escolhida: ')).strip()
print(cidade[:5].upper() == 'SANTO')
