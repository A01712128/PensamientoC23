# Importación de librerias
import random
import sys

# Variables globales
lives = 3
score = 0
edades_jugadores = []
edades_jugadores_ninos = []
edades_jugadores_jovenes = []
edades_jugadores_adultos = []

# Funcion para mostrar que el jugador perdio
def draw_perdio():
    print("Perdiste!")

# Funciones para mostrar caras felices y tristes
def draw_happyface():
    print("\n! :-D !")

def draw_sadface():
    print("\n!! :-Oh No !!")

# Funciones para imprimir el puntaje y las vidas
def print_score(score):
    print("Score Actual: %s" % score)

def print_lives(lives):
    print("Vidas Restantes: %s" % lives)

# Seleccion de dificultades
dificultades = {
    "facil": (1, 10),
    "intermedio": (1, 50),
    "dificil": (1, 100)
}

# Funcion para el juego de suma
def suma_game():
    global lives, score

    print("\nHas seleccionado Suma.\n")
#Seleccion de dificultad en suma
    while True:
        print("Selecciona una dificultad:")
        for dificultad in dificultades:
            print(f"- {dificultad.upper()}")

        seleccion = input("Dificultad: ").lower()
        if seleccion in dificultades:
            rango = dificultades[seleccion]
            break
        else:
            print("Dificultad no valida. Por favor, selecciona una dificultad valida.")
#Operacion de numero 1 y numero 2 de la suma
    while lives > 0:
        numero1 = random.randint(rango[0], rango[1])
        numero2 = random.randint(rango[0], rango[1])
        respuesta = input(f"¿Cual es la suma de {numero1} + {numero2}? (Enter 'q' to quit)")

        if respuesta == 'q':
            print("\n Gracias por jugar, Esperamos verte pronto\n")
            #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
            sys.exit(0)

        respuesta = int(respuesta)
#Respuesta correcta mas 1 punto
        if respuesta == numero1 + numero2:
            print("¡Correcto! La respuesta es correcta.")
            score += 1
            draw_happyface()
            print("\n Genial! \n")
#Respuesta incorrecta menos 1 punto
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es {numero1 + numero2}.")
            lives -= 1

        # Vidas agotadas, preguntar si desea volver a jugar
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
                #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
                sys.exit(0)
        
        # Impresion del puntaje final
        print_score(score)
        print_lives(lives)

# Funcion para el juego de resta
def resta_game():
    global lives, score

    print("Has seleccionado Resta.\n")
#Seleccion de dificultad en resta 
    while True:
        print("Selecciona una dificultad:")
        for dificultad in dificultades:
            print(f"- {dificultad.upper()}")

        seleccion = input("Dificultad: ").lower()

        if seleccion in dificultades:
            rango = dificultades[seleccion]
            break
        else:
            print("Dificultad no valida. Por favor, selecciona una dificultad valida.")
#Operacion de numero 1 y numero 2 de la resta  
    while lives > 0:
        numero1 = random.randint(rango[0], rango[1])
        numero2 = random.randint(rango[0], rango[1])
        respuesta = input(f"¿Cual es la resta de {numero1} - {numero2}? (Enter 'q' to quit)")

        if respuesta == 'q':
            print("\n Gracias por jugar, Esperamos verte pronto\n")
            #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
            sys.exit(0)

        respuesta = int(respuesta)
#Respuesta correcta mas 1 punto
        if respuesta == numero1 - numero2:
            print("¡Correcto! La respuesta es correcta.")
            score += 1
            draw_happyface()
            print("\n Genial! \n")
#Respuesta incorrecta menos 1 punto
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es {numero1 - numero2}.")
            lives -= 1

        # Vidas agotadas, preguntar si desea volver a jugar
        if lives == 0:
            draw_sadface()
            print("\n On no!, Perdiste todas tus vidas \n")
            #Preguntar si el jugador desea jugar nuevamente
            play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower()
            if play_again == 's':
                lives = 3
                score = 0
                print("\n¡Nuevo juego!\n")
            else:
                print("\nHasta luego. Gracias por jugar.\n")
                #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
                sys.exit(0)
        
        # Impresion del puntaje final
        print_score(score)
        print_lives(lives)

# Funcion para el juego de multiplicacion
def multiplicacion_game():
    global lives, score

    print("Has seleccionado Multiplicacion.\n")
    #Seleccion de dificultad en multiplicacion
    while True:
        print("Selecciona una dificultad:")
        for dificultad in dificultades:
            print(f"- {dificultad.upper()}")

        seleccion = input("Dificultad: ").lower()

        if seleccion in dificultades:
            rango = dificultades[seleccion]
            break
        else:
            print("Dificultad no valida. Por favor, selecciona una dificultad valida.")
#Operacion de numero 1 y numero 2 de la multiplicacion
    while lives > 0:
        numero1 = random.randint(rango[0], rango[1])
        numero2 = random.randint(rango[0], rango[1])
        respuesta = input(f"¿Cual es la multiplicacion de {numero1} * {numero2}? (Enter 'q' to quit)")

        if respuesta == 'q':
            print("\n Gracias por jugar, Esperamos verte pronto\n")
            #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
            sys.exit(0)

        respuesta = int(respuesta)
#Respuesta correcta mas 1 punto
        if respuesta == numero1 * numero2:
            print("¡Correcto! La respuesta es correcta.")
            score += 1
            draw_happyface()
            print("\n Genial! \n")
#Respuesta incorrecta menos 1 punto
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es {numero1 * numero2}.")
            lives -= 1

        # Vidas agotadas, preguntar si desea volver a jugar
        if lives == 0:
            draw_sadface()
            print("\n On no!, Perdiste todas tus vidas \n")
            #Preguntar si el jugador desea jugar nuevamente
            play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower()
            if play_again == 's':
                lives = 3
                score = 0
                print("\n¡Nuevo juego!\n")
            else:
                print("\nHasta luego. Gracias por jugar.\n")
                #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
                sys.exit(0)
        
        # Impresión del puntaje final
        print_score(score)
        print_lives(lives)

# Función para el juego de división
def division_game():
    global lives, score

    print("Has seleccionado Division.\n")
    
    #Seleccion de dificultad en division
    while True:
        print("Selecciona una dificultad:")
        for dificultad in dificultades:
            print(f"- {dificultad.upper()}")

        seleccion = input("Dificultad: ").lower()

        if seleccion in dificultades:
            rango = dificultades[seleccion]
            break
        else:
            print("Dificultad no valida. Por favor, selecciona una dificultad valida.")
    
    #Operacion de numero 1 y numero 2 de la division
    while lives > 0:
        numero1 = random.randint(rango[0], rango[1])
        numero2 = random.randint(rango[0], rango[1])
        respuesta = input(f"¿Cual es la division de {numero1} / {numero2}? (Enter 'q' to quit)")

        if respuesta == 'q':
            print("\n Gracias por jugar, Esperamos verte pronto\n")
            #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
            sys.exit(0)

        respuesta = int(respuesta)

#Respuesta correcta mas 1 punto
        if respuesta == numero1 / numero2:
            print("¡Correcto! La respuesta es correcta.")
            score += 1
            draw_happyface()
            print("\n Genial! \n")
#Respuesta incorrecta -1 punto
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es {numero1 / numero2}.")
            lives -= 1

        # Vidas agotadas, pregunta si desea volver a jugar
        if lives == 0:
            draw_sadface()
            print("\n On no!, Perdiste todas tus vidas \n")
            #Preguntar si el jugador desea jugar nuevamente
            play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower()
            if play_again == 's':
                lives = 3
                score = 0
                print("\n¡Nuevo juego!\n")
            else:
                print("\nHasta luego. Gracias por jugar.\n")
                #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
                sys.exit(0)
        
        # Impresión del puntaje final
        print_score(score)
        print_lives(lives)

# Inicio del programa
print("\nBienvenido a Desafia Tu Mente!\n")
name = input("Como te llamas? ")

print("\nHola " + name + "!\n")

# Pedir y registrar las edades del jugador
edad_jugador = int(input("Por favor, ingresa tu edad: "))
edades_jugadores.append(edad_jugador)
if edad_jugador < 18:
    edades_jugadores_ninos.append(edad_jugador)
elif edad_jugador < 30:
    edades_jugadores_jovenes.append(edad_jugador)
else:
    edades_jugadores_adultos.append(edad_jugador)

while True:  #Reglas del juego
    print("\nOk, Empecemos :-)!\n")
    print("Para jugar, selecciona una de las operaciones matematicas: suma, resta, multiplicacion o division.")
    print("Despues, selecciona tu nivel de dificultad.")
    print("\nResponde las operaciones matematicas.")
    print("Si contestas bien, ganas un punto.")
    print("Si contestas mal, pierdes una vida.")
    print("Si pierdes tus tres vidas, pierdes el juego :-p!\n")

    print("\nSelecciona una Opcion (Enter 'q' to quit):\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    opcion = input("\nIngresa el numero de la opcion que deseas seleccionar: ").lower()

    # Salir del juego si el jugador lo decide
    if opcion == 'q':
        print("\nGracias por jugar, Esperamos verte pronto\n")
        #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
        sys.exit(0)  

    # Opciones de operaciónes matematicas
    if opcion == "1":
        suma_game()
    elif opcion == "2":
        resta_game()
    elif opcion == "3":
        multiplicacion_game()
    elif opcion == "4":
        division_game()
    else:
        print("Opcion no valida. Por favor, selecciona una opción valida.")

    # Después de que acaba el juego
    if lives == 0:
        draw_sadface()
        print("\nOn no!, Perdiste todas tus vidas \n")
        #Preguntar si el jugador desea jugar nuevamente
        play_again = input("¿Quieres jugar de nuevo? (Sí: s / No: n): ").lower() 
        #Reinicio de juego si asi lo desea el jugador
        if play_again == 's':
            lives = 3
            score = 0
            print("\n¡Nuevo juego!\n")
        else:
            #Despedida del jugador
            print("\nHasta luego. Gracias por jugar.\n")
            #Salir del programa con un código de salida de 0.El programa ha finalizado con éxito.
            sys.exit(0)
