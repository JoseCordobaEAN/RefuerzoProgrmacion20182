def es_divisible(dividendo, divisor):
    """
    (int) -> bool

    Determina si un numero es divisible entre otro

    >>> es_divisible(10, 2)
    True
    >>> es_divisible(5, 2)
    False
    >>> es_divisible(9, 3)
    True

    :param dividendo:
    :param divisor:
    :return: True si el numero es divisible False de lo contrario
    """
    return dividendo % divisor == 0

def es_primo(numero):
    """
    (int) -> bool

    Determina si un numero es primo

    >>> es_primo(8)
    False
    >>> es_primo(7)
    True
    >>> es_primo(13)
    True

    :param numero: El entero a evaluar
    :return: True si es primo, False de lo contrario
    """
    divisores = 0
    for valor in range(1, numero+1):
        if es_divisible(numero,valor):
            divisores +=1
            if divisores > 2:
                return False
    return divisores == 2