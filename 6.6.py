n, k, m = map(int, input().split())
if n < k:
    print(m * 2)
elif n >= k:
    if n % k == 0:
        print(((n // k) * m) * 2)
    else:
        print((((n // k) + 1) * m) * 2)
