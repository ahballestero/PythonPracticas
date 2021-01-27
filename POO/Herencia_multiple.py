class Persona():

    def __init__(self, nombre, apellido, edad):  # metodo constructor

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatosPersonales(self):

        # Devuelve en consola lo que esta almacenado en las variables del constructor
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def habla(self):

        return "Estoy hablando"  # una chominada

    def piensa(self):

        return "Estoy pensando"  # etc

    def camina(self):

        return "Estoy caminando"  # etc

    def come(self):

        return "Estoy comiendo"  # etc


class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):

        # Llama al constructor de la clase
        Persona.__init__(self, nombre, apellido, edad)

        self.escuela = escuela

    def getDatosPersonales(self):

        # Llama al getter de la clase padre y le agrega lo que necesito en esta clase
        return super().getDatosPersonales() + " Escuela: " + self.escuela

    def estudia(self):

        return "Estoy estudiando"


class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):

        # Llama al constructor de la clase
        Persona.__init__(self, nombre, apellido, edad)

        self.empresa = empresa

    def getDatosPersonales(self):

        # Llama al getter de la clase padre y le agrega lo que necesito en esta clase
        return super().getDatosPersonales() + " Empresa: " + self.empresa

    def estudia(self):

        return "Estoy trabajando"


class Director(Estudiante, Trabajador):  # Segun orden de herencia da prioridad a uno o a otro

    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):

        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)

        self.bonus = bonus

    def getDatosPersonales(self):

        return super().getDatosPersonales() + " Bonus: " + str(self.bonus)

    def Dirige(self):

        return "Estoy dirigiendo"


persona1 = Persona("Ana", "Gomez", 35)

estudiante1 = Estudiante("Matías", "Ballestero", 11, "Meseta de Orcasitas")

print(persona1.getDatosPersonales())

print(estudiante1.getDatosPersonales())

print("----------------------------------------------------------------")

trabajador1 = Trabajador("Antonio", "Perez", 58, "Microsoft")
print(trabajador1.getDatosPersonales())

director1 = Director("Juan", "Perez", 55, "Microsfot",
                     "Meseta de Orcasitas", 1500)
print(director1.getDatosPersonales())
