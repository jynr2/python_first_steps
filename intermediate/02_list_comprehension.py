### list comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i + 1 for i in range(8)]
print(my_list)

my_range = range(8)
print(my_range)

def sum_five(number:int):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)
