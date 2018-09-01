def es_par(numero):
    """
    (int) ->bool
    Determina si un numero es par
    :param numero: el numero a evaluar
    :return: True si es par false de lo contrario
    """
    return numero % 2 == 0


def recorrido_100():
    """
    () -> str

    :return: Retorna los numeros entre 1 - 100
    la suma de los pares y la suma de los impares en una cadena
    """
    numero = 1
    suma_pares = 0
    suma_impares = 0
    salida = ''
    while numero < 101:
        salida += '\n' + str(numero)
        if es_par(numero):
            suma_pares += numero
        else:
            suma_impares += numero
        numero +=1
    salida += '\n suma de pares = ' + str(suma_pares)
    salida += '\n suma de impares = ' + str(suma_impares)
    return salida

print(recorrido_100())