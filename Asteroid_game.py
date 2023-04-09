import pygame
import random

WIDTH = 1024
HEIGHT = 768
BG_COLOR = (0, 0, 0)


class Player:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien.png')  # image of our character
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.ship_speed = 10
        self.lives = 5

    def ufo_movement(self):  # movement keys: W, A, S, D
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.y_movement(self.ship_speed)

        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.y_movement(-self.ship_speed)

        if keys[pygame.K_a] and self.rect.left > 0:
            self.x_movement(self.ship_speed)

        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.x_movement(-self.ship_speed)

    def x_movement(self, x):
        self.rect.x -= x

    def y_movement(self, y):
        self.rect.y -= y

    def move(self):
        self.ufo_movement()

    def draw(self):
        screen.blit(self.image, self.rect)

    def show_player(self):
        self.draw()
        self.move()


class Asteroid:
    def __init__(self, value_of_y_axis):
        self.image = pygame.image.load('Asteroid Brown.png')  # image of the asteroid
        self.value_of_y_axis = value_of_y_axis
        self.rect = self.image.get_rect(center=(self.value_of_y_axis, 0))
        self.speed = random.randint(1, 10)

    def movement(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

    def show_asteroids(self):
        self.draw()
        self.movement()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game_font = pygame.font.SysFont('arial', 30)

alien = Player()


asteroids = pygame.USEREVENT + 0
pygame.time.set_timer(asteroids, 1000)  # event for display asteroids

enemies = []  # asteroids in list


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit the game if we close the sceen
            running = False
        if event.type == asteroids:
            asteroid = Asteroid(random.randint(100, 924))  # create new asteroid
            enemies.append(asteroid)

    screen.fill(BG_COLOR)

    for enemy in enemies:
        enemy.show_asteroids()  # show asteroids
        if enemy.rect.y > 668:  # remove asteroid if out of the sceen
            enemies.remove(enemy)
        if enemy.rect.colliderect(alien.rect) and alien.lives != 0:  # if our character and asteroid meet
            alien.lives -= 1
            enemies.remove(enemy)

    if alien.lives != 0:
        alien.show_player()  # show the player

    lives_surf = game_font.render('Lives: ' + str(alien.lives), True, (255, 255, 255))  # display "Lives: "
    lives_rect = lives_surf.get_rect(topleft=(10, 10))
    screen.blit(lives_surf, lives_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
