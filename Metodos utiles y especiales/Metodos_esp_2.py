class Persona():

    almacendatos=[]

    def __init__(self, *datos):

        for i in datos:

            self.almacendatos.append(i)

        self.getDatos=(self.almacendatos)
          


    def getDatos(self, info):

        for i in info:
            print(i)

p1=("Ariel", "Caca", "Pedo", 1232334, "CULO", "pis")

print(p1)

