def cargar_fecha():
    dd=int(input("Ingrese numero de dia: "))
    mm=int(input("Ingrese numero de mes: "))
    aa=int(input("Ingrese numero de ano: "))
    tupla=(dd,mm,aa)
    return tupla

def imprimir_fecha(fecha):
    print("La fecha es: " + str(fecha[0]),fecha[1],fecha[2],sep="/")

#main 
fecha=cargar_fecha()
imprimir_fecha(fecha)