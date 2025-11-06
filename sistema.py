from registro import Registro
from ave import Ave

class Sistema:
    def __init__(self):
        self.reg = Registro()

    def menu(self):
        while True:
            print("\nmenu principal")
            print("1. agregar ave")
            print("2. mostrar aves")
            print("3. registrar produccion semanal")
            print("4. ver produccion total")
            print("5. actualizar ave")
            print("6. eliminar ave")
            print("7. salir")
            op = input("elija una opcion: ")

            if op == "1":
                codigo = input("codigo: ")
                tipo = input("tipo: ")
                edad = input("edad: ")
                ave = Ave(codigo, tipo, edad)
                self.reg.agregarAve(ave)

            elif op == "2":
                self.reg.listarAves()

            elif op == "3":
                codigo = input("codigo del ave: ")
                self.reg.registrarProduccion(codigo)

            elif op == "4":
                codigo = input("codigo del ave: ")
                self.reg.verProduccion(codigo)

            elif op == "5":
                codigo = input("codigo del ave a actualizar: ")
                self.reg.actualizarAve(codigo)

            elif op == "6":
                codigo = input("codigo del ave a eliminar: ")
                self.reg.eliminarAve(codigo)

            elif op == "7":
                print("saliendo del programa...")
                break

            else:
                print("opcion invalida")

if __name__ == "__main__":
    app = Sistema()
    app.menu()
