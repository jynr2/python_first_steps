## lists ##

my_list = list()
my_other_list = []
age_list = [18, 20, 30, 25, 30]

print(my_list.__len__())
print(len(my_list))

my_other_list = [33, 1.80, 1992, 'jyn', True]
print(my_other_list)
print(type(my_other_list))
print(type(my_other_list[0]))
print(age_list.count(30))


print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

age_list.extend([40, 50])


#insertar
my_list.append(1)
my_list.insert(0, 0)
print(my_list)
print(len(my_list))

#eliminar
age_list.remove(30)
age_list.pop(0)
print(age_list)
del age_list[0]
print(age_list)
age_list.clear()
print(age_list)

#editar
print(my_other_list)
my_other_list[0] = 34
print(my_other_list)


#desempaquetado
age, height, year, nickname, is_male = my_other_list
print(age, height, year, nickname, is_male)

# concatenar listas
print(my_list + my_other_list)

#copiar listas
my_new_list = my_list.copy()
print(my_new_list)
my_new_list.append(100)
print(my_new_list)
print(my_list)
my_new_list.reverse()
print(my_new_list)

#sort
my_new_list.sort()
print(my_new_list)