import random

aleatorio = random.randint(0, 101)

numero = 0
intentos = 0

while aleatorio != numero:
    try:

        numero = int(input("Ingresa un numero: "))

        intentos += 1

        if numero < aleatorio:
            print("Mas alto\n")
        elif numero > aleatorio:
            print("Mas bajo\n")
        else:
            print("\nHas acertado en", intentos, "intentos.\n")
            break

    except ValueError:
        print("Tienes que ingresar un número!\n")
