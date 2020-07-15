#6101012620130_Assignment1
import pygame
import random
import math

pygame.init()

width, height = 800,600
Ncircle=10

background_colour = (255,255,255)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('07/15/2020_Assign1')
screen.fill(background_colour)

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
        self.circle_character = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

c = []
for i in range(Ncircle):
    c.append('c'+str(i))
    c[i] = Circle()
    shouldprint = True
    for j in range(len(c)):
        if i != j:
            dist = int(math.hypot(c[i].x - c[j].x, c[i].y - c[j].y))
            if dist < int(c[i].r*2):
                shouldprint = False
    if shouldprint:
        c[i].character()
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if self.circle_surface.get_rect().collidepoint(x, y):
                print('clicked on image')
#loop over, quite pygame
pygame.quit()
