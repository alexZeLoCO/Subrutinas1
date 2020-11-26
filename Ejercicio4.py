def leeEntero():        #Subrutina leeEntero():

    """
    Devuelve un entero introducido por teclado.

    :return: entero - Introducido por el usuario
    """

    entero=int(input("Introduzca un entero: "))     #Solicita entero
    return entero           #Devuelve entero

def bisiesto(n):        #Subrutina Bisiesto():
    """
    Devuelve true si el año parámetro es bisiesto.

    :param n: año
    :return: True si bisiesto. False si no.
    """
    return n%400==0 or (n%4==0 and n%100!=0)        #Evalúa

if bisiesto(leeEntero()):       #Si es bisiesto
    print ("El año es bisiesto.")       #OUTPUT
else:       #Si no
    print ("El año no es bisiesto.")    #OUTPUT