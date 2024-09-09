def calcular_media(a, b, c, d):
    # Calcula a média das notas
    media_inicial = (a + b + c + d) / 4
    return media_inicial

def verificar_aprovacao(media):
    # Verifica se o aluno foi aprovado ou não
    if media >= 7:
        return "Aprovado", media
    else:
        nota_recuperacao = float(input("Qual sua nota de recuperação? "))
        nova_media = (media + nota_recuperacao) / 2
        if nova_media >= 7:
            return "Aprovado na recuperação", nova_media
        else:
            return "Reprovado", nova_media

# Entrada das notas
a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))
d = float(input("Digite a quarta nota: "))

# Chamando a função para calcular a média
media = calcular_media(a, b, c, d)

# Verificando a aprovação
resultado, media_final = verificar_aprovacao(media)

# Exibindo o resultado
print(f"Resultado: {resultado}. Média final = {media_final:.2f}")