"""
Autor: Jack Bauer
E-mail: jackbauer2018@protonmail.com
Versão: 1.0
Data: 15/08/2024
Lista de Exercícios em Python:
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
temp_fah=float(input('Insira o valor da temperatura em graus Fahrenheit:\n '))
temp_celso=5*((temp_fah-32)/9)
print(f'A conversão foi de: {temp_celso:.1f} graus Celsius')
