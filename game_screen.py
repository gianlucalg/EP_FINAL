import pygame
import random
from os import path

from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, RED, FPS, QUIT

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
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        
        # Velocidade da nave
        self.speedx = 0
        
    
    # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
                    
        
            
class Arrow(pygame.sprite.Sprite):

    def __init__(self, x, y, arrow_img):
        pygame.sprite.Sprite.__init__(self)

        #Escolhe imagem do ícone da seta que vai aparecer.
        self.image = arrow_green_img
        self.image = arrow_green_up_img
        self.image = arrow_green_down_img
        self.image = arrow_green_left_img
        self.image = arrow_green_right_img

        self.image = arrow_red_img
        self.image = arrow_red_up_img
        self.image = arrow_red_down_img
        self.image = arrow_red_left_img
        self.image = arrow_red_right_img

        #Define a posição em que as setas aparecerão.

        self.rect.x = 10
        self.rect.y = 5




# Carrega todos os assets uma vez só.
def load_assets(img_dir, snd_dir, fnt_dir):
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
    assets["background"] = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
    assets["jump_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'jump.wav'))