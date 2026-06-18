# librerias estandr de python 
- cuales son? 
Integrados : Ya vienen con Python ( math, os, sys, datetime, json).

De terceros : Se descargan con pip( requests, numpy, pandas, flask, django).

Propios : Archivos .pyque creas tú.

- ¿Cuáles son los más usados? 
**uso principal**
`os` Manejo de archivos, carpetas y sistema operativo.
print("Directorio actual:", os.getcwd())

`sys` Interacción con el intérprete de Python.
import sys
print("Versión de Python:", sys.version)

`math` Operaciones matemáticas avanzadas.  
print("Raíz cuadrada de 25:", math.sqrt(25))

`random` Generación de números aleatorios.    
print("Número aleatorio:", random.randint(1, 10))

 `datetime` Manejo de fechas y horas.       
 print("Fecha y hora actual:", datetime.now())

`time` Medición y control del tiempo.    
import time
print("Tiempo actual en segundos:", time.time())   

`json` Lectura y escritura de datos JSON.     
datos = {
    "nombre": "Ana",
    "edad": 20
}
print("Datos en JSON:", json.dumps(datos))

`csv` Lectura y escritura de archivos CSV. 
import csv
with open("datos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad"])
    escritor.writerow(["Juan", 20])

`re` Expresiones regulares para búsqueda de texto.
import re
texto = "Python 2026"
resultado = re.findall(r"\d+", texto)
print("Números encontrados:", resultado)

`collections`Estructuras de datos especializadas.  
from collections import Counter
letras = Counter("programacion")
print(letras)

`itertools` Herramientas para iteradores y ciclos.  
from itertools import permutations
print(list(permutations([1, 2, 3], 2)))

`statistics` Cálculos estadísticos básicos.
import statistics
numeros = [10, 20, 30, 40, 50]
print("Promedio:", statistics.mean(numeros))

`pathlib` Manejo moderno de rutas y archivos.    
from pathlib import Path
ruta = Path("archivo.txt")
print("Nombre del archivo:", ruta.name)

`sqlite3` Bases de datos SQLite.
import sqlite3
conexion = sqlite3.connect("ejemplo.db")
print("Base de datos conectada")
conexion.close()

`tkinter` Creación de interfaces gráficas.                
import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("300x200")
ventana.mainloop()

- ¿Y las formas de incluirlas en nuestros archivos de Python? 
  

# módulos en Python