from .Figura import Figura
import pygame


class Circulo(Figura):
    def mostrarFigura(self):
        circleImg = pygame.image.load('imagenes/circle.png')
        return circleImg
