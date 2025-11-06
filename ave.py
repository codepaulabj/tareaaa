class Ave:
    def __init__(self, codigo, tipo, edad):
        self.__codigo = codigo
        self.__tipo = tipo
        self.__edad = int(edad)
        self.__produccion = []

    def getCodigo(self):
        return self.__codigo

    def getTipo(self):
        return self.__tipo

    def getEdad(self):
        return self.__edad

    def getProduccion(self):
        return self.__produccion

    def setCodigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    def setTipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    def setEdad(self, nueva_edad):
        try:
            nueva_edad = int(nueva_edad)
            if nueva_edad >= 0:
                self.__edad = nueva_edad
            else:
                print("la edad no puede ser negativa")
        except ValueError:
            print("la edad debe ser un numero entero")

    def registrarSemana(self, huevos):
        if huevos < 0:
            print("la cantidad no puede ser negativa")
        else:
            self.__produccion.append(huevos)
            print(f"semana registrada ({huevos} huevos)")

    def totalHuevos(self):
        return sum(self.__produccion)

    def __str__(self):
        return f"codigo: {self.__codigo}, tipo: {self.__tipo}, edad: {self.__edad} años, semanas: {len(self.__produccion)}"
