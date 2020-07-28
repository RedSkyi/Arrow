from src.sprite import Sprite


class Ground(Sprite):

    def __init__(self, x: int, y: int, height: int, width: int):
        super().__init__(x, y, height, width)

    pass
