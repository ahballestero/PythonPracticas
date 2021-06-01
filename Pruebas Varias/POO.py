class CuentaCorriente:

    def __init__(self, numero, titular, saldo):
        self.numero=numero
        self.titular=titular
        self.saldo=saldo

    def GetDatos(self):

        return "El titular de la cuenta nº " + str(self.numero) + " es " + self.titular + " y tiene un saldo de: " + str(self.saldo) + "€"


    def ingresar(self, cantidad):

        self.saldo=self.saldo+cantidad

    def retirar(self, cantidad):

        self.saldo=self.saldo - cantidad

class CuentaJoven(CuentaCorriente):

    def __init__(self, numero, titular, saldo, bonus):
        super().__init__(numero, titular, saldo)
        self.bonus=bonus
        self.saldo=saldo+bonus

    def GetBonus(self):

        return "El importe del bonus es de: " + self.bonus

    def ingresar(self, cantidad):
        return super().ingresar(cantidad)
    
    def retirar(self, cantidad):
        return super().retirar(cantidad)
    
    def GetDatos(self):
        return super().GetDatos() + " El bonus es de: " + str(self.bonus) + "€"



    
c1 = CuentaJoven (123456, "Juan Fernandez", 2300, 500)
c1.retirar(800)
c1.ingresar(8000)

print(c1.GetDatos())






        






