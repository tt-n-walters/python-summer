import pygame
import time
pygame.init()


def start_menu():
    global name, name_text
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # remove the last letter typed
                # don't add the unicode, but do render
                name = name[:-1]
            else:
                name += event.unicode
            name_text = font.render(name, True, (0, 0, 0))

    # Background
    screen.fill((200, 250, 255))

    # Enter name text
    screen.fill((205, 120, 0), enter_name_border)
    screen.fill((255, 150, 0), enter_name_rect)
    screen.blit(enter_name_text, (350, 100))

    # Text input area
    screen.fill((100, 200, 250), name_enter_border)
    screen.fill((255, 255, 255), name_enter_rect)
    if len(name) > 0:
        text_width = name_text.get_width()
        screen.blit(name_text, (400 - text_width / 2, 262))
    
    # Start button
    screen.fill((60, 190, 30), start_button_border)
    screen.fill((125, 255, 80), start_button_rect)
    screen.blit(start_button_text, (338, 455))

    pygame.display.flip()


def main():
    global user_sentence, user_sentence_text
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # remove the last letter typed
                # don't add the unicode, but do render
                user_sentence = user_sentence[:-1]
            else:
                user_sentence += event.unicode
            user_sentence_text = font.render(user_sentence, True, (0, 0, 0))

    # Drawing
    screen.fill((255, 202, 95))

    # Timer
    pygame.draw.rect(screen, (255, 0, 0), (320, 40, 160, 70))
    pygame.draw.rect(screen, (0, 0, 0), (330, 50, 140, 50))
    current = time.time() - start_time
    time_f = f"{int(current // 60 % 60):02d}:{int(current % 60):02d}:{int(current * 100 % 100):02d}"
    timer_text = timer_font.render(time_f, True, (255, 0, 0))
    screen.blit(timer_text, (338, 45))

    # Actual sentence
    pygame.draw.rect(screen, (255, 166, 105), (40, 150, 720, 120))
    pygame.draw.rect(screen, (255, 241, 179), (50, 160, 700, 100))
    
    # User sentence
    pygame.draw.rect(screen, (152, 244, 255), (40, 350, 720, 120))
    pygame.draw.rect(screen, (255, 255, 255), (50, 360, 700, 100))
    if len(user_sentence) > 0:
        screen.blit(user_sentence_text, (55, 360))

    pygame.display.flip()
    


width = 800
height = 600
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Speed Typer")
pygame.display.set_icon(pygame.image.load("speed_typer/icon.png"))


font = pygame.font.Font("speed_typer/CarterOne-Regular.ttf", 32)
timer_font = pygame.font.Font("speed_typer/Teko-Regular.ttf", 48)

enter_name_rect = pygame.Rect(310, 90, 180, 70)
enter_name_border = pygame.Rect(305, 85, 190, 80)
enter_name_text = font.render("Name:", True, (255, 255, 255))

name_enter_rect = pygame.Rect(150, 250, 500, 75)
name_enter_border = pygame.Rect(140, 240, 520, 95)

start_button_rect = pygame.Rect(300, 440, 200, 80)
start_button_border = pygame.Rect(290, 430, 220, 100)
start_button_text = font.render("S T A R T", True, (255, 255, 255))


name = ""
user_sentence = ""
start_time = time.time()

while True:
    # start_menu()
    main()
    
