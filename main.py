import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatables, drawables, asteroids)

    AsteroidField.containers = (updatables)

    Shot.containers = (updatables, drawables, shots)

    asteroid_field = AsteroidField()

    while True:
        # IO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # PROCESSING
        updatables.update(dt)
        if detect_collisions_with_player(asteroids, player):
            return
        detect_collisions_with_bullets(asteroids, shots)

        # RENDERING
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000

def detect_collisions_with_player(obstacles, player):
    for obstacle in obstacles:
        if player.collides_with(obstacle):
            print("GAME OVER")
            return True
    
    return False

def detect_collisions_with_bullets(obstacles, bullets):
    for obstacle in obstacles:
        for bullet in bullets:
            if bullet.collides_with(obstacle):
                bullet.kill()
                obstacle.split()

if __name__ == "__main__":
    main()
