palabra = input("Ingrese una palabra: ").lower()

contador = 0
for letra in palabra:
    if letra == 'a':
        contador += 1

print(f"La letra 'a' aparece {contador} veces")
