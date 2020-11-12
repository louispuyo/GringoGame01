import pygame
pygame.init()


class Element:
    def __init__(self, image_path:str, x=0, y=50):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
