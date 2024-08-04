from textblob import TextBlob

def analisar_sentimento(texto):
    blob = TextBlob(texto)
    sentimento = blob.sentiment
    return sentimento

def main():
    print("Bem-vindo ao Analisador de Sentimento!")
    print("Digite seu texto (ou 'sair' para encerrar):")

    while True:
        texto = input(">> ")

        if texto.lower() == 'sair':
            print("Encerrando o Analisador de Sentimento.")
            break

        sentimento = analisar_sentimento(texto)
        print(f"Polaridade: {sentimento.polarity:.2f}, Subjetividade: {sentimento.subjectivity:.2f}")

if __name__ == "__main__":
    main()
