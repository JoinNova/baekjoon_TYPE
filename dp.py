
###1로만들기
'''
from sys import stdin
n=int(stdin.readline().strip())
#n=1*a+2**b+3**c
k=0
for i in range(n):
    print(n)
    if n==1:
        break
    elif n%3==0:
        print("n%3입니다.")
        n=int(n/3)
        k+=1
    elif (n-1)%3==0:
        print("(n-1)%3입니다.")
        n=int((n-1)/3)
        k+=2
    elif n%2==0:
        print("n%2입니다.")
        n=int(n/2)
        k+=1
    else:
        n=n-1
        k+=1
print(k)
'''
'''
from sys import stdin
def c(n,m):
    a=0
    b=0
    if not n in m:
        if n%3==0:
            a=dp(n/3)+1
        elif (n-1)%3==0:
            a=dp((n-1)/3)+2
        elif (n-2)%3==0:
            a=dp((n-2)/3)+3 
        if n%2==0:
            b=dp(n/2)+1
        elif (n-1)%2==0:
            b=dp((n-1)/2)+2
        m[n]=min(a,b)
    return m[n]
def dp(n):
    m = {1:0,2:1,3:1}
    return c(n,m)        
        
n=int(stdin.readline().strip())
print(dp(n))
'''
'''
###1로만들기2
from sys import stdin
r=[]
def c(n,m):
    a=0
    b=0    
    if not n in m:
        if n%3==0:
            a=dp(n/3)+1
        elif (n-1)%3==0:
            a=dp((n-1)/3)+2
        elif (n-2)%3==0:
            a=dp((n-2)/3)+3 
        if n%2==0:
            b=dp(n/2)+1
        elif (n-1)%2==0:
            b=dp((n-1)/2)+2
        m[n]=min(a,b)
    return m[n]
    
def dp(n):
    m = {1:0,2:1,3:1}
    return c(n,m)        
        
n=int(stdin.readline().strip())
result=dp(n)
print(result)
l=[]
if n!=1:
    for i in range(result):
        l.append(str(n))
        if n%2==0 and dp(n/2)==result-1:
            n=int(n/2)
        elif n%3==0 and dp(n/3)==result-1:
            n=int(n/3)
        else:
            n-=1
        result-=1
    print(' '.join(l),'1')
else:
    print(1)

'''
'''터렛 실패
###터렛
from sys import stdin
from math import sqrt
for i in range(int(stdin.readline())):
    x1,y1,r1,x2,y2,r2=map(int,stdin.readline().split())
    if x1==x2:
        if y1==y2:
            if r1==r2:
                if r1==0:
                    print(1)
                else:
                    print(-1)
            else:
                print(0)
        else:
            if abs(y1-y2)==r1+r2:
                print(1)
            elif abs(y1-y2)==abs(r1-r2):
                print(1)
            elif abs(y1-y2)>r1+r2:
                print(0)
            elif abs(y1-y2)<abs(r1-r2):
                print(0)
            else:
                print(2)
    else:
        if y1==y2:
            if abs(x1-x2)==r1+r2:
                print(1)
            elif abs(x1-x2)==abs(r1-r2):
                print(1)
            elif abs(x1-x2)>r1+r2:
                print(0)
            elif abs(x1-x2)<abs(r1-r2):
                print(0)
            else:
                print(2)
        else:
            if abs(x1-x2)**2+abs(y1-y2)**2==(r1+r2)**2:
                print(1)
            elif abs(x1-x2)**2+abs(y1-y2)**2>(r1+r2)**2:
                print(0)
            #elif abs(x1-x2)**2+abs(y1-y2)**2<(r1+r2)**2
            else:
                if abs(x1-x2)**2+abs(y1-y2)**2<abs(r1-r2)**2:
                    print(-1)
                elif abs(x1-x2)**2+abs(y1-y2)**2==abs(r1-r2)**2:
                    print(1)
                else:
                    print(2)
                
'''
'''
###수열 정렬
from sys import stdin
n=int(stdin.readline().strip())
l=list(map(int,stdin.readline().split()))
s=[0]*n
chk=0
for i in range(n):
    k=l.index(min(l))
    s[k]=str(chk)
    chk+=1
    l[k]=1001
print(' '.join(s))
'''
'''
###1, 2, 3 더하기         
from sys import stdin
def c(n,m):
    if not n in m:
        m[n]=dp(n-1)+dp(n-2)+dp(n-3)
    return m[n]
def dp(n):
    m = {1:1,2:2,3:4}
    return c(n,m)        

for i in range(int(stdin.readline())):        
    n=int(stdin.readline().strip())
    print(dp(n))

'''
'''
###1, 2, 3 더하기
T = int(input())
ns = []
for i in range(T):
  ns.append(int(input()))

L = max(ns)+1
d = [0]*L

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, L):
  d[i] = d[i-1]+d[i-2]+d[i-3]

for i in range(T):
  print(d[ns[i]])
'''
'''
n = int(input())
while n:
    x = int(input())
    d = [1,2,4]
    for i in range(3, x):
        d.append(d[i-1] + d[i-2] + d[i-3])
    print(d[x-1])
    n -= 1
'''
'''
def func():
	 b=int(input())
	 j=0
	 printlist=[]
	 while b>j:
		 a=int(input())
		 j+=1	 
		 i=3
		 num1=0
		 num2=1
		 num3=2
		 num4=4
		 while i<a:
			 i+=1
			 num4,num3,num2,num1=num4+num3+num2,num4,num3,num2
		 if a==3:
			 num4=4
		 elif a==2:
			 num4=2
		 elif a==1:
			 num4=1
		 printlist.append(num4%1000000009)
	 for num in printlist:
		 print(num)
            
func()
'''
'''
num = int(input())

lst = []
for _ in range(num):
    lst.append(int(input()))

ans = [1,2,4]
for i in range(3, max(lst)):
    ans.append(ans[i-1] + ans[i-2] + ans[i-3])

for i in lst:
    print(ans[i-1])

'''
'''
import sys
sys.setrecursionlimit(10000000)
limit = 150000
d = [[0]*4 for _ in range(limit+1)]

for i in range(1, limit+1):
    d[1][1]=1
    d[2][1]=1
    d[2][2]=1
    d[3][1]=2
    d[3][2]=1
    d[3][3]=1

    if(i>=4):
        d[i][1] = d[i-1][1] + d[i-1][2] + d[i-1][3]
        d[i][2] = d[i-2][1] + d[i-2][2] + d[i-2][3]
        d[i][3] = d[i-3][1] + d[i-3][2] + d[i-3][3]
 
n = int(input())
print(sum(d[n]))
'''
'''
import sys
_, *a = sys.stdin.read().splitlines()

def comb(x):
    if x==0 : return 1
    if x == 1: return 1
    if x == 2: return 2
    if cache[x] != -1 : return cache[x]
    cache[x] = comb(x-3)+comb(x-2)+comb(x-1)
    return cache[x]

for n in a:
    cache = [-1]*(int(n)+1)
    print(comb(int(n)))
'''
'''
###다리놓기 조합.
from math import factorial as f
from sys import stdin
for i in range(int(stdin.readline().strip())):
    n,m=map(int,stdin.readline().split())
    if n==m:
        print(1)
    elif n==1:
        print(m)
    else:
        print(int(f(m)/(f(n)*f(m-n))))
'''
'''
###약수 
from sys import stdin
n=int(stdin.readline().strip())
l=sorted(list(map(int,stdin.readline().split())))
print(l[0]*l[len(l)-1])
'''
'''
###직사각형에서 탈출
from sys import stdin
x,y,w,h=map(int,stdin.readline().split())
print(min(x,y,w-x,h-y))
'''
'''
###나누기
n=input()
f=int(input())
r=n[:-2]
h=0
while True:
    if h<10:
        r+='0'+str(h)
    else:
        r+=str(h)
    if int(r)%f==0:
        r=str(r)
        break
    else:
        r=r[:-2]
    h+=1
print(r[len(r)-2:])
'''
'''
###명령 프롬프트
from sys import stdin
n=int(stdin.readline().strip())
t=list(stdin.readline().strip())
for i in range(n-1):
    c=stdin.readline().strip()
    for j in range(len(t)):
        if t[j]!=c[j]:
            t[j]='?'
print(''.join(t))
'''
###저항
from sys import stdin
r=str()
chk=0
for i in range(2):
    n=stdin.readline().strip()
    if n=='black':
        if chk!=0:
            r+='0'
    elif n=='brown':
        r+='1'
    elif n=='red':
        r+='2'
    elif n=='orange':
        r+='3'
    elif n=='yellow':
        r+='4'
    elif n=='green':
        r+='5'
    elif n=='blue':
        r+='6'
    elif n=='violet':
        r+='7'
    elif n=='grey':
        r+='8'
    elif n=='white':
        r+='9'
    chk+=1
n=stdin.readline().strip()
if n=='brown':
    r+='0'
elif n=='red':
    r+='00'
elif n=='orange':
    r+='000'
elif n=='yellow':
    r+='0000'
elif n=='green':
    r+='00000'
elif n=='blue':
    r+='000000'
elif n=='violet':
    r+='0000000'
elif n=='grey':
    r+='00000000'
elif n=='white':
    r+='000000000'
if r.count('0')==len(r):
    print(0)
else:
    print(''.join(r))
