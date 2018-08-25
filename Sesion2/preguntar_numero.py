# Preguntamos por un número
numero = input('Ingrese un número ')

# Intentamos realizar el flujo normal de nuestro programa
try:
    numero = float(numero)
    print('su número es',numero)

# Si se produce un error lo manejamos
except ValueError:
    print(numero, 'no es un valor numérico')