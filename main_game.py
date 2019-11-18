import pygame
from pygame.locals import *
import sys
import os
from os import path
from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, FPS, QUIT, BLACK
from game_screen import load_assets
from game_screen import Arrow, Player
import random


pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init()


#Fazer o background mexer
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        

arrows_list = ["arrow_green_up_img","arrow_green_down_img","arrow_green_left_img","arrow_green_right_img","arrow_red_up_img","arrow_red_down_img","arrow_red_left_img","arrow_red_right_img"]


'''        
#Definir o display
    
#W, H = 576, 1024
#HW, HH = W / 2, H / 2
#AREA = W * H

#copiei essa linha de um vid n sei oq faz xD
#os.environ["n sei"] = "50,50"

#SET DO PYGAME
#personagem = pygame.image.load("img/a.png")
#pygame.init()
#CLOCK = pygame.time.Clock()
#DS = pygame.display.set_mode((W, H))
#pygame.display.set_caption("NOME DO JOGO")
#x = 0

#main loop
while True:
    events()
    
    rel_x = x % bg.get_rect().width
    DS.blit(bg, (0, rel_x - bg.get_rect().width))
    DS.blit(personagem, (0,100))
    if rel_x < W:
        DS.blit(bg, (0,rel_x))
    
    x += 2
    
    pygame.display.update()
    CLOCK.tick(FPS)
    
'''

def game_screen(screen):
    assets = load_assets(img_dir, snd_dir, fnt_dir)

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    background_rect = background.get_rect()

    # Cria o personagem. O construtor será chamado automaticamente.
    player = Player(assets["player_img"])

    directions = ['arrow_red_up_img', 'arrow_red_down_img', 'arrow_red_left_img', 'arrow_red_right_img', 'arrow_green_up_img', 'arrow_green_down_img', 'arrow_green_left_img', 'arrow_green_right_img']

    PLAYING = 0
    ERROR = 1
    DONE = 2
    TIME = 0

    state = PLAYING
    
    all_arrows = pygame.sprite.Group()

    while state != DONE:
        
        print(TIME)
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botão, etc).
            
            # a cada segundo, cria uma arrow.
            if TIME % 1*FPS == 0:
                                
                img = assets[random.choice(directions)]               
                
                arrow = Arrow(img)  
                all_arrows.add(arrow)
                
                TIME = 0
                
        TIME+=1
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        pygame.display.flip()
        
        
            
      #all_arrows.draw(screen)
        
game_screen(screen)
            
#            for event in pygame.event.get():
#                
#                # Verifica se foi fechado.
#                if event.type == pygame.QUIT:
#                    state = ERROR
#                
#                
#            
#                
#                # Verifica se apertou alguma tecla.
#                if event.type == pygame.KEYDOWN:
#                    
#
#                
#
#        # A cada loop, redesenha o fundo e os sprites
#        screen.fill(BLACK)
#        screen.blit(background, background_rect)
#    
#        # Desenha o score
#        text_surface = score_font.render("{:08d}".format(score), True, YELLOW)
#        text_rect = text_surface.get_rect()
#        text_rect.midtop = (WIDTH / 2,  10)
#        screen.blit(text_surface, text_rect)
#    
#        # Desenha as vidas
#        text_surface = score_font.render(chr(9829) * lives, True, RED)
#        text_rect = text_surface.get_rect()
#        text_rect.bottomleft = (10, HEIGHT - 10)
#        screen.blit(text_surface, text_rect)
#        
#        # Depois de desenhar tudo, inverte o display.
#        pygame.display.flip()
#    
#    return QUIT
