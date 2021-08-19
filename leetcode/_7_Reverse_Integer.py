def reverse(x):
    temp = 0
    last_temp = 0
    if x >= 0:
        while x:
            last_temp = temp
            temp = temp * 10 + x % 10
            x = x // 10
    else:
        x = -x
        while x:
            last_temp = temp
            temp = temp * 10 + x % 10
            x = x // 10
        temp = -temp
    if -2147483648 <= temp <= 2147483647:
        return temp
    else:
        return 0


list1 = [-123, 456, 70, -2147483648]
for y in list1:
    print(reverse(y))
