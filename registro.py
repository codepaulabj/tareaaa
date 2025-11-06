from ave import Ave

class Registro:
    def __init__(self):
        self.aves = []

    def agregarAve(self, ave):
        for a in self.aves:
            if a.getCodigo() == ave.getCodigo():
                print("ya existe una ave con ese codigo")
                return
        self.aves.append(ave)
        print("ave agregada correctamente")

    def listarAves(self):
        if not self.aves:
            print("no hay aves registradas")
        else:
            for a in self.aves:
                print(a)

    def registrarProduccion(self, codigo):
        for a in self.aves:
            if a.getCodigo() == codigo:
                try:
                    huevos = int(input("ingrese huevos producidos esta semana: "))
                    a.registrarSemana(huevos)
                except ValueError:
                    print("ingrese un numero valido")
                return
        print("no se encontro una ave con ese codigo")

    def verProduccion(self, codigo):
        for a in self.aves:
            if a.getCodigo() == codigo:
                total = a.totalHuevos()
                print(f"el ave {codigo} ha producido {total} huevos en total")
                return
        print("codigo no encontrado")

    def actualizarAve(self, codigo):
        for a in self.aves:
            if a.getCodigo() == codigo:
                nuevo_tipo = input("nuevo tipo (enter para mantener): ")
                nueva_edad = input("nueva edad (enter para mantener): ")
                if nuevo_tipo:
                    a.setTipo(nuevo_tipo)
                if nueva_edad:
                    a.setEdad(nueva_edad)
                print("ave actualizada correctamente")
                return
        print("no se encontro una ave con ese codigo")

    def eliminarAve(self, codigo):
        for a in self.aves:
            if a.getCodigo() == codigo:
                self.aves.remove(a)
                print(f"ave con codigo {codigo} eliminada")
                return
        print("no se encontro una ave con ese codigo")
