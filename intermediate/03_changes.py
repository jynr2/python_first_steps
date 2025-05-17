### changes ###

print('----- fizzbuzz -----')

def fizzbuzz(number:int):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')

[fizzbuzz(i) for i in range(1, 21)]

print('----- anagram -----')

def anagram(word_one:str, word_two:str) -> bool:
    if len(word_one) != len(word_two):
        return False
    if word_one.lower() == word_two.lower():
        return False
    for letter in word_one.lower():
        if letter not in word_two.lower():
            return False
    return True

def sets_anagram(word_one:str, word_two:str) -> bool:
    if len(word_one) != len(word_two) or word_one.lower() == word_two.lower():
        return False
    set_one = set(word_one.lower())
    set_two = set(word_two.lower())
    return set_one == set_two

print(sets_anagram('listen', 'silent'))

print('----- fibonacci -----')

def fibonacci_calculation(n) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_calculation(n - 1) + fibonacci_calculation(n - 2)

def fibonacci():
    for i in range(10):
        print(fibonacci_calculation(i))

def fibonacci_two():
    prev = 0
    nx = 1
    for _ in range(10):
        print(prev)
        fib = prev + next
        prev = nx
        nx = fib

fibonacci()

print('----- prime -----')

def is_prime(number:int):

    for i in range(1, 101):
        if number >= 2:
            is_divisible = False

            for j in range(2, number):
                if number % j == 0:
                    is_divisible = True
                    break
        if is_divisible:
            print(i)

    return True

is_prime(5)


print('----- reverse -----')

def reverse(text:str):
    for i in range(len(text), 0, -1):
        print(text[i-1], end='')

reverse('hello world')