from src import config
from src import sprite
from src.sprites.ground import Ground


class MovableSprite(sprite.Sprite):

    def __init__(self, x: int, y: int, height: int, width: int):
        self.speed = [0, 0]

        super().__init__(x, y, height, width)

    def check_speed(self):
        return -config.MAX_SPEED <= self.speed[0] <= config.MAX_SPEED

    def apply(self, speed: list):
        self.speed[0] += speed[0]
        self.speed[1] += speed[1]

    def update(self):
        if self.speed[0] > 0:
            self.speed[0] += -1
        elif self.speed[0] < 0:
            self.speed[0] += 1

        for sprites in sprite.sprites:
            if isinstance(sprites, Ground):
                if not sprites.check_collision(self):
                    self.apply([0, -1])
                else:
                    self.speed = [self.speed[0], 0]

        self.x += self.speed[0]
        self.y += -self.speed[1]
        super().update()

