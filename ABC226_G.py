import io
import sys

_INPUT = """\
6
3
5 1 0 0 1
0 0 0 2 1
0 3 0 0 0
0 0 2 0 0
10000000000000000 0 0 0 0
0 0 0 0 2000000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  for _ in range(T):
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    if A[0]<=B[0]: A[0]=B[0]=0
    else: A[0]-=B[0]; B[0]=0
    #2の処理
    if A[1]<=B[1]:
      B[1]-=A[1]
      A[1]=0
      if A[0]<=B[1]*2:
        A[0]=B[1]=0
      else:
        A[0]-=B[1]*2
        B[1]=0
    else:
      A[1]-=B[1]
      B[1]=0
    #3の処理
    if A[2]<=B[2]:
      B[2]-=A[2]
      A[2]=0
      if A[0]<=B[1]*2:
        A[0]=B[1]=0
      else:
        A[0]-=B[1]*2
        B[1]=0
    else:
      A[1]-=B[1]
      B[1]=0
