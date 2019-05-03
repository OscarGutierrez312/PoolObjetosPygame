class Figura(object):

    _instance = None
    disponible = 1

    def __new__(cls, *args, **kwargs):

        if not cls._instance:
            cls._instance = super(Figura, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def isDisponible(self):
        return self.disponible

    def setDisponible(self, disponible):
        self.disponible = disponible

    def mostrarFigura(self):
        pass
