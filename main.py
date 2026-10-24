import pygame
from sys import exit
import mainmenu 

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Adventure Game')
clock=pygame.time.Clock()
menu=mainmenu.MainMenu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    menu.draw(screen)
    pygame.display.update()
    clock.tick(60)
