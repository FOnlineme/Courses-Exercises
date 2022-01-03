class Operadores:
    def __init__(self,lista):
        self.lista=lista

    def visualizar(self):
        print("La lista es:")
        print(self.lista)
        print("________________________")

    def __add__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]+entero)
        return nueva
    
    def __sub__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]-entero)
        return nueva

    def __mul__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]*entero)
        return nueva

    def __floordiv__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]/entero)
        return nueva

#Main
datos=Operadores([1,2,3,4])
datos.visualizar()
print(datos+2)
print(datos-2)
print(datos*2)
print(datos//2)