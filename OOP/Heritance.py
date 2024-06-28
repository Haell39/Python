class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comunicar(self):
        pass
    
# Class derivada:

class Dog(Animal):
    def comunicar(self):
        print(f"{self.nome} diz: au au")


class Cat(Animal):
    def comunicar(self):
        print(f"{self.nome} diz: meow meow")


# Objetos das classes derivadas:

dog = Dog("Rex")
cat = Cat("Garfield")

# Chamando o método da classe derivada:

dog.comunicar()
cat.comunicar()
