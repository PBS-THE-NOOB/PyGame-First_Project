import pygame
from sys import exit
import mainmenu 
from game import Game

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Adventure Game')
clock=pygame.time.Clock()
menu=mainmenu.MainMenu()
game = Game(screen)
state = 'game_starts'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if state == 'menu':
            val = (menu.event_handeling(event))
            if val == 'play': state = 'intro'

        elif state == 'game_starts':
            game.game_event(event)
            
    if state == 'menu':
        menu.draw(screen)

    elif state == 'intro':
        state = game.Entering_animation()

    elif state == 'game_starts':
        state = game.game_begin()

    elif state == 'game_play' :
        game.game_play()

    pygame.display.update()
    clock.tick(60)
