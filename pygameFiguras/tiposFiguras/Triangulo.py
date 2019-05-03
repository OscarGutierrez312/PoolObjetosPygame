from .Figura import Figura
import pygame


class Triangulo(Figura):
    def mostrarFigura(self):
        trianguloImg = pygame.image.load('imagenes/triangulo.png')
        return trianguloImg
