import pygame

class Stat():
    def __init__(self,game):
        self.setting = game.setting

        self.reset_stats()
        self.game_active = True
        self.sq_kill = 0
    def reset_stats(self):
        self.beavers_dead = self.setting.beaver_limit

from pygame.sprite import Sprite
class Background(Sprite):
    def __init__(self,img,loc):
        super().__init__()
        self.image = pygame.image.load(img)
        self.location = loc
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.right = loc




