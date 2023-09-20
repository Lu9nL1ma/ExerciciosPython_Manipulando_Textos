# Exercício Python 06: Faça um programa que leia o nome completo de uma pessoa,
# Mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: ')).strip()
nome_fatiado = nome.split()

print('Seu primeiro nome é: {}'.format(nome_fatiado[0]))
print('Seu último nome é: {}'.format(nome_fatiado[len(nome_fatiado) - 1]))
