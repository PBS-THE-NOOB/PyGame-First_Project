import pygame
from sys import exit

class MainMenu():

    def __init__(self):
        self.background = pygame.transform.scale((pygame.image.load('Background/MainMenu_Background.png')),(800,400))
        self.text_font=pygame.font.Font(None,50)
        self.menu_terms=self.get_text()
    def draw(self,screen):
        screen.blit(self.background,(0,0))
        for surf , rect in self.menu_terms:
            screen.blit(surf,rect)
        
    def get_text(self):
        self.menu=["PLAY GAME", "VIEW STATS", "GO TO SHOP", "QUIT"]
        self.menu_items=[]
        for i, j in enumerate(self.menu):
            surf=self.text_font.render(j,0,(64,64,64))
            rect=surf.get_rect(midbottom=(400,50*(i+1)+60))
            self.menu_items.append((surf,rect))
        return self.menu_items

    def event_handeling(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1: 
                for i,(surf,rect) in enumerate(self.menu_terms):
                    if rect.collidepoint(event.pos):
                        if i == 0:
                            pass
                        elif i == 1:
                            pass
                        elif i == 2:
                            pass
                        elif i == 3:
                            pygame.quit()
                            exit()
    
                



