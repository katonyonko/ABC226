import io
import sys

_INPUT = """\
6
3
3 0
5 1 1
7 1 1
5
1000000000 0
1000000000 0
1000000000 0
1000000000 0
1000000000 4 1 2 3 4
3
3 0
5 0
7 1 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    cost=0
    while dq:
      x=dq.popleft()
      cost+=T[x]
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return cost
  N=int(input())
  T=[]
  G=[[] for _ in range(N)]
  for i in range(N):
    X=list(map(int,input().split()))
    t,K=X[0],X[1]
    if K>0: A=X[2:]
    T.append(t)
    for j in range(K):
      G[i].append(A[j]-1)
  print(bfs(G,N-1))