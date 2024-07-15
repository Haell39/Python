class NoBST:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.chave = chave

def inserir_bst(raiz, chave):
    if raiz is None:
        return NoBST(chave)
    else:
        if chave < raiz.chave:
            raiz.esquerda = inserir_bst(raiz.esquerda, chave)
        else:
            raiz.direita = inserir_bst(raiz.direita, chave)
    return raiz

def buscar_bst(raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz
    if chave < raiz.chave:
        return buscar_bst(raiz.esquerda, chave)
    return buscar_bst(raiz.direita, chave)

# Testando a árvore binária de busca
raiz = NoBST(50)
raiz = inserir_bst(raiz, 30)
raiz = inserir_bst(raiz, 20)
raiz = inserir_bst(raiz, 40)
raiz = inserir_bst(raiz, 70)
raiz = inserir_bst(raiz, 60)
raiz = inserir_bst(raiz, 80)

print("Busca pelo nó com chave 40:", buscar_bst(raiz, 40).chave)
