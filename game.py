import pygame
import sys 

class Game:
    #creates the game
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,700))
        pygame.display.set_caption("Game")
        
    #runs the game
    def runGame(self):
        p1move_up = False
        p1move_down = False
        p2move_up = False
        p2move_down = False
        player1 = Player(self.screen,0,250,"w","s")
        player2 = Player(self.screen,590,250,"up","down")
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w):
                        p1move_up=True
                    if (event.key == pygame.K_s):
                        p1move_down = True
                    if (event.key == pygame.K_UP):
                        p2move_up=True
                    if (event.key == pygame.K_DOWN):
                        p2move_down = True
                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_UP):
                        p2move_up=False
                    if (event.key == pygame.K_DOWN):
                        p2move_down=False
                    if (event.key == pygame.K_w):
                        p1move_up=False
                    if (event.key == pygame.K_s):
                        p1move_down = False
                
            self.screen.fill((0,0,0))
            player1.move(p1move_up, p1move_down, p2move_up, p2move_down, self.screen)
            player2.move(p1move_up, p1move_down, p2move_up, p2move_down, self.screen)
            
            pygame.display.update()
            clock.tick(60)

class Player:
    #initializes the player rectangles
    def __init__(self, screen, x, y, up, down):
        score = 0
        self.x=x
        self.y=y
        self.up=up
        self.down=down
        self.player = pygame.Surface((10,100))
        self.player.fill("White")
        screen.blit(self.player,(x,y))
    
    #moves the players using controls
    def move(self,p1up, p1down, p2up, p2down, screen):
        if (p2down) and (self.y < 500) and (self.down == "down"):
            self.y+=10
        if (p2up) and (self.y > 0) and (self.up=="up"):
            self.y-=10
        if (p1down) and (self.y < 500) and (self.down == "s"):
            self.y+=10
        if (p1up) and (self.y > 0) and (self.up=="w"):
            self.y-=10
        
        screen.blit(self.player, (self.x,self.y))

class Ball:
    def __init__(self):
        x=0
        y=0

if __name__ == "__main__":
    game = Game()
    game.runGame()
