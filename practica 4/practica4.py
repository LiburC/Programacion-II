import math
def area(*args):
    if len(args) == 1:  # Círculo
        radio = args[0]
        return math.pi * radio ** 2
    
    elif len(args) == 2:
        base, altura = args
        if base != altura:
            return (base * altura) / 2  # Triángulo rectángulo
        else:
            return base * altura  # Rectángulo

    elif len(args) == 3:  # Trapecio
        base_may, base_men, altura = args
        return ((base_may + base_men) * altura) / 2

    elif len(args) == 2:  # pentagono
        lado, apotema = args
        return (5 * lado * apotema) / 2
# Ejemplo de uso
print("circulo:", area(3))
print("rectangulo:", area(3, 6))  
print("triangulo rectangulo:", area(1, 6))  
print("trapecio:", area(3, 4, 2))
print("pentagono:", area(2, 4))
