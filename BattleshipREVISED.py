import pygame
import pygame, sys, os, pygame.mixer
from pygame.locals import *
# -- Global constants
 
# Colors
pygame.init() #initialize
display_width = 1200
display_height = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
LIGHTBLUE = (135, 206, 250)
x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
ship_speed = 0
file = 'modelo.ogg'
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
_image_library = {} 
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image


def ship (x,y):
        screen.blit(get_image('ship.png'), (x, y))
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(loops = -1, start = 8.0)
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, .1, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
ship(50,50)
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False
 
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5

                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    clock.tick(60)            
    x += x_change            
    ship(x,y)
    all_sprite_list.update()
         
    screen.fill(LIGHTBLUE)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
quit()
