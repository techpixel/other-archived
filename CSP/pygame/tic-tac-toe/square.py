import pygame

class Square(object):
    def __init__(self, inX, inY):
        self.x = inX
        self.y = inY
        self.block = pygame.Rect((self.x, self.y, 200, 200))
        self.player = " "

    def checkSquare(self):
        return self.player == " "

    def placePlayer(self, aP):
        if self.checkSquare() == True:
            self.player = aP
            return True
        return False

    def displaySelf(self, screen, font):
        text = font.render(self.player, False, (255, 0, 0))
        screen.blit(text, (self.x + 20, self.y + 20))
        