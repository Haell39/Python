#comissão para vendedores:


comissão = 5/100
preço_unitario = float(input("Qual o preço unitario: "))
qntd_vendida = int(input("Quantidade vendida: "))

vendedor_id = int(input("Qual o ID do vendedor: "))


total_venda = preço_unitario * qntd_vendida

total_comissao = comissão * total_venda

print(f"O valor da comissão do vendedor {vendedor_id} é {total_comissao} R$")
