# Ejercicio 1. Escriba un ciclo definido para imprimir por pantalla todos los números entre 10 y 20.
def num_entre_10y20():
    for i in range (10, 21):
        print (i)

#num_entre_10y20()

#Escriba un programa que imprima por pantalla todas las fichas del dominó, una por línea y sin repetir

def fichas_domino(x):
    for i in range (0, x + 1):
        for x in range (i, x +1 ):
            print (i, x)

#Modifique el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a n 

def fichas_juego(x):
    for i in range (0, x + 1):
        print (i)

# formula factorial = n ( n − 1 ) ! 

#Escriba una función que tome una cantidad m de valores que serán ingresados
#por el usuario y, a medida que se ingresa cada número, muestre el factorial del mismo. El valor
#de m es ingresado inicialmente por el usuario
import math
def factorial_de(m):
    for i in range (1, m + 1):
        print (math.factorial(i))

#Usando la función dada como ejemplo en la presentación de La Receta en Python
#para convertir una temperatura de Fahrenheit a Celsius, genere una tabla de conversión de
#temperaturas, desde 0◦F hasta 120◦F , de 10 en 10.

def far_cel ( f ) :
    return ((f -32) *5/9)

def tabla_far ():
    for i in range (0, 121, 10):
        print (i, "=", far_cel(i))


#Escriba una función que reciba un número n como parámetro e imprima los pri-
#meros n números triangulares, junto con sus respectivos índices

def triangular (x):
    return ((x * (x + 1))/2)

def num_triangular (n):
    for i in range (1, n + 1):
        print (i, "-", triangular(i))


def NumTriangulares (n):
    m=0
    for i in range (1, n+1):
        m =  m + i
        print (i,m)


#Escriba una función que le pida al usuario que ingrese un número positivo. Si el
#usuario ingresa cualquier cosa que no sea lo pedido se le debe informar de su error mediante
#un mensaje y volver a pedirle el número, repitiendo este proceso hasta que ingrese lo pedido.

def num (x):
    int (input, "ingrese un numero:")



def prueba():
    for i in range (1, 10, -1):
        print (i)