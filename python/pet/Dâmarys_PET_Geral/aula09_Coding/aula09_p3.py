def voto(idade):
    if idade < 16:
        print(f"Sua idade é {idade}, você NÃO PODE VOTAR.")

    elif (idade >= 16 and idade <18) or idade > 70:
            print("Seu voto é opcional.")
    
    else:
        print("Seu voto é obrigatório.")

a = int(input("Insira a sua idade: "))

voto(a)