import os
import pygame
from models import Environement, personnage
from models.elements import Element
import dotenv 

dotenv_path = dotenv.find_dotenv("/Users/snowden/Documents/COURS_L1S1/option_info/python/class/cours/python/GringoGame01/core/.env")
ENV = dotenv.load_dotenv(dotenv_path)
Isometric = os.getenv("Isometric")

pygame.init()

running = True

screen = pygame.display.set_mode((Environement.DIMENSION))
Env0 = Environement.Environment(f"/Users/snowden/Documents/COURS_L1S1/option_info/python/class/cours/python/GringoGame01/core/images/spritesheet_caveman.png")
El0 = Element(f"{Isometric}/treePineSnowed_SE.png", x=40, y=300)
El1 = Element(f"{Isometric}/treeDecorated_NW.png", x=10, y=30)
El2 = Element(f"{Isometric}/cabinWindowLarge_SW.png", x=100, y=30)
El2_1 = Element(f"{Isometric}/cabinDoor_SE.png", x=160, y=30)
El2_2 = Element(f"{Isometric}/cabinRoofCenter_NE.png", x=160, y=-40)
P1 = personnage.Personnage("/Users/snowden/Documents/COURS_L1S1/option_info/python/class/cours/python/GringoGame01/core/images/RED.png")


elements_list = [El0, El1, El2, El2_1, El2_2]
DELTA_X = 0
DELTA_Y = 0



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                DELTA_X += -P1.dx
            
            if event.key == pygame.K_LEFT:
                DELTA_X += P1.dx
            
            if event.key == pygame.K_UP:
                DELTA_Y += -P1.dy
            
            if event.key == pygame.K_DOWN:
                DELTA_Y += P1.dy

            
    Env0.surface.fill((0,0,0))
    Env0.blit_elements(elements_list)
    screen.fill((0,0,0))
    screen.blit(Env0.surface, (DELTA_X, DELTA_Y))
    screen.blit(P1.sprite1, (30, 30))
    pygame.display.update()
    