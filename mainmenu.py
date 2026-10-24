import pygame

class MainMenu():

    def __init__(self):
        self.background = pygame.transform.scale((pygame.image.load('Background/MainMenu_Background.png')),(800,400))

    def draw(self,screen):
        screen.blit(self.background,(0,0))

    def event_handeling(self,event):
        pass



