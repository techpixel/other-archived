import pygame

class WinCheck(object):

    def __init__(self):
        self.player = " "
        self.winner = False
        self.pos1 = None
        self.pos2 = None

    def checkWinners(self, grid):
        if not grid[0][0].player == ' ':
            if (grid[0][0].player == grid[1][0].player and grid[0][0].player == grid[2][0].player):
                self.pos1 = grid[0][0]
                self.pos2 = grid[2][0]
                self.player = grid[0][0].player
            elif (grid[0][0].player == grid[1][1].player and grid[0][0].player == grid[2][2].player):
                self.pos1 = grid[0][0]    
                self.pos2 = grid[2][2]
                self.player = grid[0][0].player
            elif (grid[0][0].player == grid[0][1].player and grid[0][1].player == grid[0][2].player):
                self.pos1 = grid[0][0]
                self.pos2 = grid[0][2]
                self.player = grid[0][0].player            
        if not grid[2][2].player == ' ':
            if (grid[2][2].player == grid[2][1].player and grid[2][2].player == grid[2][0].player):
                self.pos1 = grid[2][2]
                self.pos2 = grid[2][0]
                self.player = grid[2][2].player
            elif (grid[2][2].player == grid[1][2].player and grid[2][2].player == grid[0][2].player):
                self.pos1 = grid[2][2]
                self.pos2 = grid[0][2]
                self.player = grid[2][2].player
        if not grid[1][1].player == ' ':            
            if (grid[1][1].player == grid[0][2].player and grid[1][1].player == grid[2][0].player):
                self.pos1 = grid[0][2]
                self.pos2 = grid[2][0]
                self.player = grid[1][1].player
            elif (grid[1][1].player == grid[1][0].player and grid[1][1].player == grid[1][2].player):
                self.pos1 = grid[1][0]
                self.pos2 = grid[1][2]
                self.player = grid[1][1].player
            elif (grid[1][1].player == grid[0][1].player and grid[1][1].player == grid[2][1].player):
                self.pos1 = grid[0][1]
                self.pos2 = grid[2][1]
                self.player = grid[1][1].player

        if not self.player == " ":
            self.winner = True

        for r in grid:
            for square in r:
                if square.player == " ":
                    return
        
        self.player = "TIE"
        self.winner = True
        

    def displayWin(self, screen):
        font = pygame.font.Font("Smokum-Regular.ttf", 300)
        winText = font.render(self.player, False, (0, 0, 0, 0))

        if self.winner and self.player != "TIE":
            pos1calc = (self.pos1.x + 100, self.pos1.y + 100)
            pos2calc = (self.pos2.x + 100, self.pos2.y + 100)
            pygame.draw.line(screen, (0, 255, 0), pos1calc, pos2calc, 4)

        screen.blit(winText, (150, 150))