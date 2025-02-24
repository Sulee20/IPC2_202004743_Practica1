import random

class Cuenta:
    def __init__(self, nombre, nc, saldo):  
        self.nombre = nombre  
        self.nc = nc  
        self.saldo = saldo  

    def depositar(self):
        deposito = float(input("Ingrese el monto a depositar: "))
        self.saldo += deposito  
        return f"Depósito exitoso \nSu nuevo saldo es de {self.saldo:.2f}"
    
    def retirar(self):
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > self.saldo:
            return "Saldo insuficiente"
        self.saldo -= retiro
        return f"Retiro exitoso \nSu nuevo saldo es de {self.saldo:.2f}"
    
    def informacion(self):
        return f"Titular: {self.nombre} \nNumero de Cuenta: {self.nc} \nSaldo: {self.saldo:.2f}"

class Monetaria(Cuenta):
    def __init__(self, nombre, nc, saldo, limite_credito):
        super().__init__(nombre, nc, saldo)  
        self.limite_credito = limite_credito
    def informacion(self):
        info = super().informacion()
        return f"Informacion de la Cuenta Monetaria \n{info}\nLimite de credito: {self.limite_credito:.2f}"
    
class Ahorro(Cuenta):
    def __init__(self, nombre, nc, saldo, tasa_interes):
        super().__init__(nombre, nc, saldo)  
        self.tasa_interes = tasa_interes
    def informacion(self):
        info = super().informacion()
        return f"Informacion de la Cuenta Ahorro \n{info}\nTasa de interes: {self.tasa_interes:.2f}"
    def interes(self):
        interes = (self.tasa_interes * self.saldo) / 100
        self.saldo += interes
        return f"El interes de: {interes:.2f} Se ha añadido exitosamente a tu cuenta \nNuevo saldo {self.saldo:.2f}"

class SistemaBancario:
    def __init__(self):
        self.cuentas = {}

    def generar_nc(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    def crear_cuenta(self, tipo):
        nombre = input("Ingrese el nombre del titular: ")
        saldo = float(input("Ingrese el saldo inicial: "))
        nc = self.generar_nc()
        if tipo.lower() == "ahorro":
            tasa_interes = float(input("Ingrese la tasa de interés (en %): "))
            cuenta = Ahorro(nombre, nc, saldo, tasa_interes)
        elif tipo.lower() == "monetaria":
            limite_credito = float(input("Ingrese el límite de crédito: "))
            cuenta = Monetaria(nombre, nc, saldo, limite_credito)
        else:
            print("Tipo de cuenta no válido")
            return
        self.cuentas[nc] = cuenta
        print(f"Cuenta {tipo} creada con éxito!\nNúmero de cuenta: {nc}")

    def gestionar_cuenta(self):
        nc = input("Ingrese el número de cuenta: ")
        if nc not in self.cuentas:
            print("Cuenta no encontrada")
            return

        cuenta = self.cuentas[nc]
        while True:
            print("\n---------------GESTIÓN DE CUENTA---------------")
            print("1. Ver información")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Calcular interés (solo Ahorro)")
            print("5. Regresar al menú principal")
            print("-----------------------------------------------")

            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                print(cuenta.informacion())
            elif opcion == "2":
                print(cuenta.depositar())
            elif opcion == "3":
                print(cuenta.retirar())
            elif opcion == "4":
                if isinstance(cuenta, Ahorro):
                    print(cuenta.interes())
                else:
                    print("Esta operación solo está disponible para cuentas de ahorro")
            elif opcion == "5":
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida")

            

def menu_principal():
    sistema = SistemaBancario()
    while True:
        print("\n---------------MENU BANCARIO---------------")
        print("1. Crear cuenta")
        print("2. Gestionar cuenta")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            tipo = input("Tipo de cuenta (Ahorro/Monetaria): ")
            sistema.crear_cuenta(tipo)
        elif opcion == "2":
            sistema.gestionar_cuenta()
        elif opcion == "3":
            print("Hasta luego :D")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu_principal()