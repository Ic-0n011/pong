import pygame
import sys

pygame.init()
screen_xy = (1550, 800)
screen = pygame.display.set_mode(screen_xy)
rectangle_width = 50
rectangle_height = 50
rectangle_x = screen.get_width() // 2 - rectangle_width
rectangle_y = screen.get_height() // 2 - rectangle_height
rectangle = pygame.Rect(725, 350, 50, 50)
rectangle_color = (0, 255, 255)
pygame.draw.rect(screen, rectangle_color, rectangle, 0)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            rectangle.y -= 10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            rectangle.y += 10
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            rectangle.x -= 10
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            rectangle.x += 10
    pygame.draw.rect(screen,  rectangle_color, rectangle)
    pygame.display.flip()