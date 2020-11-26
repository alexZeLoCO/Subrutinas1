def leeNota():        #Subrutina leeEntero():

    """
    Devuelve un float introducido por teclado

    :return: nota - Introducido por el usuario
    """

    nota=float(input("Introduzca una nota: "))     #Solicita nota
    return nota           #Devuelve entero

def nota(n):            #Subrutina nota(n):
    """
    Devuelve una string en función del parámetro.

    :param n: Nota de alumno
    :return: Puntuación
    """

    if (n<5):         #Suspenso
        return "suspenso"
    elif (n<7):         #Aprobado
        return "aprobado"
    elif (n<9):         #Notable
        return "notable"
    elif (n<10):        #Sobresaliente
        return "sobresaliente"
    else:               #Matrícula
        return "matrícula de honor"

        #OUTPUT
print("La nota es:",nota(leeNota()))