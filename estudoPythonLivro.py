##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 02
## 01 - USO DE VARIAVEIS E SEU TIPO

"""print(type('Hello World!'))
print(type(17))
print(type(17.5))"""

## 02 - OPERADORES, EXPRESSÕES, OPERANDOS

"""soma = 20 + 32
hora = 60 - 1
minutos = 30
horasEminutos = hora * 60 * minutos
divisaoHorasMinutos = minutos / 60
exponencia = 5 ** 2
divisaoInt = minutos // 60

print(f"Soma = {soma}, Subtração = {hora}, Multiplicação = {horasEminutos}, Divisão =  {divisaoHorasMinutos},  Exponenciação =  {exponencia}, Divisao Inteira = {divisaoInt}")"""

## ORDEM DAS OPREAÇÕES >> PEMDAS
## 1 - PARENTESES
## 2 - EXPONENCIAÇÃO
## 3 - MULTIPLICAÇÃO & DIVISÃO
## 4 - ADIÇÃO & SUBTRAÇÃO

## 03 - OPERADOR DE MODULO >> QUOCIENTE E RESTO

"""quociente = 7 // 3
print(quociente)

resto = 7 % 3
print(resto)"""

## 04 - OPERANDO COM STR
"""
first = "106"
second = "901"
print(first + second)

testTres = "Teste "
tresVzs = 3
print(tresVzs * testTres)"""

## 05 - REQUISITANDO ENTRADA(VALORES) AO USER

"""nome = str(input("Qual seu nome: "))
print(f"Seu nome é {nome}! ")"""

## Erro de Syntax >> palavra escrita incorretamente, não segue regras gramaticais do Py
## Erro de Name >> nome da variavel está diferente ou não definido no escopo do programa
## Erro de Token >> caracter ou sequencia de caracteres que não faz sentido em Py

## EXERCICIOS CAPITULO 2
##2.2

"""nome = str(input("Qual seu nome: "))
print(f"Olá {nome}")"""

##2.3

"""
hora = int(input("Quantas horas voce trabalha ao dia: "))
taxa = float(input("Qual a taxa: "))
print(f"Valor a ser pago: {hora * taxa.__round__()}")
"""

##2.4

"""largura = 17
altura = 12.0

print(f"Quociente = {largura //2}, Divisão = {largura / 2.0}, Divisao Interia = {altura / 3}, Multiplicação e Soma = {1 + (2 * 5)} ")"""

##2.5

"""celsius = float(input("Qual a temperatura de hoje em Ceslius ? Digite ao lado: "))
print(f"A temperatura em Fahrenheit é {(celsius * 9/5) + 32} graus")
"""

##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 03
## 06 - EXPRESSÃO BOLEANAS

"""five = 5 == 5
noFive = 5 == 6
print(five)
print(noFive)
"""

"""x = 1
y = 2

print(x is y)
print(x is not y)
print(x != y) ##diferente
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)"""

## 07 - OPERADORES LOGICOS >> AND, OR , NOT

"""
x = 1
y = 3
n = 4
print(x > 0 and y < 10)
print(n % 2 == 0 or n % 3 == 0)
print(not(x > y))
"""

## 08 - EXECUÇÃO DE CONSDICIONAL
## IF

"""a = 10
if a > 0:
    print(f"A = {a} é um número positivo")"""

## IF e ELSE

"""a = 4

if a % 2 == 0:
    print(f"O número {a} é par.")
else:
    print("O número é impar")"""

## 09 - CONDIÇÃO ENCADEADA

"""x = 2
y = 1
if x < y:
    print(f"O número {x} é menor que {y}")
elif x > y:
    print(f"O número {x} é maior que {y}")
else:
    print(f"O número {x} é {y} são iguais")"""

## 10 - CONDIÇÃO ANINHADAS
## TIPO DE ESTRUTURA A SER EVITADA
"""a = 3
b = 7

if a == b:
    print(f"{a} e {b} são iguais.")
else:
    if a < b:
        print(f"{a} é menor que {b}")
    else:
        print(f"{a} é maior que {b}")"""

## RESCRIÇÃO FACILITADA

"""w = 5
if 0 < w and w < 10:
    print(f"{w} é um numero positivo e só possui um digito")"""

## 11 - TRY E EXCEPT

"""inp = input("Enter com a temperatura em Fahrenheit: ")
try:
    fahr = float(inp)
    cels = (fahr - 32.0) * 5.0 / 9.0
    print(cels)
except:
    print("Por favor entre com um número")"""

## EXERCICIOS CAPITULO 3
##3.1

"""hora = int(input("Quantas horas voce trabalha ao dia: "))
taxa = float(input("Qual a taxa: "))
print(f"Valor a ser pago: {hora * taxa.__round__()}")

if hora >= 40:
    print((hora * taxa) * 1.5)
else:
    print(hora * taxa)"""

##3.2

"""entrada = input("Digite as horas: ")
tax = input("Digite a taxa: ")

try:
    intEntrada = int(entrada)
    intTax = int(tax)
    print(intEntrada * intTax)
except:
    print("Erro, por favor utilize uma entrada numérica")"""

##3.3

poin = input("Digite um numéro entre 0.0 a 1.0:  ")

try:
    point = float(poin)

    if point >= 0.9:
        print(f"Digite sua Pontuação: {point} = A")
    elif point >= 0.8 and point < 0.9:
        print(f"Digite sua Pontuação: {point} = B")
    elif point >= 0.7 and point < 0.8:
        print(f"Digite sua Pontuação: {point} = C")
    elif point >= 0.6 and point < 0.7:
        print(f"Digite sua Pontuação: {point} = D")
    else:
        print(f"Digite sua Pontuação: {point} = F")

except:
    print("Pontuação Invalida")


















