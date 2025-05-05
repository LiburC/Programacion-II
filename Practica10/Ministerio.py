class Ministerio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = 0
        self.empleados = []
        self.edades = []
        self.sueldos = []

    def agregar_empleado(self, nombre, paterno, materno, edad, sueldo):
        self.empleados.append([nombre, paterno, materno])
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nroEmpleados += 1

    def mostrar_empleados(self, titulo="Empleados actuales:"):
        print("\n" + titulo)
        for i in range(self.nroEmpleados):
            print(f"{self.empleados[i]} ~ Edad: {self.edades[i]} ~ Sueldo: {self.sueldos[i]}")

    def eliminar_empleado_por_edad(self, edad_objetivo):
        print(f"\nEliminando empleados con edad {edad_objetivo}")
        i = 0
        while i < len(self.edades):
            if self.edades[i] == edad_objetivo:
                print("Empleado eliminado:", self.empleados[i])
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nroEmpleados -= 1
            else:
                i += 1
        self.mostrar_empleados("Después de eliminar:")
    def __add__(self, otro):
        print("\n Transfiriendo empleados del segundo al primero con edad <30 o sueldo <2800...")
        for i in range(otro.nroEmpleados):
            if otro.edades[i] < 30 or otro.sueldos[i] < 2800:
                emp = otro.empleados[i]
                edad = otro.edades[i]
                sueldo = otro.sueldos[i]
                self.agregar_empleado(emp[0], emp[1], emp[2], edad, sueldo)
                print("Transferido:", emp, edad, sueldo)
        return self
    def empleados_minimos(self, criterio="edad"):
        if criterio == "edad":
            print("\n Empleado(s) con menor edad:")
            min_edad = min(self.edades)
            for i, edad in enumerate(self.edades):
                if edad == min_edad:
                    print(self.empleados[i], "Edad:", edad)
        elif criterio == "sueldo":
            print("\nEmpleado(s) con menor sueldo:")
            min_sueldo = min(self.sueldos)
            for i, sueldo in enumerate(self.sueldos):
                if sueldo == min_sueldo:
                    print(self.empleados[i], "Sueldo:", sueldo)

print(" Ministerio")
m1 = Ministerio("Ministerio de Educación", "Av. Arce #123")
m2 = Ministerio(nombre="Ministerio de Salud", direccion="Calle 16 #456")
m2.agregar_empleado("Pedro", "Rojas", "Luna", 35, 2500)
m2.agregar_empleado("Lucy", "Sosa", "Rios", 43, 3250)
m2.agregar_empleado("Ana", "Perez", "Rojas", 26, 2700)
m2.agregar_empleado("Saul", "Arce", "Calle", 29, 2500)
m2.mostrar_empleados("Empleados en Ministerio 2")
m2.eliminar_empleado_por_edad(26)
m1 + m2
m1.empleados_minimos("edad")
m1.empleados_minimos("sueldo")
