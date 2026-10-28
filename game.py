import pygame
from player import Player



class Game():
    def __init__(self):
        self.Entering_surf_list=[ pygame.transform.scale(pygame.image.load(f'Background/Entering_Background/frame{i:04}.png').convert(),(800,400)) for i in range(143)]
        self.Entering_Surf_Intex=0
        self.Entering_Surf=self.Entering_surf_list[self.Entering_Surf_Intex]
        self.Game_Enter_Background=pygame.transform.scale(pygame.image.load('Background/Game_Enter_Background.png').convert(),(800,400))
        self.player=Player()
    def Entering_animation(self,screen):
        self.Entering_Surf_Intex += 0.6
        if self.Entering_Surf_Intex>=len(self.Entering_surf_list):
            return 'game_starts'
        self.Entering_Surf = self.Entering_surf_list[int(self.Entering_Surf_Intex)]
        screen.blit(self.Entering_Surf,(0,0))
        return 'intro'

    def game_begin(self,screen):
        screen.blit(self.Game_Enter_Background,(0,0))
        Idle_player =  self.player.player_animate('idle')
        Idle_player_rect = Idle_player.get_rect(bottomleft = (0,400))
        screen.blit(Idle_player,Idle_player_rect)