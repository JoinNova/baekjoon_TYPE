'''
import collections

deq = collections.deque(['a', 'b', 'c'])
deq.append('d')
print(deq)

deq.appendleft('d')

deq.extend('asdfgd')
print(deq)

while True:
    try:
        print(deq.pop(), end=' ')
    except IndexError:
        break


while True:
    try:
        print(deq.popleft(), end=' ')
    except IndexError:
        break


deq2 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq2.rotate(2)
print('deq2 >>', ' '.join(deq2))

deq4 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq4.rotate(-2)
print('deq4 >>', ' '.join(deq4))
'''
'''
###덱
from sys import stdin
import collections as c
d=c.deque()
for i in range(int(stdin.readline())):
    com=list(map(str,stdin.readline().split()))
    try:
        if com[0]=='push_front':
            d.appendleft(int(com[1]))
        elif com[0]=='push_back':
            d.append(int(com[1]))
        elif com[0]=='pop_front':        
            print(d[0])
            d.popleft()
        elif com[0]=='pop_back':        
            print(d[len(d)-1])
            d.pop()
        elif com[0]=='size':        
            print(len(d))
        elif com[0]=='empty':        
            if len(d)==0:
                print(1)
            else:
                print(0)
        elif com[0]=='front':        
            print(d[0])
        elif com[0]=='back':        
            print(d[len(d)-1])
    except:
        print(-1)
'''
'''
###회전하는큐
from sys import stdin
n,m=map(int,stdin.readline().split())
l=list(range(1,n+1))
p=list(map(int,stdin.readline().split()))
result=0
for _ in p:
    mv=0    
    while True:
        if _==l[0]:            
            if mv<=len(l)-mv:
                result+=mv
            else:
                result+=len(l)-mv
            del(l[0])
            break
        top=l[len(l)-1]
        l.pop()
        l.insert(0,top)
        mv+=1
print(result)
'''
'''
n, m = map(int, input().split())
l = [*map(int, input().split())]

cur = 1
move = 0

for idx, i in enumerate(l):
    move += min(abs(i - cur), n - abs(i - cur))
    n -= 1
    cur = i
    for a in range(idx + 1, len(l)):
        if l[a] > i:
            l[a] -= 1

print(move)
'''
'''
###AC
from sys import stdin
for i in range(int(stdin.readline())):
    c=stdin.readline().strip()
    n=int(stdin.readline())
    l=(stdin.readline().strip()[1:-1]).split(',')
    for _ in c:
        if _=='R':
            l=l[::-1]
        else:
            if len(l)!=0 and l!=['']:
                del(l[0])
            else:
                l='error'
    if l=='error':
        print('error')
    else:
        print('[',end='')
        for i in range(len(l)):
            if i == len(l)-1:
                print(l[i],end=']\n')
            else:
                print(l[i],end=',')
            
'''

###AC
from sys import stdin
for i in range(int(stdin.readline().strip())):
    chk=0
    chk2=0
    r=0
    d=0
    f=0
    e=0
    c=stdin.readline().strip()
    n=int(stdin.readline().strip())
    l=(stdin.readline().strip()[1:-1]).split(',')
    for _ in c:
        if _=='R':
            if chk==0:
                chk=1
            else:
                chk=0
        else:
            if n==0 :
                chk2=1
                break
            else:
                n-=1
                if chk==0:
                    f+=1
                else:
                    e+=1
    if chk2==1:
        print('error')
    elif n==0:
        print('[]')
    else:
        if chk==0:
            print('[',end='')
            for i in range(n):
                if i==n-1:
                    print(l[i+f],end=']\n')
                else:
                    print(l[i+f],end=',')
        else:
            print('[',end='')
            for i in range(n):
                if i==n-1:
                    print(l[len(l)-i-e-1],end=']\n')
                else:
                    print(l[len(l)-i-e-1],end=',')


