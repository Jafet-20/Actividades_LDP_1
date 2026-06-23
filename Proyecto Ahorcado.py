import random
equipos = ("ecuador", "colombia", "alemania", "argentina", "brasil", "francia", "españa", "portugal")

palabra = random.choice(equipos)

letras_correctas = []
letras_incorrectas = []
intentos = 6

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("¡Bienvenido al juego del ahorcado!")
print("Adivina el equipo de futbol del mundial 2026")
print("Tienes 6 intentos, aprovechalos al máximo")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while intentos > 0:

    print(" ")
    print("Intentos que te quedan:", intentos)
    print("Letras incorrectas:", letras_incorrectas)

    for letra in palabra:
        if letra in letras_correctas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")

    gano = True
    for letra in palabra:
        if letra not in letras_correctas:
            gano = False

    if gano == True:
        break

    letra = input("Escribe una letra: ")
    letra = letra.lower()

    if letra in letras_correctas or letra in letras_incorrectas:
        print("Cambia de letra, esa letra ya la usaste")

    elif letra in palabra:
        letras_correctas.append(letra)
        print("Correcto, esa letra está en la palabra")

    else:
        letras_incorrectas.append(letra)
        intentos = intentos - 1
        print("Letra equivocada, esa letra no está en la palabra")

print(" ")
if gano == True:
    print("Ganaste, bien hecho, el equipo era:", palabra)
else:
    print("Lastimosamente perdiste, el equipo era:", palabra)