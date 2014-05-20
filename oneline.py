#!/usr/bin/env python3
"""
One-line shoutest version.
"""

(lambda n:list(map(lambda f:f(input()),[lambda y: print(sum(map(lambda x:int(x)**2 if x[0]!='-' else 0,input().split())))]*n)))(int(input()))

