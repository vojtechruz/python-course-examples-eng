# Simple example
def out_func():
    return in_func(0)


def in_func(divisor):
    return 1 / divisor


if __name__ == '__main__':
    print(out_func())