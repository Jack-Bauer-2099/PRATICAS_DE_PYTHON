"""
Autor: Jack Bauer
E-mail: jackbauer2018@protonmail.com
Versão: 1.0
Data: 15/08/2024
Lista de Exercícios em Python:
Faça um Programa que dê a opção do usuário escolher para converter as
temperaturas de graus Celsius para Fahrenheit e de Fahrenheit para celsius e imprima o resultado.
"""
option=int(input('Escolha qual tipo de conversão você deseja:(1) Celsius para Fahrenheit (2) Fahrenheit para Celsius\n'))
temperatura=float(input("Digite a temperatura a ser convertida:\n "))

if option==1:
    celsius_fahrenheit = (temperatura * 9 / 5) + 32
    print(f'A conversão solicitada é de {celsius_fahrenheit:.1f} graus Fahrenheit')
elif option==2:
    fahrenheit_celsius = (temperatura-32)*5/9
    print(f'A conversão solicitada é de {fahrenheit_celsius:.1f} graus Celsius')
else:
    print(f'Você escolheu a opção errada! Não haverá conversão. Você deve escolher entre a opção 1 (celsius) ou 2(fahrenheit)!')

