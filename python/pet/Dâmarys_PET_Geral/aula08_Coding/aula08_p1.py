import math

print("----------------------- CALCULANDO A HPOTENUSA -----------------------")

cateto_oposto = int(input("Insira o valor do cateto oposto: "))
cateto_adjacente = int(input("Insira o valor do cateto adjacente: "))

cateto_2 = math.sqrt((cateto_oposto**2) + (cateto_adjacente**2))
print("O valor da hipotenusa é: %.2f" %cateto_2)
print("----------------------------------------------------------------------")
