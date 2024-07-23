print("datos de la primera persona")

#Para cargar por teclado una cadena de caracteres utilizaremos la funcion input
#Las variables pueden tener muchas funciones aqui tenemos la utilizacion para almacenar el valor introducido por teclado

nombre1=input("ingrese nombre del producto: ")
precio1=int(input("ingrese precio: "))
nombre2=input("ingrese nombre del producto: ")
precio2=int(input('ingrese un precio: '))

#Esta es una constante
BONIFICACION = 20

#Suma los dos precios y su resultado lo guardamos en una variable
precio_compra_total = precio1 + precio2
#Compramos si el precio1 es mayor o igual a precio2
comprar = precio1>=precio2 #Operador de comparacion
logico = (precio1<precio2 and precio1 == precio2) #operador logico

cabecera = "resultados del producto {0} y del producto:"
print(cabecera.format(nombre1,nombre2))
print("El precio del primer valor es mayor o igual al precio del segundo valor:")
print(comprar)
#Concatenar se puede hacer de esta manera con el signo+ y en la variable str
print("la suma de dos productos es:" + str(precio_compra_total))
print("precio1<precio2 and precio == precio2")
print(logico)
#VEMOS EL OPERADOR DE ASIGNACION AQUI ABAJO
precio_compra_total+= BONIFICACION #Operador de asignacion
print ("al precio total le incrementamos su valor que tiene la constante: " + str(precio_compra_total))
