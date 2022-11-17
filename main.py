import pygame, sys
from settings import *
from monsters import *



class Main():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((windowWidth, windowHeight))
        pygame.display.set_caption('Monstros rpg')
        self.clock = pygame.time.Clock()

        self.monsters = pygame.sprite.Group()

    def setPlayers(self):
        self.monster1Player1 = darkman
        self.monsters.add(self.monster1Player1)
        return self.monsters

    def choosePlayersScreen(self):
        self.chooseMonsterGroup = pygame.sprite.Group()
        self.chooseMonsterGroup.add(monstersList)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        self.battleScreen()
            dt = self.clock.tick() / 1000
            self.display_surface.fill((0, 0, 0))

            pygame.display.update()

    def battleScreen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            dt = self.clock.tick() / 1000
            self.display_surface.fill((249, 131, 103))
            self.setPlayers()
            self.monsters.draw(self.display_surface)
            self.monsters.update()

            pygame.display.update()

if __name__ == '__main__':
	main = Main()
	main.choosePlayersScreen()