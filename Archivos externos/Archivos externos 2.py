from io import open

archivo_externo = open("archivotest.txt", "r+")


# archivo_externo.seek(len(archivo_externo.read())/2)

# archivo_externo.seek(len(archivo_externo.readline()))

lista_archivo = archivo_externo.readlines()

lista_archivo[1] = "Hoy es Lunes \n"

archivo_externo.seek(0)

archivo_externo.writelines(lista_archivo)


archivo_externo.close()


