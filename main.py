from Logic import *
import pygame, sys
from random import shuffle
from database import get_best, insert_result

GAMERS_DB = get_best()


def draw_top_gamers():
    font_top = pygame.font.SysFont("simsun", 30)
    font_gamer = pygame.font.SysFont("simsun", 24)
    text_head = font_top.render("Краща трійка: ", True, COLOR_TEXT)
    screen.blit(text_head, (300, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, scor = gamer
        s = f"{index + 1}. {name} - {scor}"
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (300, 30 + 26 * index))
        print(index, name, scor)


def draw_interface(score, delta=0):
    pygame.draw.rect(screen, WHITE, ViewBar_Rec)
    font = pygame.font.SysFont("stxingkai", 70)
    font_score = pygame.font.SysFont("simsun", 48)
    text_score = font_score.render("Score:", True, COLOR_TEXT)
    text_score_val = font_score.render(f"{score}", True, COLOR_TEXT)
    font_delta = pygame.font.SysFont("simsun", 30)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_val, (140, 35))
    if delta != 0:
        text_score_delta = font_delta.render(f"+{delta}", True, COLOR_TEXT)
        screen.blit(text_score_delta, (135, 65))
    test_print(mas)
    draw_top_gamers()
    for row in range(Bloc):
        for col in range(Bloc):
            value = mas[row][col]
            text = font.render(f'{value}', True, BLACK)
            kord_square_x = Border * (col + 1) + BlocSize * col
            kord_square_y = ViewBar_Height + Border * (row + 1) + BlocSize * row
            pygame.draw.rect(screen, COLORS[value], (kord_square_x, kord_square_y, BlocSize, BlocSize))
            if value != 0:
                font_text_x, font_text_y = text.get_size()
                kord_text_x = kord_square_x + (BlocSize - font_text_x) / 2
                kord_text_y = kord_square_y + (BlocSize - font_text_y) / 2
                screen.blit(text, (kord_text_x, kord_text_y))


# кольори
COLOR_TEXT = (255, 127, 0)
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
COLORS = {
    0: GRAY,
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

Bloc = 4
BlocSize = 110
Border = 10
GameWindow_Width = Bloc * BlocSize + (Bloc + 1) * Border
ViewBar_Width = GameWindow_Width
ViewBar_Height = 110
GameWindow_Height = GameWindow_Width + ViewBar_Height
ViewBar_Rec = pygame.Rect(0, 0, ViewBar_Width, ViewBar_Height)


def init_const():
    global mas, score
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    score = 0
    empty = get_empty_list(mas)
    shuffle(empty)
    for i in range(2):
        randNum = empty.pop()
        x, y = get_ind_f_num(randNum)
        mas = insert2or4(mas, x, y)
        print(f'Був заповнений елемент під номером {randNum}')


mas = None
score = None
init_const()
Username = None


def draw_intro():
    try:
        img2048 = pygame.image.load("img2048.png")
    except:
        rect_2048 = pygame.Rect(10, 10, 200, 200)
        color_2048 = (237, 197, 63)
        font_2048 = pygame.font.SysFont("stxingkai", 70)
        text_2048 = font_2048.render("2048", True, WHITE)

    font = pygame.font.SysFont("stxingkai", 70)
    text_welcome = font.render("Welcome!", True, WHITE)
    name = 'Enter Name'

    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Enter Name':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2 and name != 'Enter Name':
                        global Username
                        Username = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center

        try:
            screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        except:
            pygame.draw.rect(screen, color_2048, rect_2048)
            size_text_x, size_text_y = text_2048.get_size()
            kord_x = 10 + (200 - size_text_x) / 2
            kord_y = 10 + (200 - size_text_y) / 2
            screen.blit(text_2048, (kord_x, kord_y))

        screen.blit(text_welcome, (230, 85))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def game_loop():
    global score, mas
    draw_interface(score)
    pygame.display.update()
    is_move = False
    while is_zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                elif event.key == pygame.K_LEFT:
                    mas, delta, is_move = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta, is_move = move_right(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta, is_move = move_down(mas)
                elif event.key == pygame.K_UP:
                    mas, delta, is_move = move_up(mas)
                score += delta
                if is_zero_in_mas(mas) and is_move:
                    empty = get_empty_list(mas)
                    shuffle(empty)
                    randNum = empty.pop()
                    x, y = get_ind_f_num(randNum)
                    mas = insert2or4(mas, x, y)
                    print(f'Був заповнений елемент під номером {randNum}')
                    is_move = False

                draw_interface(score, delta)
                pygame.display.update()


def draw_gameover():
    global Username, GAMERS_DB

    try:
        img2048 = pygame.image.load("img2048.png")
    except:
        rect_2048 = pygame.Rect(10, 10, 200, 200)
        color_2048 = (237, 197, 63)
        font_2048 = pygame.font.SysFont("stxingkai", 70)
        text_2048 = font_2048.render("2048", True, WHITE)

    font = pygame.font.SysFont("stxingkai", 54)
    text_gameover = font.render("GAME OVER!", True, WHITE)
    text_score = font.render(f"Your score: {score}", True, WHITE)
    try:
        best_score = GAMERS_DB[0][1]
    except:
        best_score = 0
    if score > best_score:
        text = "New Record!!!"
    else:
        text = f"Record {best_score}"
    text_record = font.render(text, True, WHITE)
    insert_result(Username, score)
    GAMERS_DB = get_best()
    end_wile = False
    while not end_wile:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    init_const()
                    end_wile = True
                elif event.key == pygame.K_RETURN:
                    Username = None
                    init_const()
                    end_wile = True
        screen.fill(BLACK)

        try:
            screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        except:
            pygame.draw.rect(screen, color_2048, rect_2048)
            size_text_x, size_text_y = text_2048.get_size()
            kord_x = 10 + (200 - size_text_x) / 2
            kord_y = 10 + (200 - size_text_y) / 2
            screen.blit(text_2048, (kord_x, kord_y))

        screen.blit(text_gameover, (230, 85))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        pygame.display.update()
    screen.fill(BLACK)


# Старт
pygame.init()
screen = pygame.display.set_mode((GameWindow_Width, GameWindow_Height))
pygame.display.set_caption("Game 2048")

while True:
    if Username is None:
        draw_intro()
    game_loop()
    draw_gameover()
