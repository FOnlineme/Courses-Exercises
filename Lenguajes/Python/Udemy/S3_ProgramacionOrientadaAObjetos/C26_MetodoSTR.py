class Familia:

    def __init__(self,padre,madre,hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    def __str__(self):
        cadena=self.padre+","+self.madre
        for i in self.hijos:
            cadena=cadena+","+i
        return cadena

#Main

familia1=Familia("Marcelo","Fabiola",["Julian","Carolina"])
familia2=Familia("Oscar","Nelida",["Norma","Claudia","Marcelo","Beto"])
familia3=Familia("Pepito","Fulanita")

print("La familia 1 es:\n",familia1)
print("La familia 2 es:\n",familia2)
print("La familia 3 es:\n",familia3)