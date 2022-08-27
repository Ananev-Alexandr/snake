import pygame
import sys
from pyautogui import alert
from random import randint

pygame.init()
# Инициализация
W = 790
H = 550
RED = (255, 0, 0)
GREEN = (50, 255, 50)
snakeX = 20
snakeY = 200
# кооринаты старта
new_snakeX = 0
new_snakeY = 0
appleX = 400
appleY = 250
# Координаты начального яблока
len_snake = 1
snake_blocks = []
display = pygame.display.set_mode((W, H))
# Установил размер дисплея
clock = pygame.time.Clock()


while True:
    display.fill((155, 123, 200))
    # Фон дисплея
    pygame.time.delay(30)
    snake_head = []
    snake_head.append(snakeX)
    snake_head.append(snakeY)
    snake_blocks.append(snake_head)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Событие выхода из игры

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            new_snakeX = -10
            new_snakeY = 0
        elif event.key == pygame.K_RIGHT:
            new_snakeX = 10
            new_snakeY = 0
        elif event.key == pygame.K_UP:
            new_snakeX = 0
            new_snakeY = -10
        elif event.key == pygame.K_DOWN:
            new_snakeX = 0
            new_snakeY = 10
    # События кнопок направления

    if snakeX > W or snakeY > H:
        alert('You lost')
        sys.exit()
    elif snakeX < 0 or snakeY < 0:
        alert('You lost')
        sys.exit()
    # Установлены границы игры, при выходе за границу, игра заканчивается
    for block in snake_blocks[:-2]:
        if block == snake_head:
            alert('You lost')
            sys.exit()
    # Выход из игры, если змея есть свой хвост

    if snakeX - appleX >= -20 and snakeX - appleX <= 20:
        if snakeY - appleY >= -20 and snakeY - appleY <= 20:
            len_snake += 1
            appleX = randint(10, W)
            appleY = randint(10, H)
    # Генерация рандомного местоположения яблока

    snakeX += new_snakeX
    snakeY += new_snakeY

    if len(snake_blocks) > len_snake:
        del snake_blocks[0]
    # Чтобы змея не росла в цикле бесконечно

    for block in snake_blocks:
        pygame.draw.rect(display, GREEN, [block[0], block[1], 20, 20])
        # Генерация блоков змеи
    pygame.draw.circle(display, RED, (appleX, appleY), 10)
    # Генерация яблока
    pygame.display.flip()
    # Искажение пространства))
