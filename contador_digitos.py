num = int(input("Numero entero: "))

if num == 0:
    digitos = 1
else: 
    digitos = 0
    if num < 0:
        num = abs(num)
    while num > 0:
        num //= 10
        digitos += 1
    
print(f"El numero tiene {digitos} digitos")