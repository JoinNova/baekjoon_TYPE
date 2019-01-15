'''
for i in 'a'*int(input()):
 t,a=0,0
 for i in 'a'*int(input()):
   c,s=map(float,input().split())
   t+=c
   a+=c*s
 k=str(a/t).split('.')
 if len(k[1])==1:
  k=float(k[0]+'.'+k[1][0]) 
 elif int(k[1][1])>=5:
  if str(int(k[1][0])+1)=='10':
   k=float(str(int(k[0])+1)+'.'+'0')
  else:k=float(k[0]+'.'+str(int(k[1][0])+1))
 else:
  k=float(k[0]+'.'+k[1][0])  
 print('%d %.1f'%(t,k))
'''
'''
from sys import stdin
n=int(stdin.readline())
l=list(map(int,stdin.readline().split()))
r=0
for i in range(n-1):
    for j in range(1,n-i):
        if l[j-1]>l[j]:
            l[j-1],l[j]=l[j],l[j-1]
            r+=1
            
print(r)
'''
'''
n=int(input())
a=""
while len(a)<n:
	try:
		a+=input()+" "
	except:
		break
a=list(map(int,a.split()))
while len(a)<n:
	a.append(0)
b=sorted((a[i],i) for i in range(n))
for i in range(n):
	a[b[i][1]]=n-i
d=[0]*(n+1)
r=0
for i in range(n):
	j=a[i]
	while j:
		r+=d[j]
		j-=j&-j
	j=a[i]
	while j<=n:
		d[j]+=1
		j+=j&-j
print(r)
'''
'''
input()
a=m=-1e9
for x in input().split():
    a=max(0,a)+int(x)
    m=max(m,a)
print(m)
'''
'''
T = (0,0,0)
for i in range(int(input())):
    r,g,b = [int(x) for x in input().split()]
    T = min(T[1],T[2])+r,min(T[0],T[2])+g,min(T[0],T[1])+b
print(min(T))
'''
'''
###5525
n=int(input());m=int(input());s=input();l=0;c=0
while 1:
 l=s.find('IO'*n+'I',l)
 if l<0:break
 l+=2*n+1;c+=1
 while 1:
  if s[l:l+2]=='OI':c+=1;l+=2
  else:break
print(c)
'''

'''
###9935
word, bomb = input(), list(input())
res = []
for char in word:
	res.append(char)
	if res[-len(bomb):] == bomb:
		res[-len(bomb):] = []
print(''.join(res) if res else "FRULA")
'''
'''
###10814
l=[]
for i in range(int(input())):
 a,b=input().split()
 l.append((int(a),i,b))
for e in sorted(l):print(e[0],e[2])
'''
'''
###10868
import sys
n, m = map(int, input().split())
min_d = {}
min_d[1] = [int(line) for _, line in zip(range(n), sys.stdin)]
i = 1
while i * 2 <= n:
    i *= 2
    min_d[i] = list(map(min, *2 * [iter(min_d[i // 2])]))

def trailing(s):
    for i in range(s.bit_length()):
        if s&1<<i: return i
    return 0

def d(a,b):
    x = trailing(a)
    x = x if x>0 else 1
    res = 1
    while res.bit_length()<x+1 and a + res <= b: res <<= 1
    return res >> 1


for _, line in zip(range(m), sys.stdin):
    a, b = map(int, line.split())
    a -= 1
    l = 10**10
    while a < b:
        q = d(a, b)
        l = min(l, min_d[q][a // q])
        a += q
    print(l)

'''
'''
##11051
from math import factorial
a,b=map(int,input().split())
print((factorial(a)//(factorial(b)*factorial(a-b)))%10007)
'''

###16719
'''
p='ABCDEFGHIJKLMNOPQRSTUVWXYZ'    
t=input();l=[];l.append(t);tl=len(t)
#print(l)
while 1:
    if len(t)==3:
        if ord(t[0])>ord(t[1]):
            t=t[1]+t[2]
            l.append(t)
            if ord(t[0])>ord(t[1]):
                l.append(t[1])
            else:l.append(t[0])
        else:
            if ord(t[1])>ord(t[2]):
                t=t[0]+t[2]
                l.append(t)
                if ord(t[0])>ord(t[1]):
                    l.append(t[1])
                else:l.append(t[0])
            else:
                t=t[0]+t[1]
                l.append(t)
                if ord(t[0])>ord(t[1]):
                    l.append(t[1])
                else:l.append(t[0])
        break
    try:
        for i in range(len(t)-1):
            if ord(t[i])>ord(t[i+1]):
                t=t[:i]+t[i+1:]
                #print(t)
                l.append(t)
                break
    except:pass
#print(l)
#print('\n'.join(l[::-1]))
for i in range(tl):
    print(l[tl-1-i])

'''
'''
s = input()
pub = [''] * len(s)
for i in range(len(s)):
    mn = ("[", -1)
    for j in range(len(s)):
        if pub[j]: continue
        pub[j] = s[j]
        mn = min(mn, (''.join(pub), j))
        pub[j] = ''
    pub[mn[1]] = s[mn[1]]
    print(mn[0])
'''
'''
for  i in 'a'*100:
    print('키파 생일 축하')
'''
'''
from sys import stdin
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def simplify_fraction(numer, denom):
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)

    if reduced_den == 1:
        return simplify_fraction(numer//reduced_num, denom//reduced_num)
    elif common_divisor == 1:
        return numer,denom
    else:
        return simplify_fraction(reduced_num, reduced_den)
n=int(stdin.readline())
f=e=1
for i in range(n):
    t=stdin.readline().split('/')
    k=simplify_fraction(int(t[0]),int(t[1]))
    if k[0]!=0:
        f*=k[0]
    if k[1]!=0:
        e*=k[1]
print('%d/%d'%(f,e))
'''
'''
from sys import stdin
from fractions import Fraction as f
from fractions import gcd as g
a=1
b=1
n=int(stdin.readline())
s=''
for i in range(n):
    s+=stdin.readline() 
for t in s[:-1].split('\n'):
    t=t.split('/')
    #k=str(f(int(t[0]),int(t[1]))).split('/')
    d=g(int(t[0]),int(t[1]))
    a*=int(t[0])//d
    try:
        b*=int(t[1])//d
    except:pass
print(f(a,b))
'''
