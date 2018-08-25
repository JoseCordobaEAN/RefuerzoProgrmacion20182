#Preguntar al usuario la hora
hora = int(input('''Bienvenido, ¿Qué hora es? (0 - 23)
'''))

# Si es antes de las 12m es por la mañana
if hora < 12:
    print('Buenos días')

# Si es entre las 12m y la 7pm es por la tarde
elif 19 > hora >=12:
    print('Buenas tardes')

# Si no, es de noche
else:
    print('Buenas noches')