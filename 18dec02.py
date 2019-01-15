'''
###괄호 문자열
from sys import stdin
n,k=map(int,stdin.readline().split())
l=[]
for i in range(2**n):
    print(bin(i))
    b=bin(i)[2:]
    add=str()
    if len(b)<n:
        for j in range(n-len(b)):
            add+='0'
        add+=b
        b=add
    l.append(b)
print(l)
'''
'''
from sys import stdin
print(len(stdin.readline().strip()))
'''
'''
from sys import stdin
l='abcdefghijklmnopqrstuvwxyz'
t=list(stdin.readline().strip())
tl=[]
for _ in l:
    tl.append(str(t.count(_)))
print(' '.join(tl))
'''
'''
###하얀 칸
from sys import stdin
chk=0
result=0
for i in range(8):
    t=stdin.readline().strip()
    if chk%2==0:
        for j in range(8):
            if j%2==0:
                if t[j]=='F':
                    result+=1
    else:
        for j in range(8):
            if j%2!=0:
                if t[j]=='F':
                    result+=1
    chk+=1
print(result)
'''
'''
###팰린드롬인지 확인하기
from sys import stdin
t=stdin.readline().strip()
if t==t[::-1]:
    print(1)
else:
    print(0)
'''
###듣보잡
from sys import stdin
chk=0
l=set()
result=set()
n,m=map(int,stdin.readline().split())
for i in range(n):
    t=stdin.readline().strip()
    l.add(t)
for i in range(m):
    t=stdin.readline().strip()
    result.add(t)
    #result.append(t if t in l)
#result.sort()
#print(result)
result=sorted(l.intersection(result))
print(len(result))
print('\n'.join(result))
#for i in range(len(result)):
    #print(result[i])
#print('\n'.join(result))
