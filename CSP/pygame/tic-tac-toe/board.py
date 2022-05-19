from square import Square
from winCheck import WinCheck
import pygame

class Board(object):
    P1 = 'X'
    P2 = 'O'
    activePlayer = P1

    def __init__(self):
        self.TTT = [[], [], []]
        self.wc = WinCheck()

        for r in range(3):
            for c in range(3):
                self.TTT[r].append(Square(r*200, c*200))

    def runMe(self, screen, font):
    
        # Draw board 
        for r in self.TTT:
            for c in r:
                c.displaySelf(screen, font)

        for i in range(1, 3):
            pygame.draw.line(screen, (0, 0, 0), (0, 200*i), (600, 200*i), 3)
            pygame.draw.line(screen, (0, 0, 0), (200*i, 0), (200*i, 600), 3)

        self.wc.displayWin(screen)

    def swapPlayer(self):
        if self.activePlayer == self.P1:
            self.activePlayer = self.P2
        else:
            self.activePlayer = self.P1

        self.wc.checkWinners(self.TTT)