def mirror(h: int, m: int):
    mirror_h = abs((12 - h)) % 12
    mirror_m = abs((60 - m)) % 60
    return [mirror_h, mirror_m]


if __name__ == "__main__":
    f = open('input.txt', 'r')
    task = f.readline().split(' ')
    h = int(task[0])
    m = int(task[1])
    result = mirror(h, m)
    print(f'{result[0]} {result[1]}')
