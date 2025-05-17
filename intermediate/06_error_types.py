### error types ###

# SyntaxError

#print 'hola mundo' -> Error
print ('hola mundo')

# NameError
name = 'jyn'
#print(nama) -> Error
print(name)

# IndexError
numbers = [1,2,3,4,5]
# print(numbers[5]) -> Error
print(numbers[4])

# ModuleNotFoundError

#import maths -> Error
import math

print(math.pi)

# AttributeError

# print(math.PI) -> Error
print(math.pi)

# KeyError

my_dict = {'age': 33, 'name': 'jyn', 'gender': 'male'}
# print(my_dict['test']) -> Error
print(my_dict['age'])

#TypeError

# print(numbers['1']) -> Error
print(numbers[1])


# ImportError

# from math import poww -> Error
from math import pow

print(pow(5,2))

# ValueError
my_int = int('10')
#my_int = int('10p') -> Error
print(my_int)

#ZeroDivisionError

# print(5 / 0) -> Error
print(5 / 2)