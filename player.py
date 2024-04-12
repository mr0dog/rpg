import pygame

#Constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
Chicken = pygame.image.load('chicken.png') #load your spritesheet
Chicken.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

class player:
    def __init__(self):
        #player variables
        self.xpos = 400#xpos of player
        self.ypos = 415#ypos of player
        self.vx = 0#velocity of playerkbnjk
        self.vy = 0#velocity of player
        self.frameWidth = 69
        self.frameHeight = 69
        self.RowNum = 2 #for left animation, this will need to change for other animations
        self.frameNum = 0
        self.ticker = 0
    def draw(self,screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30,30))
        screen.blit(Chicken, (self.xpos, self.ypos), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight)) 

    def move(self, keys, map):
        #LEFT movement
        if keys[LEFT] == True:
            self.vx = 3
            self.RowNum = 2
            print("moving to the left")
        #RIGHT MOVEMENT
        elif keys[RIGHT] == True:
            self.vx = 3
            self.RowNum = 3   #turn off x velocity
        else:
            self.vx = 0
                   
        #collision
        #left collision
        if map [int((self.ypos - 10) / 50)][int((self.xpos - 10) / 50)] == 2:
                    self.xpos+=3
                   
        #right collision
        if map[int((self.ypos) / 50)][int((self.xpos +30 + 5) / 50)] == 2:
                    self.xpos-=3
                   
        self.xpos+=self.vx#update player xpos
        self.ypos+=self.vy
        if self.vx != 0 or self.vy != 0:    # processor can process! Update Animation Frame each time ticker goes over
            self.ticker+=1
            if self.ticker%10==0: #only change frames every 10 ticks
              self.frameNum+=1
               #If we are over the number of frames in our sprite, reset to 0.
               #In this particular case, there are 8 frames (0 through 7)
            if self.frameNum>7: 
               self.frameNum = 0
