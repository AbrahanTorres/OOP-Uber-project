from account import Account

class User(Account):
    def __init__(self, name, document, email, password):
        super().__init__(name, document, email, password) #el super().__init__ llama a los atributos de la clase padre.