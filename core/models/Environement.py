import pygame
pygame.init()

DIMENSION = (1200,700)
# screen = pygame.display.set_mode((DIMENSION))

class Environment:
    def __init__(self, bg_image_path:str):
        self.image = pygame.image.load(bg_image_path) # image a coller sur la surface
        self.surface = pygame.Surface((DIMENSION)) # surface
    
    def blit(self):
        self.surface.blit(self.image, (0,0))
    
    def blit_element(self, element):
        self.surface.blit(element.image, (element.x, element.y))
    
    def blit_elements(self, elements_list):
        for element in elements_list:
            self.blit_element(element)
    
    def blit_perso_init(self, perso):
        
        self.surface.blit(perso.image_1, (perso.x, perso.y))
    
    def blit_perso(self, perso):
        sens = perso.sens
        if sens == "up":
            sens = 3
        else:
            sens = 1

        self.surface.blit(perso.__getattribute__(f"image_{sens}"), (perso.x, perso.y))
        


        