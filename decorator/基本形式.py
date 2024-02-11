def d1(fn):
    def _d1():
        print("Before d1")
        fn()
        print("After d1")
    return _d1


@d1
def f1():
    print("Function")


if __name__ == '__main__':
    f1()