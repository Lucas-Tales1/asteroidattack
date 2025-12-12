import random
import sys
import time
import pygame

def game_init(w, h):
    pygame.init()
    size = w, h
    display = pygame.display.set_mode(size)
    pygame.display.set_caption("Asteroid Attack")
    return display
     
display = game_init(480, 640)
imagem_fundo = pygame.image.load("jungle.png")
background = pygame.image.load("background.png")
asteroid = pygame.image.load("asteroid.png")
dino = pygame.image.load("dino_right.png")
dinorect = dino.get_rect()
dinorect.x = 200
dinorect.y = 486
asteroidrect = asteroid.get_rect()
asteroidrect.x = random.randrange(0,390)
asteroidrect.y = random.randrange(0,40)
gameover = pygame.image.load("gameover.png")
alive = True
temporizador = 0
velocidade = 5
velocidade_dino = 5
clear = pygame.image.load("clear.png")
clearect = clear.get_rect()
clearect.x = random.randrange(470,480)
clearect.y = random.randrange(0,1)
contador = 0
start_background = pygame.image.load("start_background.png")
music = pygame.mixer.music.load("menu_music.mp3")
pygame.mixer.music.play(-1)
estado = "menu"
passos = 0
tempo = pygame.time.get_ticks()

#jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if estado == "menu":
        display.blit(start_background,(0,0))
        pygame.mixer.music.set_volume(0.05)
        
        if keys[pygame.K_c]:
            estado = "jogando"
            
    elif estado == "jogando":    
        display.blit(imagem_fundo, (0, 0))
        display.blit(dino, dinorect)
        display.blit(asteroid,asteroidrect)
        display.blit(clear,clearect)
        
        clearect.y += 5
        if clearect.y == 10:
            clearect.y = 0
            contador += 1
            if contador>8:
                contador = 1
        
        if keys[pygame.K_LEFT]:
            dino = pygame.image.load("dino_left.png")
            dinorect.x -= velocidade_dino
            passos +=1
            if passos%2 == 0:
                dino = pygame.image.load("dino_l.png")
            else: 
                dino = pygame.image.load("dino_l1.png")
            if velocidade_dino <= 10:
                if temporizador%5 == 0:
                    velocidade_dino += 0.02
        if dinorect.left < 0:
            dinorect.left = 0

        if keys[pygame.K_RIGHT]:
            dino = pygame.image.load("dino_right.png")
            dinorect.x += velocidade_dino
            passos +=1
            if passos%2 == 0:
                dino = pygame.image.load("dino_r.png")
            else: 
                dino = pygame.image.load("dino_r1.png")
            if velocidade_dino <= 15:
                if temporizador%5 == 0:
                    velocidade_dino += 0.02
            if dinorect.right > 480:
                dinorect.right = 480
        
        asteroidrect.y += velocidade
        
        if contador%1==0:
            asteroid = pygame.image.load("asteroid.png")
        if contador%2==0:
            asteroid = pygame.image.load("asteroid2.png")
        if contador%3==0:
            asteroid = pygame.image.load("asteroid3.png")
        if contador%4==0:
            asteroid = pygame.image.load("asteroid4.png")
        if contador%5==0:
            asteroid = pygame.image.load("asteroid5.png")
        if contador%6==0:
            asteroid = pygame.image.load("asteroid6.png")
        if contador%7==0:
            asteroid = pygame.image.load("asteroid7.png")
        if contador%8==0:
            asteroid = pygame.image.load("asteroid8.png")
        
        if asteroidrect.y >= 440:
            asteroidrect.x = random.randrange(0,390)
            asteroidrect.y = random.randrange(0,30)
            temporizador += 1
        
        if velocidade <= 11:
            if temporizador%3 == 0:
                velocidade += 0.01
        
        if asteroidrect.colliderect(dinorect):
            dino = pygame.image.load("skull.png")
            asteroid = pygame.image.load("clear.png")
            music = pygame.mixer.music.load("gameover.mp3")
            pygame.mixer.music.set_volume(10)
            pygame.mixer.music.play()
            display.blit(gameover,(90,20))
            estado = "fim de jogo"
        
        if temporizador >= 100:
            estado = "mode2"     
            dino = pygame.image.load("dino2.png")
            pygame.mixer.music.set_volume(100)
            music = pygame.mixer.music.load("theme_music_mode2.mp3")
            pygame.mixer.music.play()      
            
    elif estado == "mode2":
        display.blit(background, (0,0))
        display.blit(dino,(150,486))
        
    elif estado == "fim de jogo":
        display.blit(imagem_fundo, (0, 0))
        display.blit(dino,dinorect)
        display.blit(gameover,(90,20))
        if keys[pygame.K_r]:
            estado = "menu" 
            music = pygame.mixer.music.load("menu_music.mp3")
            pygame.mixer.music.play()
            dino = pygame.image.load("dino_right.png")
            asteroid = pygame.image.load("asteroid.png")
            asteroidrect.y = 0
            temporizador = 0
            velocidade = 5
            velocidade_dino = 5
    print(temporizador)
    pygame.display.flip()
    time.sleep(0.015)

    
    
    