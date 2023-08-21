class Asiento:

    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if color in ["rojo" ,"verde" ,"amarillo" ,"negro" ,"blanco"]:
            self.color = color

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        totalAsientos = 1
        for x in self.asientos:
            if (type(x) == Asiento):
                totalAsientos += 1
        return totalAsientos

    def verificarIntegridad(self):
        if (self.registro == self.motor.registro):
            for x in self.asientos:
                if (type(x) == Asiento):
                    if self.registro != x.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"

class Motor:

    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if (tipo == 'electrico' or tipo == 'gasolina'):
            self.tipo = tipo
