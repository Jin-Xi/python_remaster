"""
这个脚本用于训练python的yield字段的使用：

"""
# xj 03点48分


import os
import random


def gen_list():
    return [i*2 for i in range(1000)]


def gen_list_default():
    return (i*2 for i in range(1000))


def gen_list_yield():
    """
    生成器的写法需要修改return为yield
    :return:
    """
    for i in range(1000):
        yield i*2


if __name__ == '__main__':
    # 完整列表
    print(gen_list())
    # 生成器
    print(gen_list_default())
    # 生成器
    print(gen_list_yield())




