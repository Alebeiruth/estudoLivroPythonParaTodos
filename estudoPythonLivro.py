##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 02
## 01 - USO DE VARIAVEIS E SEU TIPO

print(type('Hello World!'))
print(type(17))
print(type(17.5))

## 02 - OPERADORES, EXPRESSÕES, OPERANDOS

soma = 20 + 32
hora = 60 - 1
minutos = 30
horasEminutos = hora * 60 * minutos
divisaoHorasMinutos = minutos / 60
exponencia = 5 ** 2
divisaoInt = minutos // 60

print(f"Soma = {soma}, Subtração = {hora}, Multiplicação = {horasEminutos}, Divisão =  {divisaoHorasMinutos},  Exponenciação =  {exponencia}, Divisao Inteira = {divisaoInt}")

## ORDEM DAS OPREAÇÕES >> PEMDAS
## 1 - PARENTESES
## 2 - EXPONENCIAÇÃO
## 3 - MULTIPLICAÇÃO & DIVISÃO
## 4 - ADIÇÃO & SUBTRAÇÃO

## 03 - OPERADOR DE MODULO >> QUOCIENTE E RESTO

quociente = 7 // 3
print(quociente)

resto = 7 % 3
print(resto)

## 04 - OPERANDO COM STR

first = "106"
second = "901"
print(first + second)

testTres = "Teste "
tresVzs = 3
print(tresVzs * testTres)

## 05 - REQUISITANDO ENTRADA(VALORES) AO USER

nome = str(input("Qual seu nome: "))
print(f"Seu nome é {nome}! ")

## Erro de Syntax >> palavra escrita incorretamente, não segue regras gramaticais do Py
## Erro de Name >> nome da variavel está diferente ou não definido no escopo do programa
## Erro de Token >> caracter ou sequencia de caracteres que não faz sentido em Py

## EXERCICIOS CAPITULO 2
##2.2

nome = str(input("Qual seu nome: "))
print(f"Olá {nome}")

##2.3


hora = int(input("Quantas horas voce trabalha ao dia: "))
taxa = float(input("Qual a taxa: "))
print(f"Valor a ser pago: {hora * taxa.__round__()}")


##2.4

largura = 17
altura = 12.0

print(f"Quociente = {largura //2}, Divisão = {largura / 2.0}, Divisao Interia = {altura / 3}, Multiplicação e Soma = {1 + (2 * 5)} ")

##2.5

celsius = float(input("Qual a temperatura de hoje em Ceslius ? Digite ao lado: "))
print(f"A temperatura em Fahrenheit é {(celsius * 9/5) + 32} graus")


##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 03
## 06 - EXPRESSÃO BOLEANAS

five = 5 == 5
noFive = 5 == 6
print(five)
print(noFive)


x = 1
y = 2

print(x is y)
print(x is not y)
print(x != y) ##diferente
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

## 07 - OPERADORES LOGICOS >> AND, OR , NOT


x = 1
y = 3
n = 4
print(x > 0 and y < 10)
print(n % 2 == 0 or n % 3 == 0)
print(not(x > y))


## 08 - EXECUÇÃO DE CONSDICIONAL
## IF

a = 10
if a > 0:
    print(f"A = {a} é um número positivo")

## IF e ELSE

a = 4

if a % 2 == 0:
    print(f"O número {a} é par.")
else:
    print("O número é impar")

## 09 - CONDIÇÃO ENCADEADA

x = 2
y = 1
if x < y:
    print(f"O número {x} é menor que {y}")
elif x > y:
    print(f"O número {x} é maior que {y}")
else:
    print(f"O número {x} é {y} são iguais")

## 10 - CONDIÇÃO ANINHADAS
## TIPO DE ESTRUTURA A SER EVITADA
a = 3
b = 7

if a == b:
    print(f"{a} e {b} são iguais.")
else:
    if a < b:
        print(f"{a} é menor que {b}")
    else:
        print(f"{a} é maior que {b}")

## RESCRIÇÃO FACILITADA

w = 5
if 0 < w and w < 10:
    print(f"{w} é um numero positivo e só possui um digito")

## 11 - TRY E EXCEPT

inp = input("Enter com a temperatura em Fahrenheit: ")
try:
    fahr = float(inp)
    cels = (fahr - 32.0) * 5.0 / 9.0
    print(cels)
except:
    print("Por favor entre com um número")

## EXERCICIOS CAPITULO 3
##3.1

hora = int(input("Quantas horas voce trabalha ao dia: "))
taxa = float(input("Qual a taxa: "))
print(f"Valor a ser pago: {hora * taxa.__round__()}")

if hora >= 40:
    print((hora * taxa) * 1.5)
else:
    print(hora * taxa)

##3.2

entrada = input("Digite as horas: ")
tax = input("Digite a taxa: ")

try:
    intEntrada = int(entrada)
    intTax = int(tax)
    print(intEntrada * intTax)
except:
    print("Erro, por favor utilize uma entrada numérica")

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


##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 04

## 12 - FUNÇÃO DE CONVERSÃO DE TIPOS

print(float("3.12455"))
print(int(3.999998))
print(str(985) + " str")

## 13 - FUNÇÃO MATH

import  math

decibes = 10 * math.log10(10)
radianos = 0.7
modulo = math.sin(radianos)
print(modulo)

graus = 45
radianos2 = graus / 360.0 * 2 * math.pi
print(math.sin(radianos2))

print(math.sqrt(2) / 2.0)

## 14 - NUMEROS ALEATORIOS -> RANDOM, RANDINT, CHOICE

import random

for i in range(5):
    y = random.randint(5, 10)
    x = random.random()
    print(f"{i + 1} -> X = {x}, Y = {y}")

t = [1, 2, 3, 4, 5]
print(random.choice(t))

## 14 - ADC NOVAS FUNÇÕES

def Print_LetraDeMusica():
    return "Eu sou um lenhador, e eu estou bem.\nEu durmo a noite toda e trabalho o dia todo.\n"

def Repetir_LetraDeMusica():
    return 2 * Print_LetraDeMusica()

print(Print_LetraDeMusica())
print(Repetir_LetraDeMusica())

## 15 - PARAMETROS E ARGUMENTOS

bruce = " Bruce"
def mostraDuasVezes(str):
    return 2 * str

print(mostraDuasVezes(bruce))

## 16 - FUNÇÃO FRUTIFERA

def soma(x, y):
    return x + y

print(soma(1,2))

## EXERCICIOS CAPITULO 4
##4.6

hora = float(input("Quantas horas por dia voce trabalha: "))
extra = float(input("Qual a taxa: "))

def calculoPagamento(hora, taxaHora):
    pagamento = hora * taxaHora
    return f"Pagamento: {pagamento}"

print(calculoPagamento(hora, extra))

##4.7
pontos = input("Insira sua pontuação entre 0.0 a 1.0: ")

def computerNotas(pontuacao):

    try:
        pontos = float(pontuacao)

        if pontos >= 0.9:
            return f"Insira a pontuação: {pontos}\nA"
        elif pontos >= 0.8 and pontos < 0.9:
            return f"Insira a pontuação: {pontos}\nB"
        elif pontos >= 0.7 and pontos < 0.8:
            return f"Insira a pontuação: {pontos}\nC"
        elif pontos >= 0.6 and pontos < 0.7:
            return f"Insira a pontuação: {pontos}\nD"
        else:
            return f"Insira a pontuação: {pontos}\nF"

    except:
        return f"Pontuação Inválida"

print(computerNotas(pontos))



##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 05

## 17 - WHILE

n = 5 ##contador e parametro de parada para o WHILE

while n > 0:
    print(n)
    n = n - 1

print("Lançar")

## 18 - WHILE TRUE, CONTINUE E BREAK

while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done": ## codigo só para quando for escrito "done"
        break
    print(line)
print("Done!")

## 19 - LAÇO FOR

amigos = ["Jose", "Gleice", "Sara"]
for i in amigos:
    print("Feliz Ano Novo ", i)
print("Enviado")

## 19 - FOR, CONTADO E SOMANDO REPETIÇÕES

contador = 0
lista = [3, 41, 12, 9, 74, 15]

for iterar in lista:
    contador += 1

print(f"Contagem: {contador}")

## SOMANDO
total = 0

for i in [3, 41, 12, 9, 74, 15]:
    total += i
    
print(f"Soma total: {total}")

## 19 - FOR MAXIMOS E MINIMOS
## None é vazia

maximo = 0
lista1 = [3, 41, 12, 9, 74, 15]

print(f"Antes: {maximo}")

for i in lista1:
    if maximo is None or i > maximo:
        maximo = i
    print(f"Laço: {i}, {maximo}")
print(f"Máximo Atual: {maximo}")

minimu = None
lista1 = [3, 41, 12, 9, 74, 15]
print(f"Antes: {minimu}")

for i in lista1:
    if minimu is None or i < minimu:
        minimu = i
    print(f"Laço: {i}, {minimu}")
print(f"Minimo Atual: {minimu}")

## EXERCICIOS CAPITULO 5
##5.1

try:
    total = 0
    quantidade = 0

    while True:
        entrada = input("Digite um numero: ")

        if entrada == "pronto":
            break

        try:
            numero = int(entrada)

            if numero < 0:
                print("Número negativo não é permitido")
                continue
            total += numero
            quantidade += 1
        except ValueError:
            print("Entrada Invalida")
    if quantidade > 0:
        media = total / quantidade
        print(f"Soma total: {total}, Quantidae: {quantidade}, Média {media}")
    else:
        print("Número negativo não é permitido")
except KeyboardInterrupt:
    print("\nOperação interrupida pelo usuario")
except Exception as ex:
    print(f"Ocorreu erro {ex}")

print("Pronto")

##5.2

try:
    total = 0
    quantidade = 0
    max = None
    min = None
    lista = []

    while True:
        entrada = input("Digite um numero: ")

        if entrada == "pronto":
            break

        try:
            numero = int(entrada)

            if numero < 0:
                print("Número negativo não é valido")
                continue

            lista.append(numero)
            total += numero
            quantidade += 1

            if max is None or numero > max:
                max = numero

            if min is None or numero < min:
                min = numero

        except ValueError:
            print("Entrada Invalida")

    for i in lista:
        print(f"Laço: {i}, Maximo: {max}")

    for i in lista:
        print(f"Laço: {i}, Minimu: {min}")

except KeyboardInterrupt:
    print("Operação interrupida pelo usuario")
except Exception as ex:
    print(f"Ocorreu erro {ex}")

print("Pronto")


















