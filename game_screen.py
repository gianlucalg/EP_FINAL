import pygame
#import random
#from main_game import screen
from os import path
from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, RED, FPS, QUIT
pygame.init()


# Carrega todos os assets uma vez só.
def load_assets():
    assets = {}
    assets["player_img"] = pygame.image.load(path.join(img_dir, "player.png")).convert()
    assets["arrow_green_up_img"] = pygame.image.load(path.join(img_dir, "arrow_green_up.png")).convert()
    assets["arrow_green_down_img"] = pygame.image.load(path.join(img_dir, "arrow_green_down.png")).convert()
    assets["arrow_green_left_img"] = pygame.image.load(path.join(img_dir, "arrow_green_left.png")).convert()
    assets["arrow_green_right_img"] = pygame.image.load(path.join(img_dir, "arrow_green_right.png")).convert()
    assets["arrow_red_up_img"] = pygame.image.load(path.join(img_dir, "arrow_red_up.png")).convert()
    assets["arrow_red_down_img"] = pygame.image.load(path.join(img_dir, "arrow_red_down.png")).convert()
    assets["arrow_red_left_img"] = pygame.image.load(path.join(img_dir, "arrow_red_left.png")).convert()
    assets["arrow_red_right_img"] = pygame.image.load(path.join(img_dir, "arrow_red_right.png")).convert()
    assets["background"] = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    #assets["jump_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'jump_sound.wav')).convert()

    return assets



# Classe Jogador que representa o personagem
class Player(pygame.sprite.Sprite):

    def __init__(self, player_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH -8
        self.rect.bottom = HEIGHT / 2
        
        # Velocidade da nave
        self.speedx = 0
        

                    
            
class Arrow(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        #Atributo da classe arrow.
        self.direction = " "

        #Escolhe imagem do ícone da seta que vai aparecer.
        self.image = pygame.transform.scale(img, (50, 38))

        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2 - 10
        
        
class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/background.png').convert()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.x, self.y   
    
    def update(self,cam):
        self.rect.left = self.y + (0.2*cam.state.left)
        self.rect.top = self.x + (0.2*cam.state.top)
        


        


      



