#!/usr/bin/env python3
"""
Multi-line, clear version.
"""

def calculate(n):
    square = lambda x: x * x
    positive = lambda x: x > 0
    ans = sum(map(square, filter(positive, map(int, input().split()))))
    print(ans)


def main(deep):
    calculate(int(input()))
    if deep > 1:
        main(deep - 1)


if __name__ == '__main__':
    main(int(input()))
