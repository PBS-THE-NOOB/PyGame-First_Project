import pygame

PLAYER_WIDTH = 96
PLAYER_HEIGHT = 100

class Player(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.Attack_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Attack ({i}).png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range(1,11)]
        self.Dead_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Dead ({i}).png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range(1,11)]
        self.Idle_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Idle ({i}).png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range(1,11)]
        self.Jump_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Jump ({i}).png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range(1,11)]
        self.Run_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Run ({i}).png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range(1,11)]
        self.Walk_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/Walk ({i}).png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range(1,11)]
        self.JumpAttack_Surf_List=[pygame.transform.scale(pygame.image.load(f'Player/JumpAttack ({i}).png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range(1,11)]
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
        self.state =  'idle'
        self.jump_velocity = -4
        self.gravity = 0.8
        self.player_x = -100
        self.player_y = 1000
        self.grounded = True

    def player_animate(self,player_state : str): #returns frames 
        self.animaion_index += 0.1
        if self.animaion_index >= len(self.animation_dict[player_state]) :
            self.animaion_index = 0
        return self.animation_dict[player_state][int(self.animaion_index)]

    def check_state(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and keys[pygame.K_SPACE]:
            self.state = 'jump_attack'
        elif keys[pygame.K_SPACE]:
            self.state = 'jump'
        elif keys[pygame.K_RETURN]:
            self.state = 'attack'
        elif keys[pygame.K_a] or keys[pygame.K_d]:
            self.state = 'walk'
        else:
            self.state = 'idle'
    
    def render_player(self,x,y):
        self.player_x = x
        self.check_state()
        self.player_jump(y) 
        player_surf = self.player_animate(self.state)
        player_rect = player_surf.get_rect(midbottom = (self.player_x,self.player_y))
        return player_surf,player_rect

    def player_jump(self,y_input : int):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.grounded:
            self.jump_velocity = -20
            self.grounded = False

        if not self.grounded:
            self.jump_velocity += self.gravity
            self.player_y += self.jump_velocity
            
        if self.player_y >= y_input :
            self.player_y = y_input
            self.grounded = True


        return self.player_y