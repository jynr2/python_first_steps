## dicts ##

my_dict = dict()
my_othrt_dict = {}
print(type(my_dict))
print(type(my_othrt_dict))


my_othrt_dict = {'name': 'jyn', 'lastname': 'trujillo', 'age': 33, 1: 'python'}
print(my_othrt_dict['age'])
my_dict = {
    'name': 'jyn',
    'lastname': 'trujillo',
    'age': 33, 
    'laguages': {'python', 'javascript', 'c#'},
    1:1.80
    }

#actualizar
my_dict['name'] = 'nancy'
print(my_dict['name'])

print(type(my_dict['laguages']))


#agregar
my_dict['email'] = 'jyn@mail.com'
print(my_dict)

#elimiar
del my_dict['email']
print(my_dict)
my_dict.pop('name')
print(my_dict)
my_dict.popitem()
print(my_dict)

#buscar
print('age' in my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items()) # retorna una lista de tuplas
print(my_dict.fromkeys(('a', 'b', 'c'), 'jyn')) # retorna un diccionario con las llaves de la cadena y el valor que se le asigna