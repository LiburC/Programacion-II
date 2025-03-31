import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        mag = self.magnitude()
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def projection_on(self, other):
        other_mag_sq = other.magnitude() ** 2
        scalar = self.dot(other) / other_mag_sq
        return scalar * other
    
    def component_in(self, other):
        other_mag = other.magnitude()
        return self.dot(other) / other_mag
    
    def __str__(self):
        return f"({self.x:.0f}, {self.y:.0f}, {self.z:.0f})"

# Pruebas
a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)
print("Suma:", a + b)
print("Multiplicación por escalar:", 2 * a)
print("Magnitud de a:", a.magnitude())
print("Vector normalizado de a:", a.normalize())
print("Producto escalar:", a.dot(b))
print("Producto vectorial:", a.cross(b))
print("Proyección de a sobre b:", a.projection_on(b))
print("Componente de a en b:", a.component_in(b))
