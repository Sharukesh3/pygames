import pygame
import time

#setup
pygame.init()

#variables
screen_width = 1300
screen_height = 600
color_screen = (32,33,36)
color_text = (154,160,166)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("kanthan challenge 1")
clock=pygame.time.Clock()
running = True
is_jumping = False
jump_count = 10
jump_vel = 1

dt=0
player_pos=pygame.Vector2(screen_width/2,screen_height/2)

dino = pygame.image.load("pic/google_dino.jpg")
cactus = pygame.image.load("pic/cactus.jpeg")
dino_rect = dino.get_rect()
cactus_rect = cactus.get_rect()
dino_rect.bottomright = (150,((2/3)*screen_height-2))
sound_jump = pygame.mixer.Sound("sound/jump.wav")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
 
    screen.fill(color_screen)
   
    #pygame.draw.circle(screen,"red",player_pos,10)  
    pygame.draw.line(screen,color_text,(0,(2/3)*screen_height),(screen_width,(2/3)*screen_height),5)  
    
    keys = pygame.key.get_pressed()    
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dino_rect.x -=300*dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dino_rect.x +=300*dt
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not is_jumping:  # Check if not already jumping
            sound_jump.play()
            is_jumping = True
        
    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_rect.y -= (jump_count ** 2) * 0.5 * neg * jump_vel
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10
        
    screen.blit(dino,dino_rect)
        
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(screen,"blue",player_pos,10)
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            player_pos.x = pos[0]
            player_pos.y = pos[1]
        
    
    pygame.display.flip()
    
    dt = clock.tick(60)/1000

pygame.quit()