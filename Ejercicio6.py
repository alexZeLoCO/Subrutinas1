def leeValor():        #Subrutina leeValor():
    """
    Devuelve un valor introducido por teclado

    :return: valor - Introducido por el usuario
    """

    valor=float(input("Introduzca un valor: "))     #Solicita valor
    return valor           #Devuelve valor

def imc(peso, altura):      #Subrutina imc(peso,altura):
    """
    Calcula el IMC

    :param peso: peso introducido por el usuario
    :param altura: altura introducida por el usuario
    :return: IMC calculado en función de los parámetros
    """

    return peso/altura**2       #IMC

def calificaciónIMC(IMC):       #Subrutina calificaciónIMC(IMC):
    """
    Califica estado nutricional

    :param IMC: Calculado por subrutina imc(peso,altura):
    :return: String en función de parámetro
    """

    if IMC<18.50:       #Si es menor que 18.50
        return "Bajo peso"
    elif IMC<25:        #Si es menor que 25
        return "Normal"
    elif IMC<30:        #Si es menor que 30
        return "Sobrepeso"
    else:               #Los demás
        return "Obesidad"

            #OUTPUT
print("Su estado nutricional es:",calificaciónIMC(imc(leeValor(),leeValor())))