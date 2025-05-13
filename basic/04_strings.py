
my_string = 'Mi string'
my_other_string = 'Mi otro string'

print(my_string)
print(len(my_other_string))
print(my_string + ' ' + my_other_string)

my_new_line_string = 'este es un string \ncon salto de linea'
print(my_new_line_string)

my_tab_string = '\teste es un string con tabulación'
print(my_tab_string)

my_scape_tab_string = '\teste es un string \n con escape'
print(my_scape_tab_string)

# formateo
name, surname, age = 'jyn', 'test', 32
print('Mi nombre es {} {} y ni edad es {}'.format(name, surname, age))
print(f'Mi nombre es {name} {surname} y ni edad es {age}')
print('Mi nombre es %s %s y ni edad es %d' % (name, surname, age))

#desempaquetado de caracteres
language = 'python'
a,b,c,d,e,f = language
print(a)
print(b)

#división

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[:3]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#reversa

reversed_language = language[::-1]
print(reversed_language)

#funciones
print(language.capitalize())
print(language.count('o'))
print(language.upper())
print(language.isupper())
print('HOLA'.lower())
print(language.isnumeric())
print(language.startswith('py'))
print(language.endswith('p'))