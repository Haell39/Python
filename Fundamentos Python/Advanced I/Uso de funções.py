# Definir uma função simples
def saudacao(nome):
    return f"Olá, {nome}!"

# Chamar a função e imprimir o resultado
mensagem = saudacao("João")
print(mensagem)  # Saída: Olá, João!

# Função com múltiplos argumentos
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(f"Soma: {resultado}")  # Saída: 7
