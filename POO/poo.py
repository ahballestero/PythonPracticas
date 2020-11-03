class Coche():
    ruedas=4
    largoChasis=260
    anchoChasis=130
    arrancado=False
    puertas=4

    def arrancar(self):
        self.arrancado=True
    
    def estadoCoche(self):
        if (self.arrancado):
            return "El coche esta arrancado"
        else:
           return "El coche esta parado"


bmw=Coche() #ejemplar de clase

bmw.arrancar()

print("El coche tiene", bmw.ruedas, "ruedas")
print("El coche tiene", bmw.puertas, "puertas")
print(bmw.estadoCoche())
