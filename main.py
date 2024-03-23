import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kill Python")

icon = pygame.image.load("Images/python.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("Images/target_python.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_speed_x = 3
target_speed_y = 3

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    target_x += target_speed_x
    target_y += target_speed_y
    if target_x <= 0 or target_x >= (SCREEN_WIDTH - target_width):
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= (SCREEN_HEIGHT - target_height):
        target_speed_y = -target_speed_y

    screen.blit(target_image, (target_x, target_y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
