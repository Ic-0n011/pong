import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        WHITE = (255, 255, 255)
        screen_info = pygame.display.Info()
        self.W = screen_info.current_w
        self.H = screen_info.current_h
        self.screen = pygame.display.set_mode((self.W, self.H),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.player1 = Paddle(self.screen_rect.width * 0.1, self.screen_rect.centery, WHITE)
        self.player2 = Paddle(self.screen_rect.width * 0.9, self.screen_rect.centery, WHITE)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player1, self.player2)

    def main_loop(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                game = False
            self.all_sprites.draw(self.screen)
            pygame.display.flip()


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color: tuple, center_x: int, center_y: int) -> None:
        super().__init__()
        self.image = pygame.Surface((10, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.image.fill(color)


game = Game()
game.main_loop()
pygame.quit()
sys.exit()