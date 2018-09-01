def rango_letras(letra_1, letra_2):
    """
    (str, str) -> str

    Retorna una cadena con las letras en el rango entre dos letras

    >>> rango_letras('a', 'd')
    'abcd'
    >>> rango_letras('p', 'r')
    'pqr'

    :param letra_1: la letra mas baja a evaluar
    :param letra_2: la letra limite a evaluar
    :return: la candena con las letras resultantes
    """
    ord_1 = ord(letra_1)
    ord_2 = ord(letra_2)
    salida = ''
    for letra in range(ord_1, ord_2+1):
        salida += chr(letra)
    return salida