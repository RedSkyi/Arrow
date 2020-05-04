from src.sprites.movable_sprite import MovableSprite


class Player(MovableSprite):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, 100, 100)

    pass
