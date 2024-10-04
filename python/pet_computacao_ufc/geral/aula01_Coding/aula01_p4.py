#leia 3 variaveis A,B e C e (A+B) (B*C) (A+B+C+2)
A = int(input("Digite um número.\t"))
B = int(input("Digite o segundo número.\t"))
C = int(input("Digite o terceiro número.\t"))

ab = A + B
bc = B * C
abc2 = (A + B + C) + 2

print("Os valores originais de A, B e C são, respectivamente,", A, B, "e", C,)
print("A soma de", A, "+", B, "é igual a", ab, "\n O produto da multiplicação de", B, "e", C, "é igual a", bc, "e a soma de", A, "+", B, "+", C, "+ 2 é igual a", abc2)