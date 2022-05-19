import pygame
from board import Board

pygame.init()
screen = pygame.display.set_mode((600, 600))
fonts = pygame.font.Font("Smokum-Regular.ttf", 190)
game = Board()

while True:
    screen.fill((255,255,255))

    game.runMe(screen, fonts)

    pygame.display.update()

    for event in pygame.event.get():
        if pygame.mouse.get_pressed() == (True, False, False) and game.wc.winner == False:
            for r in range(3):
                for c in range(3):
                    if game.TTT[r][c].block.collidepoint(pygame.mouse.get_pos()):
                        if game.TTT[r][c].placePlayer(game.activePlayer):
                            game.swapPlayer()                
        elif pygame.mouse.get_pressed() == (False, False, True) and game.wc.winner == True:
            game = Board()
            
