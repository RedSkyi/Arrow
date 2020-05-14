from src import EZ


class Sprite:

    def __init__(self, x: int, y: int, height: int, width: int):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        sprites.append(self)

    def check_collision(self, sprite):
        return self.x <= sprite.x <= self.x + self.width and self.y <= sprite.y + sprite.height <= self.y + self.height

    def draw_hitbox(self):
        EZ.trace_segment(self.x, self.y, self.x + self.width, self.y)
        EZ.trace_segment(self.x, self.y, self.x, self.y + self.height)
        EZ.trace_segment(self.x + self.width, self.y, self.x + self.width, self.y + self.height)
        EZ.trace_segment(self.x, self.y + self.height, self.x + self.width, self.y + self.height)

    def update(self):
        pass

    def draw(self):
        pass


sprites: list = []
