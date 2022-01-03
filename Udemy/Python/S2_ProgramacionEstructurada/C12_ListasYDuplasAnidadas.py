def cargar_paises(cantidad):
    paises=[]    #Lista
    for x in range(cantidad):
        nom=input("Ingrese el nombre del pais: ")
        cant=int(input("Ingrese la cantidad de habitantes del pais: "))
        paises.append((nom,cant))
    return paises

def imprimir(paises,n):
    print("Los paises y poblacion cargados en la lista fueron:")
    for x in range (n):
        print(paises[x][0],paises[x][1])

def mayor_habitantes(paises,n):
    pos=0
    for x in range(n):
        if paises [x][1]>paises[pos][1]:
            pos=x
    print("El pais con mayor cantidad de habitantes es:",paises[pos][0],"\nCon",paises[pos][1],"habitantes")

#main
n=int(input("Ingrese la cantidad de paises a registrar: "))
paises=cargar_paises(n)
imprimir(paises,n)
mayor_habitantes(paises,n)