import random
from tiposFiguras.Cuadrado import Cuadrado
from tiposFiguras.Circulo import Circulo
from tiposFiguras.Triangulo import Triangulo


class pool(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(pool, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.figura = ["", "", ""]
        for i in range(0, 2):
            opc = self.aleatorio()
            if (opc == 0):
                self.figura[i] = Circulo()
            if (opc == 1):
                self.figura[i] = Cuadrado()
            if (opc == 2):
                self.figura[i] = Triangulo()

    def getFigura(self):
        for i in range(0, 2):
            if(self.figura[i].isDisponible() == 1):
                self.figura[i].setDisponible(0)
                return self.figura[i]

    def aleatorio(self):
        return random.randint(0, 2)
