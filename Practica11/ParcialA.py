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

    def get_artista_mas_experimentado(self):
        return max(self.artistas, key=lambda a: a.anios_experiencia)

    def agregar_anuncio(self, anuncio):
        self.anuncio = anuncio

    def monto_total_venta(self):
        return self.anuncio.precio if self.anuncio else 0


class Pintura(Obra):
    def __init__(self, titulo, material, genero, artista1, artista2=None, anuncio=None):
        super().__init__(titulo, material, artista1, artista2, anuncio)
        self.genero = genero
a1 = Artista("Carlos Lopez", "123456", 10)
a2 = Artista("Maria Ruiz", "654321", 15)
a3 = Artista("Luis Perez", "111111", 8)
print("Artistas:")
print(a1.mostrar())
print(a2.mostrar())
print(a3.mostrar())

anuncio1 = Anuncio(1, 1500)
print("\nAnuncio:")
print(anuncio1.mostrar())
pintura1 = Pintura("El Sol", "Óleo", "Paisaje", a1, a2, anuncio1)
pintura2 = Pintura("La Luna", "Acrílico", "Retrato", a3)
print("\nPintura 1:")
print(f"Título: {pintura1.titulo}, Material: {pintura1.material}, Género: {pintura1.genero}")
print("Artistas:")
for artista in pintura1.artistas:
    print("-", artista.mostrar())
if pintura1.anuncio:
    print("Anuncio:", pintura1.anuncio.mostrar())

print("\nPintura 2:")
print(f"Título: {pintura2.titulo}, Material: {pintura2.material}, Género: {pintura2.genero}")
print("Artistas:")
for artista in pintura2.artistas:
    print("-", artista.mostrar())
if pintura2.anuncio:
    print("Anuncio:", pintura2.anuncio.mostrar())
else:
    print("Sin anuncio")
print("\nArtista con más experiencia entre ambas pinturas")
experto1 = pintura1.get_artista_mas_experimentado()
experto2 = pintura2.get_artista_mas_experimentado()
if experto1.anios_experiencia > experto2.anios_experiencia:
    mas_experto = experto1
else:
    mas_experto = experto2
print(mas_experto.nombre)
print("\nAgregar anuncio a pintura2 y calcular monto total de venta")
anuncio2 = Anuncio(2, 1200)
pintura2.agregar_anuncio(anuncio2)
print(pintura2.anuncio.mostrar())
total_venta = pintura1.monto_total_venta() + pintura2.monto_total_venta()
print("Monto total de venta de ambas pinturas:", total_venta, "Bs")
