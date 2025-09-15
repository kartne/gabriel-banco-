import pygame
import os

#Inicializando o Pygame
pygame.init()

#Definindo o tamanho da janela padrão
WIDTH, HEIGHT 800, 600
screen pygame.display.set_node((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Hover Imagem com setas")

#Definindo a cor de fundo
BG_COLOR = (193, 6, 40) # cor de fundo (un tom escuro)

#Carregar a imagen
image_file "GAME\\player.png" Coloque o nome correto da sua imagem
if: os.path.exists(image_file):
  img pygame.image.load(image_file).convert_alpha()
  img rect img.get_rect(center(WIDTH // 2, HEIGHT // 2)) # Central
else:
  print("Imagem não encontrada!")
  
velocidade de movimento
SPEED = 1 #pixels por movimento

#Função para centralizar a imagen conforme o tamanho da tela
def centralize_image():
global ing_rect, WIDTH, HEIGHT
img_rect.center = (WIDTH // 2, HEIGHT // 2) # Centraliza a imagem no centro da tela
Variáveis para controle de redimensionamento
last width, last_height = WIDTH, HEIGHT
# Limite de novimento para que o personagem não saia da tela
def limit_movement():
global ing rect, WIDTH, HEIGHT
#Limita a posição da imagem para não sair da tela
if img rect.left < 0:
ing_rect.left-
if img rect.right > WIDTH:
ing rect.right = WIDTH
if img rect.top < 0:
ing rect.top
if img_rect.bottom> HEIGHT:
ing rect.bottom = HEIGHT
Loop principal do jogo
running = True
while running:
for event in pygame.event.get():
if event.type pygame.QUIT:
running = False
