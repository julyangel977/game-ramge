import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kill Python")
icon = pygame.image.load("Images/python.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("Images/target_python.jpg")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 5
target_speed_y = 5

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    pass

pygame.quit()
