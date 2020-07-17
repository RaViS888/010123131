import pygame, sys, random
from pygame.locals import *


pygame.init()

width=800
height=600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Bouncing')


# Set our color constants

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Circle():
    def __init__(self):
        self.circle_surface = screen
        self.circle_radius = random.randint(10,20)
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.r = random.randint(10,20)
        self.R = random.randint(0,255)
        self.G = random.randint(0,255)
        self.B = random.randint(0,255)
        self.circle_color = (self.R,self.G,self.B)
        self.circle_pos = (self.x, self.y)  ###position
        self.circle_width = 0

    def character(self):
        self.circle_character = pygame.draw.circle(self.circle_surface, self.circle_color,
         self.circle_pos, self.circle_radius, self.circle_width)





speed = [1, 0]


# Game loop

while True:

    # Handle events

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


    # Update game state

    box = Circle.character.move(speed)


    if box.right >= DISPLAYSURF.get_width() or box.left <= 0:

        speed[0] = -speed[0]


    # Draw screen

    DISPLAYSURF.fill(BLACK)

    pygame.draw.circle(DISPLAYSURF, WHITE, (0,0),20)

    pygame.display.update()
