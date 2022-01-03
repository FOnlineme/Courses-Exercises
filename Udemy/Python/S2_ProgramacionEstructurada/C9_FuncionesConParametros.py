def mostrar_mensaje(mensaje):
    #funciones con parametros simples
    print("******************************************")
    print(mensaje)
    print("******************************************")

def cargar_suma():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    suma=valor2+valor1
    print("La suma es:",suma)

#Main
mostrar_mensaje("Bienvenido al programa para sumar dos valores, por favor siga las instrucciones")
cargar_suma()

