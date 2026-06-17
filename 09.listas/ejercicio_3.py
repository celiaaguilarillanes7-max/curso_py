alumnos:list[str]=['deduardo','noemy','victor','emerson','yo']
print(alumno)
# eliminar por valor
alumnos.remove('yo')
print(alumno)
#eliminar el ultimo valor por defecto
alumnos.pop()
print(alumnos)
##pop tambien elemina elementos por indice
### el metodo pop tiene la caracteristica de recuperar el elemento eliminado eso quiere decir que podemos almacenarlo en la variable
alumnos.pop(1)
print(f"mi lista de desaprobados sera: {alumnos}")

## tengo una lista de marcas de vehiculos (toyota,nissan,datsun,daewod,simo mack,mazda,honda), crear un programa que realize lo siguienteeeeee;
'''
1. eliminar el 5 elemento.
2. en su lugar agregar la marca mitsubishi
3. buscar nissan y mostrar su valor por terminal
4. mostrar si exixte honda en mi lista de vehiculos
'''
"""""""""""""""""""""""""""""""""""""""""
MARCAS DE VEHICULOS
"""""""""""""""""""""""""""""""""""""""""
vehiculos = ["toyota", "nissan", "datsun", "daewoo", "simo mack", "mazda", "honda"]

"""""""""""""""""""""""""""""""""""""""""
# 1. Eliminar el 5º elemento 
"""""""""""""""""""""""""""""""""""""""""
vehiculos.pop(4)

"""
# 2. Agregar "MISTSUBISHI" en su lugar
"""
vehiculos.insert(4, "MISTSUBISHI")

"""
# 3. Buscar "nissan" y mostrar su posición
"""
buscar: int = vehiculos.index("NISSAN")
print("NISSAN se encuentra en la posición:", buscar)
""
existe: bool = "HONDA" in vehiculos
print("¿Existe HONDA?:", existe)

# 4. Mostrar si existe 
print(vehiculos)