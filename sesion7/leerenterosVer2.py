def leer(n):
    lista = []
    for i in range(0, n):
        lista.append(leer_numero(n-i))
    return lista


def leer_numero(faltantes):
    mensaje = 'Ingrese un numero (faltan '+str(faltantes)+') '
    while True:
        try:
            return float(input(mensaje))
        except:
            print('No ingresó un numero')

print(leer(10))