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



