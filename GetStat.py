import pygame

class Stat():
    def __init__(self,game):
        self.setting = game.setting

        self.reset_stats()

    def reset_stats(self):
        self.beavers_dead = self.setting.beaver_limit

