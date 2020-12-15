from io import open


# (w)-escribe (r)-lee y (a)-modifica/agrega
file = open("archivotest.txt", "a")

file.write("\n Agregamos algo para probar") #escribir


# open_file=file.read() #con esto lee la infomacion

#open_file = file.readlines()

file.close()
