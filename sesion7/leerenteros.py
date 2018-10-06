def leer(n):
    lista = []
    contador = 0
    while contador < n:
        try:
            lista.append(float(input('ingrese un numero (numeros pendientes '
                                     +str(n - contador)+')')))
            contador += 1
        except:
            print('No ingresó un numero')
    return lista

print(leer(10))