N = int(input("Numero positivo: "))
i = 1

while True:
    if i % 2 != 0:
        print(i, end = " ")
    i += 1
    if i > N: 
        break

print("Fin. Se mostraron los impartes hasta", N)