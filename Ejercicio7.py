from math import sqrt
from math import pow

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
    return sqrt(pow(x,2)*pow(y,2))      #Calcula distancia

        #OUTPUT
print ("La distancia al centro del punto designado es:",distanciaOrigen(leeValor(),leeValor()))