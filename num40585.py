from math import factorial

'有哪些数字，它每个位数的阶乘相加等于它本身？'


#  http://www.cxyzjd.com/article/zhangzhengyi03539/46811065


def func(x):
    result = 0
    while x > 0:
        result += factorial(x % 10)
        x //= 10
    return result


num = 0
for i in range(1, 9999999):
    if i == func(i):
        print(i)
