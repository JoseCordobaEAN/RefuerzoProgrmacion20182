def ecuacion(x):
    """
    (num)-> num

    Calcula x + 3

    >>> ecuacion(0)
    3
    >>> ecuacion(3)
    6
    >>> ecuacion(-10.0)
    -7.0

    :param x:
    :return:
    """
    return x + 3


def cuadrado(x):
    """
    (num) -> num
    Calcula el cuadrado de un numero

    >>> cuadrado(2)
    4
    >>> cuadrado(6.0)
    36.0
    >>> cuadrado(-20)
    400


    :param x:
    :return:
    """
    #return x * x
    return x ** 2


def ecuacion2(x, y):
    """
    (num, num) -> num
    Calcula 2 x^2 + y

    >>> ecuacion2(1, 2)
    4
    >>> ecuacion2(2, 0)
    8

    :param x:
    :param y:
    :return:
    """
    return 2 * cuadrado(x) + y


def abs(x):
    """
    (num) -> num
    calcula el valor absoluto dado un número

    >>> abs(0)
    0
    >>> abs(300)
    300
    >>> abs(-1255.87)
    1255.87

    :param x:
    :return:
    """
    if x < 0:
        return -x
    return x

def es_vocal(letra):
    """
    (str) -> bool
    Determina si una letra es vocal

    >>> es_vocal('a')
    True
    >>> es_vocal('d')
    False

    :param letra:
    :return:
    """
    return letra in 'aeiouAEIOU'

def cuenta_vocales(texto):
    """
    (str) -> int
    Determina cuantas vocales hay en un texto

    >>> cuenta_vocales('hola mundo')
    4
    >>> cuenta_vocales('Colombia tierra querida')
    11
    >>> cuenta_vocales('')
    0

    :param texto:
    :return:
    """
    contador = 0
    for letra in texto:
        if es_vocal(letra):
            contador += 1
    return contador



def contar_impares(lista):
    """
    (list of int) -> int

    Cuenta cuantos números en la lista son impares

    >>> contar_impares([1, 2 , 3, 100])
    2
    >>> contar_impares([3, 3 , 3, 1])
    4
    >>> contar_impares([5, 3, 9, 20])
    3
    >>> contar_impares([])
    0

    :param lista:
    :return:
    """
    contador = 0
    for numero in lista:
        contador += numero % 2
    return contador


def contar_pares(lista):
    """
    (list of int) -> int

    Cuenta cuantos números en la lista son pares

    >>> contar_pares([1, 2 , 3, 100])
    2
    >>> contar_pares([3, 3 , 3, 1])
    0
    >>> contar_pares([5, 3, 9, 20])
    1
    >>> contar_pares([])
    0

    :param lista:
    :return:
    """
    return len(lista) - contar_impares(lista)
