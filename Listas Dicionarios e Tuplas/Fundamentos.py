# Fundamentos de Listas, Dicionários e Manipulação de Usuários em Python

# Parte 1: Listas

# 1. Criação de uma lista
usuarios = ["Alice", "Bob", "Charlie"]
print("Lista inicial de usuários:", usuarios)

# 2. Adição de elementos a uma lista
usuarios.append("Diana")
print("Lista após adicionar um usuário:", usuarios)

# 3. Inserção de um elemento em uma posição específica
usuarios.insert(1, "Eve")
print("Lista após inserir um usuário na segunda posição:", usuarios)

# 4. Remoção de um elemento de uma lista
usuarios.remove("Bob")
print("Lista após remover um usuário:", usuarios)

# 5. Acesso a elementos da lista por índice
print("Primeiro usuário na lista:", usuarios[0])
print("Último usuário na lista:", usuarios[-1])

# 6. Modificação de um elemento na lista
usuarios[2] = "Carlos"
print("Lista após modificar um usuário:", usuarios)

# 7. Iteração sobre uma lista
print("Iterando sobre a lista de usuários:")
for usuario in usuarios:
    print(usuario)

# 8. Comprimento de uma lista
print("Número total de usuários:", len(usuarios))

# 9. Listas aninhadas (listas dentro de listas)
dados_usuarios = [
    ["Alice", 25, "alice@example.com"],
    ["Eve", 30, "eve@example.com"],
    ["Carlos", 28, "carlos@example.com"],
    ["Diana", 22, "diana@example.com"]
]
print("Dados completos dos usuários:", dados_usuarios)

# 10. Acesso e manipulação de dados em listas aninhadas
print("Primeiro usuário e seus dados:", dados_usuarios[0])
print("Email do terceiro usuário:", dados_usuarios[2][2])

# 11. Adicionar um novo usuário com dados completos
novo_usuario = ["Bob", 35, "bob@example.com"]
dados_usuarios.append(novo_usuario)
print("Dados completos após adicionar um novo usuário:", dados_usuarios)

# 12. Atualização de dados de um usuário
dados_usuarios[1][1] = 31  # Atualiza a idade de Eve
print("Dados completos após atualizar a idade de Eve:", dados_usuarios)

# 13. Remoção de um usuário
dados_usuarios.remove(dados_usuarios[2])  # Remove Carlos
print("Dados completos após remover Carlos:", dados_usuarios)

# 14. Iteração sobre dados de usuários e formatação de saída
print("Listando todos os usuários e seus dados:")
for usuario in dados_usuarios:
    nome, idade, email = usuario
    print(f"Nome: {nome}, Idade: {idade}, Email: {email}")

# Parte 2: Dicionários

# 1. Criação de um dicionário
usuario_info = {
    "nome": "Alice",
    "idade": 25,
    "email": "alice@example.com"
}
print("\nDicionário inicial do usuário:", usuario_info)

# 2. Acesso a valores por chaves
print("Nome do usuário:", usuario_info["nome"])
print("Idade do usuário:", usuario_info["idade"])

# 3. Adição e modificação de pares chave-valor
usuario_info["cidade"] = "Nova York"  # Adicionar nova chave-valor
usuario_info["idade"] = 26  # Modificar valor existente
print("Dicionário após adições e modificações:", usuario_info)

# 4. Remoção de pares chave-valor
del usuario_info["email"]
print("Dicionário após remover a chave 'email':", usuario_info)

# 5. Iteração sobre chaves e valores
print("Iterando sobre o dicionário de usuário:")
for chave, valor in usuario_info.items():
    print(f"{chave}: {valor}")

# 6. Verificação de existência de chave
if "nome" in usuario_info:
    print("O nome do usuário é:", usuario_info["nome"])

# 7. Dicionários aninhados (dicionários dentro de dicionários)
usuarios_detalhados = {
    "Alice": {"idade": 26, "email": "alice@example.com", "cidade": "Nova York"},
    "Eve": {"idade": 31, "email": "eve@example.com", "cidade": "Chicago"},
    "Diana": {"idade": 22, "email": "diana@example.com", "cidade": "Los Angeles"}
}
print("\nDicionários aninhados com detalhes dos usuários:", usuarios_detalhados)

# 8. Acesso e manipulação de dados em dicionários aninhados
print("Dados de Alice:", usuarios_detalhados["Alice"])
print("Email de Eve:", usuarios_detalhados["Eve"]["email"])

# 9. Adição de um novo usuário ao dicionário aninhado
usuarios_detalhados["Bob"] = {"idade": 35, "email": "bob@example.com", "cidade": "Miami"}
print("Dicionário aninhado após adicionar Bob:", usuarios_detalhados)

# 10. Atualização de dados em dicionários aninhados
usuarios_detalhados["Diana"]["idade"] = 23
print("Dicionário aninhado após atualizar a idade de Diana:", usuarios_detalhados)

# 11. Remoção de um usuário do dicionário aninhado
del usuarios_detalhados["Alice"]
print("Dicionário aninhado após remover Alice:", usuarios_detalhados)

# 12. Iteração sobre dicionários aninhados
print("Listando todos os usuários e seus detalhes:")
for nome, detalhes in usuarios_detalhados.items():
    idade = detalhes["idade"]
    email = detalhes["email"]
    cidade = detalhes["cidade"]
    print(f"Nome: {nome}, Idade: {idade}, Email: {email}, Cidade: {cidade}")

# Fim do código exemplo
