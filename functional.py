#!/usr/bin/env python3
"""
Functional version.
"""

(lambda n:
    list(map(
        lambda f: f(input()),   # call the function

        # make a n-elem list contains the functions we want to call.
        [
            lambda y: print(sum(map(
                lambda x: x*x if x>0 else 0,
                map(int, input().split())
            )))
        ] * n

    ))
)(int(input()))

