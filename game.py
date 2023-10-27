import pygame

# Inisialisasi Pygame
pygame.init()

# Membuat Windows Pygame
screen = pygame.display.set_mode((800,500))

# Background
background = pygame.image.load("images/background.jpg")

# Mengatur caption dan icon
pygame.display.set_caption("Perang Angkasa")
icon = pygame.image.load("images/ufo-flying.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/battleship.png')
playerX = 370
playerY = 200

def player(x,y):
    screen.blit(playerImg,(x,y))

# Game Loop
running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player(playerX,playerY)
    pygame.display.update()
