# La estructura de decisión if nos permite ejecutar
# Instrucciones si se cumple una condición lógica
# Este programa evaua si un número es par

# Preguntamos el número al usuario
numero = int(input('Ingrese un número: '))

# Evaluamos si el número es par
if numero % 2 == 0:
    print('El número', numero,'es par')
else:
    print('El número', numero, 'es impar')