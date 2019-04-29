class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
        print("la figura es :" + self.nombre)

    def mostrar(self):
        '''Sólo define una interfaz.'''
        pass

    def __del__(self):
        print("El animal {} acaba de fallecer.".format(self.nombre))
# https://www.tutorialspoint.com/python/python_pass_statement.htm

# herencia en python
# https://pythonista.io/cursos/py111/clases-abstractas-y-duck-typing
