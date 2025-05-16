### exceptions handlings ###

number_one, number_two = 5, 1
print(number_one + number_two)

# try except
try:
    #number_two = '5'
    print(number_one + number_two)
    print('No se ha producido un error')
except:
    print('Se ha producido un error')


# try except else
try:
    #number_two = '5'
    print(number_one + number_two)
except:
    print('Se ha producido un error')
else:
    print('Se ejecuta si no hay error')


# try except else finally
try:
    number_two = '5'
    print(number_one + number_two)
except:
    print('Se ha producido un error')
else: # opcional
    print('Se ejecuta si no hay error')
finally: # opcional
    print('Se ejecuta siempre')
    print('Fin del programa')

#captura de excepciones por tipo
try:
    number_two = 0
    print(number_one / number_two)
except TypeError as e:
    print(f'{type(e).__name__}: Se ha producido un error')
except ZeroDivisionError as e:
    print(f'{type(e).__name__}: No se puede dividir entre cero')

#captura de la información de la excepción
try:
    number_two = 0
    print(number_one / number_two)
except Exception as e:
    print(f'{type(e).__name__}: No se puede dividir entre cero')
    print(e)
