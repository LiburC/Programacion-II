class LineaTeleferico:
    def __init__(self, color, tramo, nroCabinas):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = 0
        self.empleados = []
        self.edades = []
        self.sueldos = []
    def agregar_empleado(self, nombre, paterno, materno, edad, sueldo):
        self.empleados.append([nombre, paterno, materno])
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nroEmpleados += 1
    def mostrar_empleados(self, titulo="Empleados:"):
        print("\n" + titulo)
        for i in range(self.nroEmpleados):
            print(f"{self.empleados[i]} ~ Edad: {self.edades[i]} ~ Sueldo: {self.sueldos[i]}")
    def eliminar_empleado_por_apellido(self, apellido):
        print(f"\n Eliminando empleados con apellido '{apellido}'")

        i = 0
        while i < len(self.empleados):
            if apellido == self.empleados[i][1] or apellido == self.empleados[i][2]:
                print("Empleado eliminado:", self.empleados[i])
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nroEmpleados -= 1
            else:
                i += 1

        print("Después de eliminar:")
        self.mostrar_empleados()
    def __add__(self, otro):
        print("\n[c] Transfiriendo empleados")
        nuevos_mayores_edad = []
        nuevos_mayores_sueldo = []
        for i in range(self.nroEmpleados):
            if self.edades[i] >= 18:
                nuevos_mayores_edad.append((self.empleados[i], self.edades[i], self.sueldos[i]))
            if self.sueldos[i] >= 3000:
                nuevos_mayores_sueldo.append((self.empleados[i], self.edades[i], self.sueldos[i]))

        for emp, edad, sueldo in nuevos_mayores_edad + nuevos_mayores_sueldo:
            if emp not in otro.empleados:
                otro.agregar_empleado(emp[0], emp[1], emp[2], edad, sueldo)
                print("Transferido:", emp, edad, sueldo)

        return otro
    def empleados_mayor_edad(self, modo=1):
        if not self.edades:
            return
        if modo == 1:
            print("\n[d1] Empleado(s) con mayor edad")
            max_edad = max(self.edades)
            for i, edad in enumerate(self.edades):
                if edad == max_edad:
                    print(self.empleados[i], "Edad:", edad)
        elif modo == 2:
            print("\n[d1] Empleado(s) con mayor edad con sobrecarga")
            emp_edad = list(zip(self.empleados, self.edades))
            max_edad = max(self.edades)
            for emp, edad in emp_edad:
                if edad == max_edad:
                    print(emp, "Edad:", edad)
    def empleados_mayor_sueldo(self, modo=1):
        if not self.sueldos:
            return
        if modo == 1:
            print("\n[d2] Empleado(s) con mayor sueldo:")
            max_sueldo = max(self.sueldos)
            for i, sueldo in enumerate(self.sueldos):
                if sueldo == max_sueldo:
                    print(self.empleados[i], "Sueldo:", sueldo)
        elif modo == 2:
            print("\n[d2] Empleado(s) con mayor sueldo con sobrecarga")
            emp_sueldo = list(zip(self.empleados, self.sueldos))
            max_sueldo = max(self.sueldos)
            for emp, sueldo in emp_sueldo:
                if sueldo == max_sueldo:
                    print(emp, "Sueldo:", sueldo)

print("LineaTeleferico...")
linea1 = LineaTeleferico("Rojo", "Estación Central, Cementerio, 16 de Julio", 20)
linea2 = LineaTeleferico(color="Verde", tramo="Estación Busch - Plaza", nroCabinas=15)
linea1.agregar_empleado("Pedro", "Rojas", "Luna", 35, 2500)
linea1.agregar_empleado("Lucy", "Sosa", "Rios", 43, 3250)
linea1.agregar_empleado("Ana", "Perez", "Rojas", 26, 2700)
linea1.agregar_empleado("Saul", "Arce", "Calle", 29, 2500)
linea1.mostrar_empleados()
linea1.eliminar_empleado_por_apellido("Rojas")
linea1 + linea2
linea2.empleados_mayor_edad(modo=1)
linea2.empleados_mayor_edad(modo=2)
linea2.empleados_mayor_sueldo(modo=1)
linea2.empleados_mayor_sueldo(modo=2)
