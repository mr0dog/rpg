import pygame
from wow import player
pygame.init()
pygame.display.set_caption("top down grid game")
screen = pygame.display.set_mode((550, 550))
clock = pygame.time.Clock()
gameover = False


p1 = player() 

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False]
map = [[2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,2,2,3,3,3,2],
       [2,1,1,1,1,2,2,3,3,3,2],
       [2,1,1,2,2,2,2,3,3,3,2],
       [2,1,1,1,3,3,3,3,3,3,2], 
       [2,1,1,3,3,3,3,3,3,3,2],
       [2,1,2,3,3,3,3,3,3,3,2],
       [2,1,2,3,3,3,3,3,3,3,2],
       [2,1,2,3,3,3,3,3,3,3,2],
       [2,1,2,3,3,3,3,3,3,3,2],
       [2,2,2,2,2,2,2,2,2,2,2]]
brick = pygame.image.load('uwen.jpg')
dirt = pygame.image.load('dirbt.jpg')
grass = pygame.image.load('gwass.jpg')
while not gameover:#GAME LOOP 3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    clock.tick(60) #fps
    #input section----------------------------------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False

        
         #physics section---------------------------------------------------------------------------------------------------------------------------------------------------

         #render section---------------------------------------------------------------------------------------------------------------------------------------------------------

        screen.fill((0,0,0)) #wipe screen so it doesn't smear
        #draw map
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
            if map[i][j] == 2:
                screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
            if map[i][j] == 3:
                screen.blit(grass, (j * 50, i * 50), (0, 0, 50, 50))
    
    p1.draw(screen)
    pygame.display.flip()#this is actually puts the pixel on the screen 

# End Gameloop 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
pygame.quit() 
