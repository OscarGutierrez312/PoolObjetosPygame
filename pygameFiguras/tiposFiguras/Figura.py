class Figura(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Figura, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def mostrarFigura(self):
        pass

# https://www.tutorialspoint.com/python/python_pass_statement.htm

# herencia en python
# https://pythonista.io/cursos/py111/clases-abstractas-y-duck-typing
