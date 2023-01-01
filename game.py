import pygame
import sys 

background = pygame.Surface((600,600))
background.fill("Black")

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,700))
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
        if (event.key == pygame.K_UP) and (self.y > 0) and (self.up=="up"):
            self.y-=10
            screen.blit(self.player, (self.x,self.y))
        elif (event.key == pygame.K_w) and (self.y > 0) and (self.up=="w"):
            self.y-=10
            screen.blit(self.player, (self.x,self.y))
        elif (event.key == pygame.K_DOWN) and (self.y < 500) and (self.down == "down"):
            self.y+=10
            screen.blit(self.player, (self.x,self.y))
        elif (event.key == pygame.K_s) and (self.y < 500) and (self.down == "s"):
            self.y+=10
            screen.blit(self.player, (self.x,self.y))
        else:
            screen.blit(self.player, (self.x,self.y))


if __name__ == "__main__":
    game = Game()
    game.runGame()
