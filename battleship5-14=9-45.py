####GALAGA######

import pygame, sys, os, pygame.mixer
from pygame.locals import *


pygame.init() #initialize
display_width = 1200
display_height = 800
size = [display_width , display_height] #screen size
screen = pygame.display.set_mode(size)

pygame.display.set_caption('BATTLESHIP')

done = False
clock = pygame.time.Clock()

_image_library = {} 
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

#colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
LIGHTBLUE = (135, 206, 250)
x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
ship_speed = 0
file = 'modelo.ogg'
def ship(x,y):
    screen.blit(get_image('ship.png'), (x, y))
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(loops = -1, start = 8.0)

bullets = []

bulletpicture = pygame.image.load("laser.png").convert_alpha()
bulletpicture = pygame.transform.scale(bulletpicture, (64, 64))
shot = pygame.mixer.Sound("laser.wav")
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_SPACE:
                shot.play()
                bullets.append([x+50, y-16])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        
    clock.tick(60)    
    x += x_change    
    screen.fill(LIGHTBLUE)
    ship(x,y)

    for b in range(len(bullets)):
        bullets[b][1] -= 10

    # Iterate over a slice copy if you want to mutate a list.
    for bullet in bullets[:]:
        if bullet[0] < 0:
            bullets.remove(bullet)

    for bullet in bullets:
        screen.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))
    
    pygame.display.flip()

pygame.quit()#finish
quit()
