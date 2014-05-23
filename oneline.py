#!/usr/bin/env python3
"""
One-line with exec() version.
Shortest version, with only 98 characters.
"""

exec('input();print(sum(map(lambda x:x*x if x>0 else 0,map(int,input().split()))));'*int(input()))

# Python2 can be shorter, only 94 characters.
#exec'input();print sum(map(lambda x:x*x if x>0 else 0,map(int,raw_input().split())));'*input()
