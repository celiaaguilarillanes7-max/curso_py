# modulos y librerias estandar

# libreria estandar typing tipar datos a list y diccionarios para hacer optimo el codigo
# modulo es una porcion de codigo utilizable,  para poder usarlo necesitamos inporta la parte del codigo que deceamos utilizar.

# en este codigo estoy inportando desde 1 libreria typing la funcion union,
# union me permite tipar una coleccion de tipos, que si no saves el tipo de dato con posibles tipos de datos que puede tener mi valor  
from typing import Union
# sin libreria
# alumno:dict[str:str|int]
alumno:dict[str:Union[str,int,float,bool]]={
    "id_alumno":1,
    "dni":12654893,
    "nombre":"mio",
    "edad":20,
    "matricula":True
}
# acceder
## clasica 
print(alumno["dni"])
# codigo erronio print(alumno["tricula"])
# metodos 
print(alumno.get("edad","valor no encontrado"))
# crear/modificar un valor
print(alumno)
alumno["nombre"]="otro" # si existe la clave actualiza el valor
alumno["ruc"]=102547863254 # si no existe la clave lo cre
print(alumno)
# crear /modificar varios
alumno.update({"nombre":"celia","edad":15})
alumno.update({"carrera":"agro","semestre":III})
print(alumno)
# eliminar
eliminado=alumno.pop("carrera")
print(f"el elemento eliminado es:{eliminado}")
print(f"mi nuevo diccionario{alumno}")