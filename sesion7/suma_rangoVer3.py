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
    acumulador = 0
    contador = desde
    while contador <= hasta:
        acumulador += contador
        contador += 1
    return acumulador