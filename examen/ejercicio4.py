"""
Ejercicio 4 (2 puntos): Calculadora de Interés Mensual en
Tkinter
1. Crea una aplicación de Tkinter para calcular el interés mensual a partir de un saldo y un tipo
de interés anual.
2. Añade dos Entry: uno para el saldo inicial y otro para el tipo de interés anual (porcentaje).
3. Incluye un Button que, al pulsarlo, realice el cálculo aproximado mediante la fórmula:
Interes_mensual = (
saldo *interes_anual / 100)
12 )
4. Muestra el resultado en un Label y asegúrate de que la interfaz permanezca operativa sin
bloquearse.
 
"""

# Importamos la libreria tkinter
from tkinter import *

# Creamos la clase CalculadoraInteres
import tkinter as tk
from tkinter import messagebox


# Clase CalculadoraInteres que hereda de tk.Frame para crear la interfaz gráfica
import tkinter as tk
from tkinter import messagebox

class CalculadoraInteres:
    def __init__(self, root):
        """ Inicializa la ventana principal y los elementos de la interfaz gráfica """
        self.root = root
        
        # Título de la ventana
        self.root.title("Calculadora de Interés Mensual")  
        
        # Tamaño de la ventana
        self.root.geometry("350x250")  

        # Etiqueta y entrada para el saldo inicial
        self.label_saldo = tk.Label(root, text="Saldo inicial:")  # Texto indicativo
        
        # Empaquetar con margen
        self.label_saldo.pack(pady=5)  

        # Entrada de texto para saldo inicial
        self.entry_saldo = tk.Entry(root)
          
        self.entry_saldo.pack(pady=5)

        # Etiqueta y entrada para el interés anual
        self.label_interes = tk.Label(root, text="Interés Anual (%)")  # Texto indicativo
        
        self.label_interes.pack(pady=5)


        # Entrada de texto para el interés anual
        self.entry_interes = tk.Entry(root)  
        
        self.entry_interes.pack(pady=5)

        # Botón para calcular el interés mensual
        self.boton_calcular = tk.Button(root, text="Calcular Interés Mensual", command=self.calcular_interes)
        
        # Empaquetar con margen
        self.boton_calcular.pack(pady=10)  

        # Etiqueta para mostrar el resultado del cálculo
        self.label_resultado = tk.Label(root, text="Interés Mensual: 0.00€", font=("Arial", 12, "bold"))
        
        # Empaquetar con margen adicional para separar del botón anterior y centrar en la ventana
        self.label_resultado.pack(pady=10)



    # Calcula el interés mensual basado en el saldo y el interés anual ingresados.
    def calcular_interes(self):
        
        # Intenta realizar el cálculo del interés mensual y mostrar el resultado,  por si acaso try sirve para  capturar errores en tiempo de ejecución y evitar que el programa se bloquee. No me acuerdo si lo hemos dado en clase o no por eso lo pongo.
        try:
            
            # Obtiene los valores ingresados por el usuario y los convierte en números
            saldo = float(self.entry_saldo.get())
            
            interes_anual = float(self.entry_interes.get())


            # Validación: no permite valores negativos
            if saldo < 0 or interes_anual < 0:
                
                # Tampoco me acuerdo si esto lo hemos dado o no pero el messagebox.showwarning sirve para mostrar un mensaje de advertencia en una ventana emergente.
                
                messagebox.showwarning("Error", "Ingrese valores positivos.")  
                # Muestra una alerta si los valores son negativos
                return

            # Cálculo del interés mensual con la fórmula:
            # Interes_mensual = (saldo * interes_anual) / (100 * 12)
            interes_mensual = (saldo * interes_anual) / (100 * 12)

            # Muestra el resultado en la etiqueta
            
            # El .2f es para que solo muestre dos decimales.
            self.label_resultado['text'] = f"Interés Mensual: {interes_mensual:.2f}€"

        except ValueError:
            # Captura el error si el usuario no ingresa valores numéricos
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
            

# Ejecutamos el bucle principal de la aplicacion para que se mantenga abierta
if __name__ == "__main__":
    
    root = tk.Tk()  # Crear la ventana principal
    
    app = CalculadoraInteres(root)  # Instanciar la clase CalculadoraInteres con la ventana principal como argumento.
    
    root.mainloop()  # Ejecutar la aplicación
    
    
# CREADO POR MIGUEL TORRES MARTINEZ 2ºB SMR

