m = input()
a = m[0]
b = int(m[1])
nmr = ord(a) - 1
b = int(b)
c = m[3]
nmr2 = ord(c) - 1
d = int(m[4])
if abs(nmr - nmr2) == 1 and abs(b - d) == 2:
    print('верно')
elif abs(nmr - nmr2) == 2 and abs(b - d) == 1:
    print('верно')
else:
    print('ошибка')
