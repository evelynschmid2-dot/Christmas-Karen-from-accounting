# Karen from Accounting - Face Animation Engine
# ---------------------------------------------
# SETUP (first time only):
#   python3 -m venv venv
#
# ACTIVATE (every time before running):
#   source venv/bin/activate
#
# INSTALL DEPENDENCIES (first time only, after activating):
#   pip3 install pygame
#
# RUN:
#   python3 karen_face.py
#
# DEACTIVATE when done:
#   deactivate

import pygame
from datetime import datetime

pygame.init()

karen_img = pygame.image.load("ChristmasKaren.png")
karen_img = pygame.transform.scale(karen_img, (600, 600))
karenglobe_img = pygame.image.load("karenglobe.png")
karenglobe_x, karenglobe_y = 100, 100
karenglobe_speed_x, karenglobe_speed_y = 3, 2
karenglobe_img = pygame.transform.scale(karenglobe_img, (300, 300))
buiscetglobe_img = pygame.image.load("buiscetglobe.png")
buiscetglobe_x, buiscetglobe_y = 500, 300
buiscetglobe_speed_x, buiscetglobe_speed_y = -2, 3
buiscetglobe_img = pygame.transform.scale(buiscetglobe_img, (300, 300))

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Karen Alderman")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((26, 71, 42))
    karenglobe_x += karenglobe_speed_x
    karenglobe_y += karenglobe_speed_y
    buiscetglobe_x += buiscetglobe_speed_x
    buiscetglobe_y += buiscetglobe_speed_y

    if karenglobe_x <= 0 or karenglobe_x >=1280 - 300:
        karenglobe_speed_x *= -1
    if karenglobe_y<= 0 or karenglobe_y >= 720 - 300:
        karenglobe_speed_y *= -1
    
    if buiscetglobe_x <= 0 or buiscetglobe_x >= 1280 - 300:
        buiscetglobe_speed_x *= -1
    if buiscetglobe_y <= 0 or buiscetglobe_y >= 720 - 300:
        buiscetglobe_speed_y *= -1
    
    screen.blit(karenglobe_img, (karenglobe_x, karenglobe_y))
    screen.blit(buiscetglobe_img, (buiscetglobe_x, buiscetglobe_y))
    screen.blit(karen_img, (0, 0))
    font = pygame.font.SysFont("comicsansms", 48)
    time_str = datetime.now().strftime("%H:%M:%S")
    clock_surface = font.render(time_str, True, (255, 255, 255))
    screen.blit(clock_surface, (20, 20))
    pygame.display.flip()

pygame.quit()