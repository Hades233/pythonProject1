# 写于2022年1月19日00:07:59
# 用途：批量打开文件夹及其子目录。因为爱数的文件必须打开文件夹后才会被缓存，后续用文件夹比较的方式比较爱数和投标公用电脑。
import os
import time
import win32gui  # pip install pywin32
import win32con
import win32api

hwnd1 = []  # 初始状态的窗口的句柄清单
hwnd2 = []  # 结束状态的窗口的句柄清单


def get_dir_walk(file_dir):  # 输入目标文件夹地址，输出子目录地址列表
    # paths = os.walk(r'E:\ShareCache\吉蒋\Test1')
    paths = os.walk(file_dir)  # 遍历目标文件夹地址
    data1 = []  # 带\\的路径清单
    data2 = []  # data1转换为路径带/的路径
    for path, dir_lst, file_lst in paths:
        for dir_name in dir_lst:  # dir_name是遍历文件夹路径
            # print(os.path.join(path, dir_name))
            data1.append(os.path.join(path, dir_name))
            data2.append(os.path.join(path, dir_name).replace("\\", "/"))  # 替换\\为\
    return data2


def open_dir(file_dir_list):  # 输入地址列表，打开文件夹，输出已打开的地址列表，然后关闭文件夹
    num_data = 0  # 打开的文件夹计数
    open_data2 = []  # 已打开的文件夹路径列表
    # not_open_data2 = []  # 未打开的文件夹路径列表
    for li in file_dir_list:
        os.startfile(li)  # 按照地址打开文件夹 https://www.cnblogs.com/yanjiayi098-001/p/12030032.html
        open_data2.append(li)  # 更新到已打开的文件夹路径列表
        time.sleep(0.6)  # 暂停0.6秒
        num_data += 1
        if num_data % 10 == 0 or num_data == len(file_dir_list):  # 如果打开的文件夹个数被10整除或等于全部的文件夹个数就执行批量关闭窗口命令
            time.sleep(2)  # 暂停2秒
            # 获取结束状态的窗口的句柄清单
            win32gui.EnumWindows(get_all_hwnd, 0)
            for h2, t2 in hwnd_title.items():
                # print(h2, t2)
                if t2 != "":  # 判断无标题的窗口的句柄
                    hwnd2.append(h2)
            dif_hwnd = set(hwnd2).difference(hwnd1)  # 新增加出来的窗口的句柄清单
            for hw in dif_hwnd:  # 批量关闭新增加出来的窗口
                if win32gui.IsWindowVisible(hw):
                    try:
                        win32gui.PostMessage(hw, win32con.WM_CLOSE, 0, 0)
                    except:
                        pass
            hwnd2.clear()  # 清空结束状态的窗口的句柄清单
    return open_data2


hwnd_title = dict()  # 创建一个字典，窗口的句柄：窗口的标题


def get_all_hwnd(hwnd, mouse):  # 遍历windows下 所有句柄及窗口名称 https://zhuanlan.zhihu.com/p/259632749
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


if __name__ == '__main__':

    # path_str='E:\ShareCache\吉蒋\Test1'
    path_str = str(input("请输入目标文件夹地址:"))
    start_time = time.time()  # 计时开始

    list1 = []  # 遍历的文件目录路径列表
    list2 = []  # 已打开的文件夹路径列表
    dif_list = []  # 未打开的文件夹路径列表

    # 获取初始状态的窗口的句柄清单
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h1, t1 in hwnd_title.items():
        # print(h1, t1)
        if t1 != "":  # 判断无标题的窗口的句柄
            hwnd1.append(h1)

    list1 = get_dir_walk(path_str)  # 遍历的文件目录路径列表
    list2 = open_dir(list1)  # 打开文件夹，更新已打开的文件夹路径列表

    list1 = get_dir_walk(path_str)  # 重新遍历的文件目录路径列表
    dif_list = set(list1).difference(list2)  # 未打开的文件夹路径列表 https://blog.51cto.com/lj23for1/2139933

    while len(dif_list):  # 未打开的文件夹路径列表不为空则循环打开
        # temp = []
        temp = open_dir(dif_list)  # 打开文件夹，temp存储本次打开的文件夹路径列表
        list2.extend(temp)  # 更新已打开的文件夹路径列表 https://blog.csdn.net/weixin_42350212/article/details/80628539
        list1 = get_dir_walk(path_str)  # 重新遍历的文件目录路径列表
        dif_list = set(list1).difference(list2)  # 未打开的文件夹路径列表
        temp.clear()  # 清除临时路径列表

    end_time = time.time()  # 计时开始
    win32api.MessageBox(0, "已打开的文件夹个数为 " + str(len(list2)) + " 个，耗时" + str(int(end_time - start_time)) + "秒", "提醒",
                        win32con.MB_OK)
    # print('已打开的文件夹个数', len(list2))
    # os.system("pause")
