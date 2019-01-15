'''
###완전제곱수
from sys import stdin
from math import sqrt
m=int(stdin.readline().strip())
n=int(stdin.readline().strip())
l=[]
for i in range(int(sqrt(m)),int(sqrt(n))+1):
    k=i**2
    if k>=m and k<=n:
        l.append(k)
if l==[]:
    print(-1)
else:
    print('{0}\n{1}'.format(sum(l),l[0]))
'''

###제곱ㄴㄴ수
from sys import stdin
from math import sqrt
n,m = map(int,stdin.readline().split())
l=[]
for i in range(int(sqrt(n)),int(sqrt(m))+1):
    k=i**2
    if k>=n and k<=m:
        l.append(k)
print((m-n+1)-len(l))
