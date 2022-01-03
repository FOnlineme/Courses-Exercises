class Cliente:
    suspendidos=[]

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre
    
    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre",self.nombre)
        self.esta_suspendido()
    
    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("___________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

#Main

cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Julian")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Marcelo")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()