import pygame
import sys
import random

pygame.init()
game = True
# кадров в секунду
c = pygame.time.Clock()

# Размеры для окна
width = 1000
height = 600

# создание игрового окна
screen = pygame.display.set_mode((width, height))

# Название и значок
pygame.display.set_caption("Pong Game")

# Игровой фигуры
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
player1 = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, height / 2 - 70, 10, 140)

# Игровые переменные
ball_speedx = 6 * random.choice((1, -1))
ball_speedy = 6 * random.choice((1, -1))
player1_speed = 0
player2_speed = 6
player1_score = 0
player2_score = 0


# Функция движения мяча
def ball_movement():
    global ball_speedx, ball_speedy, player1_score, player2_score
    ball.x += ball_speedx
    ball.y += ball_speedy

    # Отскок мяча
    if ball.top <= 0 or ball.bottom >= height:
        ball_speedy *= -1
    if ball.left <= 0:
        player1_score += 1
        ball_restart()
    if ball.right >= width:
        player2_score += 1
        ball_restart()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speedx *= -1


# функция движения player1
def player1_movement():
    global player1_speed
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= height:
        player1.bottom = height


# функция движения player2
def player2_movement():
    global player2_speed
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed
    if player2.bottom >= height:
        player2.bottom = height


# Функция сброса положения мяча
def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (width / 2, height / 2)
    ball_speedy *= random.choice((1, -1))
    ball_speedx *= random.choice((1, -1))


# Переменная шрифта
font = pygame.font.SysFont("calibri", 25)

# Цикл игры
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 8
            if event.key == pygame.K_UP:
                player1_speed -= 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 8
            if event.key == pygame.K_UP or pygame.K_UP:
                player1_speed += 8

    # вызов функций
    ball_movement()
    player1_movement()
    player2_movement()

    # установка условия оценки
    if ball.x < 0:
        player1_score += 1
    elif ball.x > width:
        player2_score += 1

    # Визуальные эффекты
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (220, 220, 220), player1)
    pygame.draw.rect(screen, (220, 220, 220), player2)
    pygame.draw.ellipse(screen, (220, 220, 220), ball)
    pygame.draw.aaline(screen, (220, 220, 220), (width / 2, 0), (width / 2, height))

    # Чтобы нарисовать шрифт партитуры
    player1_text = font.render("Score:" + str(player1_score), False, (255, 255, 255))
    screen.blit(player1_text, [600, 50])
    player2_text = font.render("Score:" + str(player2_score), False, (255, 255, 255))
    screen.blit(player2_text, [300, 50])

    # Обновление игрового окна
    pygame.display.update()

    # 60 кадров в секунду
    c.tick(75)