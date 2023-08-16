
class CuentaBancaria:
    def __init__(self, numero_cuenta,propietarios,balance) :
        self.numero_cuenta=numero_cuenta
        self.propietarios=propietarios
        self.balance=balance
    def depositar(self,deposito):
        self.balnce=+ deposito
        return self.balance
    def retirar(self,retiro):
        if retiro<self.balance:
            self.balance=self.balance-retiro
    def Cuota_manejo(self): 
        self.balance=self.balance-(self.balnce)*0.02
    def mostrar(self):
        print(f"({self.numero_cuenta},{self.propietarios},{self.balance})")
