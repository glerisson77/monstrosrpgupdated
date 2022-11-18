import pygame, sys
from graphics import *

class Monsters(pygame.sprite.Sprite):
    def __init__(self,  name, type, atk, defense, hp, pos):
        super().__init__()
        self.name = name
        self.type = type
        self.atack = atk
        self.defense = defense
        self.hp = hp
        self.pos = pos

        self.image = pygame.image.load(f"images/monsters/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=pos)

darkman = Monsters('darkman', 'dark', 300, 300, 300, (200, 200))
darkthing = Monsters('darkthing', 'dark', 300, 300, 300, (400, 200))
monstersList = [darkman, darkthing]

