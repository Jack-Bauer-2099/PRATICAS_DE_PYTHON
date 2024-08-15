"""
Autor: Jack Bauer
E-mail: jackbauer2018@protonmail.com
Versão: 1.0
Data: 15/08/2024
Lista de Exercícios em Python:
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
ganho_por_hora=float(input('Insira o valor em R$ de quanto você ganha por hora:\n'))
horas_trabalhadas=int(input('Insira o valor em horas trabalhadas:\n'))
salario=ganho_por_hora*horas_trabalhadas
print(f'O seu salário referente aos dados informados é de R$:{salario:.2f}')