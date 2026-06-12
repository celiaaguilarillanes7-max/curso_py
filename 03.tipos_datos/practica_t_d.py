# crear haciendo uso de las clases anteriores, una calculadora
#que pida al usuario dos numeros enteros y luego 
# de manera ordenada mostrar por terminal el resultado

mensaje_bienvenida:str="""
=====================================
= BIENVENIDOS A MI CALCULADORA =
=====================================
"""
print(mensaje_bienvenida)
print("a continuacion ingrese dos numeros para realizar la suma")
numero_uno:int=int(input("Ingresa el primer numero:"))
numero_dos:int=int(input("Ingrese el segundo numero:"))
resultado_suma:int=numero_uno+numero_dos
mensaje_resultado:str=f"""
el resultado de la suma del numero
{numero_uno}
con el numero
{numero_dos}
es igual a {resultado_suma}
"""
print(mensaje_resultado)