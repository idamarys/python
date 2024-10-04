def mais_Sig(n):
    if n < 10:
        return n
    else:
        return mais_Sig(n//10)

print(mais_Sig(1046958438796))