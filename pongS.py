import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 120

class Game:
    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.W = screen_info.current_w
        self.H = screen_info.current_h
        self.screen = pygame.display.set_mode((self.W, self.H), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.player1 = Paddle(self.screen_rect, WHITE, (self.screen_rect.height * 0.1, self.screen_rect.centery), keys=(pygame.K_w, pygame.K_s))
        self.player2 = Paddle(self.screen_rect, WHITE, (self.screen_rect.width * 0.9, self.screen_rect.centery), keys=(pygame.K_UP, pygame.K_DOWN), is_automatic=True)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player1, self.player2)
        self.clock = pygame.time.Clock()
        self.main_loop()

    def main_loop(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                game = False
            
            self.all_sprites.update()
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


class Paddle(pygame.sprite.Sprite):  #TODO: поведение автомат. ракетки - от движения мяча 
    def __init__(self,screen_rect=None,color=WHITE,center=(0, 0),size=None,keys=(pygame.K_UP, pygame.K_DOWN),speed=3,is_automatic=False,) -> None:
        super().__init__()
        if not size:
            size = (screen_rect.width * 0.01, screen_rect.height * 0.05)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.image.fill(color)
        self.speed = speed
        self.keys = keys
        self.is_automatic = is_automatic
        self.screen_rect = screen_rect

    def update(self):
        if not self.is_automatic:
            keys = pygame.key.get_pressed()
            if keys[self.keys[0]]:
                if self.rect.top > self.screen_rect.top:
                    self.rect.y -= self.speed
            if keys[self.keys[1]]:
                if self.rect.bottom < self.screen_rect.bottom:
                    self.rect.y += self.speed
        else:
            keys = pygame.key.get_pressed()
            if keys[self.keys[0]]:
                if self.rect.top > self.screen_rect.top:
                    self.rect.y -= self.speed
            if keys[self.keys[1]]:
                if self.rect.bottom < self.screen_rect.bottom:
                    self.rect.y += self.speed


class Ball:
    pass


class Score:
    pass

game = Game()