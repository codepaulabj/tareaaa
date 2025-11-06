from modelo_pollos import Registro
from interfaz import pedir_opcion, ejecutar_accion, mostrar_resultado

def main():
    rg = Registro()
    while True:
        op = pedir_opcion()
        res = ejecutar_accion(op, rg)
        if res == "salir":
            print("adiós")
            break
        mostrar_resultado(res)

if __name__ == "__main__":
    main()
