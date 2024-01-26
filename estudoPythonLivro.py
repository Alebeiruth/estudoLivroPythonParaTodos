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


##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 06

##STRING

fruta = "banana"
letra = fruta[0]
print(letra)

##LEN

fruta = "banana"
comprimento = len(fruta)
ultimaLetra = fruta[comprimento - 1]

print(len(fruta))
print(ultimaLetra)

##LAÇO EM STRINGs

fruta = "banana"
indice = 0

while indice < len(fruta):
    letras = fruta[indice]
    print(letras)
    indice += 1

## EXERCICIOS CAPITULO 6
##6.1

fruta = "banana"
index = len(fruta) - 1

while index >= 0:
    letrasContrarias = fruta[index]
    print(letrasContrarias)
    index -= 1

## SEGMENTOS EM STRINGs

s = "Monty Python"
fruta = "banana"
print(s[0:5]) ## 0 inclui o primeiro numero e 5 exclui o ultimo
print(s[6:12])
print(fruta[:3]) ## começa do inicio até 3
print(fruta[3:]) ## começa do 3 até o ultimo
print(fruta[:]) ## printa tudo
print(fruta[3:3]) ## string vazia

## LAÇO E CONTAGEM

palavra = "banana"
count = 0

for i in palavra:
    if i == "a":
        count += 1
print(count)


## Operador In

palavra = "banana"

if "x" in palavra:
    print(True)
else:
    print(False)

## COMPARAÇÃO DE STRINGS

palavra = "banana"

if palavra < "banana":
    print("Sua palavra" + palavra + ", vem antes de banana")
elif palavra > "banana":
    print("Sua palavra" + palavra + ", vem depois de banana")
else:
    print("Certo, banana")

## metodo DIR > dir(coisa) >> lista metodo disponiveis em um objeto
## metodo HELP >> help(str.capitalize) >> acesso a documentação sobre o método
## método é similar a função, mas a sintaxe é diferente veja abaixo:


##METODOS

palavra = "banana"
palavra1 = "maça"

novaPalavra = palavra.upper()
print(novaPalavra)

indice = palavra1.find("a")
print(indice)

linha = " Aqui vamos nós  "
semEspaço = linha.strip()
print(semEspaço)

frase = "Tem um bom dia"
temEssaStr = frase.lower().startswith("dia")
print(temEssaStr)

contagem = palavra.count("a")
print(contagem)

##PARTICIONANDO STRING

data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ", atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

##OPERADOR DE FORMATAÇÃO

camelos = 42
print("Eu vi %d camelos" % camelos)
print("Em %d anos eu vi %g porcento só %s e os outros porcentos %g eram viados." % (3, 99.9, "camelos", 1))

## EXERCICIOS CAPITULO 6
##6.5

str = "X-DSPAM-Confidence:0.8475"
antes = str.find(":")
apos = str.find(" ", antes)

hosp = str[antes+1: apos]
print(float(hosp))

##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 07

##ARQUIVOS > ABRIR

arquivo = open("mbox.txt.")
print(arquivo)

##ARQUIVOS > LENDO

fhand = open("mbox-short.txt")
count = 0

for i in fhand:
    count += 1
print("Contagem de linhas:", count)

fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20])

##ARQUIVOS > BUSCAR USANDO STARTSWITCH OU RSTRIP

fhand = open("mbox-short.txt")
count = 0
for i in fhand:
    if i.startswith("From:"):
        print(i)

fhand = open("mbox-short.txt")
for i in fhand:
    i = i.rstrip()
    if i.startswith("From:"):
        print(i)

fhand = open("mbox-short.txt")
for i in fhand:
    i = i.rstrip()
    ## passar qaudno for interresante
    if not i.startswith("From:"):
        continue
    ## prcessa nossa linha de interrese
    print(i)


fhand = open("mbox-short.txt")

for i in fhand:
    i = i.rstrip()
    if i.find("@uct.ac.za") == -1:
        continue
    print(i)

##ARQUIVOS > ESCOLHENDO NOME DO ARQUIVO

fname = input("Entre com o nome do arquivo: ")
fhand = open(fname)
count = 0

for i in fhand:
    if i.startswith("Subject:"):
        count += 1
print("Aqui está", count, "linha do objeto", fname)


##ARQUIVOS > TRY, EXCEPT E OPEN

fname = input("Entre com o nome do arquivo: ")
try:
    fhand = open(fname)
except:
    print("Arquivo não pode ser aberto:", fname)
    exit()
count = 0
for i in fhand:
    if i.startswith("Subject:"):
        count += 1
print("Aqui está", count, "linha do objeto", fname)

##ARQUIVOS > ESCREVENDO ARQUIVOS

fout = open("output.txt", "w")

line1 = "This here's the wattle, \n"
line2 = "the e,blem of our land. \n"
fout.write(line1)
fout.write(line2)
fout.close()


##LIVRO > PYTHON PARA TODOS, SEVERANCE CHARLES
## CAPITULO 08
##LISTA

variosTipos = ["spam", 2.5, 5, [10, 20]]
queijos = ["Cheddar", "Edam", "Gouda"]
numbers = [17, 123]
empty = []

print(queijos, numbers, empty, variosTipos)

##LISTA SÃO MUTAVEIS

numeros = [17, 123]
numeros[1] = -1
print(numeros)
print(17 in numeros)

##LISTA LAÇOS

queijos = ["Cheddar", "Edam", "Gouda"]
for chees in queijos:
    print(chees)

## ESCREVER OU ATUALIZAR ELEMENTOS DE UMA LISTA

numbers = [17, 123]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

##OPERAÇÕES COM LISTA

x = [0]
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c, x * 4)

##FATIAMENTO COM LISTA

t = ["a", "b", "c", "d", "e", "f"]
print(t[1:3], t[:4], t[3:])

##METODOS COM LISTA >> APPEND, EXTEND, SORT

t = ["a", "b", "c"]
t.append("d")
print(t)

t1 = ["a", "b", "c"]
t2 = ["d", "e", "f"]
t1.extend(t2)
print(t1)

t3 = ["d", "c", "e", "b", "a", "f"]
t3.sort()
print(t3)

##APAGANDO ELEMENTOS >> POP, DEL, REMOVE

t = ["a", "b", "c"]
popp = t.pop(1)
print(popp)
print(t)

t = ["a", "b", "c"]
del t[1]
print(t)

t3 = ["d", "c", "e", "b", "a", "f"]
del t3[1:5]
print(t3)

t = ["a", "b", "c"]
t.remove("b")
print(t)

##LISTAS E FUNÇÕES >> LEN, MAX, MIN, SUM

numbs = [3, 41, 12, 9, 74, 15]
print(len(numbs))
print(max(numbs))
print(min(numbs))
print(sum(numbs))
print(f"média: {sum(numbs) / len(numbs)}")

total = 0
count = 0

while (True):
    inp = input("Entre com um numero: ")
    if inp == "done":
        break
    value = float(inp)
    total += value
    count += 1
media = total / count
print(f"A média é: {media}")

numList = list()

while(True):
    inp = input("Entre com numeros: ")
    if inp == "done":
        break
    valor = float(inp)
    numList.append(valor)
media = sum(numList) / len(numList)
print(f"A média é: {media}")

##LISTAS E STRINGS >> SPLIT, JOIN

s = "spam"
l = list(s)
print(l)


s = "sentido falta dos fiordes"
l = s.split()
print(l)
print(l[2])

spam = "spam-spam-spam"
delimitador = "-"
a = spam.split(delimitador)
print(a)


t = ["sentido", "falta", "dos", "fiordes"]
delimitador = " " ##coloca espaço entre as palavras
a = delimitador.join(t)
print(a)

##LINHAS ALIADAS

fhand = open("mbox-short.txt")
for i in fhand:
    i = i.rstrip()
    if not i.startswith("From "):
        continue
    words = i.split()
    print(words[2])

##OBJETOS E VALORES
##LISTAS SÃO OBETOS DIFERENTES APESAR DE POSSUIR ELEMENTOS IGUAIS

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

##LINHAS COMO ARGUMENTO


def removePrimeiroElemento(lista):
    del lista[0]

letras = ["a", "b", "c"]

removePrimeiroElemento(letras)
print(letras)


## EXERCICIOS CAPITULO 8
##8.1

def corte(lista):
    del lista[0]
    lista.pop()
    return None

def meio(lista):
    return lista[1:-1]

listt = [1, 2, 4, 6, 8, 9]

print(meio(listt))
print(corte(listt))

##8.4

abrirArquivo = open("romeo.txt")
lista = []

for linha in abrirArquivo:
    palavra = linha.split()
    
    for i in palavra:
        if i not in lista:
            lista.append(i)
abrirArquivo.close()
lista.sort()
print(lista)

##8.5

nomeArquivo = open("mbox-short.txt")
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
contador = 0

for i in nomeArquivo:
    if i.startswith("From"):
        contador += 1
        separa = i.split()

##8.6


lista = []

while(True):
    entrada = input("Digite numeros: ")
    if entrada == "done":
        break
    try:
        numero = float(entrada)
        lista.append(numero)
    except ValueError:
        print("Insira o numerou ou 'done' ")
    if lista:
        maximo = max(lista)
        minimu = min(lista)
        print(maximo, minimu)
    else:
        print("nenhum foi digitado")




















