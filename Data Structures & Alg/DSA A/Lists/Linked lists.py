class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None
    
    def inserir_no_inicio(self, novo_dado):
        novo_no = No(novo_dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
    
    def exibir_lista(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print(None)

# Testando a lista ligada
lista = ListaLigada()
lista.inserir_no_inicio(3)
lista.inserir_no_inicio(2)
lista.inserir_no_inicio(1)
print("Lista ligada:")
lista.exibir_lista()
