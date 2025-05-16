### classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    
    def __init__(self, name:str, surname:str, nickname:str = 'sin apodo'):
        self.full_name = f'{name} {surname} ({nickname})'
        self.__name = name
        self.__surname = surname

    def walk(self):
        print(f'{self.full_name} está caminando')

    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname

my_person = Person('Carolina', 'Diaz', 'Caro')
print(my_person.full_name)
my_person.walk()

my_other_person = Person('jyn', 'r2')
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = 'jyn'
print(my_other_person.full_name)

my_other_person.full_name = 333
print(my_other_person.full_name)
print(my_other_person.get_name())
print(my_other_person.get_surname())
