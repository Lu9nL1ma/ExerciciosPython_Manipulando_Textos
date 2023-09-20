# Exercício Python 25: Crie um programa que leia o nome de uma pessoa
# E diga se ela tem “SILVA” no nome.

nome = str(input('Insira o seu nome: ')).strip()
print('O seu nome tem Silva? {}'.format('silva' in nome.lower()))
