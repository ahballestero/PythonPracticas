nombresPersonas = []


def agregar_a_lista(lista, nombreIntroducido):
    try:
        if nombreIntroducido in lista:
            raise ValueError
        else:
            lista.append(nombreIntroducido)
            print("El nombre " + "'"+nombreIntroducido+"'" +
                  " ha sido agregado a la lista")
    except ValueError:
        print("Error, el nombre '", nombreIntroducido, "'ya se ha introducido")


introducidos = 1

while introducidos < 11:
    nombre = input("Introduce nombre: ")
    agregar_a_lista(nombresPersonas, nombre)
    introducidos += 1

print(nombresPersonas)
