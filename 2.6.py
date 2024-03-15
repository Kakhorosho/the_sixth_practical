a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))
s = a * b
if s >= c * d or s >= c * e or s >= e * d:
    print('да')
else:
    print('нет')
