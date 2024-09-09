from collections import deque

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_no(self, no):
        self.grafo[no] = []

    def adicionar_aresta(self, no1, no2):
        self.grafo[no1].append(no2)
        self.grafo[no2].append(no1)

class GrafoBusca(Grafo):
    def bfs(self, inicio):
        visitados = set()
        fila = deque([inicio])
        while fila:
            no = fila.popleft()
            if no not in visitados:
                print(no, end=" ")
                visitados.add(no)
                fila.extend(self.grafo[no])

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        if inicio not in visitados:
            print(inicio, end=" ")
            visitados.add(inicio)
            for vizinho in self.grafo[inicio]:
                self.dfs(vizinho, visitados)

# Testando BFS e DFS
grafo_busca = GrafoBusca()
grafo_busca.adicionar_no(1)
grafo_busca.adicionar_no(2)
grafo_busca.adicionar_no(3)
grafo_busca.adicionar_no(4)

grafo_busca.adicionar_aresta(1, 2)
grafo_busca.adicionar_aresta(1, 3)
grafo_busca.adicionar_aresta(2, 4)

print("\nBusca em Largura (BFS):")
grafo_busca.bfs(1)

print("\n\nBusca em Profundidade (DFS):")
grafo_busca.dfs(1)
