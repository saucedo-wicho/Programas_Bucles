n = int(input("Cantidad de numeros a ingresar: "))

mayores = 0
menores = 0
iguales = 0

for i in range(n):
    num = int(input("Numero: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print(f"Mayores a 0: {mayores}")
print(f"Menores a 0: {menores}")
print(f"Iguales a 0: {iguales}")