import random
import sys


def tamanho():
    tamanhodado = input("Forneça o tamanho do dado que será rolado (ENTER para sair): ")
    if not tamanhodado.isdigit():#verifica se é string
        print('Programa encerrado')
        sys.exit()
    else:
        tamanhodado = int(tamanhodado)
        if tamanhodado < 1:
            print('O número passado deve ser maior que zero!')
            sys.exit()
        else:
            return tamanhodado


def numdados():
    numd = input("Forneça o número de dados que serão rolados (em branco == 1): ")
    if not numd.isdigit():#verifica se é string
        return 1
    else:
        numd = int(numd)
        while numd < 1:
            numd = input("Digite o número de dados: ")
            numd = int(numd)
        else:
            return numd

def girar_dado(x,y):
    for i in range(y):
        resultado = random.randint(1,x)
        print('Lançamento n.',(i+1),' -> ',resultado)

tamanho_do_dado = tamanho()
numero_de_dados = numdados()
print(numero_de_dados,' dado(s) de ',tamanho_do_dado,' lados:')
resultadodado = girar_dado(tamanho_do_dado,numero_de_dados)

import sys

resultado = 0.0

def start():
    input("Aperte ENTER para continuar!")

def calculadora():
    global resultado
    while True:
        print(resultado)
        n1 = input("Informe um número, ou aperte ENTER para sair: ")
        if not n1.isdigit():
            print("Calculadora encerrada")
            sys.exit()
        else:
            n1 = float(n1)
            print(n1)

        op = input("Operação (+, -, *, /), X para zerar ou Enter para sair: ")
        if not (op == "+" or op == "-" or op == "*" or op == "/" or op.lower() == "x"):
            print("Calculadora encerrada")
            sys.exit()
        elif op.lower() == "x":
            resultado = 0
        else:
            n2 = input("Informe um número, ou aperte ENTER para sair: ")
            if not n2.isdigit():
                print("Calculadora encerrada")
                sys.exit()
            else:
                n2 = float(n2)
                print(n2)

            if op == "+":
                resultado = n1 + n2
            elif op == "-":
                resultado = n1 - n2
            elif op	 == "*":
                resultado = n1 * n2
            elif op == "/":
                if n2 != 0:
                    resultado = n1 / n2
                else:
                    print("Não é possivel dividir por zero!")
            else:
                print("Operação inválida")


# start()
# calculadora()