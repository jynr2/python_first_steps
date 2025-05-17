### regular expressions ###

import re

print('----- match -----')
# busca desde el inicio

my_string = 'Esta es la lección número 8: Lección Expresiones Regulares'
my_other_string = 'Esta no es la lección número 7: Expresiones Regulares'

my_match = re.match('Esta es la lección', my_string, re.I)
print(my_string)
my_span = my_match.span()
print(my_span)
print(my_string[my_span[0]: my_span[-1]])

my_other_match = re.match('Esta es la lección', my_other_string, re.I)
if my_other_match is not None:
    print(my_other_match)
    my_other_span = my_other_match.span()
    print(my_other_span)
    start, end = my_other_span
    print(my_other_string[start: end])


print('----- search -----')
# busca en toda la cadena

my_search = re.search('Expresiones Regulares', my_string, re.I)
print(my_search)
start, end = my_search.span()
print(my_string[start:end])

print('----- findall -----')
# busca todas las conincidencias en la cadena

my_findall = re.findall('lección', my_string, re.I)
print(my_findall)

print('----- split -----')
# divide en base al patron dado

my_split = re.split(':', my_string)
print(my_split)

print('----- sub -----')
# sustituye los valores

my_sub = re.sub('[l|L]ección', 'clase', my_string)
print(my_sub)


print('----- patterns -----')
# patrones propios
# https://regex101.com

pattern = r'[l|L]ección'
print(re.findall(pattern, my_string))

pattern = r'[l|L]ección|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[A-Z]'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

# email validation regular expression
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email = 'jyn@mail.com'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = 'jyn@mail.e'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))