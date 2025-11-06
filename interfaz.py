def pedir_opcion():
    print("\n--- menú granja de pollos ---")
    print("1) nuevo pollo")
    print("2) listar pollos")
    print("3) registrar huevos por semana")
    print("4) consultar huevos de una semana")
    print("5) consultar huevos totales")
    print("6) actualizar pollo")
    print("7) eliminar pollo")
    print("8) salir")
    return input("opción: ").strip()

def ejecutar_accion(op, rg):
    if op == "1":
        c = input("código: ").strip()
        r = input("raza: ").strip()
        try:
            e = int(input("edad (años): "))
        except:
            return "edad inválida"
        return rg.crear(c, r, e)

    if op == "2":
        return rg.listar()

    if op == "3":
        c = input("código: ").strip()
        try:
            s = int(input("semana: "))
            h = int(input("huevos: "))
        except:
            return "números inválidos"
        return rg.registrar(c, s, h)

    if op == "4":
        c = input("código: ").strip()
        try:
            s = int(input("semana: "))
        except:
            return "semana inválida"
        r = rg.consultar_semana(c, s)
        if r == "no existe":
            return r
        return f"huevos en semana {s}: {r}"

    if op == "5":
        c = input("código: ").strip()
        r = rg.consultar_total(c)
        if r == "no existe":
            return r
        return f"total de huevos: {r}"

    if op == "6":
        c = input("código: ").strip()
        r = input("nueva raza: ").strip()
        try:
            e = int(input("nueva edad: "))
        except:
            return "edad inválida"
        return rg.editar(c, r, e)

    if op == "7":
        c = input("código: ").strip()
        return rg.eliminar(c)

    if op == "8":
        return "salir"

    return "opción inválida"

def mostrar_resultado(msg):
    print("\n>> resultado")
    print(msg)
