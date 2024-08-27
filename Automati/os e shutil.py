import os
import shutil

# Criando uma nova pasta
os.makedirs('Nova_Pasta', exist_ok=True)

# Movendo um arquivo para a nova pasta
shutil.move('arquivo.txt', 'Nova_Pasta/arquivo.txt')

# Copiando um arquivo
shutil.copy('Nova_Pasta/arquivo.txt', 'arquivo_backup.txt')

# Renomeando um arquivo
os.rename('arquivo_backup.txt', 'arquivo_copia.txt')

# Removendo um arquivo
os.remove('arquivo_copia.txt')
