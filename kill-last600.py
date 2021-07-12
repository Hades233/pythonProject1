# 600 个人站一排，每次随机杀掉一个奇数位的人，几号最安全？ - 布丁的回答 - 知乎
# https://www.zhihu.com/question/55445739/answer/1935747223
# 无法运行的样子
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

total = 600


# 随机杀掉一个队伍里奇数号的人
def kill_one_person(lin):
    length = len(lin)
    lin = np.delete(lin, np.random.choice(int((length + 1) / 2)) * 2)
    return lin


# 模拟次数
M = 1000
# 储存每次模拟最终剩余人的编号
number = np.zeros(M)

for m in range(M):
    line = np.arange(total)
    for i in range(total - 1):
        line = kill_one_person(line)
    number[m] = line

plt.hist(number, bins=100)
plt.show()
