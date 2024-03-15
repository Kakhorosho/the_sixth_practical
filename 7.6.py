k = int(input())
if k % 5 == 0 or k % 7 == 0:
    print('да')
elif k % 10 == 7:
    if (k - 7) % 5 == 0 and k - 7 > 0:
        print('да')
    else:
        print('нет')
elif k % 10 == 4:
    if (k - 14) % 5 == 0 and k - 14 > 0:
        print('да')
    else:
        print('нет')
elif k % 10 == 1:
    if (k - 21) % 5 == 0 and k - 21 > 0:
        print('да')
    else:
        print('нет')
elif k % 10 == 8:
    if (k - 28) % 5 == 0 and k - 28 > 0:
        print('да')
    else:
        print('нет')
elif k % 10 == 2:
    if (k - 42) % 5 == 0 and k - 42 > 0:
        print('да')
    else:
        print('нет')
elif k % 10 == 9:
    if (k - 49) % 5 == 0 and k - 49 > 0:
        print('да')
    else:
        print('нет')
elif k % 10 == 6:
    if (k - 56) % 5 == 0 and k - 56 > 0:
        print('да')
    else:
        print('нет')
elif k % 10 == 3:
    if (k - 63) % 5 == 0 and k - 63 > 0:
        print('да')
    else:
        print('нет')
else:
    print('нет')
