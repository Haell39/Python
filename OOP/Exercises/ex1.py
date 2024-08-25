# Definição da classe Cachorro
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: Au au!")

# Criação de objetos da classe Cachorro
cachorro1 = Cachorro("Rex", 5)
cachorro2 = Cachorro("Bella", 3)

# Chamando o método latir para cada cachorro
cachorro1.latir()
cachorro2.latir()
