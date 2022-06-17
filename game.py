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
    movimentoX = random.randrange(0, largura)
    movimentoY = 0
    badBurger = pygame.image.load("assets/badburger.png")
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    while True:

        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if jogando == True:
            #aqui é a parte do jogo 

            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(badBurger, (movimentoX, movimentoY))
  
        pygameDisplay.update()
        clock.tick(60)

main()
