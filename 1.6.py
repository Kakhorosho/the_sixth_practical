import math

a, b = map(int, input().split('x'))
r = 6.5
d = 2 * r

if a < d and b < d:
    if a <= b:
        if a <= 2 * math.sqrt(r**2 - (b / 2) ** 2):
            print('да')
        else:
            print('нет')
    else:
        if b <= 2 * math.sqrt(r**2 - (a / 2) ** 2):
            print('да')
        else:
            print('нет')
else:
    print('нет')

