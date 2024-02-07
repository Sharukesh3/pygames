import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
GROUND_HEIGHT = 50
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Dino Game")

# Load images
dino_img = pygame.image.load("pic/google_dino.jpg")  # Replace "dino.png" with your dino image
cactus_img = pygame.image.load("pic/cactus.jpeg")  # Replace "cactus.png" with your cactus image

# Scale images
dino_img = pygame.transform.scale(dino_img, (60, 60))

# Scale the cactus image to your desired dimensions (width, height)
cactus_width, cactus_height = 10, 20  # Adjust these values according to your preferences
cactus_img = pygame.transform.scale(cactus_img, (cactus_width, cactus_height))

# Game variables
dino_x, dino_y = 50, HEIGHT - GROUND_HEIGHT - dino_img.get_height()
cactus_x, cactus_y = WIDTH + 100, HEIGHT - GROUND_HEIGHT - cactus_img.get_height()
cactus_speed = 5
jumping = False
jump_count = 10

clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

def draw_window():
    screen.fill((32,33,36))
    pygame.draw.line(screen, BLACK, (0, HEIGHT - GROUND_HEIGHT), (WIDTH, HEIGHT - GROUND_HEIGHT), 2)
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(cactus_img, (cactus_x, cactus_y))
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))
    pygame.display.update()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not jumping:
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    cactus_x -= cactus_speed
    if cactus_x < -cactus_img.get_width():
        cactus_x = WIDTH + random.randint(300, 600)
        score += 1

    # Collision detection
    if (cactus_x <= dino_x + dino_img.get_width() <= cactus_x + cactus_img.get_width() or
            cactus_x <= dino_x <= cactus_x + cactus_img.get_width()) and \
            dino_y + dino_img.get_height() >= cactus_y:
        running = False

    draw_window()

pygame.quit()
