import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona con el nombre de:", self.nombre)

    def __str__(self):
        return f"{self.nombre} {self.genero} {self.edad}"

class ListaPersonas:

    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print(f"Se cargaron {len(self.personas)} personas del fichero externo")
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
        

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarP()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarP(self): #Guarda personas en fichero externo
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def mostrarInfo(self):
        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()
persona=Persona("Sandra", "Femenino", 29) #Segun cambie esto se van agregando personas nuevas
miLista.agregarPersonas(persona)
miLista.mostrarInfo()






        