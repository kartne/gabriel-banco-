import pygame
import os

# Inicilizando o Pygame 
pygame.init()

# Definindo o tamanho da janela
WIDTH,  HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set-caption("Janela simples")

# Definido a cor de fundo
BG_COLOR = (30, 30, 40) # cor de fundo (um tom escuro)

#carregar a imagem
image_file ="player.png" #coloque sua imagem aqui
if os.path.exists(image_file):
    img+pygame.image.load(image_file).convert_alpha() #carregar a imagem
    img_rect = 



#Loop principal do jogo
runnig = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    pygame.display.flip

#Finalizar o Pygame
pygame.quit()
