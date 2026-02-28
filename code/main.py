import pygame
from settings import *
from sprites import *
from random import randint

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Window_Width, Window_Height))
        pygame.display.set_caption('Space Shooter')
        self.running = True
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.meteor_sprites = pygame.sprite.Group()
        self.laser_sprites = pygame.sprite.Group()
        self.load_assets()
        
        for i in range(20):
            Star(self.all_sprites, self.star_surf)
        self.player = Player(self.all_sprites, self.laser_surf, self.laser_sprites, self.laser_sound)

        self.meteor_event = pygame.event.custom_type()
        pygame.time.set_timer(self.meteor_event, 500)

    def load_assets(self):
        self.star_surf = pygame.image.load('images/star.png').convert_alpha()
        self.laser_surf = pygame.image.load('images/laser.png').convert_alpha()
        self.meteor_surf = pygame.image.load('images/meteor.png').convert_alpha()
        self.font = pygame.font.Font('images/Oxanium-Bold.ttf', 40)
        self.explosion_frames = [pygame.image.load(f'images/explosion/{i}.png').convert_alpha() for i in range(21)]
        self.laser_sound = pygame.mixer.Sound('audio/laser.wav')
        self.explosion_sound = pygame.mixer.Sound('audio/explosion.wav')

    def collisions(self):
        if pygame.sprite.spritecollide(self.player, self.meteor_sprites, False, pygame.sprite.collide_mask):
            self.running = False

        for laser in self.laser_sprites:
            collided = pygame.sprite.spritecollide(laser, self.meteor_sprites, True)
            if collided:
                laser.kill()
                AnimatedExplosion(self.explosion_frames, laser.rect.midtop, self.all_sprites)
                self.explosion_sound.play()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.meteor_event:
                    x, y = randint(0, Window_Width), randint(-200, -100)
                    Meteor(self.meteor_surf, (x, y), (self.all_sprites, self.meteor_sprites))

            self.all_sprites.update(dt)
            self.collisions()

            self.screen.fill(BG_COLOR)
            self.all_sprites.draw(self.screen)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()