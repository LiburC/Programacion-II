import math
class Estadisticas:
    def __init__(self, datos):
        self.datos = datos
    def get_promedio(self):
        return sum(self.datos) / len(self.datos)
    def get_desviacion(self):
        promedio = self.get_promedio()
        return math.sqrt(sum((x - promedio) ** 2 for x in self.datos) / (len(self.datos) - 1))
    
    def resultados(self):
        print(f"El promedio es {self.get_promedio():.2f}")
        print(f"La desviación estándar es {self.get_desviacion():.5f}")
datos = list(map(float, input("10 datos:\n").split()))
if len(datos) == 10:
    estadisticas = Estadisticas(datos)
    estadisticas.resultados()
else:
    print("Debe ingresar exactamente 10 números.")
