n, m = map(int, input().split('x'))
k = int(input())
if k % 2 == 0 and k < n*m:
    print('успешно')
else:
    if k % n == 0 or n % k == 0 or k % m == 0 or m % k == 0:
        print('успешно')
    else:
        print('неосуществимо')