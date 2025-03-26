import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_discriminante(self):
        return self.b ** 2 - 4 * self.a * self.c
    
    def get_raiz1(self):
        if self.get_discriminante() >= 0:
            return (-self.b + math.sqrt(self.get_discriminante())) / (2 * self.a)
        return None
    
    def get_raiz2(self):
        if self.get_discriminante() > 0:
            return (-self.b - math.sqrt(self.get_discriminante())) / (2 * self.a)
        return None

    def respuesta(self):
        discriminante = self.get_discriminante()
        if discriminante > 0:
            print(f"La ecuación tiene dos raíces {self.get_raiz1():.5f} y {self.get_raiz2():.5f}")
        elif discriminante == 0:
            print(f"La ecuación tiene una raíz {self.get_raiz1():.5f}")
        else:
            print("La ecuación no tiene raíces reales")
            
a, b, c = map(float, input("Ingrese a, b, c: ").split())
ecuacion = EcuacionCuadratica(a, b, c)
ecuacion.respuesta()
