import math

option = int(input(
    "Elige una figura: \n 1: Cuadrado \n 2: Rectángulo \n 3: Triángulo \n 4: Círculo \n"))

while True:
    if option == 1:
        lado = int(input("Introduce el lado: "))
        print("El área del cuadrado es:", math.pow(lado, 2))
        break

    elif option == 2:
        base = int(input("Introduce la base: "))
        altura = int(input("Introduce la altura: "))
        print("El área del rectángulo es:", base * altura)
        break

    elif option == 3:
        base2 = int(input("Introduce la base: "))
        altura2 = int(input("Introduce la altura: "))
        print("El área del triángulo es:", (base2 * altura2)/2)
        break

    elif option == 4:
        radio = float(input("Introduce el radio: "))
        print("El área del círculo es:", math.pi * (math.pow(radio, 2)))
        break

    else:
        print("Opción no valida")
        break
