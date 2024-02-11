"""
这两个函数用于展示，yield函数和直接递归生成的区别：
1、内存占用情况
2、是否支持多线程
3、执行时间
（对于输入4，”abcd“）
"""
# xj 2024

import os


def generate_text_yield(n, chars):
    """
    对于这个函数
    :param n:
    :param chars:
    :return:
    """
    if n == 0:
        yield ""
    else:
        """
        对于 pw_list 中的每一个长度为 n-1 的字符串 pw，我们遍历 chars 列表中的每一个字符 c，然后将 c 添加到 pw 的末尾，
        生成一个长度为 n 的新字符串。
        疑问：
        1、为什么要通过for ... in 来取生成器的返回值: 你需要生成的不止是一个值，而是依次生成不同的值
        2、第一次生成的是”“
        """
        pw_list = generate_text_yield(n - 1, chars)
        for pw in pw_list:
            for c in chars:
                yield pw + c


# 错误示范：在递归过程中使用了return导致当前层递归中的循环无法继续，只会输出一个结果，此写法只适用于结果为1的搜索，不适用于遍历
# FIXME：错误示范
def outer1():
    def generate_text(n, chars):
        if n == 0:
            return ""
        for c in chars:
            res = generate_text(n - 1, chars) + c
            if len(res) == n:
                print(res)
            return res
    return generate_text


# 非yield的实际写法,可以通过传递中间变量path来完成
def outer2():
    res = []
    def generate_text(n, path, chars):
        if n == 0:
            print(path)
            res.append(path)
            print(res)
            return
        for c in chars:
            generate_text(n-1, c+path, chars)

    print(res)
    return generate_text


if __name__ == '__main__':
    # inner = outer2()
    # # print(os.inner(3, "", "abcd"))
    # print(inner(3, "", "abcd"))

    g = generate_text_yield(3, "abcd")
    print(g)
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())

