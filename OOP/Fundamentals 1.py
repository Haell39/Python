# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Definição da classe Estudante, que herda de Pessoa
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    
    def estudar(self):
        print(f"{self.nome} está estudando no curso de {self.curso}.")

# Definição da classe Professor, que também herda de Pessoa
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    
    def ensinar(self):
        print(f"Professor {self.nome} está ensinando {self.disciplina}.")

# Testando as classes
if __name__ == "__main__":
    pessoa1 = Pessoa("João", 30)
    pessoa1.apresentar()  # Saída: Olá, meu nome é João e tenho 30 anos.

    estudante1 = Estudante("Maria", 20, "Ciência da Computação")
    estudante1.apresentar()  # Saída: Olá, meu nome é Maria e tenho 20 anos.
    estudante1.estudar()     # Saída: Maria está estudando no curso de Ciência da Computação.

    professor1 = Professor("Carlos", 45, "Matemática")
    professor1.apresentar()  # Saída: Olá, meu nome é Carlos e tenho 45 anos.
    professor1.ensinar()     # Saída: Professor Carlos está ensinando Matemática.
