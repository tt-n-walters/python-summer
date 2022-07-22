import pygame
pygame.init()

width = 800
height = 600
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Speed Typer")
pygame.display.set_icon(pygame.image.load("speed_typer/icon.png"))

image = pygame.transform.scale(image, (200, 200))

font = pygame.font.Font("speed_typer/CarterOne-Regular.ttf", 32)
enter_name_rect = pygame.Rect(310, 90, 180, 70)
enter_name_border = pygame.Rect(305, 85, 190, 80)
enter_name_text = font.render("Name:", True, (255, 255, 255))

name_enter_rect = pygame.Rect(150, 250, 500, 75)
name_enter_border = pygame.Rect(140, 240, 520, 95)

start_button_rect = pygame.Rect(300, 450, 200, 80)
start_button_border = pygame.Rect(290, 440, 220, 100)
start_button_text = font.render("S T A R T", True, (255, 255, 255))

rectangle = pygame.Rect(0, 0, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()     # Find the current mouse position
            x, y = mouse_position                       # Separate into the x and y coordinates
            rectangle.centerx = x                       # Set the rectangle position to the mouse
            rectangle.centery = y

    
    screen.fill((200, 250, 255))

    screen.fill((205, 120, 0), enter_name_border)
    screen.fill((255, 150, 0), enter_name_rect)
    screen.blit(enter_name_text, (350, 100))

    screen.fill((100, 200, 250), name_enter_border)
    screen.fill((255, 255, 255), name_enter_rect)
    
    screen.fill((60, 190, 30), start_button_border)
    screen.fill((125, 255, 80), start_button_rect)
    screen.blit(start_button_text, (338, 465))

    pygame.display.flip()
    
