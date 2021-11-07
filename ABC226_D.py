import io
import sys

_INPUT = """\
6
3
1 2
3 6
7 4
3
1 2
2 2
4 2
4
0 0
0 1000000000
1000000000 0
1000000000 1000000000
5
0 0
3 1
6 2
9 3
-3 -1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  N=int(input())
  points=[list(map(int,input().split())) for _ in range(N)]
  ans=set()
  for i in range(N):
    for j in range(N):
      if i==j: continue
      x,y=points[i][0]-points[j][0],points[i][1]-points[j][1]
      if x==0:
        if y>0: ans.add((0,1))
        else: ans.add((0,-1))
      elif y==0:
        if x>0: ans.add((1,0))
        else: ans.add((-1,0))
      else:
        d=math.gcd(abs(x),abs(y))
        ans.add((x//d,y//d))
  print(len(ans))