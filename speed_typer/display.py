import pygame
import time
import speedtyper
pygame.init()



def start_menu():
    global name, name_text, state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # remove the last letter typed
                # don't add the unicode, but do render
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                state = 1
            else:
                name += event.unicode
            name_text = font.render(name, True, (0, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 300 < x < 500 and 440 < y < 520:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                state = 1
                return

    x, y = pygame.mouse.get_pos()
    if 300 < x < 500 and 440 < y < 520:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        button_colour = (213, 255, 80)
        button_border_colour = (136, 207, 26)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        button_colour = (125, 255, 80)
        button_border_colour = (60, 190, 30)

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
    screen.fill(button_border_colour, start_button_border)
    screen.fill(button_colour, start_button_rect)
    screen.blit(start_button_text, (338, 455))

    pygame.display.flip()


def main():
    global user_sentence, user_sentence_text, has_typed_before, start_time, state
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # remove the last letter typed
                # don't add the unicode, but do render
                user_sentence = user_sentence[:-1]
            elif event.key == pygame.K_RETURN:
                state = 2
            else:
                user_sentence += event.unicode
            user_sentence_text = font.render(user_sentence, True, (0, 0, 0))
            
            # Check if it's the first time we typed
            if has_typed_before == False:
                start_time = time.time()
                has_typed_before = True


    # Drawing
    screen.fill((255, 202, 95))

    # Timer
    pygame.draw.rect(screen, (255, 0, 0), (320, 40, 160, 70))
    pygame.draw.rect(screen, (0, 0, 0), (330, 50, 140, 50))
    if has_typed_before == True:
        current = time.time() - start_time
        time_f = f"{int(current // 60 % 60):02d}:{int(current % 60):02d}:{int(current * 100 % 100):02d}"
        timer_text = timer_font.render(time_f, True, (255, 0, 0))
        screen.blit(timer_text, (338, 45))
    else:
        timer_text = timer_font.render("00:00:00", True, (255, 0, 0))
        screen.blit(timer_text, (338, 45))

    # Actual sentence
    pygame.draw.rect(screen, (255, 166, 105), (40, 150, 720, 120))
    pygame.draw.rect(screen, (255, 241, 179), (50, 160, 700, 100))
    lines = speedtyper.split_sentence(speedtyper.sentence, 43)

    sentence_text = font.render(lines[0], True, (0, 0, 0))
    screen.blit(sentence_text, (55, 160))
    sentence_text = font.render(lines[1], True, (0, 0, 0))
    screen.blit(sentence_text, (55, 200))
    
    # User sentence
    pygame.draw.rect(screen, (152, 244, 255), (40, 350, 720, 120))
    pygame.draw.rect(screen, (255, 255, 255), (50, 360, 700, 100))
    if len(user_sentence) > 0:
        if len(user_sentence) > 43:
            # split up
            lines = speedtyper.split_sentence(user_sentence, 43)
            sentence_text = font.render(lines[0], True, (0, 0, 0))
            screen.blit(sentence_text, (55, 360))
            sentence_text = font.render(lines[1], True, (0, 0, 0))
            screen.blit(sentence_text, (55, 400))
        else:
            # draw once
            screen.blit(user_sentence_text, (55, 360))

    pygame.display.flip()
    

def results():
    global has_calculated, stuff, cpm_text, accuracy_text, user_name_text
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 110 < x < 310 and 460 < y < 520:
                setup()
                return
            if 490 < x < 690 and 460 < y < 520:
                setup(state_chosen=1, name_chosen=name)
                return


    if has_calculated == False:
        stuff = speedtyper.calculate_stuff(user_sentence, time.time() - start_time)
        cpm_text = "Characters per minute: "  + str(stuff[0]) + " cpm"
        accuracy_text = "Accuracy: " + stuff[1]
        cpm_text = font.render(cpm_text, True, (255, 255, 255))
        accuracy_text = font.render(accuracy_text, True, (255, 255, 255))
        user_name_text = font.render(name, True, (255, 150, 0))
        has_calculated = True
        
    # Background
    screen.fill((102, 202, 95))

    screen.blit(user_name_text, (400 - user_name_text.get_width() / 2, 100))

    # Results
    screen.blit(cpm_text, (400 - cpm_text.get_width() / 2, 200))
    screen.blit(accuracy_text, (400 - accuracy_text.get_width() / 2, 250))
    # Menu button
    pygame.draw.rect(screen, (73, 163, 246), (100, 450, 220, 80))
    pygame.draw.rect(screen, (56, 106, 209), (110, 460, 200, 60))
    screen.blit(font.render("MENU", True, (255, 255, 255)), (210 - 45, 465))

    # Retry button
    pygame.draw.rect(screen, (255, 250, 73), (480, 450, 220, 80))
    pygame.draw.rect(screen, (255, 217, 43), (490, 460, 200, 60))
    screen.blit(font.render("RETRY", True, (255, 255, 255)), (590 - 45, 465))

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


def setup(state_chosen = 0, name_chosen = ""):
    global name, user_sentence, state, has_typed_before, has_calculated
    name = name_chosen
    user_sentence = ""
    state = state_chosen
    has_typed_before = False
    has_calculated = False
    speedtyper.pick_sentence()


speedtyper.download_sentences()
speedtyper.read_sentences()
setup()

while True:
    if state == 0:
        start_menu()
    if state == 1:
        main()
    if state == 2:
        results()
