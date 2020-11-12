import pygame
pygame.init()


class Personnage(object):

    def __init__(self, image_path:str, name="gringo"):
        self.x = 140
        self.y = 40 
        self.spriteSheet = pygame.image.load(image_path).convert_alpha()
        self.sprite1 = self.spriteSheet

        with open("/Users/snowden/Documents/COURS_L1S1/option_info/python/class/cours/python/GringoGame01/core/images/red.json", "r") as file_json:
            content = file_json.read().split("},{")
            for i,obj in enumerate(content):
                print({obj})
                # self.__setattr__(f"sprite{i}", )
                self.__setattr__(f"sprite{i}"+".x", obj.index(','))
                self.__setattr__(f"sprite{i}"+".height", obj.index(','))
                self.__setattr__(f"sprite{i}"+".y", obj.index(','))
                self.__setattr__(f"sprite{i}"+".width", obj.index(','))


        self.dx = 10 # deplacement en x
        self.dy = 5 # deplacement en y
        self.sens = 0
    
    def move(self, direction:str, sens:int): 
        """
        # vecteur | direction : 'x' ou 'y' | sens -1(gauche) 
        # ou 1 (droite)         
        """
        new_position = self.__getattribute__(direction)*self.sens_decision(sens)
        self.__setattr__(direction, new_position)

    def sens_decision(self, sens:int):
        if sens > 0:
            return 1
        elif sens == 0:  
            return 0
        else: # au pire si aucune des condition est vrai 
            return -1



        
# gringo = Personage("/Users/snowden/Documents/COURS_L1S1/option_info/python/class/cours/python/GringoGame01/core/images/spritesheet_caveman.png")
# gringo.move('x', 'negatif') 
