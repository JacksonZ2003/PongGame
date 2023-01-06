import pygame
import sys 
import random

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
        ball = Ball(self.screen)
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
            ball.moveBall(self.screen)
            
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
        self.player = pygame.Rect(x,y,10,100)
        pygame.draw.rect(screen, (255,255,255), self.player)
    
    #moves the players using controls
    def move(self,p1up, p1down, p2up, p2down, screen):
        if (p2down) and (self.player.y < 500) and (self.down == "down"):
            self.player.y+=10
        elif (p2up) and (self.player.y > 0) and (self.up=="up"):
            self.player.y-=10
        elif (p1down) and (self.player.y < 500) and (self.down == "s"):
            self.player.y+=10
        elif (p1up) and (self.player.y > 0) and (self.up=="w"):
            self.player.y-=10
        
        pygame.draw.rect(screen, (255,255,255), self.player)

class Ball:
    yvelocity = random.choice([5, 0, -5])
    xvelocity = random.choice([5,-5])

    def __init__(self, screen):
        self.x=290
        self.y=290
        self.ball = pygame.Rect(self.x,self.y,10,10)
        pygame.draw.rect(screen, (255,255,255), self.ball)
    
    def moveBall(self, screen):
        self.ball.x+=self.xvelocity
        self.ball.y+=self.yvelocity
        if (self.ball.y == 600 and self.ball.y == 0) and (self.yvelocity!=0): 
            self.yvelocity*=-1
        elif (self.ball.y == 600 and self.ball.y == 0) and (self.yvelocity==0): 
            self.yvelocity=random.choice([5,-5])
        elif self.ball.x == 0 or self.ball.x == 600:
            self.xvelocity*=-1
        
        pygame.draw.rect(screen,(255,255,255), self.ball)

if __name__ == "__main__":
    game = Game()
    game.runGame()
