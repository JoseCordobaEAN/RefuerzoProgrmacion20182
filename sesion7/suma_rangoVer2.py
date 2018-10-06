def suma_rango(desde, hasta):
    """

    >>> suma_rango(1, 10)
    55
    >>> suma_rango(1, 11)
    66

    :param desde:
    :param hasta:
    :return:
    """
    total = (hasta // 2) * (desde + hasta)
    # si la sucesión de numeros es par sumo por extremos
    if hasta % 2 == 0:
        return total
    # si la sucesión es impar agrego al total el numero que queda en mmedio
    el_de_enmedio = (hasta // 2) + 1
    return total + el_de_enmedio