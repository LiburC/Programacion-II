class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

    def mostrar(self):
        return f"Anuncio Nro: {self.numero}, Precio: {self.precio} Bs"


class Artista:
    def __init__(self, nombre, ci, anios_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.anios_experiencia = anios_experiencia

    def mostrar(self):
        return f"{self.nombre} ({self.ci}) - {self.anios_experiencia} años experiencia"


class Obra:
    def __init__(self, titulo, material, artista1, artista2=None, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artistas = [artista1] + ([artista2] if artista2 else [])
        self.anuncio = anuncio

    def promedio_experiencia(self):
        total = sum(a.anios_experiencia for a in self.artistas)
        return total / len(self.artistas)

    def agregar_anuncio(self, anuncio):
        self.anuncio = anuncio

    def monto_total_venta(self):
        return self.anuncio.precio if self.anuncio else 0

    def incrementar_precio(self, incremento):
        if self.anuncio:
            self.anuncio.precio += incremento


class Pintura(Obra):
    def __init__(self, titulo, material, genero, artista1, artista2=None, anuncio=None):
        super().__init__(titulo, material, artista1, artista2, anuncio)
        self.genero = genero
a1 = Artista("Juan Rojas", "100001", 12)
a2 = Artista("Ana Vargas", "100002", 8)
a3 = Artista("Mario López", "100003", 20)
anuncio1 = Anuncio(10, 1800)
anuncio2 = Anuncio(11, 2300)
p1 = Pintura("Atardecer", "Óleo", "Paisaje", a1, a2, anuncio1)
p2 = Pintura("Montaña", "Acrílico", "Naturaleza", a3, anuncio=anuncio2)
print("Pintura 1:")
print(f"Título: {p1.titulo}, Material: {p1.material}, Género: {p1.genero}")
print("Artistas:")
for artista in p1.artistas:
    print("-", artista.mostrar())
print("Anuncio:", p1.anuncio.mostrar())

print("\nPintura 2:")
print(f"Título: {p2.titulo}, Material: {p2.material}, Género: {p2.genero}")
print("Artistas:")
for artista in p2.artistas:
    print("-", artista.mostrar())
print("Anuncio:", p2.anuncio.mostrar())
prom1 = p1.promedio_experiencia()
prom2 = p2.promedio_experiencia()
promedio_general = (prom1 + prom2) / 2

print(f"Promedio de experiencia de Pintura 1 ('{p1.titulo}'): {prom1:.2f} años")
print(f"Promedio de experiencia de Pintura 2 ('{p2.titulo}'): {prom2:.2f} años")
print(f"Promedio general: {promedio_general:.2f} años")
def incrementar_precio_por_nombre(pinturas, nombre_busqueda, incremento):
    encontrado = False
    for pintura in pinturas:
        for artista in pintura.artistas:
            if artista.nombre == nombre_busqueda:
                pintura.incrementar_precio(incremento)
                print(f"Se incrementó el precio de '{pintura.titulo}' en {incremento} Bs (nuevo precio: {pintura.anuncio.precio} Bs)")
                encontrado = True
                break
        if encontrado:
            break
    if not encontrado:
        print(f"No se encontró al artista con nombre '{nombre_busqueda}'.")
incrementar_precio_por_nombre([p1, p2], "Mario López", 200)
