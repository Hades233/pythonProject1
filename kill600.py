#!/usr/bin/env python3
# https://www.zhihu.com/question/55445739
import sys
import random

from matplotlib import pyplot as plt


def kill_one(to_die, dead, n):
    xlen = len(to_die)
    r = random.randint(0, (xlen - 1) // 2)
    r *= 2
    dead[to_die[r]] = n
    return [to_die[i] for i in range(xlen) if i != r]


def kill_all(num):
    to_die = [i for i in range(num)]
    dead = [0 for _ in range(num)]
    for i in range(num):
        to_die = kill_one(to_die, dead, i + 1)
    return dead


def main(script, *argv):
    num = int(argv[0])
    sta = [0 for _ in range(num)]
    last = [0 for _ in range(num)]
    K = 1000
    for i in range(K):
        print(i)
        dead = kill_all(num)
        x = dead.index(num)
        last[x] += 1
        sta = [sta[i] + dead[i] for i in range(num)]
    stat = [s / K for s in sta]
    plt.plot(stat)
    plt.plot(last)
    plt.show()


if __name__ == "__main__":
    main(*sys.argv)
