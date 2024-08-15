"""
Autor: Jack Bauer
E-mail: jackbauer2018@protonmail.com
Versão: 1.0
Data: 15/08/2024
Lista de Exercícios em Python:
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math

valor_raio=float(input("Insira o valor do raio:\n "))
pi=math.pi
#calculo
area=pi*(valor_raio**2)
print(f'A área calculada foi de {area:.2f}')

