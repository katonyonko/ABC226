import io
import sys

_INPUT = """\
6
3.456
99.500
0.000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X,Y=input().split('.')
  X=int(X)
  if int(Y[0])>4: X+=1
  print(X)