from payment import Payment

class Efectivo(Payment):


    def __init__(self, id):
        super().__init__(id)