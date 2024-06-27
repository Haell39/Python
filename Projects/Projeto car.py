MAX_CARROS = 10

class Carro:
    def __init__(self, marca, modelo, codigo):
        self.marca = marca
        self.modelo = modelo
        self.codigo = codigo

def registrar_carro(carros):
    if len(carros) >= MAX_CARROS:
        print("Limite máximo de carros atingido!")
        return

    marca = input("Marca do veículo: ")
    modelo = input("Modelo do veículo: ")
    codigo = int(input("Código do veículo: "))

    carros.append(Carro(marca, modelo, codigo))
    print("Carro registrado com sucesso!")

def gerar_relatorio(carros):
    with open("relatorio.txt", "w") as arquivo:
        arquivo.write("----- Relatório de Veículos -----\n\n")
        for i, carro in enumerate(carros):
            arquivo.write(f"Carro {i+1}:\n")
            arquivo.write(f"  Marca: {carro.marca}\n")
            arquivo.write(f"  Modelo: {carro.modelo}\n")
            arquivo.write(f"  Código: {carro.codigo}\n\n")
    
    print("Relatório gerado com sucesso em 'relatorio.txt'!")

def main():
    carros = []

    while True:
        print("\nMenu:")
        print("[1] Registrar Carro")
        print("[2] Registrar Moto (Ainda não implementado)")
        print("[3] Registrar Caminhão (Ainda não implementado)")
        print("[4] Gerar Relatório")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_carro(carros)
        elif opcao == '4':
            gerar_relatorio(carros)
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
