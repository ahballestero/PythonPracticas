class Persona():

    def __init__(self, nom, ape, edad):

        self.nombre=nom
        self.apellido=ape
        self.edad=edad

    def __str__(self):

        return "Datos de la persona\n" + "Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nEdad: " + str(self.edad)

p1=Persona("Ariel", "Ballestero", 21)

print(p1)
