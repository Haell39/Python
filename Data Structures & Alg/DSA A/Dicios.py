# Criação de um dicionário
dicionario = {"nome": "Alice", "idade": 30, "cidade": "Nova York"}
print("Dicionário inicial:", dicionario)

# Acesso a valores
print("Nome:", dicionario["nome"])

# Adição e modificação de pares chave-valor
dicionario["idade"] = 31
dicionario["email"] = "alice@example.com"
print("Dicionário após adições e modificações:", dicionario)

# Remoção de pares chave-valor
del dicionario["cidade"]
print("Dicionário após remover 'cidade':", dicionario)

# Iteração sobre chaves e valores
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
