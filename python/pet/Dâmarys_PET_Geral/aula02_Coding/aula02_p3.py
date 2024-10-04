sf = float(input("Qual o salário fixo do funcionário?\n"))
tv = float(input("Qual o total de vendas do mesmo?\n"))

st = round(((tv * 0.15) + sf), 2)

print("O salário final do vendedor é R$", st)