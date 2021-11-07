import io
import sys

_INPUT = """\
6
3 3
1 2
1 3
2 3
2 1
1 2
7 7
1 2
2 3
3 4
4 2
5 6
6 7
7 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  mod=998244353
  def bfs(G,s):
    res=[]
    D[s]=0
    dq=deque()
    dq.append(s)
    res.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
          res.append(y)
    res=list(set(res))
    return res
  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    u,v=map(int,input().split())
    u-=1; v-=1
    G[u].append(v)
    G[v].append(u)
  inf=10**30
  ans=1
  D=[inf]*len(G)
  for i in range(N):
    if D[i]<inf: continue
    p=bfs(G,i)
    c=0
    for j in p:
      c+=len(G[j])
    if len(p)*2==c: ans=ans*2%mod
    else: ans=0
  print(ans)