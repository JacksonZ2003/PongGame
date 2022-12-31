import pygame
import sys 

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption("Game")

    def runGame(self):
        player1 = Player(self.screen,0,250,"w","s")
        player2 = Player(self.screen,590,250,"up","down")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            pygame.display.update()

class Player:
    def __init__(self, screen, x, y, up, down):
        player = pygame.Surface((10,100))
        player.fill("White")
        screen.blit(player, (x,y))


if __name__ == "__main__":
    game = Game()
    game.runGame()
