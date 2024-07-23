#EJEMPLO 01 - PARAMETROS TIPO LISTA
def cargar_valores(n):
    lista=[]
    for x in range(n):
        lista.append(int(input("Introduce un valor al final de la lista: ")))
    return lista
def sumarizar(longitud, lista):
    suma=0
    for x in range(longitud):
        suma=suma+lista[x]
    return suma
def mayor(longitud, lista):
    may=lista[0]
    for x in range(longitud):
        if lista[x]>may:
            may=lista[x]
    return may
def men(longitud, lista):
    men=lista[0]
    for x in range(longitud):
        if lista[x]<men:
            men=lista[x]
    return men    
#main 
n=int(input("Ingrese la cantidad de valores a ingresar en la lista: "))
lista=cargar_valores(n)
print("Lista completa: \n",lista)
print("Suma de todos sus elementos:\n",sumarizar(n, lista))
print("Mayor valor de la lista: \n",mayor(n, lista))
print("Menor valor de la lista: \n",men(n, lista))
