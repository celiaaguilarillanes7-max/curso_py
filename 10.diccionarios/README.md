# Diccionario
*los diccionarios son la forma mas comun de almacenar datos estructurados de objetos que nos rodea en el mundo, al igual que las listas que guardan informacion en `elementos`, de igual ,manera los diccionarios almacenan sus datos en `elementos` separados por comas.
la diferancia es que las listas almacenan los elementos por `indice` y `valor`.
y los diccionarios almacenan los elementos por `clave:valor`.😒*

**EJEMPLO📑** 
``` python
vocales:list[str]=['a','e','i','o','u']
#  indices          0   1   2   3   4
# un elemento en una lista esta conformado por dos cositas el indice y su valor.
# para acceder aun valor en una lista
vocales[2] # i
alumno:diccionario={'nombre':'maria','edad':40}
# un elementyo en un diccionario esta conformado por clave:valor
# paraacceder a un diccionario
alumno["nombre"] # maria
```
## ACCEDER A ELEMENTOS
- **por clave (forma directa)📝**
  ```python
  persona:dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com",
  }
  print(persona["edad"] # 16
  print(persona["email"]) #celi@email.com
  ```
- **por su metodo (forma mas segura)🧏‍♀️**
  ```  python
   persona:dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com",
  }
  print(persona.get("nombre")) #celia
  # la diferencia de este m3etodo es que no permite  manejar errores
  print(persona.git("telefono")) # none
    print(persona.git("telefono"."no disponible")) # si la clave telefono no exixte no mostrara None si no el segundo parametro que le pasemos al metodo git,
  ```
  ## MODIFICAR ELEMENTO✔️
  **cambiar un valor existente**
  ```python
   persona:dict={
    "nombre":"celia",
    "edad":16,
  }
  persona["edad"]=19
  # agregar una nueva clave:valor
  persona["carrera"]="agro"
  # si la clave no existe se crea automaticamente. si existe se actualiza.
  ```
  ## 📈AGREGAR/ACTUALIZARCMULTIPLES ELEMENTOS
  para esto tenemos que hacer uso de el metodo `.update` 
  se puede agregar si los pares de `clave:valor`no existe y actualizar si el `clave:valor` existe.
  ```  python
  tienda:dict[str:str|int]={
    "razon social":"bigote",
    "ruc":20464952526
  }
  # puedo actualizar usando el metodo .update tengo dos maneras de usar este metodo
  # 1. diccionarios
  tienda.update({"ruc":2469756315,"telefono":964587235})
  # 2. pares clave=valor
  tienda.update(h_atencion="9-12",gerente="kevin")
  ```

  ## 🚮ELIMINAR ELEMENTO❌
  ```python
   tienda:dict[str:str|int]={
    "razon social":"bigote",
    "ruc":20464952526
  }
  el_eliminado=tienda.pop("ruc")
  # para elimonar todo el diccionario
  tienda.clear()
  ```