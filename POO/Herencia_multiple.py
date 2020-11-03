class Persona():

    def __init__(self, nombre, apellido, edad): #metodo constructor
        
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def getDatosPersonales (self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad) #Devuelve en consola lo que esta almacenado en las variables del constructor

    def habla(self):
        
        return "Estoy hablando" #una chominada
    
    def piensa(self):

        return "Estoy pensando" #etc
    
    def camina(self):      
        
        return "Estoy caminando" #etc
    
    def come(self):       
        
        return "Estoy comiendo" #etc

class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):

        Persona.__init__(self, nombre, apellido, edad) #Llama al constructor de la clase
        
        self.escuela=escuela

    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Escuela: " + self.escuela #Llama al getter de la clase padre y le agrega lo que necesito en esta clase
        

    def estudia(self):

        return "Estoy estudiando"


class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):

        Persona.__init__(self, nombre, apellido, edad) #Llama al constructor de la clase
        
        self.empresa=empresa

    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Empresa: " + self.empresa #Llama al getter de la clase padre y le agrega lo que necesito en esta clase
        

    def estudia(self):

        return "Estoy trabajando"


class Director(Estudiante, Trabajador): #Segun orden de herencia da prioridad a uno o a otro

    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):

        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre,apellido,edad, escuela)

        self.bonus=bonus
    
    def getDatosPersonales(self):

        return super().getDatosPersonales() + " Bonus: " + str(self.bonus)
    
    def Dirige(self):

        return "Estoy dirigiendo"








persona1=Persona("Ana", "Gomez", 35)

estudiante1=Estudiante("Matías", "Ballestero", 11, "Meseta de Orcasitas")

print(persona1.getDatosPersonales())

print(estudiante1.getDatosPersonales())

print("----------------------------------------------------------------")

trabajador1=Trabajador("Antonio", "Perez", 58, "Microsoft")
print(trabajador1.getDatosPersonales())

director1=Director("Juan", "Perez", 55, "Microsfot", "Meseta de Orcasitas", 1500)
print(director1.getDatosPersonales())

