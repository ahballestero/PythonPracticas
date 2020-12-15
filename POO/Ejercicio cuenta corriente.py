class CuentaCorriente():

    def __init__(self, numero, titular, saldo):

        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def getDatos(self):

        return "El titular de la cuenta nº " + str(self.numero) + " es " + self.titular + " y tiene un saldo de: " + str(self.saldo) + "€"

    def ingresar(self, cantidad):

        self.saldo = self.saldo+cantidad

    def retirar(self, cantidad):

        self.saldo = self.saldo-cantidad


class CuentaJoven(CuentaCorriente):  # CuentaJoven hereda de CuentaCorriente

    def __init__(self, numero, titular, saldo, bonus_promocion=0):

        super().__init__(numero, titular, saldo)

        self.bonus_promocion = bonus_promocion

        self.saldo += bonus_promocion

    def getBonus(self):

        return self.bonus_promocion

    def getDatos(self):

        return super().getDatos() + " Bonus: " + str(self.bonus_promocion) + "€"

    def ingresar(self, cantidad):

        super().ingresar(cantidad)

    def retirar(self, cantidad):

        super().retirar(cantidad)


c1 = CuentaJoven(57485784, "Elvio Lento", 4000, 1500)

#c1=CuentaCorriente("453654", "Juan Perez", 3500)

c1.ingresar(1000)

c1.retirar(2000)

print(c1.getDatos())
