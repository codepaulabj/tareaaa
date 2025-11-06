class Animal:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.registros = []

    def guardar_semana(self, semana, huevos):
        for i, par in enumerate(self.registros):
            if par[0] == semana:
                self.registros[i] = (semana, huevos)
                return "actualizado"
        self.registros.append((semana, huevos))
        return "agregado"

    def huevos_semana(self, semana):
        for s, h in self.registros:
            if s == semana:
                return h
        return 0

    def huevos_totales(self):
        t = 0
        for _, h in self.registros:
            t += h
        return t


class Registro:
    def __init__(self):
        self.animales = []

    def buscar(self, codigo):
        for a in self.animales:
            if a.codigo == codigo:
                return a
        return None

    def crear(self, codigo, raza, edad):
        if self.buscar(codigo):
            return "existe"
        self.animales.append(Animal(codigo, raza, edad))
        return "creado"

    def listar(self):
        if not self.animales:
            return "sin animales"
        filas = []
        for a in self.animales:
            filas.append(f"{a.codigo} | {a.raza} | {a.edad} años | sem:{len(a.registros)}")
        return "\n".join(filas)

    def editar(self, codigo, raza, edad):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        a.raza = raza
        a.edad = edad
        return "editado"

    def eliminar(self, codigo):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        self.animales.remove(a)
        return "eliminado"

    def registrar(self, codigo, semana, huevos):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        return a.guardar_semana(semana, huevos)

    def consultar_semana(self, codigo, semana):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        return a.huevos_semana(semana)

    def consultar_total(self, codigo):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        return a.huevos_totales()
