# Exercício Python 05: Faça um programa que leia uma frase pelo teclado
# E mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez
# E em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).lower().strip()
print('A sua frase possui {} vezes a letra A'.format(frase.count('a')))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('a')+1))
print('A última vez que A apareceu foi na posição: {}'.format(frase.rfind('a')+1))
