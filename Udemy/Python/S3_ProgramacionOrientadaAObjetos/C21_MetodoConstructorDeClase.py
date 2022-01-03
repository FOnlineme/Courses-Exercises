class Usuario:
    def __init__(self):
        self.usuario=""
        self.ingresos=0

    def intro(self):
        self.usuario=input("Ingrese el nombre del usuario: ")
        self.ingresos=float(input("Cantidad de ingresos anual: "))

    def visualizar(self):
        print("Nombre:",self.usuario)
        print("Ingresos:",self.ingresos)

    def fiscalidad(self):
        if self.ingresos>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

#main

seleccion="s"
usuarios=[]
i=0
while seleccion=="s":
    usuario=Usuario()
    usuario.intro()
    usuario.visualizar()
    usuario.fiscalidad()
#    usuarios[i]=usuario
#    i=i+1
    seleccion=input("Desea agregar otro usuario? [s/n] ")

seleccion=input("Desea consultar la informacion de un usuario? [s/n] ")
if seleccion=="s":
    usuario.visualizar()
else:
    print("Fin del programa")
