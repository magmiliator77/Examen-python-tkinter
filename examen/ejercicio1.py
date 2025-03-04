"""
Ejercicio 1 (4 puntos): Clase CuentaBancaria
1. ¿Qué es una clase? ¿Y un constructor?
2. ¿Que diferencia hay entre un método y una función?
3. Crea una clase llamada CuentaBancaria con los siguientes atributos:
• titular
• saldo
• tipo_cuenta
• moneda
4. Define un constructor que inicialice esos atributos.
5. Instancia un objeto de la clase y muestra sus datos por pantalla.
6. Añade los métodos siguientes a la clase:
• ingresar: incrementa el saldo en la cantidad indicada.
• retirar: decrementa el saldo en la cantidad indicada, si existe saldo suficiente; en
caso contrario, muestra un mensaje de error.
• consultar_saldo: devuelve el saldo actual.
7. Crea dos objetos adicionales de la clase.
8. En cada uno de ellos, realiza una operación de ingreso y otra de retirada; muestra el saldo
final de la cuenta tras dichas operaciones. 

"""

#Clase: Es una estructura que define un conjunto de atributos (datos) y métodos (funciones que operan sobre esos datos).

#Constructor: Es un método especial dentro de una clase que se ejecuta automaticamente al crear un objeto. En Python, se define con __init__.

"""
-- Diferencia entre método y función --

Método: Es una función definida dentro de una clase y opera sobre los datos de un objeto.

Función: Es un bloque de código independiente que puede recibir argumentos y devolver valores.    
    
"""

class CuentaBancaria:
    def __init__(self, titular, saldo, tipo_cuenta, moneda):
        
        """ Constructor que inicializa los atributos de la cuenta bancaria. """
        
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.moneda = moneda

    def ingresar(self, cantidad):
        
        """ Incrementa el saldo en la cantidad indicada. """
        
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se ingresaron {cantidad} {self.moneda}. Nuevo saldo: {self.saldo} {self.moneda}.")
        
        else:
            print("No se puede ingresar una cantidad negativa.")

    def retirar(self, cantidad):
        
        """ Decrementa el saldo si hay fondos suficientes. """
        
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} {self.moneda}. Nuevo saldo: {self.saldo} {self.moneda}.")
            
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def consultar_saldo(self):
        
        """ Devuelve el saldo actual. """
        return self.saldo

    def mostrar_datos(self):
        
        """ Muestra los datos de la cuenta. """
        print(f"Titular: {self.titular}")
        print(f"Tipo de Cuenta: {self.tipo_cuenta}")
        print(f"Saldo: {self.saldo} {self.moneda}")



# Crear un objeto de la clase CuentaBancaria
cuenta1 = CuentaBancaria("Juan Pérez", 1000, "Ahorro", "€")

# Mostrar datos de la cuenta
cuenta1.mostrar_datos()

# Crear dos cuentas adicionales
cuenta2 = CuentaBancaria("María López", 500, "Corriente", "EUR")

cuenta3 = CuentaBancaria("Carlos Gómez", 2000, "Ahorro", "€")

# Realizar operaciones en cuenta2
print("Operaciones en la cuenta de María:")

cuenta2.ingresar(300)

cuenta2.retirar(100)

print(f" Saldo final de María: {cuenta2.consultar_saldo()} EUR")

# Realizar operaciones en cuenta3
print("Operaciones en la cuenta de Carlos:")

cuenta3.ingresar(200)

cuenta3.retirar(2500)  # Intento de retiro mayor al saldo

print(f"Saldo final de Carlos: {cuenta3.consultar_saldo()} €")


# CREADO POR MIGUEL TORRES MARTINEZ 2ºB SMR