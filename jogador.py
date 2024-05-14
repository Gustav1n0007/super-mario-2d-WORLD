import pygame
    
class Player:
    def __init__(self,arquivo_da_img,alturaIMG,larguraIMG,x_inicial,y_inicial) -> None:
        self.imagem = pygame.image.load(arquivo_da_img)
        
        self.largura = larguraIMG
        self.altura = alturaIMG

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial
    
        self.mascara = pygame.mask.from_surface(self.imagem)

    def desenho(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))

    def movimento(self):
        keys = pygame.key.get_pressed() #verificar se uma tecla foi clicada
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pos_x += 3
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos_x -= 3

        if self.pos_x < -80:
            self.pos_x =-80
        if self.pos_y < -0:
            self.pos_y = -0
        if self.pos_y > 400:
            self.pos_y = 400
        if self.pos_x > 750:
            self.pos_x = 750

class Fundo:
    def __init__(self,arquivo_da_img,alturaIMG,larguraIMG,x_inicial,y_inicial) -> None:
        self.imagem = pygame.image.load(arquivo_da_img)
        
        self.largura = larguraIMG
        self.altura = alturaIMG

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial
    
        self.mascara = pygame.mask.from_surface(self.imagem)

    def desenho(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))
