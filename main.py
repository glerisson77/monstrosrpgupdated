import pygame, sys
from settings import *
from monsters import *
from debug import *


class Main():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((windowWidth, windowHeight))
        pygame.display.set_caption('Monstros rpg')
        self.clock = pygame.time.Clock()

        # images convertalpha part
        for icon in buttonsList:
            icon = icon.convert_alpha()

        self.monsters = pygame.sprite.Group()

    def setPlayers(self):
        self.monster1Player1 = darkman
        self.monsters.add(self.monster1Player1)
        return self.monsters

    def buttonsCollision(self):
        pass

    def displayBackgroundChoosePS(self, rect):
        if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            # if rect ==
            print('col')
            return self.display_surface.blit(redBackground, (redBackgroundRect))

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


            #display all icons
            self.yPosition = 50
            for icon in buttonsList:
                if icon != playButton:
                    iconRect = icon.get_rect(center = (150, self.yPosition))
                    self.display_surface.blit(icon, (iconRect))
                    self.yPosition += 50
                    self.displayBackgroundChoosePS(iconRect)
                if icon == playButton:
                    playButtonX = 150
                    playButtonY = windowHeight - playButton.get_height() - 20
                    playButtonRect = playButton.get_rect(center = (playButtonX, playButtonY))
                    self.display_surface.blit(playButton, (playButtonRect))

            if pygame.mouse.get_pressed()[0]:
                if playButtonRect.collidepoint(pygame.mouse.get_pos()):
                    self.battleScreen()



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