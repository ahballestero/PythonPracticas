class Persona():

    def __init__(self, nombre, apellido, edad):
        
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def getDatosPersonales (self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad) #Devuelve en consola lo que esta almacenado

    def habla(self):
        
        return "Estoy hablando"
    
    def piensa(self):

        return "Estoy pensando"
    
    def camina(self):      
        
        return "Estoy caminando"
    
    def come(self):       
        
        return "Estoy comiendo"

class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):

        super().__init__(nombre, apellido, edad) #Llama al constructor de la clase padre
        
        self.escuela=escuela

    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Escuela: " + self.escuela #Llama al getter de la clase padre y le agrega lo que necesito en esta clase
        

    def estudia(self):

        return "Estoy estudiando"



persona1=Persona("Ana", "Gomez", 35)

estudiante1=Estudiante("Matías", "Ballestero", 11, "Meseta de Orcasitas")

print(persona1.getDatosPersonales())

print(estudiante1.getDatosPersonales())
