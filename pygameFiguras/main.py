from tiposFiguras.pool import pool
import pygame

display_width = 800
display_height = 600

white = (255, 255, 255)


def main():
    pygame.init()
    poolA = pool()

    gameDisplay = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Figuras locas')
    clock = pygame.time.Clock()

    figuraUno = poolA.getFigura()
    img = figuraUno.mostrarFigura()

    def mostar(x, y):
        gameDisplay.blit(img, (x, y))
    x = (0)
    y = (0)

    salida = False

    while not salida:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salida = True

        gameDisplay.fill(white)

        mostar(x, y)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
