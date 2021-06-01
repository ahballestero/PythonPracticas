import re

lista_terminos=["Camión", "Camion", "Niños", "Niñas", "Ejemplo"]

for termino in lista_terminos:
    if re.findall("cami[oó]n", termino):
        print(termino)
    else:
        print("No se encontro nada")
