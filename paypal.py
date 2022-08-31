from payment import Payment

class Paypal(Payment):
    referencia = str
    modo = str

    def __init__(self, id, referencia, modo):
        super().__init__(id)
        self.referencia = referencia
        self.modo = modo


