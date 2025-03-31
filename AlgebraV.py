import math

class Vectores:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vectores(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vectores(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return Vectores(self.x * scalar, self.y * scalar, self.z * scalar)
    def __rmul__(self, scalar):
        return self * scalar
    
    def __truediv__(self, scalar):
        return Vectores(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        mag = self.magnitude()
        return self / mag if mag != 0 else Vectores(0, 0, 0)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vectores(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def is_perpendicular(self, other):
        return self.dot(other) == 0
    
    def is_parallel(self, other):
        return self.cross(other) == Vectores(0, 0, 0)
    
    def projection_on(self, other):
        return (self.dot(other) / other.magnitude()**2) * other
    
    def component_on(self, other):
        return self.dot(other) / other.magnitude()
    
    def __str__(self):
        return f"Vectores({self.x:.0f}, {self.y:.0f}, {self.z:.0f})"
    
v1 = Vectores(1, 1, 1)
v2 = Vectores(1, 1, 1)
print("Suma:", v1 + v2)
print("Resta:", v1 - v2)
print("Multiplicación por escalar:", v1 * 2)
print("Producto escalar:", v1.dot(v2))
print("Producto cruz:", v1.cross(v2))
print("¿Son perpendiculares?", v1.is_perpendicular(v2))
print("¿Son paralelos?", v1.is_parallel(v2))
print("Proyección de v1 sobre v2:", v1.projection_on(v2))
print("Componente de v1 sobre v2:", v1.component_on(v2))
