import pygame

class World():
    def __init__(self):

        self.background = pygame.transform.scale(pygame.image.load('Background/Game_Bg/BackGround.png').convert(),(800, 400))

        self.cloud = pygame.image.load('Background/Game_Bg/cloud.png').convert_alpha()
        self.cloud_rect = self.cloud.get_rect()

        self.mountain = pygame.transform.scale(pygame.image.load('Background/Game_Bg/mountain.png').convert_alpha(),(800,300))
        self.mountain_rect = self.mountain.get_rect(bottomleft = (0,400))

        self.far_trees = pygame.image.load('Background/Game_Bg/FarTrees.png').convert_alpha()
        self.far_trees_rect = self.far_trees.get_rect()

        self.middle_trees = pygame.image.load('Background/Game_Bg/MiddleTrees.png').convert_alpha()
        self.middle_trees_rect = self.middle_trees.get_rect()

        self.near_trees = pygame.image.load('Background/Game_Bg/NearTrees.png').convert_alpha()
        self.near_trees_rect = self.near_trees.get_rect()

        self.ground = pygame.transform.scale(pygame.image.load('Background/Game_Bg/Ground.png').convert_alpha(),(800,200))
        self.ground_rect = self.ground.get_rect(bottomleft = (0,400))

        self.fore_ground = pygame.image.load('Background/Game_Bg/ForeGround.png').convert_alpha()
        self.fore_ground_rect = self.fore_ground.get_rect()

        self.front_bushes = pygame.image.load('Background/Game_Bg/FrontBushes.png').convert_alpha()
        self.front_bushes_rect = self.front_bushes.get_rect()

        self.layer_positions = {
            #name : [x coordinate , movement speed]
            'cloud': [0.0, 0.2],
            'mountain': [0.0, 0.4],
            'far_trees': [0.0, 0.6],
            'middle_trees': [0.0, 0.8],
            'near_trees': [0.0, 1.2],
            'ground': [0.0, 1.5],
            'fore_ground': [0.0, 2.0],
            'front_bushes': [0.0, 2.5]
            }
        
        self.background_x = 0

    def show_world(self,screen):
        screen.blit(self.background,(self.background_x,0))
        direction = self.handel_movement_inputs()
        self.movement(self.mountain,self.mountain_rect,screen,'mountain',False,direction)
        self.movement(self.ground,self.ground_rect,screen,'ground',False,direction)
        # cloud moves continuously
        self.movement(self.cloud,self.cloud_rect,screen,'cloud',True)

    def movement(self,surf,rect,screen,layer : str, continuous : bool ,direction = 0) :
        if continuous : 
            self.layer_positions[layer][0] += self.layer_positions[layer][1]
            if self.layer_positions[layer][0] > 900 : 
                self.layer_positions[layer][0] = -rect.width
        else : 
            self.layer_positions[layer][0] += (self.layer_positions[layer][1]) * direction
        
        rect.x = int(self.layer_positions[layer][0])
        screen.blit(surf,rect)

    def handel_movement_inputs(self):

        event =pygame.key.get_pressed()
        if event[pygame.K_a]:
            return -1
        elif event[pygame.K_d]:
            return 1
        return 0
