"""
PROBLEMA
Confeccionar un programa que permita cargar un codigo de producto como clave en un diccionario. Guardar
para dicha clave el nombre del producto, su precio y cantidad en stock

Implementar las siguientes funciones
1) Carga de datos
2) Listado completo de productos
3) Consulta de un producto por su clave, mostrar el nombre, precio y stock
4) Mostrar un listado de todos los productos que tengan un stock en 0
"""

def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codigo del producto: "))
        nombre=input("Ingrese el nombre del producto: ")
        precio=float(input("Ingrese el precio del producto: "))
        stock=int(input("Ingrese el stock del producto: "))
        productos[codigo]=(nombre,precio,stock)
        continua=input("Desea cargar otro producto? [s/n]")
    return productos

def listado(productos):
    print("El listado completo de productos es:")
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

def consulta(productos):
    busqueda=int(input("Ingrese el codigo del producto a buscar: "))
    if busqueda in productos:
        print("El producto se encuentra en nuestra lista")
        print("\nSu nombre es:",productos[busqueda][0],"\nSu precio es:",productos[busqueda][1],"\nY su stock es:",productos[busqueda][2])


def sin_stock(productos):
    print("Los articulos sin stock son:")
    for x in productos:
        if productos[x][2]==0:
            print(x,productos[x][0],productos[x][1])

#main
productos=cargar()
listado(productos)
consulta(productos)
sin_stock(productos)

