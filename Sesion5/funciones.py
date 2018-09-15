def filtrar_enteros(lista):
    """
    (list) -> lista de enteros

    Filtra solo los elementos de tipo entero en una lista

    >>> filtrar_enteros([10, 'hola', 7.5, 'jose', 20, 'pedro', 30])
    [10, 20, 30]

    :param lista:
    :return:
    """
    lista_resultante = []
    for elemento in lista:
        if int == type(elemento):
            lista_resultante.append(elemento)
    return lista_resultante
