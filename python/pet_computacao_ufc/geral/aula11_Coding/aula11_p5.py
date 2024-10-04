def div (divisor, dividendo):
    if dividendo < divisor:
        return 0
    else:
        return +1 + div (divisor, dividendo - divisor)

print(div(3,7))