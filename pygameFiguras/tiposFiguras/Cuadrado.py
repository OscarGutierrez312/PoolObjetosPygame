from .Figura import Figura
import pygame


class Cuadrado(Figura):
    def mostrarFigura(self):
        cuadradoImg = pygame.image.load('imagenes/square.jpeg')
        return cuadradoImg
