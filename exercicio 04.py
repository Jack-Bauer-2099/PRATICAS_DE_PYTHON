"""
Autor: Jack Bauer
E-mail: jackbauer2018@protonmail.com
Versão: 1.0
Data: 15/08/2024
Lista de Exercícios em Python:
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
nota1=float(input('Insira a sua primeira nota do bimestre\n'))
nota2=float(input('Insira a sua segunda nota do bimestre\n'))
nota3=float(input('Insira a sua terceira nota do bimestre\n'))
nota4=float(input('Insira a sua quarta nota do bimestre\n'))
media=(nota1+nota2+nota3+nota4)/4
print(f'A sua média de notas bimestrais foi de:{media:.2f}')
