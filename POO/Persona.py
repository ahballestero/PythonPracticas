class Persona():
    __nombre = ""
    __apellido = ""
    __edad = 0
    __genero = "sin definir"

    def __init__(self, nombre, apellido, genero):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero

    def setEdad(self, laEdad):
        if laEdad < 0 or laEdad > 100:
            print("La edad no es valida")
        else:
            self.__edad = laEdad
            return self.__edad

    def habla(self):

        return "La persona que se llama" + self.__nombre + "está hablando"

    def camina(self):

        return "La persona que se llama" + self.__nombre + "está caminando"

    def getDatos(self):

        return "Nombre: " + self.__nombre + " Apellido: " + self.__apellido + \
            " Edad: " + str(self.__edad) + " Género: " + self.__genero


p1 = Persona("Ariel", "Ballestero", "masculino")

p1.setEdad(14)

print(p1.getDatos())

p1.nombre = "Alicia"

print(p1.getDatos())
