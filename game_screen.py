import pygame
import random
from os import path

from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, RED, FPS, QUIT


# Carrega todos os assets uma vez só.
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
    assets["background"] = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
    assets["jump_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'jump_sound.wav'))

    return assets

assets = load_assets(img_dir, snd_dir)

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
        self.img_lib = []
        self.img_lib.append(assets["arrow_green_up_img"])
        self.img_lib.append(assets["arrow_green_down_img"])
        self.img_lib.append(assets["w_green_left_img"])
        self.img_lib.append(assets["w_green_right_img"])
        self.img_lib.append(assets["w_red_up_img"])
        self.img_lib.append(assets["w_red_down_img"])
        self.img_lib.append(assets["w_red_left_img"])
        self.img_lib.append(assets["w_red_right_img"])

        self.change_arrow()

    def change_arrow(self):
        arrow = random.randint(len(self.img_lib))
        self.image = pygame.transform.scale(self.img_lib[arrow], (50, 38))

        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        self.rect.x += self.speedx
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        



def game_screen(screen):
    assets = load_assets(img_dir, snd_dir, fnt_dir)

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    background_rect = background.get_rect()

    # Carrega os sons do jogo
    pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    jump_sound = assets["jump_sound"]

    # Cria o personagem. O construtor será chamado automaticamente.
    player = Player(assets["player_img"])

    # Carrega a fonte para desenhar o score.
    score_font = assets["score_font"]
'''
    # Loop principal.
    pygame.mixer.music.play(loops=-1)

    score = 0

    PLAYING = 0
    ERROR = 1
    DONE = 2

    state = PLAYING

    while state != DONE:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:




            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = ERROR
                
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Verifica se a tecla apertada corresponde à seta mostrada na tela.

                    if event.key == pygame.K_LEFT and arrow == img_lib["w_green_left_img"]


                    event.key == pygame.K_RIGHT


                        
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update() 

        TIME += 1     



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