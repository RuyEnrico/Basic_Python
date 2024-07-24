#Monte uma função que recebe um salário por hora e o número de horas trabalhadas no mês, e retorne o salário a ser recebido.

Salario_hora = float(input("Digite quanto ganha por hora: "))
horas_trab = int(input("Digite quantas horas trabalhou no mês: "))

def calculo_salario_mes(x,y):
    salario = x*y
    return salario

salario_mes = calculo_salario_mes(Salario_hora,horas_trab)
print("seu salario esse mês foi de:",salario_mes)

#Elabore uma função que receba três números e exiba na tela: 
#(1) o produto do dobro do primeiro com metade do segundo;
#(2) a soma do triplo do primeiro com o terceiro; e 
#(3) o terceiro elevado ao cubo.
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))

def numeros(x,y,z):
    a = (x*2) * (y/2)
    b = (3*x) + z
    c = z**3
    return a,b,c

print(numeros(num_1,num_2,num_3))

#Elabore uma função com as mesmas regras do exercício anterior, 
#porém retornando os três resultados, ao invés de exibi-los na tela.
#Elabore uma função que receba três números e exiba na tela: 

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))

def numeros(x,y,z):
    a = (x*2) * (y/2)
    b = (3*x) + z
    c = z**3
    return a,b,c

#Elabore uma função que receba uma variável inteira ano.
#Em seguida, retorne o resultado da expressão lógica que indica se um ano é ou não bissexto.
#Um ano é bissexto se ele é múltiplo de quatro.
#No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
#Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

ano = int(input("Digite o ano: "))

def bissexto(x):
    b = (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)
    return b

print("O ano ",ano," é bissexto? ", bissexto(ano))