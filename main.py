import pygame
from sys import exit
import mainmenu 
import game

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Adventure Game')
clock=pygame.time.Clock()
menu=mainmenu.MainMenu()
game = game.Game()
state = 'menu'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if state == 'menu':
            val = (menu.event_handeling(event))
            if val == 'play': state = 'intro'
    if state == 'menu':
        menu.draw(screen)
    elif state == 'intro':
        state=game.Entering_animation(screen)
    elif state == 'game_starts':
        game.game_begin(screen)
    pygame.display.update()
    clock.tick(60)
