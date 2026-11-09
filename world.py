import pygame
import random
from player import Player,PLAYER_HEIGHT,PLAYER_WIDTH
GROUND_Y=400
GROUND_WIDTH = 300
TOP_GROUND = 370

class World():
    def __init__(self):
        self.Player = Player()
        self.player_x = 400
        self.x_pos = 400.0
        self.background = pygame.transform.scale(pygame.image.load('Background/Game_Bg/BackGround.png').convert(),(800, 400))

        self.Cloud_List = [self.scale(pygame.image.load(f'Background/Game_Bg/Cloud/clouds_{i}.png').convert_alpha(),100) for i in range(1,5)]
        self.current_cloud = random.choice(self.Cloud_List)
        self.current_cloud_rect = self.current_cloud.get_rect(topleft = (0,0))

        self.mountain = pygame.transform.scale(pygame.image.load('Background/Game_Bg/mountain.png').convert_alpha(),(800,400))
        self.mountain_rect = self.mountain.get_rect(bottomleft = (0,400))

        self.far_trees = self.scale(pygame.image.load('Background/Game_Bg/FarTrees.png').convert_alpha(),180)
        self.far_trees_rect = self.far_trees.get_rect(bottomleft=(0, 400))

        self.middle_trees = self.scale(pygame.image.load('Background/Game_Bg/MiddleTrees.png').convert_alpha(),200)
        self.middle_trees_rect = self.middle_trees.get_rect(bottomleft=(0, 400))

        self.near_trees = self.scale(pygame.image.load('Background/Game_Bg/Near_Trees.png').convert_alpha(),250)
        self.near_trees_rect = self.near_trees.get_rect(bottomleft=(0, 400))

        self.ground = pygame.transform.scale(pygame.image.load('Background/Game_Bg/Ground.png').convert_alpha(),(800,GROUND_WIDTH))
        self.ground_rect = self.ground.get_rect(bottomleft = (0,GROUND_Y))

        self.front_bushes = self.scale(pygame.image.load('Background/Game_Bg/FrontBushes.png').convert_alpha(),200)
        self.front_bushes_rect = self.front_bushes.get_rect(bottomleft = (0,GROUND_Y))

        self.layer_positions = {
            #name : [x coordinate , movement speed]
            'cloud': [0.0, 0.2],
            'mountain': [0.0, 0.4],
            'far_trees': [0.0, 0.6],
            'middle_trees': [0.0, 0.8],
            'near_trees': [0.0, 1.2],
            'ground': [0.0, 1.5],
            'fore_ground': [0.0, 1.6],
            'front_bushes': [0.0, 1.2]
            }
        
        self.background_x = 0

    def show_world(self,screen,half:str):
        direction = self.handel_movement_inputs()
        player_surf,player_rect,scrool = self.camera()
        if half == 'first' :
            screen.blit(self.background,(self.background_x,0))
            self.discontinuos_movement(self.mountain,self.mountain_rect,screen,'mountain',direction,scrool)
            self.cloud_movement(screen)
            self.discontinuos_movement(self.far_trees,self.far_trees_rect,screen,'far_trees',direction,scrool)
            self.discontinuos_movement(self.middle_trees,self.middle_trees_rect,screen,'middle_trees',direction,scrool)
            self.discontinuos_movement(self.near_trees,self.near_trees_rect,screen,'near_trees',direction,scrool)
            self.discontinuos_movement(self.front_bushes,self.front_bushes_rect,screen,'front_bushes',direction,scrool)
        elif half == 'second' :
            self.player_movement(player_surf,player_rect,screen,direction)
            self.discontinuos_movement(self.ground,self.ground_rect,screen,'ground',direction,scrool)

    def discontinuos_movement(self,surf,rect,screen,layer : str,direction,scrool : bool) :
            if scrool:
                self.layer_positions[layer][0] += (self.layer_positions[layer][1]) * direction

                if self.layer_positions[layer][0] >= rect.width :
                    self.layer_positions[layer][0] -= rect.width
                elif self.layer_positions[layer][0] <= -rect.width :
                    self.layer_positions[layer][0] += rect.width

            rect.x = int(self.layer_positions[layer][0])

            for i in range (-1,screen.get_width()//rect.width +2):
                screen.blit(surf , (rect.x + rect.width * i ,rect.y))
        
    def player_movement(self,surf,rect,screen,direction):
        if (self.player_x >=500-PLAYER_WIDTH and direction == -1) or (self.player_x<=300 and direction == 1) :self.player_x += 0
        else : self.x_pos -= 1.2 * direction
        self.player_x = int(self.x_pos)
        screen.blit(surf,rect)

    def cloud_movement(self,screen):
        if self.current_cloud_rect.left > screen.get_width()+100 : 
            self.current_cloud = random.choice(self.Cloud_List)
            self.current_cloud_rect = self.current_cloud.get_rect(topleft = (0,0))
            self.current_cloud_rect.left= -self.current_cloud_rect.width
        else  : self.current_cloud_rect.x += 0.5
        screen.blit(self.current_cloud,self.current_cloud_rect)

    def camera(self):
        player_surf , player_rect = self.Player.render_player(self.player_x,TOP_GROUND)
        scrool = False
        if player_rect.right >=500 or player_rect.left <= 300 :scrool = True
        return player_surf , player_rect , scrool
    
    def scale(self, image, height):
        original_width, original_height = image.get_size()
        new_width = int(original_width * (height / original_height))
        return pygame.transform.scale(image, (new_width, height))

    def handel_movement_inputs(self):

        event =pygame.key.get_pressed()
        if event[pygame.K_a]:
            return +1
        elif event[pygame.K_d]:
            return -1
        return 0
