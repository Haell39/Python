import os

def rename_files(directory, prefix):
    # Verifica se o diretório existe
    if not os.path.isdir(directory):
        print(f"O diretório {directory} não existe.")
        return

    # Percorre todos os arquivos no diretório
    for filename in os.listdir(directory):
        # Constrói o caminho completo do arquivo
        old_file = os.path.join(directory, filename)
        # Ignora se não for um arquivo
        if os.path.isfile(old_file):
            # Constrói o novo nome do arquivo com o prefixo
            new_file = os.path.join(directory, prefix + filename)
            # Renomeia o arquivo
            os.rename(old_file, new_file)
            print(f"Renomeado: {old_file} -> {new_file}")

if __name__ == "__main__":
    # Diretório que contém os arquivos
    directory = input("Digite o caminho do diretório: ")
    # Prefixo para adicionar aos arquivos
    prefix = input("Digite o prefixo a ser adicionado: ")
    # Chama a função de renomear arquivos
    rename_files(directory, prefix)
