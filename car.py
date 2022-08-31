from account import Account
class Car:
    id = int
    license = str
    driver = Account(str,str,str,str,) #De la clase Account sacamos sus atributos, son 4, name, document, email, password.
    passengers = int

    def __init__(self, license, driver):  #De la clase Car solo llamamos a license y driver.
        self.license = license
        self.driver = driver 