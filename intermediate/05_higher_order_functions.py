### higher order functions ###

"""
sum_two_values_and_add_value() es de orden superior
Una función de orden superior es aquella que:
Recibe una función como argumento, o
Devuelve una función como resultado.
"""

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(num1, num2, f_sum):
    return f_sum(num1 + num2)

print(sum_two_values_and_add_value(5,2, sum_one))
print(sum_two_values_and_add_value(5,2, sum_five))


### closures ###

"""
Un closure es una función que:
Se define dentro de otra función, y
Recuerda (cierra sobre) el entorno en el que fue creada, incluso si ese entorno ya no existe.
"""

def sum_ten(original_value:int):
    def add(value:int):
        return value + 10 + original_value
    return add
    
add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(5)(1))

### built-in higher order functions ###

#map
numbers = [2,5,10,21]
map_result = map(lambda i: i * 2, numbers) # edita
print(list(map_result))

#filter
filter_result = filter(lambda i: i % 2 == 0, numbers) #filtra
print(list(filter_result))

#reduce
from functools import reduce

reduce_result = reduce(lambda x,y: x + y, numbers) # opera
print(reduce_result)
