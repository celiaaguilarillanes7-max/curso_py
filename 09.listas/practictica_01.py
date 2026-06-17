## una ferreteria tiene separada en dos listas los siguientes peoductos
""" 
1. lista de productos de limpieza (10 productos)
2. lista de materiales de construccion (10 productos)
-------------------------------------------------
el dueño desea realizar las siguientes acciones:
1. en su lista de limpieza exixte un material de construccion, deves eliminarlos y pasar el producto a la lista que corresponde.
2. indicar si e3n la lista de M.C existe cemento.
3. en la lista de P.L buscar el producto lejia y cambiar su valor por lejia sapolio.
4. mostrar un mensaje donde se detalle cual es la lista de M.C y la lista de P.L formateado.
"""
""""""
#crear mi lista de productos de limpieza
productos_limpieza:list[str]=["lejía", "detergente", "cloro", "cemento", "jabón", "desinfectante", "limpiador", "esponja", "trapo", "ambientador"]
# crear mi lista de  material de trabalo 
materiales_construcción:list[str]=["ladrillo", "arena", "cal", "pintura", "clavo", "martillo", "tubo", "varilla", "yeso", "teja"]
""""""
#1. cambiar de lista al cemento
elemento_retirado=productos_limpieza.pop(productos_limpieza.index("cemento"))
materiales_construcción.append(elemento_retirado)
#2. indicar si existe cemento m.c
existe:bool="varilla"in materiales_construcción
print (f"exixte varilla?:{existe}")
## segunda opcion utilizando un operador ternario
print("varilla si existe"if existe else "varilla no existe")
#3.cambiar lejia por lejia sapolio
buscar=productos_limpieza.index("lejia")
productos_limpieza[buscar]= "lejia sapolio"
#4.muestra un mensaje donde se detalla lista de M.C
mensaje:str=f"""
mi lista de producros de limpieza despues de las
modificaciones queda de la siguiente manera 
{productos_limpieza}
-------------------------------------------------
mi lista de materiales de construccion despues de
las modificaciones queda de la siguiente manera
{materiales_construcción}
"""