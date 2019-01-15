'''
###서버
n,t=map(int, input().split());l=list(map(int,input().split()));c=0
for i in range(n):
 t-=l[i]
 if t<0:print(i);c=1;break
 elif t==0:print(i+1);c=1;break
if c==0:print(n)
'''
'''
###택시 기하학
import math;n=int(input());print(math.pi*n*n);print(n*n*2)
'''

'''
###올림픽
n,k=map(int,input().split());l=[]
for i in 'a'*n:
 a=list(map(int,input().split()))
 if a[0]==k:k=a[1:]
 l.append(a[1:])
l.sort(reverse=True);print(l.index(k)+1)
'''
'''
###소음
#a=input();x=input();b=input()
#print(eval(input()+input()+input()))
#결혼식
input();l=[];f=[];a=set()
for i in'a'*int(input()):
 m=sorted(list(map(int,input().split())))
 if m[0]==1 and m[1]!=1:f.append(m[1])
 else:l.append(m)
for _ in l:
 if f.count(_[0])==1 and f.count(_[1])==0:a.add(_[1])
 elif f.count(_[1])==1 and f.count(_[0])==0:a.add(_[0])
print(len(f)+len(a))
'''

'''
###수 이어쓰기 1
t=input();r=0
if len(t)==1:print(t)
else:
 for i in range(len(t)-1):r+=(i+1)*9*10**i
 print(r+(int(t[1:])+1)*(i+2)+(i+2)*(int(t[0])-1)*10**(i+1))
'''
'''
###폭죽쇼
from sys import stdin
n,c=map(int,stdin.readline().split());l=set()
for i in range(n):
    k=int(stdin.readline())
    for j in range(c//k):
        l.add(k*(j+1))
print(len(l))
'''
'''
n,c=map(int,input().split());l=[0]*(c+1)
for i in range(n):
 k = int(input())
 for _ in range(k,c+1,k):l[_]=1
print(sum(l))
'''
'''
n,c=map(int,input().split());t=[0]*(c+1)
for i in range(n):a=int(input());t[a::a]=[1]*len(t[a::a])
print(sum(t))
'''
'''
###수 정렬하기
import sys;l=[0]*10001;n=int(input())
for i in range(n):l[int(sys.stdin.readline())]+=1
for i in range(10001):print('%s\n'%i*l[i],end='')
'''
'''
E=5**6
l=[0]*E
f=open(0)
f.readline()
for i in f:l[int(i)]+=1
for i in range(E):print("%s\n"%i*l[i],end="")
'''
###DFS와 BFS

n,m,v=map(int,input().split());
l=[[]for x in range(n)];bfs=[];dfs=[]
for i in range(m):
    a,b=map(int,input().split())
    l[a-1].append(b)
    l[b-1].append(a)
dfs.append(v);stack=[];stack.append(v)
while 1:
    
    for _ in l[stack[-1]]:
        if not in stack:
            stack.append(_)
        
    



    
'''
v=dfs[0]

que=[]
que.append(v)
while 1:    
    for _ in l[v-1]:
        if bfs.count(_)==0 and que.count(_)==0:
            que.append(_)
    bfs.append(v)
    if len(bfs)==n:
        print(*bfs)
        break    
    del(que[0])
    #print(que,bfs)
    v=que[0]

''' 




'''
###수이어쓰기
n,t=map(str,input().split())
r=0
for i in range(len(t)):
    if (i+1)==len(t):
        r+=(int(t)%(10**i)+1)*(i+1)+(i+1)*(int(t[0])-1)*10**i
    else:
        r+=(i+1)*9*10**i   
print(r)
'''
'''
###순열의 순서
p='abcdefghijklmnopqrst'
#n=list(range(1,int(input())+1))
#k=list(map(int,input().split()))
#if k[0]==1:
for i in range():    
        
#else:
'''
