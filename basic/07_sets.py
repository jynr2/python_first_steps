## sets ##
# Los sets son colecciones desordenadas de elementos únicos.

my_set = set()
my_set.add('jyn')
my_other_set = {}
print(type(my_set))
print(type(my_other_set))

my_other_set = {'jyn', 33, True}
print(type(my_other_set))
print(len(my_other_set))

#agregar
my_other_set.add('jynr2')
print(my_other_set)
copy_set =  my_other_set.copy()

my_other_set.add('jynr2') # No se agrega porque ya existe
print(my_other_set)

#buscar
print('jyn' in my_other_set)
print('jyr' in my_other_set)

#eliminar
my_other_set.remove('jynr2')
print(my_other_set)
my_other_set.discard(33)
print(my_other_set)
#my_other_set.clear()
print(my_other_set)
my_other_set.copy()
#del my_other_set
#print(my_other_set) # NameError: name 'my_other_set' is not defined
print(my_other_set)
print(copy_set)
print(copy_set.difference(my_other_set))

languages_set = {'python', 'java', 'c#'}
my_new_set = my_set.union(languages_set)
print(my_new_set)