from cuenta import Cuenta

class CuentaConDescubierto(Cuenta):
    def __init__(self, titular, numero_cuenta, saldo, descubierto_autorizado):
        super().__init__(titular, numero_cuenta, saldo)
        self.descubierto_autorizado = descubierto_autorizado

    def retirar(self, cantidad):
        if self.saldo - cantidad >= -self.descubierto_autorizado:
            self.saldo -= cantidad
            return True
        else:
            print("No se puede retirar fondos. Saldo insuficiente.")
            return False
