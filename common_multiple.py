'''
####최소공배수
import time
from sys import stdin
from fractions import Fraction
from math import gcd

for i in range(int(stdin.readline())):
    start_time = time.time()
    m, n= map(int, stdin.readline().split())
    g = gcd(m, n)
    k=Fraction(m, n)
    print(int(str(k).split('/')[0])*n)
print("run time: " + str(time.time() - start_time))

####최소공배수
from sys import stdin
from fractions import Fraction
for i in range(int(stdin.readline())):
    m, n= map(int, stdin.readline().split())
    k=Fraction(m, n)
    print(int(str(k).split('/')[0])*n)

####최대공약수와 최소공배수
from sys import stdin
from fractions import Fraction
from math import gcd
m, n= map(int, stdin.readline().split())
k=Fraction(m, n)
print(gcd(m, n))
print(int(str(k).split('/')[0])*n)
'''
'''
###최대공약수
from sys import stdin
from math import gcd
m, n= map(int, stdin.readline().split())
for _ in range(gcd(m, n)):
    print('1',end='')
'''

###검문
from sys import stdin
from math import gcd
from fractions import Fraction
n=int(stdin.readline())
a=int(stdin.readline())
l=[]
result=0
if n>2:
    for i in range(n-1):
        b=int(stdin.readline())
        c=b-a
        if i!=0:
            result=gcd(c,d)
        d=c
        a=b
        #l.append(b)
        #k=Fraction(a, b)
        #print(int(str(k).split('/')[0])*n)
else:
    b=int(stdin.readline())
    result=b-a
for i in range(2,result+1):
    if result==i:
        #l.append(i)
        print(i)
        #i+=k
    elif result%i==0:
        #l.append(str(i))
        print(i,end=' ')
        #i+=k

        
'''    
i=2
k=1
while result>=i:
    if result==i:
        l.append(i)
        print(i)
        i+=k
    elif result%i==0:
        l.append(str(i))
        print(i,end=' ')
        i+=k
    else:
        i+=k
        k+=1
'''        
#print(' '.join(l))
#for i in range(n):
'''
###링
from sys import stdin
from fractions import Fraction
n=int(stdin.readline())
nl=list(map(int,stdin.readline().split(' ')))
for i in range(n-1):
    if nl[i+1]<nl[0]:
        print('{0}/{1}'.format(str(Fraction(nl[i+1],nl[0])).split('/')[1],str(Fraction(nl[i+1],nl[0])).split('/')[0]))
    elif nl[i+1]==nl[0]:
        print('1/1')
    else:
        print('{0}/{1}'.format(str(Fraction(nl[0],nl[i+1])).split('/')[0],str(Fraction(nl[0],nl[i+1])).split('/')[1]))
'''
