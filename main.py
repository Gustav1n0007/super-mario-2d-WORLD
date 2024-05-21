import pygame
import random
from jogador import *
from obstaculos import *
from objetivos import *
import time
import os
pygame.init()
# Definir as cores
pontuacao = 0 #Pontuacao do jogo
vidas = 5 #Vidas do jogo
tela = pygame.display.set_mode((800,500)) #Escolhendo o tamanho da tela

pygame.display.set_caption("Fruit Drops") #Alterando o nome do jogo
clock = pygame.time.Clock() #Limitando o FPS
tela.fill((255,0,0)) #escolhendo a cor de fundo do jogo
#Configurando a fonte
fonte = pygame.font.SysFont('Berlin sans FB Demi',36)
fonte2 = pygame.font.SysFont('Berlin sans FB Demi',18)
# Definição do diretório onde está a música

# Carregamento da música
pygame.mixer.music.load('musica.mp3')
# Reprodução da música em loop (-1 para loop infinito)
pygame.mixer.music.play(-1) 

rodando = True #fazendo o jogo rodar infinitamente
mario = Player('mario.png',70,70,350,500) #criando o personagem principal
luigi = Player('luigi.png',65,75,450,500)
lista_inimigos = [Obstaculos('casco.png',40,45,0), #LISTA COM OS inimigos
                  Obstaculos('casco.png',40,45,0),
                  Obstaculos('casco.png',40,45,0),
                  Obstaculos('casco.png',40,45,0), #LISTA COM OS inimigos
                  Obstaculos('casco.png',40,45,0),]

lista_objetivos = [Objetivos('cogumelo.png',40,45,0), #Lista com os objetivos   
                   Objetivos('cogumelo.png',40,45,0),
                   Objetivos('cogumelo.png',40,45,0),
                   Objetivos('cogumelo.png',40,45,0),]

lista_bonus = [Objetivos('cogumelo_verde.png',40,45,0),] #Lista com os objetivos extras
fundo = Fundo('fundoMario.jpg',500,800,0,0) #Fundo do jogo
marioWin = Fundo('marioWIn.png',400,170,100,100) #Caso você venca
luigi_aparece = False
while rodando:
    for evento in pygame.event.get():          
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                luigi_aparece = True
                vidas += 5
    tela.fill((255,0,0)) #pintando a tela
    fundo.desenho(tela) #Colocando o fundo como fundo
    mario.movimento() #funcao para o movimento do mario
    mario.desenho(tela) #funcao para o mario aparecer
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    if luigi_aparece == False:
        pass
    if luigi_aparece == True:
        luigi.desenho(tela)
        luigi.movimento2()
    for cogumelos_verde in lista_bonus: #Loop para jogar os itens
        cogumelos_verde.movimento_obj() #movimento dos itens
        cogumelos_verde.desenho(tela) #para os itens aparecerem na tela
        if cogumelos_verde.pos_y > 500: #quando chegar no fim
           cogumelos_verde.pos_x = random.randint(50,750)  #voltar numa posicao aleatoria
           cogumelos_verde.velocidade = random.randint(4,8) #Com velocidade aleatoria
        if mario.mascara.overlap(cogumelos_verde.mascara,(cogumelos_verde.pos_x-mario.pos_x , mario.pos_y-cogumelos_verde.pos_y)): #Colisao        
            cogumelos_verde.pos_x = random.randint(50,750)  #voltar numa posicao aleatoria
            cogumelos_verde.velocidade = random.randint(4,8) #Com velocidade aleatoria
            pontuacao +=3 #Pontuacao caso acerte o item
            cogumelos.pos_y=0
        if luigi.mascara.overlap(cogumelos_verde.mascara,(cogumelos_verde.pos_x-luigi.pos_x , luigi.pos_y-cogumelos_verde.pos_y)): #Colisao        
            cogumelos_verde.pos_x = random.randint(50,750)  #voltar numa posicao aleatoria
            cogumelos_verde.velocidade = random.randint(4,8) #Com velocidade aleatoria
            pontuacao +=3 #Pontuacao caso acerte o item
            cogumelos.pos_y=0
    for cogumelos in lista_objetivos: #loop para jogar os itens
        cogumelos.movimento_obj() #movimento dos itens
        cogumelos.desenho(tela) #desenhando os ittens na tela
        
        if cogumelos.pos_y > 500: #quando chegar no fim
            cogumelos.pos_x = random.randint(50,750) #voltar numa posicao aleatoria
            cogumelos.velocidade = random.randint(4,8) #com velocidade aleatoria
        if mario.mascara.overlap(cogumelos.mascara,(cogumelos.pos_x-mario.pos_x , mario.pos_y-cogumelos.pos_y)): #colisao
            cogumelos.pos_x = random.randint(50,750) #voltar numa posicao aleatoria
            cogumelos.velocidade = random.randint(4,8) #com velocidade aleatoria
        if luigi.mascara.overlap(cogumelos.mascara,(cogumelos.pos_x-luigi.pos_x , luigi.pos_y-cogumelos.pos_y)): #colisao
            cogumelos.pos_x = random.randint(50,750) #voltar numa posicao aleatoria
            cogumelos.velocidade = random.randint(4,8) #com velocidade aleatoria

            pontuacao +=1 #pontuacao
            cogumelos.pos_y=0
    for inimigos in lista_inimigos: #loop para jogar os inimigos
        inimigos.movimento_inimigo2() #movimento
        inimigos.desenho(tela) #desenho deles na tela
       
        if inimigos.pos_y > 500: #caso chegue ao limite
            inimigos.pos_x = random.randint(50,750) #voltar em pos aleatoria  
            inimigos.velocidade = random.randint(4,8) #velocidade aleatora
        if mario.mascara.overlap(inimigos.mascara,(inimigos.pos_x-mario.pos_x , mario.pos_y-inimigos.pos_y)): #colsiao
            inimigos.pos_x = random.randint(50,750) #voltar em pos aleatoria  
            inimigos.velocidade = random.randint(4,8) #velocidade aleatora
        if luigi.mascara.overlap(inimigos.mascara,(inimigos.pos_x-luigi.pos_x , luigi.pos_y-inimigos.pos_y)): #colsiao
            inimigos.pos_x = random.randint(50,750) #voltar em pos aleatoria  
            inimigos.velocidade = random.randint(4,8) #velocidade aleatora
            
            vidas -=1
            mario.pos_x = 350
            mario.pos_y = 500
            inimigos.pos_y = 0
    
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}",True,(0,0,0)) #para mostrar a pontuacao
    texto_vidas = fonte.render(f'Vidas: {vidas}',True,(0,0,0)) #mostrar a qtd de vidas
    tela.blit(texto_pontuacao,(0,10)) #desenho da pontuacao
    tela.blit(texto_vidas,(0,40)) #desenho das vidas
    texto_gameOver = fonte.render("Game Over", True,(0,0,0))
    texto_WIN = fonte.render("Você venceu", True,(0,0,0))
    testo_pontos = fonte2.render("Você vence com 50 pontos!",True,(0,0,0))
    texto_ajuda = fonte2.render("Pressione e segure ESPAÇO para uma ajudinha!",True,(0,0,0))
    tela.blit(texto_ajuda,(400,10))
    tela.blit(testo_pontos,(560,40))
    if vidas == 0 or vidas < 0:
        fundo.desenho(tela) #tela de derrota, caso perca
        tela.blit(texto_gameOver,(320,200))
    
    if pontuacao == 50 or pontuacao >50: #tela de vitoria caso ganhe
        fundo.desenho(tela)
        tela.blit(texto_WIN,(320,200))
        marioWin.desenho(tela)
    pygame.display.update()
    clock.tick(60)
    
