A = float(input("Qual o valor da primeira nota?\n"))
B = float(input("Qual o valor da segunda nota?\n"))

peso_a = 2.5
peso_b = 7.5

m = ((peso_a * A) + (peso_b * B))/(peso_a + peso_b)
m = round(m, 1)

print("A média poderada do indivíduo é", m)