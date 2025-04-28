# Variables

#Es correcto, pero python usa por convención snake case
from typing import Final


MyVariable = 'My Variable'
print(MyVariable)

#Es correcto, y recomendable en python
my_variable = 'my variable'
print(my_variable)

my_bool_variable = True

#Disferentes argumentos
my_int = 5
print(MyVariable, my_variable, my_bool_variable)
print(MyVariable, my_variable, str(my_int)) #pasar de int a str
print(type(print())) # tipo de print <class 'NoneType'>
print('Este es el valor de: ', my_int)

#obtener la lonfigtud de una cadena lista, tupla
print(len(my_variable))


#Decaracion de variables en una sola linea
name, last_name, nick_name, age = 'Jhon', 'Montealegre', 'jyn', 32
print(f'My nombre es {name}, mi apellido es {last_name}, me dicen {nick_name} y tengo {age} años')


#Cambiar valores de variables
#age = int(input('Ingresa tu edad: '))
print('Tu edad es:', age)

#cambiar tipo de dato en una varible
name = 30.1
print('Se cambia el tipo de valor de la variable name, nuevo tipo:', type(name))


#declaración de variables especificando el tipo de dato
december:int = 12
print('Diciembre es el mes #:', december)

