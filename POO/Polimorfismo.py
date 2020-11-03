class Persona():

    def hablar(self):

        return "Hablo como una persona"

class Trabajador(Persona):

    def hablar(self):

        return "Hablo como un trabajador"

class Director(Trabajador):

    def hablar(self):

        return "Hablo como un director"

def hazlesHablar(listaDeLasPersonas): #parametro, no confundir con la lista de mas abajo

    for persona in listaDeLasPersonas: #persona es el que tiene polimorfismo
        print(persona.hablar())


Antonio=Persona()

Maria=Trabajador()

Ana=Director()

print(Antonio.hablar())

print(Maria.hablar())

print(Ana.hablar())

print("-------------------------------------------------------")

listaPersonas=[Antonio, Ana, Maria]

hazlesHablar(listaPersonas)




