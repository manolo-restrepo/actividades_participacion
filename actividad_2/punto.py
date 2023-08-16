import math
class punto:
    def  __init__(self,coordenada_x, coordenada_y) :
        self.coordenada_x=coordenada_x
        self.coordenada_y=coordenada_y
    def mostrar(self):
        print(f"({self.coordenada_x},{self.coordenada_y})")
    def mover(self,morver_x,mover_y):
        self.coordenada_x=morver_x
        self.coordenada_y=mover_y
    def calcular(self,punto):
        distancia=math.sqrt((punto.coordenada_x-self.coordenada_x)**2+(punto.coordenada_y-self.coordenada_y)**2)
        return distancia
punto1=punto(2,2)
punto2=punto(3,3)
punto.mostrar(punto2)
print(punto.calcular(punto1,punto2))

