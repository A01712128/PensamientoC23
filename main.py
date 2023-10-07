#LIBRERIAS
import random
import sys


#VARIABLES GLOBALES
lives = 3
score = 0
edades_jugadores = []
edades_jugadores_niños = []
edades_jugadores_jovenes = []
edades_jugadores_adultos = []

def draw_perdio():
    print("Perdiste!")


def draw_happyface():
    print("\n! :-D !")


def draw_sadface():
    print("\n!! Oh No !!")

def print_score(score):
    print("Score Actual: %s" % score)

def print_lives(lives):
    print("Vidas Restantes: %s" % lives)

#SELECCION DIFICULTADES
dificultades = {
    "facil": (1, 10),
    "intermedio": (1, 50),
    "dificil": (1, 100)
}


#CODIGO DE LA SUMA
def suma_game():
    global lives, score

    print("\nHas seleccionado Suma.\n")
    
    while True:
        print("Selecciona una dificultad:")
        for dificultad in dificultades:
            print(f"- {dificultad.capitalize()}")

        seleccion = input("Dificultad: ").lower()
        if seleccion in dificultades:
            rango = dificultades[seleccion]
            break
        else:
            print("Dificultad no válida. Por favor, selecciona una dificultad válida.")
    
    while lives > 0:
        numero1 = random.randint(rango[0], rango[1])
        numero2 = random.randint(rango[0], rango[1])
        respuesta = input(f"¿Cuál es la suma de {numero1} + {numero2}? (Enter 'q' to quit)")

        if respuesta == 'q':
            print("\n Gracias por jugar, Esperamos verte pronto\n")
            sys.exit(0)

        respuesta = int(respuesta)

        if respuesta == numero1 + numero2:
            print("¡Correcto! La respuesta es correcta.")
            score += 1
            draw_happyface()
            print("\n Genial! \n")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es {numero1 + numero2}.")
            lives -= 1
#VIDAS 0, PREGUNTAR SI DESEA VOLVER A JUGAR
        if lives == 0:
            draw_sadface()
            print("\n On no!, Perdiste todas tus vidas \n")
            play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower()
            if play_again== 's':
                lives = 3
                score = 0
                print("\n¡Nuevo juego!\n")
            else:
                print("\nHasta luego. Gracias por jugar.\n")
                sys.exit(0)
#IMPRESION SCORE FINAL
        print_score(score)
        print_lives(lives)


#CODIGO PARA LA RESTA
def resta_game():
    global lives, score

    print("Has seleccionado Resta.\n")
    
    while True:
        print("Selecciona una dificultad:")
        for dificultad in dificultades:
            print(f"- {dificultad.capitalize()}")

        seleccion = input("Dificultad: ").lower()

        if seleccion in dificultades:
            rango = dificultades[seleccion]
            break
        else:
            print("Dificultad no válida. Por favor, selecciona una dificultad válida.")
    
    while lives > 0:
        numero1 = random.randint(rango[0], rango[1])
        numero2 = random.randint(rango[0], rango[1])
        respuesta = input(f"¿Cuál es la resta de {numero1} - {numero2}? (Enter 'q' to quit)")

        if respuesta == 'q':
            print("\n Gracias por jugar, Esperamos verte pronto\n")
            sys.exit(0)

        respuesta = int(respuesta)

        if respuesta == numero1 - numero2:
            print("¡Correcto! La respuesta es correcta.")
            score += 1
            draw_happyface()
            print("\n Genial! \n")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es {numero1 - numero2}.")
            lives -= 1
#VIDAS 0, PREGUNTAR SI DESEA VOLVER A JUGAR
        if lives == 0:
            draw_sadface()
            print("\n On no!, Perdiste todas tus vidas \n")
            play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower()
            if play_again== 's':
                lives = 3
                score = 0
                print("\n¡Nuevo juego!\n")
            else:
                print("\nHasta luego. Gracias por jugar.\n")
                sys.exit(0)
#IMPRESION SCORE FINAL
        print_score(score)
        print_lives(lives)


#CODIGO PARA LA MULTIPLICACION
def multiplicacion_game():
    global lives, score

    print("Has seleccionado Multiplicacion.\n")
    
    while True:
        print("Selecciona una dificultad:")
        for dificultad in dificultades:
            print(f"- {dificultad.capitalize()}")

        seleccion = input("Dificultad: ").lower()

        if seleccion in dificultades:
            rango = dificultades[seleccion]
            break
        else:
            print("Dificultad no válida. Por favor, selecciona una dificultad válida.")
    
    while lives > 0:
        numero1 = random.randint(rango[0], rango[1])
        numero2 = random.randint(rango[0], rango[1])
        respuesta = input(f"¿Cuál es la multiplicacion de {numero1} * {numero2}? (Enter 'q' to quit)")

        if respuesta == 'q':
            print("\n Gracias por jugar, Esperamos verte pronto\n")
            sys.exit(0)

        respuesta = int(respuesta)

        if respuesta == numero1 * numero2:
            print("¡Correcto! La respuesta es correcta.")
            score += 1
            draw_happyface()
            print("\n Genial! \n")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es {numero1 * numero2}.")
            lives -= 1

#VIDAS 0, PREGUNTAR SI DESEA VOLVER A JUGAR
        if lives == 0:
            draw_sadface()
            print("\n On no!, Perdiste todas tus vidas \n")
            play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower()
            if play_again == 's':
                lives = 3
                score = 0
                print("\n¡Nuevo juego!\n")
            else:
                print("\nHasta luego. Gracias por jugar.\n")
                sys.exit(0)
#IMPRESION SCORE FINAL
        print_score(score)
        print_lives(lives)


#CODIGO PARA LA DIVISION
def division_game():
    global lives, score

    print("Has seleccionado Division.\n")
    
    while True:
        print("Selecciona una dificultad:")
        for dificultad in dificultades:
            print(f"- {dificultad.capitalize()}")

        seleccion = input("Dificultad: ").lower()

        if seleccion in dificultades:
            rango = dificultades[seleccion]
            break
        else:
            print("Dificultad no válida. Por favor, selecciona una dificultad válida.")
    
    while lives > 0:
        numero1 = random.randint(rango[0], rango[1])
        numero2 = random.randint(rango[0], rango[1])
        respuesta = input(f"¿Cuál es la division de {numero1} / {numero2}? (Enter 'q' to quit)")

        if respuesta == 'q':
            print("\n Gracias por jugar, Esperamos verte pronto\n")
            sys.exit(0)

        respuesta = int(respuesta)

        if respuesta == numero1 / numero2:
            print("¡Correcto! La respuesta es correcta.")
            score += 1
            draw_happyface()
            print("\n Genial! \n")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es {numero1 / numero2}.")
            lives -= 1

#VIDAS 0, PREGUNTAR SI DESEA VOLVER A JUGAR
        if lives == 0:
            draw_sadface()
            print("\n On no!, Perdiste todas tus vidas \n")
            play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower()
            if play_again == 's':
                lives = 3
                score = 0
                print("\n¡Nuevo juego!\n")
            else:
                print("\nHasta luego. Gracias por jugar.\n")
                sys.exit(0)
#IMPRESION SCORE FINAL
        print_score(score)
        print_lives(lives)


# INICIO DEL PROGRAMA
print("\nBienvenido a Desafía Tu Mente!\n")
name = input("Como te llamas? ")

print("\nHola " + name + "!\n")

#PEDIR Y REGISTRAR LAS EDADES DEL JUGADOR
edad_jugador = int(input("Por favor, ingresa tu edad: "))
edades_jugadores.append(edad_jugador)
if edad_jugador < 18:
    edades_jugadores_niños.append(edad_jugador)
elif edad_jugador < 30:
    edades_jugadores_jovenes.append(edad_jugador)
else:
    edades_jugadores_adultos.append(edad_jugador)

while True:  #BUCLE PARA QUE EL JUGAR PUEDA VOLVER A JUGAR
    print("\nOk, Empecemos :-)!\n")
    print("Para jugar, selecciona una de las operaciones matemáticas: suma, resta, multiplicación o división.")
    print("Después, selecciona tu nivel de dificultad.")
    print("\nResponde las operaciones matemáticas.")
    print("Si contestas bien, ganas un punto.")
    print("Si contestas mal, pierdes una vida.")
    print("Si pierdes tus tres vidas, pierdes el juego :-p!\n")

    print("\nSelecciona una Opción (Enter 'q' to quit):\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("\nIngresa el número de la opción que deseas seleccionar: ").lower()

#SALIR DEL JUEGO SI EL JUGADOR LO DECIDE
    if opcion == 'q':
        print("\nGracias por jugar, Esperamos verte pronto\n")
        sys.exit(0)  

#OPCIONES DE OPERACION
    if opcion == "1":
        suma_game()
    elif opcion == "2":
        resta_game()
    elif opcion == "3":
        multiplicacion_game()
    elif opcion == "4":
        division_game()
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

#DESPUES DE QUE ACABA EL JUEGO
    if lives == 0:
        draw_sadface()
        print("\nOn no!, Perdiste todas tus vidas \n")
        play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower()
        if play_again == 's':
            lives = 3
            score = 0
            print("\n¡Nuevo juego!\n")
        else:
            print("\nHasta luego. Gracias por jugar.\n")
            sys.exit(0)
