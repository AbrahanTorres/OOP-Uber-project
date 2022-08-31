from car import Car
from account import Account
from UberX import UberX  #desde el archivo UberX importamos la clase UberX. Lo mismo con las otras importaciones.
from user import User

if __name__ == "__main__":
    print("Inicializando la información de los carros")
    print("Car")
    car = Car("AMS234", Account("Abrahan  Torres", "ANDA876", "abrahamtorres2021@gmail.com", "2563"))  #Llamamos la clase car, fijarse la construcción, llama a la licencia
                                                                                                       # y al driver, sin embargo el driver lleva a Account en la clase car.           
    
    print(vars(car))  #Usamos vars para llamar al objeto
    print(vars(car.driver))


    print("UberX")
    uberX = UberX("KLO365", Account("Marco Lois", "SGHJ12336", "marzo@platzi.com", "7856"), "Toyota", "Corolla")  #Se saca de la classe UberX que tiene license, driver, brand y model.
    print(vars(uberX))
    print(vars(uberX.driver))


    print("User")
    user = User("Mariana Valle", "SDFG125F", "marina@platzi.com", 7856)
    print(vars(user))











