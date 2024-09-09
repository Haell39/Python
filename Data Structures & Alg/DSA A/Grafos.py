class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def adicionar_no(self, no):
        if no not in self.grafo:
            self.grafo[no] = []
    
    def adicionar_aresta(self, no1, no2):
        if no1 in self.grafo and no2 in self.grafo:
            self.grafo[no1].append(no2)
            self.grafo[no2].append(no1)
    
    def exibir_grafo(self):
        for no in self.grafo:
            print(no, "->", " -> ".join([str(n) for n in self.grafo[no]]))

# Testando o grafo
grafo = Grafo()
grafo.adicionar_no(1)
grafo.adicionar_no(2)
grafo.adicionar_no(3)
grafo.adicionar_no(4)

grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(1, 3)
grafo.adicionar_aresta(2, 4)

print("Grafo:")
grafo.exibir_grafo()
