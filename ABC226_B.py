import io
import sys

_INPUT = """\
6
4
2 1 2
2 1 1
2 2 1
2 1 2
5
1 1
1 1
1 2
2 1 1
3 1 1 1
1
1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  s=set()
  for i in range(N):
    X=tuple(list(map(int,input().split()))[1:])
    s.add(X)
  print(len(s))