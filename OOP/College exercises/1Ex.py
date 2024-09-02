#Calcula o estoque medio:
print("Estoque medio:")
print("Insira as quantidades:")
qntd_min = int(input("Quantidade minima: "))
qntd_max = int(input("Quantidade maxima: "))

def avg_stock():
    AVG = qntd_min + qntd_max / 2
    return AVG


print(f'O estoque medio é ({avg_stock()})') 

