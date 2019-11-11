import pygame
from pygame.locals import *
import sys
import os
from os import path
from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, FPS, QUIT

#Fazer o background mexer
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
            
            
def load_assets(img_dir, snd_dir):
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
    assets["background_img"] = pygame.image.load(path.join(img_dir,"background.png")).convert()
    
    return assets

assets = load_assets(img_dir, snd_dir)

arrows_list = ["arrow_green_up_img","arrow_green_down_img","arrow_green_left_img","arrow_green_right_img","arrow_red_up_img","arrow_red_down_img","arrow_red_left_img","arrow_red_right
_img"]


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

    # Carrega os sons do jogo
#   pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
#   pygame.mixer.music.set_volume(0.4)
    #jump_sound = assets["jump_sound"]

    # Cria o personagem. O construtor será chamado automaticamente.
    player = Player(assets["player_img"])


    # Loop principal.
    #pygame.mixer.music.play(loops=-1)

    #score = 0

    PLAYING = 0
    ERROR = 1
    DONE = 2
    TIME = 0

    state = PLAYING

    while state != DONE:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botão, etc).
            
          
            if TIME % 1*FPS == 0:
                arrow = Arrow(pygame.sprite.Sprite)           
            
            
            for event in pygame.event.get():
                
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = ERROR
                
                
            
                
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Verifica se a tecla apertada corresponde à seta mostrada na tela.

                    if event.key == pygame.K_LEFT and arrow == 


                    event.key == pygame.K_RIGHT
                    
                    
            


                        
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()     


                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(hit.rect.center, assets["explosion_anim"])
                all_sprites.add(explosao)

                # Ganhou pontos!
                score += 100
            
            # Verifica se houve colisão entre nave e me

            
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Player(assets["player_img"])
                    all_sprites.add(player)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)

        # Desenha o score
        text_surface = score_font.render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)

        # Desenha as vidas
        text_surface = score_font.render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        screen.blit(text_surface, text_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return QUIT