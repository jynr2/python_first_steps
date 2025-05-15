## tuples ##

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (33, 1.80, 'jyn', True, 33)
my_other_tuple = (60, 30, 22)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(33))
print(my_tuple.index('jyn'))
#print(my_tuple.index('kdgdk')) -> # ValueError
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

#convertir tupla en lista
my_tuple = list(my_tuple)
print(type(my_tuple))
print(my_tuple)
my_tuple[0] = 99
my_tuple.insert(1, False)
print(my_tuple)