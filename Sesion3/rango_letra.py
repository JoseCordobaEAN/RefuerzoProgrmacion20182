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
    if type(letra_1) != str:
        raise ValueError(str(letra_1)+ ' no es de tipo cadena')
    if type(letra_2) != str:
        raise ValueError(str(letra_2) + ' no es de tipo cadena')

    alfabeto = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    pos = 0
    while True:
        if letra_1 == alfabeto[pos]:
            break
        pos += 1
    salida = ''
    while True:
        # salida += alfabeto[pos]
        if letra_2 == alfabeto[pos]:
            break
        pos += 1
    return salida