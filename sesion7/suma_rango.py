def suma_rango(desde, hasta):
    """

    >>> suma_rango(1, 10)
    55

    :param desde:
    :param hasta:
    :return:
    """
    acumulador = 0
    for i in range(desde, hasta+1):
        acumulador += i
    return acumulador