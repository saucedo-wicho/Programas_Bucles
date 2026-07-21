inicio = int(input("Primer numero: "))
diferencia = int(input("Diferencia: "))
limite = int(input("Limite máximo: "))

num = inicio
while True:
    print(num, end= " ")
    num += diferencia
    if num > limite:
        break

print(f"Secuencia aritmética desde {inicio} hasta {limite}")