import pygame

#buttons import/monster appear icons
fireMonstersButtonImg = pygame.image.load("images/icons/mfbutton.png")
waterMonstersButtonImg = pygame.image.load("images/icons/mabutton.png")
natureMonstersButtonImg = pygame.image.load("images/icons/mnbutton.png")
terrainMonstersButtonImg = pygame.image.load("images/icons/mtbutton.png")
darkMonstersButtonImg = pygame.image.load("images/icons/mtrbutton.png")
lightMonstersButtonImg = pygame.image.load("images/icons/mlbutton.png")
#settings icons
playButton = pygame.image.load("images/icons/JOGARBUTTONC.png")




#backgrounds images
redBackground = pygame.image.load("images/icons/bgairchose.png")

#images rects
redBackgroundRect = redBackground.get_rect(center = (1000, 500))

cardsHeight = 50
cardsWidth = 300
fireMonstersButtonImg = pygame.transform.scale(fireMonstersButtonImg, (cardsWidth, cardsHeight))
waterMonstersButtonImg = pygame.transform.scale(waterMonstersButtonImg, (cardsWidth, cardsHeight))
natureMonstersButtonImg = pygame.transform.scale(natureMonstersButtonImg, (cardsWidth, cardsHeight))
terrainMonstersButtonImg = pygame.transform.scale(terrainMonstersButtonImg, (cardsWidth, cardsHeight))
darkMonstersButtonImg = pygame.transform.scale(darkMonstersButtonImg, (cardsWidth, cardsHeight))
lightMonstersButtonImg = pygame.transform.scale(lightMonstersButtonImg, (cardsWidth, cardsHeight))
playButton = pygame.transform.scale(playButton, (200, 100))

redBackground = pygame.transform.scale(redBackground, (700, 600))

buttonsList = [fireMonstersButtonImg, waterMonstersButtonImg, natureMonstersButtonImg, terrainMonstersButtonImg, darkMonstersButtonImg, lightMonstersButtonImg, playButton]


