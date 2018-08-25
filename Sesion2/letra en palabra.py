# Preguntamos la palabra
print('''Bienvenido, este programa evalua si una letra está en una palabra
''')
palabra = input('Cual es su palabra ')

letra = input('Cual es su letra ')

# Evaluamos si la letra esté en la palabra
if letra in palabra:
    print('La letra', letra, 'esta en la palabra', palabra)
else:
    print('La letra', letra, 'no esta en la palabra', palabra)