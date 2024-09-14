def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def peso_ideal_homem(altura):
    return 72.7 * altura - 58

def peso_ideal_mulher(altura):
    return 62.1 * altura - 44.7

def status_peso_homem(peso_atual, altura):
    peso_ideal = peso_ideal_homem(altura)
    if peso_atual < peso_ideal:
        return 'Abaixo do peso ideal'
    elif peso_atual > peso_ideal:
        return 'Acima do peso ideal'
    else:
        return 'No peso ideal'

def status_peso_mulher(peso_atual, altura):
    peso_ideal = peso_ideal_mulher(altura)
    if peso_atual < peso_ideal:
        return 'Abaixo do peso ideal'
    elif peso_atual > peso_ideal:
        return 'Acima do peso ideal'
    else:
        return 'No peso ideal'

while True:
    print("Escolha uma opção:")
    print("1 – Conversão de Graus Celsius em Graus Fahrenheit")
    print("2 – Conversão de Graus Fahrenheit em Graus Celsius")
    print("3 – Peso ideal do homem")
    print("4 – Peso ideal da mulher")
    
    opcao = input("Digite sua opção (1/2/3/4): ")

    if opcao == '1':
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit.")
    
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit é igual a {celsius} graus Celsius.")
    
    elif opcao == '3':
        altura = float(input("Digite sua altura em metros: "))
        peso_atual = float(input("Digite seu peso atual em kg: "))
        status = status_peso_homem(peso_atual, altura)
        peso_ideal = peso_ideal_homem(altura)
        print(f"O peso ideal para sua altura é {peso_ideal:.2f} kg. Você está {status}.")
    
    elif opcao == '4':
        altura = float(input("Digite sua altura em metros: "))
        peso_atual = float(input("Digite seu peso atual em kg: "))
        status = status_peso_mulher(peso_atual, altura)
        peso_ideal = peso_ideal_mulher(altura)
        print(f"O peso ideal para sua altura é {peso_ideal:.2f} kg. Você está {status}.")
    
    else:
        print("Opção inválida. Tente novamente.")

    encerrar = input("Deseja encerrar o programa? (S/N): ").strip().upper()
    if encerrar == 'S':
        break