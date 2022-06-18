import pygame
import random

pygame.init()
altura = 480
largura = 854
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Burger rain")
bg = pygame.image.load("assets/background.png")


gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

icone = pygame.image.load("assets/burger.ico")
pygameDisplay.set_icon(icone)

def main():
    jogando = True
    rightPress = False
    leftPress = False
    movimentoX = random.randrange(0, largura)
    movimentoY = 0
    velocidade = 1
    direcao = True
    posicaoXPlayer = 0
    posicaoYPlayer = 373
    movimentoXPlayer = 0
    boneco = pygame.image.load("assets/personagem.png")
    badBurger = pygame.image.load("assets/badburger.png")
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    larguraPlayer = 101
    velocidadePlayer = 10

    while True:

        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftPress = True
                elif event.key == pygame.K_RIGHT:
                    rightPress = True
                elif event.key == pygame.K_RETURN:
                    main()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftPress = False
                elif event.key == pygame.K_RIGHT:
                    rightPress = False


        if jogando == True:
            #aqui é a parte do jogo
            movimentoXPlayer = 0
            if rightPress:
                movimentoXPlayer = velocidadePlayer
            if leftPress:
                movimentoXPlayer = -velocidadePlayer

            #controlar limites do boneco
            posicaoXPlayer = posicaoXPlayer + movimentoXPlayer
            if posicaoXPlayer < 0:
                posicaoXPlayer = 0
            elif posicaoXPlayer > largura - larguraPlayer:
                posicaoXPlayer = largura - larguraPlayer
            

            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(boneco, (posicaoXPlayer, posicaoYPlayer))
            gameDisplay.blit(badBurger, (movimentoX - 68, movimentoY))


            if direcao == True:
                if movimentoY <= 480 - 68:
                    movimentoY = movimentoY + velocidade
                else:
                    movimentoY = 0
                    movimentoX = random.randrange(0, largura)
                    velocidade = velocidade + 2
                    direcao = True


  
        pygameDisplay.update()
        clock.tick(60)

main()
