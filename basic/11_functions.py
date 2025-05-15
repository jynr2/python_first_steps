### Functions ###

def my_function():
    print('Esto es una función')

my_function()
my_function()
my_function()


def sum_two_values(first_value:int, second_value:int): # si se asigna una función sin retorno, se asigna None
    print(first_value + second_value)

def sum_two_values_with_return(first_value:int, second_value:int)->int:
    sum_result = first_value + second_value
    return sum_result

sum_two_values(5, 10)
sum_two_values('5', '10')
#sum_two_values('5', 10) # TypeError
my_result = sum_two_values_with_return(5, 15)
print(my_result)


def print_name(name: str, surname:str):
    print(f'{name} {surname}')

print_name(surname = 'R2', name = 'jyn') # cambiar el orden de los argumentos

def print_name_with_default(name: str, surname:str, nickname:str = 'Sin apodo'):
    print(f'{name} {surname} {nickname}')

print_name_with_default('Carolina', 'Diaz')
print_name_with_default('Carolina', 'Diaz', 'Caro')


def my_function_args(* args): # args(tuple) función con argumentos variables
    print(args)

my_function_args(1, 2, 3, 4, 5, 'jyn')

def my_function_kwargs(** kwargs): # kwargs(dict) función con argumentos variables
    print(kwargs)

my_function_kwargs(name='jyn', age=33, country='Colombia')
