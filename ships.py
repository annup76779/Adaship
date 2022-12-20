class Ship:
    def __init__(self, ship_name: str, size: int, x: int = None, y: int = None, direction = None):
        self.name = ship_name
        self.size = size
        self.status = size
        self.x = x
        self.y = y
        self.direction = direction

    @property
    def get_xyd(self):
        return self.x, self.y, self.direction

    def hit(self):
        self.status -= 1

    def is_sunken(self) -> bool:
        return self.status == 0

    def total_hits(self) -> int:
        return self.size - self.status

    def __str__(self):
        return self.name[0].upper()

    def __repr__(self):
        return self.name[0].upper()
