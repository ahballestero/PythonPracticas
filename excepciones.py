import sys


def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def multiplica(n1,n2):
    return n1*n2

def divide(n1,n2):

    try:
        return n1/n2    

    except ZeroDivisionError:
        print("No se puede dividir entre cero")
intentos=0

while True:
    op1=(int(input("Ingrese el primer número: ")))
    op2=(int(input("Ingrese el segundo número: ")))

    operation=input("Ingrese la operación a realizar (suma,resta,multiplica,divide :" )
    intentos+=1
    if intentos == 3:
        print("Has excedido el número de intentos")
        sys.exit()

    if operation == "suma":
        print("El resultado de la suma es:" ,suma(op1,op2))
    elif operation == "resta":
        print(resta(op1,op2))
    elif operation == "multiplica":
        print(multiplica(op1,op2))
    elif operation == "divide":
        print(divide(op1,op2))
    else:
        print("Operación no válida")

print("Continua la ejecución del programa")