import pygame
from player import Player



class Game():
    def __init__(self):
        self.Entering_surf_list=[ pygame.transform.scale(pygame.image.load(f'Background/Entering_Background/frame{i:04}.png').convert(),(800,400)) for i in range(143)]
        self.Entering_Surf_Intex=0
        self.Entering_Surf=self.Entering_surf_list[self.Entering_Surf_Intex]
        self.Game_Enter_Background=pygame.transform.scale(pygame.image.load('Background/Game_Enter_Background.png').convert(),(800,400))
        self.player=Player()
        self.text_box_background = pygame.image.load('Background/Text_Box.png').convert()
        self.text_font=pygame.font.Font('Fonts/Menu_Font/MedievalSharp-Regular.ttf',30)
        self.Dialogue_Finished = False
        self.Counter_Variable= 0
        self.temporary_counter= 0

    def game_event(self,event):
        if self.Dialogue_Finished : 
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                self.temporary_counter = int(self.Counter_Variable)
                self.Dialogue_Finished = False

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
        self.load_text_box(screen)
        screen.blit(Idle_player,Idle_player_rect)
        self.typing_animation('Hello Player!',screen,(100,330))
        
    
    def load_text_box(self,screen):
        text_box_surf = pygame.transform.scale(self.text_box_background,(800,80))
        text_box_rect = text_box_surf.get_rect(bottomleft = (0,390))
        screen.blit (text_box_surf,text_box_rect)

    def typing_animation(self,text:str, screen, top_left_location :tuple):
            
        text_state = text[self.temporary_counter:int(self.Counter_Variable)]
        text_surf = self.text_font.render(text_state, 0, 'White')
        if text_surf.get_width() < 650 and self.Counter_Variable < len(text):
            self.Counter_Variable += 0.2
        else :
            self.Dialogue_Finished = True
        text_rect = text_surf.get_rect(topleft=top_left_location)
        screen.blit(text_surf, text_rect)
    
            