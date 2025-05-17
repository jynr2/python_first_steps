### lambdas ###

sum_two_values = lambda num1, num2: num1 + num2

print(type(sum_two_values))
print(sum_two_values(6, 12))

mutiplay_values = lambda num1, num2 : num1 * num2 - 3
print(mutiplay_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))


# Decorador con lambda: agrega 1 al resultado de la función
incrementa = lambda f: lambda *args, **kwargs: f(*args, **kwargs) + 1

@incrementa
def suma():
    return 4

print(suma())  # Salida: 5
