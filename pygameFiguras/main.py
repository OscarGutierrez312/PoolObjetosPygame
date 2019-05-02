from tiposFiguras.Figura import Figura
from tiposFiguras.Cuadrado import Cuadrado
from .pool import ObjectPool
# https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
# https://stackoverflow.com/a/1810367


def main():
    pass


if __name__ == '__main__':
    s1 = Figura()
    s1.setNombre('ricardo')
    s2 = Figura()
    print(s2.getNombre())
    if (id(s1) == id(s2)):
        print("Same")
    else:
        print("Different")

    c1 = Cuadrado()
    c2 = Cuadrado()

    c1.setNombre('Cuadrado')
    print(c2.getNombre())

    print("fin del programa")

    pool = ObjectPool().getInstance()

    figura1 = pool.getResource()
    figura2 = pool.getResource()

    figura1.setNombre("triangulo1")
    figura2.setNombre("triangulo2")

    print(figura1.getNombre())
    print(figura2.getNombre())

    pool.returnResource(figura1)
    pool.returnResource(figura2)

    figura1 = None
    figura2 = None
