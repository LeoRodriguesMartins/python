"""

print("texto")  #exibira um texto na tela


if 5 > 8:
    print("Cinco é maior")
else:
    print("Cinco é menor")
        print("testando espaço") #exibirá um erro por conta da identação
                                 #deve seguir a identação dos comandos anteriores

"""
        
#comentário em python

"""
COMENTARIO
MULTILINHAS
NO PYTHON
"""

"""
    Regras para variáveis ​​Python:
    Um nome de variável deve começar com uma letra ou o caractere de sublinhado
    Um nome de variável não pode começar com um número
    Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (Az, 0-9 e _ )
    Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas (idade, Idade e IDADE são três variáveis ​​diferentes)
    Um nome de variável não pode ser nenhuma das palavras-chave do Python.
"""

"""
#Variaveis em Python são declaradas atribuindo valor a elas
#exemplo:

x = 5 #variavel do tipo int (inteiro)
y = "Jhon" #variavel do tipo string (texto)

print(x)
print(y)



#Variavies podem mudar seu tipo no meio do código
#exemplo:

x = 4 #tipo int
x = "Texto" #agora mudou para string

print(x)


#para especificar o tipo de dados em uma variável, pode ser usado a conversão
#exemplo:
x = str(3) #será '3' por string/texto
y = int(3) #será 3 por inteiro
z = float(3) #z será 3.0 por número flutuante

print(x)
print(y)
print(z)


#Para obter o tipo de dados colocado em uma variável utilizando type()

x = 5
y = "john"

print(type(x))
print(type(y))


# string podem ser declaradas com aspas simples 'texto' ou aspas duplas "texto"

x = 'aspas simples'
y = "aspas duplas"

print(x)
print(y)



#o nome de variáveis se diferenciam entre minúsculas e maiúsculas
a = 4
A = "Sally"

print(a)
print(A)



#O Python permite que você atribua valores a várias variáveis ​​em uma linha:

x, y, z = "Orange", "Banana", "Morango"

print(y)
print(x)
print(z)



#Permite atribuir o mesmo valor a várias variáveis ​​em uma linha:

x, y, z = "Orange"
print(y)
print(x)
print(z)


#caso possua uma coleção de valores em uma list, tupla... é possível extrai os valores e distribuir em variáveis. É chamado de descompactação

fruits = ["apple", "banana", "morango"]
x, y, z = fruits
print(x)
print(y)
print(z)



#Variaveis de saída. A função print() é usada frequentemente para variáveis de saida
#exemplo:

x = "Python var saída"
print(x)

# é possivel gerar várias variáveis, separadas por uma vírgula:
#obs.: neste caso, note que já será com exibido o espaçamento nas palavras
x = "Python"
y = "is"
z = "awesome"

print(x,y,z)

# pode ser utilizado + para gerar várias variáveis
#obs.: note que neste caso será
x = "Python "
y = "is "
z = "awseome"
print(x + y + z)

# Para números, o + funciona como operador matemático realizando a soma das váriavies
#exemplo:
x = 5
y = 10
print(x + y)

# o simbolo + não permita a utilização quando os valores das variáveis são de tipos direntes
#exemplo:  

x = 5 #tipo int
y = "Jhon" #tipo string
print(x + y)
#gera erro


# para gerar variáveis de diferentes valores no print() o ideal é a utilização de ,
#exemplo:

x = 5
y = "Jhon"
print(x, y)



#Váriáveis criadas fora de uma função são conhecidas como variáveis globais
#Variáveis globais podem ser usados por todos, tanto dentro quanto fora de funções

#exemplo:

x = "awesome"

def myFunc():
    print("Python is " + x)
myFunc()



#se for criado uma variável com o mesmo nome dentro de uma função,
#esta variável será local, e só poderá ser utilizada dentro da função

#a variável local permanecerá como global

#exemplo:

x = "awesome"

def myFunc():
    x = "fantastic"
    print("Python is " + x)
    
myFunc()

print("Python is " + x)




#para criar um variável global dentro de uma função, pode-se utilizar a palavra-chave: global
#exemplo:

def myFunc():
    global x    #indica que a variavel será global
    x = "fantastic" #valor e tipo da variável
myFunc()

print("Python is", x)



#a palavra-chave 'global' pode ser utilizada para trocar o valor de uma variável global dentro de uma função
#exemplo:

x = "awesome"
def myFunc():
    global x
    x = "fantastic"
myFunc()

print("Python is " + x)

"""
