MAX_VEICULOS = 10
MAX_MARCA_MODELO = 29

import os


class Veiculo:
    def __init__(self):
        self.tipo = ""
        self.marca = ""
        self.modelo = ""
        self.codigo = 0


def registrar_veiculo(veiculos):
    if len(veiculos) >= MAX_VEICULOS:
        print("Limite maximo de veiculos atingido!")
        return

    print("\nRegistro de Veiculo:")

    tipo = int(input("Tipo de veiculo: (1 -> Carro || 2 -> Moto || 3 -> Caminhao): "))
    while tipo < 1 or tipo > 3:
        print("Opcao invalida! Escolha entre as opcoes disponiveis: 1, 2 ou 3.")
        tipo = int(
            input("Tipo de veiculo: (1 -> Carro || 2 -> Moto || 3 -> Caminhao): ")
        )

    veiculo = Veiculo()
    veiculo.tipo = "Carro" if tipo == 1 else "Moto" if tipo == 2 else "Caminhao"
    veiculo.marca = input("Marca: ")
    veiculo.modelo = input("Modelo: ")
    veiculo.codigo = int(input("Codigo: "))

    veiculos.append(veiculo)
    print("Veiculo registrado com sucesso!")


def gerar_relatorio(veiculos):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "relatorio.txt")
    with open(file_path, "w") as arquivo:
        arquivo.write("----- Relatorio de Veiculos -----\n\n")
        for i, veiculo in enumerate(veiculos):
            arquivo.write(f"Veiculo {i + 1}:\n")
            arquivo.write(f"  Tipo: {veiculo.tipo}\n")
            arquivo.write(f"  Marca: {veiculo.marca}\n")
            arquivo.write(f"  Modelo: {veiculo.modelo}\n")
            arquivo.write(f"  Codigo: {veiculo.codigo}\n\n")
    print("Relatorio gerado com sucesso em '{}'!".format(file_path))
    
    def atualizar_veiculo(veiculos):
        if len(veiculos) == 0:
            print(
                "Nenhum veiculo registrado. Registre um veiculo antes de atualizar."
            )
            return

        print("\nAtualizar Veiculo:")
        print("Selecione o veiculo que deseja atualizar:")
        for i, veiculo in enumerate(veiculos):
            print(f"[{i + 1}] {veiculo.marca} - {veiculo.modelo} - {veiculo.codigo}")


def main():
    veiculos = []
    while True:
        print("\nMenu:")
        print("[1] Registrar Veiculo")
        print("[2] Gerar Relatorio")
        print("[3] Atualizar veiculo")
        print("[0] Sair")
        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:
            registrar_veiculo(veiculos)
        elif opcao == 2:
            if len(veiculos) == 0:
                print(
                    "Nenhum veiculo registrado. Registre um veiculo antes de gerar o relatorio."
                )
            else:
                gerar_relatorio(veiculos)
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    main()
