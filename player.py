import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.Attack_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Attack ({i}).png').convert_alpha(),(96,128)) for i in range(1,11)]
        self.Dead_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Dead ({i}).png').convert_alpha(),(96,128)) for i in range(1,11)]
        self.Idle_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Idle ({i}).png').convert_alpha(),(96,128)) for i in range(1,11)]
        self.Jump_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Jump ({i}).png').convert_alpha(),(96,128)) for i in range(1,11)]
        self.Run_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Run ({i}).png').convert_alpha(),(96,128)) for i in range(1,11)]
        self.Walk_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Walk ({i}).png').convert_alpha(),(96,128)) for i in range(1,11)]
        self.JumpAttack_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/JumpAttack ({i}).png').convert_alpha(),(96,128)) for i in range(1,11)]
        self.animation_dict={
            'attack' : self.Attack_Surf_List,
            'dead' : self.Dead_Surf_List , 
            'idle': self.Idle_Surf_List,
            'jump': self.Jump_Surf_List,
            'run': self.Run_Surf_List,
            'walk': self.Walk_Surf_List,
            'jump_attack': self.JumpAttack_Surf_List
        }
        self.animaion_index = 0

    def player_animate(self,player_state): #returns frames 
        self.animaion_index += 0.1
        if self.animaion_index >= len(self.animation_dict[player_state]) :
            self.animaion_index = 0
        return self.animation_dict[player_state][int(self.animaion_index)]

        

