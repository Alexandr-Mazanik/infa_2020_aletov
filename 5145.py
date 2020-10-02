import pygame
from pygame.draw import *
from random import randint

pygame.init()

white = (255, 255, 255)
gray = (210, 210, 210)
red = (220, 20, 20)
yellow = (255, 255, 0)
black = (0, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
light_blue = (0, 0, 120)
brown = (200, 120, 200)
dark_green = (50, 255, 50)

FPS = 30
xsize, ysize = 1000, 800
screen = pygame.display.set_mode((xsize, ysize))
screen.fill(gray)

def bkground(screen, color1, color2, y):
    rect(screen, color1,(0, y, xsize, ysize))
    rect(screen, color2, (0, 0, xsize, y))


def circles_sheet(screen,
                  x, y, height, R,
                  color_sheet):
    y0 = y - height
    circle(screen, color_sheet, (x0, y0 - R), R)
    circle(screen, color_sheet, (x0, y0 + R), R)
    

def house(screen,
          x, y,
          width, height,
          color_house, color_roof, color_window):
    x0 = x - int(width / 2)
    y0 = y - int(height / 2)
    wind_width = int(width / 2)
    wind_height = int(height / 3)
    x0_wind = x - int(wind_width / 2)
    y0_wind = y - int(height / 4)
    rect(screen, color_house, (x0, y0,
                               width, height))
    polygon(screen, color_roof, [(x0, y0), (x, y - height), (x0 + width, y0)])
    rect(screen, color_window, (x0_wind, y0_wind, wind_width, wind_height))


def tree(screen,
         x, y,
         width, height,
         color_tree, color_sheet):
    x0 = x - int(width / 2)
    y0 = y - height
    rect(screen, color_tree, (x0, y0, width, height))
    R = 60
    circle(screen, color_sheet, (x, y0 - R), R)
    circle(screen, color_sheet, (x - width, y0 - 25), R)
    circle(screen, color_sheet, (x - width, y0 - 2 * R), R)
    circle(screen, color_sheet, (x + width, y0 - 25), R)
    circle(screen, color_sheet, (x + width, y0 - 2 * R), R)
    circle(screen, color_sheet, (x, y0 - 3 * R), R)


def clouds(screen,
           x, y,
           color_cloud):
    R = 50
    for i in range(0, 10):
        x0 = randint(x - R, x + R)
        y0 = randint(y - R, y + R)
        circle(screen, color_cloud, (x0, y0), R)

    
bkground(screen, green, blue, 400)
house(screen, 250, 600, 275, 225, brown, red, light_blue)
tree(screen, 550, 750, 50, 150, black, dark_green)
clouds(screen, 500, 200, white)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()