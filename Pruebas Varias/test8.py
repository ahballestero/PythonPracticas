class Empleado:
    def __init__(self, nombre, cargo, salario):

        self.nombre = nombre

        self.cargo = cargo

        self.salario = salario
    
    def __str__(self):

        return "El empleado {} que trabaja como {} ,tiene un salario de {}".format(self.nombre, self.cargo, self.salario)
    

empleados = [

Empleado("Antonio", "Ascensorista", 900),
Empleado("Juana", "Cientifica", 2300)



]

for i in empleados:
    print(i)

#print(filter(lambda empleado:(empleado.salario>=1000, empleados)))