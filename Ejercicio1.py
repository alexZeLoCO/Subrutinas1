def leeEntero():        #Subrutina leeEntero():

    """
    :return: entero - Introducido por el usuario
    """

    entero=int(input("Introduzca un entero: "))     #Solicita entero
    return entero           #Devuelve entero

def devuelveMayor(a,b):     #Subrutina devuelveMayor(a,b):

    """
    :param: a - número entero
    :param: b - número entero

    :return: a or b or None. El mayor, None si son iguales.
    """

    if a>b:         #Si a>b (mayor=a)
        return a        #return a
    elif (a<b):     #Si no (y a!=b) (mayor=b)
        return b        #return b
    #Si ninguna se cumple ==> a==b ==> mayor=None

help(leeEntero)         #Imprime docstring de Subrutina leeEntero
help(devuelveMayor)     #Imprime docstring de Subrutina devuelveMayor

         #OUTPUT
print("El número mayor es:",devuelveMayor(devuelveMayor(leeEntero(),leeEntero()),leeEntero()))
