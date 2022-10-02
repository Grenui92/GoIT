import sys


def parse_args():
    return " ".join([i for i in sys.argv][1:])

print(parse_args())