import random
import sys

lives = 3
score = 0

def draw_perdio():
    print("Perdiste!")


def draw_happyface():
    print("\n!!!!! :-D !!!!!")


def draw_sadface():
    print("\n!!$%@ :-( @%$!!")

def print_score(score):
    print("Score Actual: %s" % score)

def print_lives(lives):
    print("Vidas Restantes: %s" % lives)

def ask_range():
    print("Selecciona un numero a multiplicar")
    while(True):
        val_1 = input("Entre: ")
        try:
            val_1 = int(val_1)
        except ValueError:
            print("'%s' No es un numero entero. Intenta Otra Vez :-)." % val_1)
            continue

        if val_1 < 0:
            print("Unicamente numeros positivos. Intenta Otra vez :-).")
            continue

        break

    while(True):
        val_2 = input("Y El: ")

        try:
            val_2 = int(val_2)
        except ValueError:
            print("'%s' No es un numero entero. Intenta Otra Vez :-)." % val_2)
            continue

        if val_2 < 0:
            print("Unicamente numeros positivos. Intenta Otra vez :-).")
            continue

        if val_1 >= val_2:
            print("El segundo numero debe ser mayor o igual a "
                    + "El primero! Intenta Otra Vez :-).")
            continue

        break

    return (val_1, val_2)

print("\nBienvenido!\n")
name = input("Como te llamas? ")

print("\nHola " + name + "!\n")

tuple_int = ask_range()
min_int, max_int = tuple_int[0], tuple_int[1]


print("\nOk, Empezemos :-)!\n")
print("Para jugar responde las siguientes operaciones.")
print("Si contestas bien te ganas un punto.")
print("Si contestas mal pierdes una vida.")
print("Si pierdes tus tres vidas, pierdes el juego :-p!")
print("Ingresa la letra q si quieres terminar el juego.\n")

print_score(score)
print_lives(lives)

while True:
        x = random.randint(min_int, max_int)
        y = random.randint(min_int, max_int)

        while True:
            ans = input("\nQue es %s*%s? " % (x,y))
    
            if ans == 'q':
                print ("\nGracias por jugar!" + " :-D!\n")
                #sys.exit(0)     
                exit()

            try:
                ans = int(ans)
                break
            except ValueError:
                print("'%s' No es un numero entero, intenta otra vez :-)." % ans)
        right_answer = x*y

        if (ans==right_answer):
            score = score + 1

            draw_happyface()
            print("\nGenial!!!")

        else:
            lives = lives - 1

            if lives == 0:
                draw_perdio()
                print("Oh NO, Perdiste todas tus vidas!!!")
                print("Suerte para la proxima :-P!\n")
                #sys.exit(0) 
                exit()

            draw_sadface()
            print("\nQue mal! Respuesta Incorrecta!")

            print_score(score)
            print_lives(lives)
