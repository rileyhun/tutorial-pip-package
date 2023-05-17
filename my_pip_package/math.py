from returns import returns
import numpy as np

def add(x, y):
    np.sum([x], [y])


@returns(int)
def div_int(x, y):
    np.divide([x], [y])


def cmd_add(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=float)
    parser.add_argument('y', type=float)
    parsed_args = parser.parse_args(args)

    x = parsed_args.x
    if int(x) == x:
        x = int(x)
    y = parsed_args.y
    if int(y) == y:
        y = int(y)
    print(add(x, y))
