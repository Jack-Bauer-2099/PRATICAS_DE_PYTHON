"""
Autor: Jack Bauer
E-mail: jackbauer2018@protonmail.com
Versão: 1.0
Data: 15/08/2024
Lista de Exercícios em Python:
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
opcao=(int(input('Digite o numero referente ao seu sexo: (1) Masculino (2) Feminino\n')))
if opcao == 1:
    altura=(float(input("Digite a sua altura em metros:\n ")))
elif opcao == 2:
    altura=float(input("Digite a sua altura em metros:\n "))
else:
    print(f'Você digitou errado! Escolha entre o número (1) Masculino ou (2) Feminino. ')

if opcao ==1:
    peso_ideal=(altura*72.7) - 58
    print(f' Seu peso ideal deveria ser de: {peso_ideal:.2f}Kg')
elif opcao ==2:
    peso_ideal=(altura*62.1) - 44.7
    print(f'Seu peso ideal deveria ser de: {peso_ideal:.2f}kg')
else:
    print(f'Tente de novo. Insira o valor correto!!!')

# Este exercio está quase correto. Porém a versão 2 faz uma correção inserindo
#wile not in.