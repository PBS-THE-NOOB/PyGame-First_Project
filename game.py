import pygame

class Game():
    def __init__(self):
        self.Entering_surf_list=[ pygame.transform.scale(pygame.image.load(f'Background/Entering_Background/frame{i:04}.png').convert(),(800,400)) for i in range(143)]
        self.Entering_Surf_Intex=1
        self.Entering_Surf=self.Entering_surf_list[self.Entering_Surf_Intex]

    def Entering_animation(self,screen):
        self.Entering_Surf_Intex += 0.2
        if self.Entering_Surf_Intex>=len(self.Entering_surf_list):
            self.Entering_Surf_Intex = 1
        self.Entering_Surf = self.Entering_surf_list[int(self.Entering_Surf_Intex)]
        screen.blit(self.Entering_Surf,(0,0))