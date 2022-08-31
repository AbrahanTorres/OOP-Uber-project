from payment import Payment
from datetime import date

class Tarjeta(Payment):
    franquicia = str
    fechaVencimiento = date.today()
    cvv = str

    def __init__(self, id, franquicia, fechaVencimiento, cvv):
        super().__init__(id)
        self.franquicia = franquicia
        self.fechaVencimiento = fechaVencimiento
        self.cvv = cvv

        
