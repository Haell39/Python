class No:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.chave = chave

# Inserção em uma árvore binária
def inserir(raiz, chave):
    if raiz is None:
        return No(chave)
    else:
        if chave < raiz.chave:
            raiz.esquerda = inserir(raiz.esquerda, chave)
        else:
            raiz.direita = inserir(raiz.direita, chave)
    return raiz

# Percorrendo uma árvore (em ordem)
def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esquerda)
        print(raiz.chave, end=" ")
        em_ordem(raiz.direita)

# Testando a árvore binária
raiz = No(50)
raiz = inserir(raiz, 30)
raiz = inserir(raiz, 20)
raiz = inserir(raiz, 40)
raiz = inserir(raiz, 70)
raiz = inserir(raiz, 60)
raiz = inserir(raiz, 80)

print("Percorrendo a árvore em ordem:")
em_ordem(raiz)
