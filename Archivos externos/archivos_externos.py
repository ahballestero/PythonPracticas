from io import open
import os

os.makedirs("PruebaDirectorios2")
os.chdir("PruebaDirectorios2")

# (w)-escribe (r)-lee y (a)-modifica/agrega
file = open("archivotestdirs2.txt", "w")

file.write("Agregamos algo para probar")  # escribir
file.write("\n Agregamos algo mas para probar")  # escribir

# open_file=file.read() #con esto lee la infomacion

#open_file = file.readlines()
print(os.getcwd())
print(os.listdir())



file.close()
