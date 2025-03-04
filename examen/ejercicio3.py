"""

Ejercicio 3 (2 puntos): Temporizador Digital en Tkinter
1. Desarrolla una aplicación de Tkinter que permita introducir un número de segundos en un
Entry.
2. Añade un Button para iniciar una cuenta atrás y un Label que muestre el tiempo restante.
3. La cuenta atrás debe disminuir segundo a segundo hasta llegar a cero, actualizando el
Label en pantalla sin bloquear la ventana.
4. Cuando el tiempo llegue a cero, muestra un mensaje indicando que el tiempo ha finalizado.     
    
"""


import tkinter as tk
from tkinter import messagebox


class Temporizador:
    
    # Constructor de la clase Temporizador
    def __init__(self, root):
        self.root = root
        self.root.title("Temporizador Digital")
        self.root.geometry("300x200")

        # Atributos de la clase
        self.tiempo_restante = 0
        self.corriendo = False

        # Entrada para los segundos
        # Aqui root es el padre de la etiqueta y la entrada de texto 
        
        self.label = tk.Label(root, text="Ingrese segundos:")
        
        # Empaquetar la etiqueta en la ventana
        self.label.pack(pady=5)

        # Ya he explicado que hace root anteriormente
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)


        # Botón para iniciar la cuenta regresiva
        self.boton_inicio = tk.Button(root, text="Iniciar", command=self.iniciar)
        self.boton_inicio.pack(pady=5)


        # Etiqueta para mostrar el tiempo restante
        self.label_tiempo = tk.Label(root, text="00", font=("Arial", 24))
        self.label_tiempo.pack(pady=10)


    # Función para actualizar el tiempo en la pantalla y seguir la cuenta regresiva
    def actualizar_tiempo(self):
  
        if self.tiempo_restante > 0:
            
            # AQUI EL TEXT=F ES PARA QUE SE ACTUALICE EL TIEMPO RESTANTE EN LA PANTALLA
            self.label_tiempo.config(text=f"{self.tiempo_restante}")
            
            self.tiempo_restante -= 1
            
            self.root.after(1000, self.actualizar_tiempo)  # Llama a la función después de 1 segundo
        else:
            self.label_tiempo.config(text="00")
            messagebox.showinfo("¡Tiempo Finalizado!", " El tiempo ha llegado a cero.")


    # Inicia la cuenta regresiva con los segundos ingresados. 
    def iniciar(self):
    
    # Si no se está ejecutando la cuenta regresiva, se inicia con los segundos ingresados en la entrada de texto.
    
        if not self.corriendo:
            
            try:
                self.tiempo_restante = int(self.entry.get())
                
                if self.tiempo_restante > 0:
                    self.corriendo = True
                    self.actualizar_tiempo()
                    
                else:
                    messagebox.showwarning("Error", "Ingrese un número mayor a cero.")
            
            # Manejo de excepciones para el caso de que se ingrese un valor no numérico.
            except ValueError:
                messagebox.showwarning("Error", "Ingrese un número válido.")


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Temporizador(root)
    root.mainloop()



# CREADO POR MIGUEL TORRES MARTINEZ 2ºB SMR
