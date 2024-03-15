n = int(input())
if 1 <= n <= 10:
    print(n - 1)
elif 11 <= n <= 190:
    if n % 2 == 0:
        first_digit_check = ((n // 10) - 1) * 10
        number = n - first_digit_check
        k = number / 2 - 6
        print(int(k))
    else:
        if (n // 10) % 2 != 0:
            print(((n // 10) // 2) + 1)
        elif (n // 10) % 2 == 0:
            print((n // 10) // 2)
elif 191 <= n <= 403:
    if n % 3 != 0:
        first_digit_check = (n // 100 - 2) * 100
        second_digit_check = ((n % 100) // 10 + 1) * 10
        a = first_digit_check + second_digit_check
        number = n - a
        n = int(input())
        if n % 3 != 0:
            first_digit_check = (n // 100 - 2) * 100
            second_digit_check = ((n % 100) // 10 + 1) * 10
            a = first_digit_check + second_digit_check
            number = n - a
            print(int((number - 193) / 3))
        else:
            if a / 30 > 7:
                print(2)
            else:
                print(1)
    elif n % 3 == 0:
        first_digit_check = (n // 100 - 2) * 100
        second_digit_check = ((n % 100) // 10 + 1) * 10
        number = n - (first_digit_check + second_digit_check)
        print(int((n - number) / 30))

