from tiposFiguras.Figura import Figura
from tiposFiguras.Cuadrado import Cuadrado
from tiposFiguras.Circulo import Circulo
from tiposFiguras.Triangulo import Triangulo
from tiposFiguras.pool import pool
import pygame


def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Figuras locas')
    clock = pygame.time.Clock()

    salida = False
    while not salida:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salida = True
            print(event)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()

    poolA = pool()

    figuraUno = poolA.getFigura()
    print(figuraUno.mostrarFigura())


if __name__ == '__main__':
    main()
