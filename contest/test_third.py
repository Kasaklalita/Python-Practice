

class Circle:
    def __init__(self, r: int, center: Point) -> None:
        self.radius = r
        self.center = center

    def __str__(self) -> str:
        return f'center: {self.center}, radius: {self.radius}'


class Rectangle:
    def __init__(self, first: Point, second: Point, third: Point, fourth: Point) -> None:
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
