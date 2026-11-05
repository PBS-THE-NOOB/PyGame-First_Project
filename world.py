import pygame

class World():
    def __init__(self):
        self.background = pygame.transform.scale(pygame.image.load('Background/Game_Bg/BackGround.png'),(800,400))
        self.cloud = pygame.image.load('Background/Game_Bg/cloud.png')
        self.mountain = pygame.image.load('Background/Game_Bg/mountain.png')
        self.far_trees = pygame.image.load('Background/Game_Bg/FarTrees.png')
        self.middle_trees = pygame.image.load('Background/Game_Bg/MiddleTrees.png')
        self.near_trees = pygame.image.load('Background/Game_Bg/NearTrees.png')
        self.ground = pygame.image.load('Background/Game_Bg/Ground.png')
        self.fore_ground = pygame.image.load('Background/Game_Bg/ForeGround.png')
        self.front_bushes = pygame.image.load('Background/Game_Bg/FrontBushes.png')
        self.background_x = 0
        self.scrool_speed = 3

    def show_world(self,screen):
        screen.blit(self.background,(self.background_x,0))