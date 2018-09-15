# Hacer una funcion que me retorne el valor numérico de un caracter
def valor_numerico(c):
    """
    (str) -> int

    Retorna el valor numerico de un caracter si a = 1, b = 2 etc...

    >>> valor_numerico('a')
    1
    >>> valor_numerico('z')
    26
    >>> valor_numerico(' ')
    -64
    >>> valor_numerico('ñ')
    145

    :param c: str con un solo caracter alpha y minuscula
    :return:
    """
    return ord(c) - 96


# Hacer una funcion que encripte el caracter dada la llave
def encriptar_caracter(c, k):
    """
    (str, str) -> num

    Encripta un caracter con una llave utilizando la formula dada

    >>> encriptar_caracter('a', 'a')
    1
    >>> encriptar_caracter('b', 'b')
    2

    :param c:
    :param k:
    :return:
    """
    return (valor_numerico(c) + valor_numerico(k)) / 2


# Hacer una funcion que me encripte una cadena
def encriptar_cadena(cadena, k):
    """
    (str) -> list of int

    Encripta una cadena y la transforma en una lista de flotantes

    >>> encriptar_cadena('abcd', 'a')
    [1.0, 1.5, 2.0, 2.5]

    :param cadena:
    :return:
    """
    resultado = []
    for elemento in cadena:
        resultado.append(encriptar_caracter(elemento, k))
    return resultado

