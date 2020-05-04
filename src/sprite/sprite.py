from src import EZ


class Sprite:

    def __init__(self, x: int, y: int, height: int, width: int):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.direction = [0, 0]
        self.speed = [0, 0]

        sprites.append(self)

    def check_collision(self, sprite):
        return self.x <= sprite.x <= self.x + self.width and self.y <= sprite.y <= self.y + self.height

    def draw_hitbox(self):
        EZ.trace_segment(self.x, self.y, self.x + self.height, self.y)
        EZ.trace_segment(self.x, self.y, self.x, self.y + self.width)
        EZ.trace_segment(self.x + self.height, self.y, self.x + self.height, self.y + self.width)
        EZ.trace_segment(self.x, self.y + self.width, self.x + self.height, self.y + self.width)

    def apply(self, speed: list):
        if self.speed[0] >= 0:
            self.speed[0] += speed[0]
        elif self.speed[1] >= 0:
            self.speed[1] += speed[1]

    def update(self):
        if self.speed[0] > 0:
            self.apply([-1, 0])

        self.x += self.speed[0] * self.direction[0]
        self.y += self.speed[1] * self.direction[1]


sprites: list = []
