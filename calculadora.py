from math import *

def soma():
    x = float(input("\nPrimeiro número: "))
    y = float(input("Segundo número: "))
    print("Soma", x+y)

def subtracao():
    x = float(input("\nPrimeiro número: "))
    y = float(input("Segundo número: "))
    print("Subtracao: ",x-y)

def multiplicacao():
    x = float(input("\nPrimeiro número: "))
    y = float(input("Segundo número: "))
    print("Multiplicação: ",x*y)

def divisao():
    x = float(input("\nPrimeiro número: "))
    y = float(input("Segundo número: "))
    print("Divisão: ",x/y)
    
def raiz_quadrada():
    x = float(input("\nNúmero que deseja saber a raiz quadrada: "))
    print(sqrt(x))
    
def potencia():
    x = float(input("\nPrimeiro número: "))
    y = float(input("Segundo número: "))
    print(pow(x,y))
    
def seno():
    x = float(input("\nNúmero que deseja saber o seno: "))
    print(sin(x))

def cosseno():
    x = float(input("\nNúmero que deseja saber o cosseno: "))
    print(cos(x))

def tangente():
    x = float(input("\nNúmero que deseja saber a tangente: "))
    print(tan(x))


while True:
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    print("5. Raiz quadrada ")
    print("6. Potenciação")
    print("7. Seno")
    print("8. Cosseno")
    print("9. Tangente")
    opcao = int(input('\nOlá, seja bem vindo à nossa calculadora, selecione uma opção: '))
    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    elif opcao == 5:
        raiz_quadrada()
    elif opcao == 6:
        potencia()
    elif opcao == 7:
        seno()
    elif opcao == 8:
        cosseno()
    elif opcao == 9:
        tangente()
    else:
        print("\nValor invalido")
    controle = input('\npressione "enter" para parar ou um número para continuar ')
    if controle.isnumeric():
        continue
        
    else:
        print('\nObrigado por usar nossa calculadora')
        print('\nAss. Juan e Jessica')
        break