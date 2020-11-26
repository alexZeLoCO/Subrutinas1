from math import sqrt
from math import pow
from math import pi

def leeValor():        #Subrutina leeValor():
    """
    Devuelve un valor introducido por teclado

    :return: valor - Introducido por el usuario
    """

    valor=float(input("Introduzca un valor: "))     #Solicita valor
    return valor           #Devuelve valor

def distanciaOrigen(x,y):       #Subrutina distanciaOrigen(x,y):
    """
    Calcula la distancia al origen

    :param x: Posición x del punto
    :param y: Posición y del punto
    :return: Distancia al origen
    """
    return sqrt(pow(x,2)+pow(y,2))      #Calcula distancia

def calculaLongitud(radio):         #Subrutina calculaLongitud(radio):
    """
    Calcula la longitud de una circunferencia

    :param radio: Radio de la circunferencia
    :return: Longitud de la circunferencia
    """
    return 2*pi*radio           #Calcula longitud

x=leeValor()        #Posición abcisas
y=leeValor()        #Posición ordenadas

        #OUTPUT
print ("La distancia al centro del punto designado es:",distanciaOrigen(x,y))
print ("La longitud de la circunferencia de centro el origen y radio la distancia hasta el punto definido es:",calculaLongitud(distanciaOrigen(x,y)))