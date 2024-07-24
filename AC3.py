
num = []

def contador():
    n = int(input("Digite o N: "))
    for i in range(n):
        num.append(i+1)
        print(num)

resposta = contador()

#______________________________________________________________________________


def contador_dig():
    numero = int(input("Digite um número: "))
    numero = str(numero)
    print(len(numero))

resposta = contador_dig()

#______________________________________________________________________________

def divisao():

    div = None
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        div = n1/n2
    except ZeroDivisionError:
        print("Você não pode dividir por zero")
    except ValueError:
        print("Você deve digitar um número válido")
    finally:
        if div is not None:
            print(f"O resultado é {div}")
        else:
            print("Não é possível calcular o resultado")

reposta = divisao()