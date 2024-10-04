from math import ceil

custo = float(input("Tirulipa, por favor, insira o custo total do seu show: "))
ingresso = float(input("Insira o valor do ingresso: "))

meta_venda = custo / ingresso

print("Deverás vender, no mínimo, %.0f" %meta_venda, "ingressos para custear o show.")

lucro = ceil((custo*1.23) / ingresso)

print("-----------------------------------------------------------------")
print("Para obteres um lucro de 23%, deverás vender" ,lucro, "ingressos.")
print("-----------------------------------------------------------------")