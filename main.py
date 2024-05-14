import pygame
import random
from jogador import *
from obstaculos import *
from objetivos import *
pygame.init()
# Definir as cores
pontuacao = 5
tela = pygame.display.set_mode((800,500)) #Escolhendo o tamanho da tela

pygame.display.set_caption("Fruit Drops") #Alterando o nome do jogo
clock = pygame.time.Clock() #Limitando o FPS
tela.fill((255,0,0)) #escolhendo a cor de fundo do jogo

rodando = True #fazendo o jogo rodar infinitamente
mario = Player('mario.png',75,75,350,500)
lista_inimigos = [Obstaculos('casco.png',30,30,350,0,3),
                  Obstaculos('casco.png',30,30,500,0,2),
                  Obstaculos('casco.png',30,30,700,0,7),
                  Obstaculos('casco.png',30,30,200,0,6),
                  Obstaculos('casco.png',30,30,400,0,5),
                  Obstaculos('casco.png',30,30,100,0,4)]

lista_objetivos = [Objetivos('cogumelo.png',30,30,320,0,2),
                   Objetivos('cogumelo.png',30,30,250,0,8),
                   Objetivos('cogumelo.png',30,30,150,0,7),
                   Objetivos('cogumelo.png',30,30,60,0,6),
                   Objetivos('cogumelo.png',30,30,400,0,3),
                   Objetivos('cogumelo.png',30,30,450,0,2),
                   Objetivos('cogumelo.png',30,30,500,0,2),
                   Objetivos('cogumelo.png',30,30,650,0,2)]

while True:
    for evento in pygame.event.get():          
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((255,0,0))
    mario.movimento()
    mario.desenho(tela)
    for cogumelos in lista_objetivos:
        cogumelos.movimento_obj()
        cogumelos.desenho(tela)
        if mario.mascara.overlap(cogumelos.mascara,(cogumelos.pos_x-mario.pos_x , mario.pos_y-mario.pos_y)):
            pontuacao +=1
    for inimigos in lista_inimigos:
        inimigos.movimento_inimigo2()
        inimigos.desenho(tela)
        if mario.mascara.overlap(inimigos.mascara,(inimigos.pos_x-mario.pos_x , mario.pos_y-mario.pos_y)):
            pontuacao -= 1
    
   
    
    pygame.display.update()
    clock.tick(60)
    
