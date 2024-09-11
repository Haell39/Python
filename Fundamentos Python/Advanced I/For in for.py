def enquanto_loop():
    # Solicita ao usuário o número de iterações
    n = int(input("Quantas vezes você deseja executar o loop? "))
    
    # Loop externo que se repete n vezes
    for _ in range(n):
        # Solicita um número ao usuário
        x = int(input("Digite um número: "))
        
        # Loop interno que imprime números de 0 até x - 1
        for i in range(x):
            print(i)
        print("Fim do loop para este número.\n")  # Mensagem de fim de loop

# Chama a função
enquanto_loop()