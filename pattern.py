'''
###벌집
#1,7,19,37,61
#_6_12_18_24
n=int(input())
k=2
if n!=1:
    for i in range(0,n):
        k+=6*i
        if k>n:
            r=i+1
            break
else:
    r=1
print(r)

###분수찾기
n=int(input())
k=0
t=0
for i in range(1,10000000000):
    k+=i
    if k+1>n:
        t=i+1
        break
k=0
for i in range(1,10000000000,2):
    for j in range(i):
        k+=1
        u=j+1
        if n==k:
            break
    if n==k:
        break
    for j in range(u-1,0,-1):
        k+=1
        u=j
        if n==k:
            break
    if n==k:
        break
if n!=1:
    print("{0}/{1}".format(u,t-u))
else:
    print('1/1')

###Fly me to the Alpha Centauri
for i in range(int(input())):
    x,y=input().split()
    n=int(y)-int(x)
    a=0
    chk=0
    for i in range(n):
        chk+=1
        a+=int(i/2)+1
        if a>=n:
            break
    print(chk)
       
###ACM 호텔
for i in range(int(input())):
    p=str()
    h,w,n=input().split()
    x=(int(n)-1)//int(h)+1
    y=int(n)%int(h)
    if y==0:
        y=h
    x=str(x)
    if len(x)!=2:
        x='0'+x
    print('{0}{1}'.format(y,x))

###부녀회장이 될테야
for i in range(int(input())):
    k,n=input(),input()
    l=[]
    for j in range(int(n)):
        l.append(j+1)  
    for _ in range(int(k)):
        c=[]
        for j in range(int(n)):
            c.append(sum(l[:j+1]))
        l=c
    print(l[int(n)-1])

###방 번호
n=input()
n=n.replace('9','6')
d='012345678'
l=[]
for _ in d:
    l.append(n.count(_))
l[6]=int((l[6]+1)/2)
print(max(l))
'''

###카잉 달력
from fractions import Fraction
from sys import stdin

for i in range(int(stdin.readline())):
    m, n, x, y = map(int, stdin.readline().split())
    r=-1
    xl=[]
    yl=[]
    kb=int(str(Fraction(m,n)).split('/')[0])*n
    for i in range(int(kb/m)):
        xl.append(m*i+x)
    for i in range(int(kb/n)):
        yl.append(n*i+y)
    p=set(xl).intersection(yl)
    if len(p)!=0:
        print(int(list(p)[0]))
    else:
        print(r)

'''
for i in range(int(input())):
    m,n,x,y=map(int,input().split())    
    b=x%n
    c=x-m
    first=True
    while True:
        c+=m
        if c%n==y%n:
            break
        if c%n==b and first==False:
            c=-1
            break
        first=False
    print(str(c))
'''
'''
from fractions import Fraction
from sys import stdin
from math import gcd
for i in range(int(stdin.readline())):
    m, n, x, y = map(int, stdin.readline().split())
    g = gcd(m, n)
    k=Fraction(m, n)
    print(g,k)    
    mx = set([m * i + x % m for i in range(n // g)])
    ny = set([n * i + y % n for i in range(m // g)])
    if mx & ny:
        if mx & ny == {0}:
            print(m * n // g)
        else:
            print(list(mx & ny).pop())
    else: print(-1)
'''
