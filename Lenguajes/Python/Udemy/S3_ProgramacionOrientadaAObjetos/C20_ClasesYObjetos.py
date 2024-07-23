class Alumno:
    def declarar(self,nombre,dato):
        self.nombre=nombre
        self.puntuacion=dato
    
    def visualizar(self):
        print("Nombre:",self.nombre)
        print("Puntuacion:",self.puntuacion)

    def estadistica(self):
        if self.puntuacion<4:
            print("Libre")
        elif self.puntuacion>=5:
            print("Notable")
        elif self.puntuacion>=8:
            print("Sobresaliente")
        else:
            print("Regular")

#Main

alumno1=Alumno()
alumno1.declarar("Diego",2)
alumno1.visualizar()
alumno1.estadistica()

alumno2=Alumno()
alumno2.declarar("Ana",4.5)
alumno2.visualizar()
alumno2.estadistica()
