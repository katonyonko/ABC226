import io
import sys

_INPUT = """\
6
2 2
3 3
50 10000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,K=map(int,input().split())