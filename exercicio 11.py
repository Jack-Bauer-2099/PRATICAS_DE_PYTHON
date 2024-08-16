"""
Autor: Jack Bauer
E-mail: jackbauer2018@protonmail.com
Versão: 1.0
Data: 15/08/2024
Lista de Exercícios em Python:
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""
num1=int(input('Insira o primeiro número\n'))
num2=int(input('Insira o segundo número\n'))
num3=float(input('Insira o terceiro número\n'))

conta1=(2*num1)+(0.5*num2)
conta2=(3*num1)+num3
conta3=(num3**3)

print(f'a) tem como resulltado: {conta1}')
print(f'b) tem como resulltado: {conta2}')
print(f'c) tem como resulltado: {conta3}')

