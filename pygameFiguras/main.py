from tiposFiguras.Figura import Figura
from tiposFiguras.Cuadrado import Cuadrado
# https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons


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
