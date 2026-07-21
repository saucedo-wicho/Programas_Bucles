while True: 
    letra = input("Ingresa letra (espacio termina): ")
    
    if letra == " ":
        break
    letra = letra.lower()
    
    if letra in "aeiou":
        print("Vocal")
    else:
        print("Consonante")
    
print("Programa finalizado")