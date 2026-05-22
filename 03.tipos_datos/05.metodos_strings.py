### los metodos son funciones que estan dentro de metodos 
#metodo para conbertir un texto en mayuscula 
texto_minuscula:str="hola"  
print(texto_minuscula.upper()) 
#metodo para convertir un texto en minusculas
texto_mayuscula:str="HOLASSS"
print(texto_mayuscula.lower())
#metodo para convertir solo la primera letra en mayuscula
texto:str="buenos dias"
print(texto.capitalize())
# metodo para convertir la primera letra de cada palabra en mayuscula como como un titulo
print(texto.title())
#metodo para quitar espacios 
texto_espacios:str="         osos          " 
print(texto_espacios)
#este metodo quita los espacios que estan a la derecha e isquierda . si deseamos quitar solo los espacios de la izquierda usamos el metodo lstrip() y si deseamos quitar los espacios solo de la derecha usamos rstrip()
print(texto_espacios.strip())
#metodo para buscar un caracter o conjunto de caracteres
#find retorna el indise donde comienza el texto a buscar si el texto no se encuentre retornara -1
parrafo:str="mi mama me ama yo amo a mi mama de mi celia"
print(parrafo.find("celia"))
print(parrafo[38:])
# metodo para remplazar una parte del texto
texto_incorrecto:str="gianfranco es malo"
print(texto_incorrecto.replace("malo","bueno"))
# (metodo) operador binario de existencia
# este operador verifica si sierto texto existe o no dentro de otro retorna true si existe y false si no
vocales:str="aeiouAEIOU"
print("a" in vocales)

#tarea aberiguar que son y cuales son los operadores unarios,binarios y ternarios 

##1. Operadores Unarios
## Actúan sobre un solo operando.
#Ejemplos comunes:

#Incremento/Decremento: ++x, --y
#Negación: -a (cambia el signo de a)
#Negación lógica: !b (invierte el valor booleano de b)
#Operador de dirección (en algunos lenguajes): &variable (obtiene la dirección de me
# moria
x = 5
y = -x  # y será -5

###2. Operadores Binarios
## Requiere dos operandos para realizar una operación.
#Categorías principales:

#Aritméticos: +, -, *, /, % (módulo), ** (potencia)
#Relacionales: ==, !=, >, <, >=, <=
#Lógicos: && (AND), || (OR)
#Asignación: =, +=, -=, *=, etc.
#Bit a bit: &, |, ^, <<, >>
a = 10
b = 3
suma = a + b  # suma será 13

###3. Operadores Ternarios
# Es un operador que evalúa tres operandos y se usa como una forma abreviada de una estructura condicional

# Sintaxis: [valor_si_verdadero] if [condición] else [valor_si_falso]
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
# mensaje será "Mayor de edad"

### realizar un programa que nos pida la contraseña si la contraseña es correcta el usuario podra ingresar caso contrario le dara un mensaje de contraseña incorrecta

password_user:str=("ingresa tu contraseña:")
print("bienvenido al sistema" if password_user=="hola1234"
else"contraseña incorrecta")