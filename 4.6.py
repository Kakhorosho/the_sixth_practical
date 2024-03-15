m = input()
a = m[0]
b = int(m[1])
nmr = ord(a) - 1
b = int(b)
if nmr % 2 != 0:
    if b % 2 == 0:
        print('чёрная')
    else:
        print('белая')
elif nmr % 2 == 0:
    if b % 2 != 0:
        print('чёрная')
    else:
        print('белая')
