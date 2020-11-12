import pygame
import settings
import random
# Pour transmettre deux coordonées plus simplement
spd = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, app, x, y):
        # Directement add au group
        self.groups = app.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.app = app
        #création du joueur et sa surface
        self.image = pygame.Surface((settings.Screen.TSIZE, settings.Screen.TSIZE))
        self.rect = self.image.get_rect()
        self.spd = spd(0, 0)
        self.pos = spd(x, y)
        self.currentFrame = 2
        self.cells = []
        self.frames = []
        self.hh = False
        self.guerir = False
        for i in range(15):

            # On crée une case
            cell = (self.app.datared[i]['x'], self.app.datared[i]['y'], self.app.datared[i]['width'], self.app.datared[i]['height'])

            # On crée une Surface de la taille d'une case
            frame = pygame.surface.Surface((self.app.datared[i]['width'], self.app.datared[i]['height']))
            # Sur laquelle on dessine la case de la spritesheet qui nous intéresse
            frame.blit(self.app.pl_img, (0, 0), cell)
            frame = pygame.transform.scale(frame,(settings.Screen.TSIZE,settings.Screen.TSIZE))

            # On ajoute la frame à une liste
            self.frames.append(frame)

            # Et pareil pour la case (pour garder ton fonctionnement à toi ou tu reblit une image à chaque frame)
            self.cells.append(cell)


