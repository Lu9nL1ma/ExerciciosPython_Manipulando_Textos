# Exercício Python 02: Faça um programa que leia um número de 0 a 9999
# E mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('O número digitado foi: {}'.format(numero))
print('Sua unidade é: {}'.format(unidade))
print('Sua dezena é: {}'.format(dezena))
print('Sua centena é: {}'.format(centena))
print('Sua milhar: {}'.format(milhar))
