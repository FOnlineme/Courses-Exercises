#Ejemplo 2 RETORNO DE DATOS
#Retorno de datos se devuelven a la llamada de la funcion que recoge los datos

def retorno_superficie(lado):
    sup=lado*lado
    return sup

#Main
va=int(input("Introduce el valor "))
superficie=retorno_superficie(va)
print("La superficie del cuadrado es:",superficie)
