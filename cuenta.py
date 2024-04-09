class Cuenta:
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        return f"Cuenta de {self.titular} - Número: {self.numero_cuenta} - Saldo: {self.saldo}"

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
            return True
        else:
            print("No se puede retirar fondos. Saldo insuficiente.")
            return False
