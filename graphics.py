import pygame

class Buttons(pygame.sprite.Sprite):
    def __init__(self, name, pos, groups):
        super(Buttons, self).__init__(groups)
        self.name = name
        self.pos = pos
        self.cardsHeight = 50
        self.cardsWidth = 300
        self.image = pygame.image.load(f"images/icons/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (self.cardsWidth, self.cardsHeight))
        self.rect = self.image.get_rect(center = (pos))
        self.buttonPressed = None

    def colission(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                self.buttonPressed = True

    def update(self):
        self.colission()


#settings icons
playButton = pygame.image.load("images/icons/JOGARBUTTONC.png")

#backgrounds images
redBackgroundImg = pygame.image.load("images/icons/bgfirechose.png")
blueBackgroundImg = pygame.image.load("images/icons/bgwaterchose.png")
greenBackgroundImg = pygame.image.load("images/icons/bgplantchose.png")
whiteBackgroundImg = pygame.image.load("images/icons/bglightchose.png")
blackBackgroundImg = pygame.image.load("images/icons/bgdarkchose.png")
yellowredBackgroundImg = pygame.image.load("images/icons/bgeletricchose.png")

# class backgroundImages():
#     def __init__(self, pos, name):
#         self.image =

#images rects
redBackgroundRect = pygame.transform.scale(redBackgroundImg, (700, 600))
blueBackgroundImg = pygame.transform.scale(blueBackgroundImg, (700, 600))
greenBackgroundImg = pygame.transform.scale(greenBackgroundImg, (700, 600))
whiteBackgroundImg = pygame.transform.scale(whiteBackgroundImg, (700, 600))

buttonsGroup = pygame.sprite.Group()
buttonsAtributesGroup = []
fireMonstersButtonImg = Buttons("mfbutton", (0, 0), [buttonsGroup, buttonsAtributesGroup])
waterMonstersButtonImg = Buttons("mabutton", (0, 0), [buttonsGroup, buttonsAtributesGroup])
natureMonstersButtonImg = Buttons("mnbutton", (0, 0), [buttonsGroup, buttonsAtributesGroup])
terrainMonstersButtonImg = Buttons("mtbutton", (0, 0), [buttonsGroup, buttonsAtributesGroup])
darkMonstersButtonImg = Buttons("mtrbutton", (0, 0), [buttonsGroup, buttonsAtributesGroup])
lightMonstersButtonImg = Buttons("marbutton", (0, 0), [buttonsGroup, buttonsAtributesGroup])
playButton = pygame.transform.scale(playButton, (200, 100))