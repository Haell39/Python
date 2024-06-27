#Class definition

class Pessoa:
    def __init__(self,nome,age):
        self.nome = nome
        self.age = age
        
    def cumprimentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.age} anos')
        


#Object creation
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)


#Method call

pessoa1.cumprimentar()
pessoa2.cumprimentar()        


#Other Class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("Woof!")
        

my_dog = Dog("Ben", 5)
print(my_dog.name)
my_dog.bark()