"""
Ejercicio 2 (2 puntos): Otra Clase y Funciones Globales

Define una clase llamada Pelicula con los atributos:
titulo
director
anio_estreno
genero
Crea cinco objetos de la clase y guárdalos en una lista lista_peliculas.
Implementa dos funciones globales (no métodos de la clase):
contar_por_genero: cuenta cuántas películas de la lista pertenecen a un género dado.
pelicula_mas_reciente:: devuelve la película con mayor año de estreno.
Muestra los resultados al ejecutar ambas funciones con la lista.       
    
"""
#Definimos la clase Pelicula con sus atributos

class Pelicula:
    def __init__(self, titulo, director, anio_estreno, genero):
        
        self.titulo = titulo
        
        self.director = director
        
        self.anio_estreno = anio_estreno
        
        self.genero = genero
        

#Creamos cinco objetos de la clase Pelicula y los guardamos en una lista lista_peliculas

lista_peliculas = [
    Pelicula("Titanic", "James Cameron", 1997, "Romance"),
    Pelicula("Inception", "Christopher Nolan", 2010, "Ciencia Ficcion"),
    Pelicula("The toyotaYaris", "Cristobal Colon", 1972, "Crimen"),
    Pelicula("The Dark Knight", "Christopher Nolan", 2008, "Accion"),
    Pelicula("Ficcion pulpinica", "Mr.llantas", 1994, "Crimen")
]

#Imeplementamos las funciones globales (no métodos de la clase)

def contar_por_genero(lista_peliculas, genero):
    contador = 0
    
    for pelicula in lista_peliculas:
        if pelicula.genero == genero:
            contador += 1
            
    return contador

def pelicula_mas_reciente(lista_peliculas):
    
    pelicula_mas_reciente = lista_peliculas[0]
    
    for pelicula in lista_peliculas:
        if pelicula.anio_estreno > pelicula_mas_reciente.anio_estreno:
            pelicula_mas_reciente = pelicula
            
    return pelicula_mas_reciente


#Mostramos los resultados al ejecutar ambas funciones con la lista

print(f"Películas de Romance: {contar_por_genero(lista_peliculas, 'Romance')}")

print(f"Películas de Crimen: {contar_por_genero(lista_peliculas, 'Crimen')}")

print(f"Películas de Ciencia Ficción: {contar_por_genero(lista_peliculas, 'Ciencia Ficcion')}")

print(f"Películas de Acción: {contar_por_genero(lista_peliculas, 'Accion')}")

print(f"Película más reciente: {pelicula_mas_reciente(lista_peliculas).titulo}")

        
# CREADO POR MIGUEL TORRES MARTINEZ 2ºB SMR






