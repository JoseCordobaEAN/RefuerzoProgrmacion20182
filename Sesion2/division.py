# Intentar leer dos números
numero_1 = input('Ingrese su número ')
numero_2 = input('Ingrese su divisor ')
try:
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)

    # Intentar la división
    try:
        resultado = numero_1 / numero_2
        print('el resultado de', numero_1, '/', numero_2,
              'es', resultado)
    except ZeroDivisionError:
        print('No es posible dividir por 0')

except ValueError:
    print(numero_1, 'o', numero_2, 'No son números')