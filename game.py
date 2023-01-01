import pygame
import sys 

background = pygame.Surface((600,600))
background.fill("Black")

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
                if event.type == pygame.KEYDOWN:
                    self.screen.blit(background,(0,0))
                    player1.move(self.screen, event)
                    player2.move(self.screen, event)
            
            pygame.display.update()

class Player:
    def __init__(self, screen, x, y, up, down):
        self.x=x
        self.y=y
        self.up=up
        self.down=down
        self.player = pygame.Surface((10,100))
        self.player.fill("White")
        screen.blit(self.player,(x,y))
    
    def move(self, screen, event): 
        if event.key == pygame.K_UP:
            self.y-=10
            screen.blit(self.player, (self.x,self.y))
        elif event.key == pygame.K_DOWN:
            self.y+=10
            screen.blit(self.player, (self.x,self.y))


if __name__ == "__main__":
    game = Game()
    game.runGame()
