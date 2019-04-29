from .Figura import Figura


class Cuadrado(Figura):
    def __init__(self, nombre, lados):
        super().__init__(nombre)
        self.lados = lados

    def mostrar(self):
        print("soy un Cuadrado")
# https://stackoverflow.com/questions/4534438/typeerror-module-object-is-not-callable
# https://stackoverflow.com/questions/40237354/how-to-inherit-class-from-different-file
