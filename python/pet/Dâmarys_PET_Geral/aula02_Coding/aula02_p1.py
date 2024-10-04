x = int(input("Quantas unidades do produto 1 o usuário deseja comprar?\n"))
x_p = float(input("Qual o preço do produto 1?\n"))
y = int(input("Quantas unidades do produto 2 o usuário deseja comprar?\n"))
y_p = float(input("Qual o preço do produto 2?\n"))

z = (x*x_p) + (y*y_p)

print("O valor total a ser pago é R$", z)