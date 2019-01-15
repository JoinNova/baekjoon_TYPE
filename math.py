###다면체
#for i in range(int(input())):v,e=map(int,input().split());print(2+e-v)
#for i in'a'*int(input()):a,b=map(int,input().split());print(b+2-a)
#exec("print(2-eval(input().replace(' ','-')));"*int(input()))
###아이들은 사탕을 좋아해
#for i in'a'*int(input()):n,k=map(int,input().split());print(sum(r//k for r in map(int,input().split())))
#exec("a,b=map(int,input().split());print(sum(map(lambda x:int(x)//b,input().split())));"*int(input()))
#for i in'a'*int(input()):N,K=map(int,input().split());print(sum(i//K for i in map(int,input().split())))
###남욱이의 닭장
#for i in'a'*int(input()):n,m=map(int,input().split());print(2*m-n,n-m)
#exec("n,m=map(int,input().split());print(2*m-n,n-m);"*int(input()))
#다각형의 대각선
#n=int(input());print(n*(n-1)*(n-2)*(n-3)//24)
#도미노
'''
n=int(input());i=0;s=0
while 1:
 i+=1;s+=i*(i+1)//2+i*(i+1)
 if i==n:break    
print(s)
'''
#n=int(input());print(n*(n+1)*(n+2)//2)
# 1  2    3     4   5   6   7   8   9   10
# 3 3+9 3+9+12+6
# 3  12   30

###3000번 버스
#for i in'a'*int(input()):print(2**int(input())-1)
#exec("print(2**int(input())-1);"*int(input()))
 #k=int(input())
 #r=2**(k-1)+k-1
 #for j in'b'*int(input()):r*=2;r+=1;print(r)
 #print(r)
#7 3.5 1.75 0.8
#1 0.5
'''
###사탕
n=int(input());l=[0]*n
for i in range(n):l[i]=int(input())
t=sum(l)/2
for i in range(int(n/2)):t-=l[2*i+1]
for i in range(n):print(int(t));t=l[i]-t

#print(l)
#a+b b+c c+d d+e e+a
#bc2d2e2fa -t =cdef
#cdef-def=c
#l-l[0]=cdef
'''
'''
###피보나치 수
a,b=0,1
for i in'a'*(int(input())%1500000):a,b=b,(a+b)%1000000
print(a)
'''
#a=0;b=1
#exec("a,b=b,a+b;"*int(input()));print(a)
'''
#a=0;b=1;exec("a,b=b,(a+b)%1000000;"*(int(input())%1500000));print(a)
'''

'''
###피보나치7
a,b=0,1
for i in'a'*(int(input())%1500000):a,b=b,(a+b)%1000000007
print(a)
'''
'''
###피보나치7
#a=0;b=1;exec("a,b=b,a+b;"*int(input()));print(a)
print('%.0f'%(((1+5**0.5)/2)**int(input())/5**0.5))
'''
'''
###곱셈
def f(a,b):
    if(b==0):return 1
    if(b%2==1):return a*f(a,b-1)%c
    else:h=f(a,b/2);return h*h%c
a,b,c=map(int,input().split())
print(f(a,b))
'''
'''
#print(pow(*map(int,input().split())))
###피보나치6
def f(n):
 m=1000000007
 if n==1:return [[1,1],[1,0]]
 else:
  t=f(n//2)
  t2=[[0,0],[0,0]]
  t2[0][0]=(t[0][0]*t[0][0]+t[0][1]*t[1][0])%m
  t2[0][1]=(t[0][0]*t[0][1]+t[0][1]*t[1][1])%m
  t2[1][0]=(t[1][0]*t[0][0]+t[1][1]*t[1][0])%m
  t2[1][1]=(t[1][0]*t[0][1]+t[1][1]*t[1][1])%m
  if n&1:
   t[0][0]=(t2[0][0]+t2[1][0])%m
   t[0][1]=(t2[0][1]+t2[1][1])%m
   t[1][0]=t2[0][0]
   t[1][1]=t2[0][1]
   return t
  return t2
n=int(input());print(f(n)[0][1])

'''
'''
###피보나치4
a=0;b=1;exec("a,b=b,a+b;"*int(input()));print(a)
'''
'''
###피보나치
#l=[1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,165580141,267914296,433494437,701408733][::-1]
for i in'a'*(int(input())):
 l=[];n=int(input());a,b=0,1
 for i in'a'*44:a,b=b,a+b;l.append(a)
 r=str();l=l[::-1]
 for _ in l:
  if n-_==0:r+=str(_)[::-1];break
  elif n-_>0:n-=_;r+=str(_)[::-1]+' '
 print(r[::-1])

#print(a,end=',')
'''
'''
###피보나치
def f(p,q):
 if p==1:return [[1,1],[1,0]]
 else:
  t=f(p//2,q)
  t2=[[0,0],[0,0]]
  t2[0][0]=(t[0][0]*t[0][0]+t[0][1]*t[1][0])%q
  t2[0][1]=(t[0][0]*t[0][1]+t[0][1]*t[1][1])%q
  t2[1][0]=(t[1][0]*t[0][0]+t[1][1]*t[1][0])%q
  t2[1][1]=(t[1][0]*t[0][1]+t[1][1]*t[1][1])%q
  if p&1:
   t[0][0]=(t2[0][0]+t2[1][0])%q
   t[0][1]=(t2[0][1]+t2[1][1])%q
   t[1][0]=t2[0][0]
   t[1][1]=t2[0][1]
   return t
  return t2
for i in range(int(input())):
 p,q=map(int,input().split())
 print('Case #{0}: {1}'.format(i+1,f(p,q)[0][1]))
'''
'''pypy3
for i in range(int(input())):
 a,b=0,1
 p,q=map(int,input().split())
 for _ in'a'*(p%1500000):a,b=b,(a+b)%q
 print('Case #{0}: {1}'.format(i+1,a))
'''
'''
###피보나치수의 개수
while True:
 x,y=map(int,input().split())
 if x==0 and y==0:break
 a,b,l=0,1,0
 while b<=y:
  a,b=b,(a+b)
  if b>=x and b<=y:l+=1
 print(l)
'''
'''
###수들의 합
s=int(input())
#(a*(a+1))//2)
for i in range(1,10000000000):
    s-=i
    if s<0:
        break
print(i-1)

'''
'''
###시그마
a,b=map(int,input().split())
if a>b:a,b=b,a
r=((b*(b+1))/2)-(((a-1)*a)/2)
if r>2147483647:
    r=2147483647
elif r<-2147483648:
    r=-2147483648
print('%d'%r)
'''
'''
###TV
a,h,l=map(int,input().split());r=a/(h*h+l*l)**0.5;print(int(h*r),int(r*l))
'''
###나머지와 몫이 같은 수
#n=int(input());print(sum(range(n))*(n+1))
'''
##진짜공간
import math;n,r=int(input()),0;s=list(map(int,input().split()));c=int(input());
for _ in s:r+=math.ceil(_/c)
print(r*c)
'''
'''
###손익분기점
a,b,c=map(int,input().split())
#a=고정비
#b=가변비
#c=판매단가
#r=손익분기점
#r=a/(c-b)
if b>=c:print(-1)
else:print(int(a/(c-b))+1)
'''
##한줄로서기
n=int(input())
l=list(map(int,input().split()))
r=['0']*n
print(r)





#chk=0
#n,l=map(int,input().split())
'''(m*(m+1))/2-((l-m-1)*(l-m))/2=n
m**m+m-(l-m-1)*(l-m)=2n   
2n=-l**l+l*m+l+m*l
2n=l(-l+2m+1)
2n/l=-l+2m+1
(2*n/l+l-1)/2=m'''
#print(n/l+l/2-1/2)


'''
a,b=map(int,input().split())
if a==b:print(a)
elif a>b:print('%d'%(((a*(a+1))/2)-(((b-1)*b)/2)))
else:print('%d'%(((b*(b+1))/2)-(((a-1)*a)/2)))
'''
'''
from sys import stdin
n,k=map(int,stdin.readline().split())
a,b,c,chk=0,0,0,0
q=n-k
for i in range(1,n+1):
    if i%5==0:

    if q//5!=0:
        b+=1
        q=q//5
    if q==0:
        break
for i in range(1,n+1):
    if k//5!=0:
        c+=1
        k=k//5
    if k==0:
        break
print(a,b,c)
print(a-b-c)

'''
#a,b=0,1
#for i in'a'*(int(input())):a,b=b,a+b
#print(a)

'''
def mul(a,b,r):
	return [[sum(i*j for i,j in zip(x,y))%r for y in b] for x in a]
def power(a,n,r):
	if n>1:
		x=power(a,n//2,r)
		x=mul(x,x,r)
		if n%2!=0:
			return mul(x,a,r)
		else:
			return(x)
	else:
		return(a)
for i in range(int(input())):
	b,n=map(int,input().split())
	print("Case #%d: %d"%(i+1,power([[1,1],[1,0]],b,n)[1][0]))

'''
'''
from sys import stdin
for i in range(int(stdin.readline())):
    n=stdin.readline().strip()
    k=n[len(n)-6:]
    a,b,r=0,1,0
    if n==1:
        r==2
    else:
        for i in range(100001):
            if str(b)[len(str(b))-6:]==k:
                r=i+1
                break
            a,b=b,a+b        
    print(r)
'''




'''
###
t=int(input())
chk=0
chk2=0

for i in range(t):
    l=[]
    c=i+1
    a=c
    for j in range(t):
        d=a+j
        b=d
        for i in'a'*(t):
            a,b=b,a+b
            l.append(a)
            if b==t:
                chk=1
                break
            elif b>t:
                chk2=1
                break
        if chk==1 or chk2==1:
            break
    if chk==1:
        break
print(c,d)
print(l)
'''



'''
from sys import stdin
while True:
    try:
        a,b='0','1'
        n=int(stdin.readline())
        p=stdin.readline().strip()[::-1]
        for i in range(n):
            a,b=b,a+b
        c=0
        for i in range(len(a)-len(p)+1):
            if a[i:i+len(p)]==p:
                c+=1
        print(c)
    except EOFError:
        break
'''


'''
###피보나치 홀수합
a,b=0,1
for i in'a'*((int(input())*2+2)%1500000):a,b=b,(a+b)%1000000007
print(a-1)
'''
