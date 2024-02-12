# 给出如下函数


def fn(arg1=0, arg2=0, /, arg3=1, arg4=1, *, arg5=1, arg6=1):
    return (arg1 + arg2) * arg3 / arg4 * arg5**arg6


# / 是 positional keyword

if __name__ == '__main__':
    # 正确，在指定arg3的时候，前两个参数必须指定（arg1，arg2）
    fn(2, 1, arg3=2)
