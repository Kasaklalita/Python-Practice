import math


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x} {self.y})'

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self):
        return hash(f'{self.x} {self.y}')


def is_on_line(x, y, xa, xb, ya, yb):
    return math.isclose((x - xa) * (yb - ya), (xb - xa) * (y - ya))


if __name__ == "__main__":
    f = open('input.txt', 'r')
    n = int(f.readline()[:-1])
    all_centers = []
    is_ok = True
    for i in range(0, n):
        center = Point(0, 0)
        figure = f.readline().split(' ')
        if figure[0] == '0':
            center.x = int(figure[2]) * 2
            center.y = int(figure[3]) * 2
        elif figure[0] == '1':
            center.x = (int(figure[1]) + int(figure[5]))
            center.y = (int(figure[2]) + int(figure[6]))
        all_centers.append(center)
    all_centers = list(set(all_centers))
    xa, xb, ya, yb = all_centers[0].x, all_centers[-1].x, all_centers[0].y, all_centers[-1].y
    for i in range(1, len(all_centers) - 1):
        if not is_on_line(all_centers[i].x, all_centers[i].y, xa, xb, ya, yb):
            is_ok = False
    if is_ok:
        print("Yes")
    else:
        print("No")
    # if n <= 2:
    #     print("Yes")
    # else:
    #     is_ok = True
    #     centers = []
    #     for i in range(0, 2):
    #         center = Point(0, 0)
    #         figure = f.readline().split(' ')
    #         if figure[0] == '0':
    #             center.x = int(figure[2]) * 2
    #             center.y = int(figure[3]) * 2
    #         else:
    #             center.x = (int(figure[1]) + int(figure[5]))
    #             center.y = (int(figure[2]) + int(figure[6]))
    #         centers.append(center)
    #     xa, xb, ya, yb = centers[0].x, centers[1].x, centers[0].y, centers[1].y
    #     # print(xa, xb, ya, yb)
    #     # print(is_on_line(2, 2, xa, xb, ya, yb))
    #     for i in range(0, n - 2):
    #         center = Point(0, 0)
    #         figure = f.readline().split(' ')
    #         if figure[0] == '0':
    #             center.x = int(figure[2]) * 2
    #             center.y = int(figure[3]) * 2
    #         elif figure[0] == '1':
    #             center.x = (int(figure[1]) + int(figure[5]))
    #             center.y = (int(figure[2]) + int(figure[6]))
    #         if is_on_line(center.x, center.y, xa, xb, ya, yb):
    #             pass
    #         else:
    #             is_ok = False
    #     if is_ok:
    #         print('Yes')
    #     else:
    #         print('No')
