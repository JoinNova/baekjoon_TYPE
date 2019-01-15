'''
###피보나치 수
from sys import stdin
a=0
b=1
n=int(stdin.readline())
if n==1:
    print(1)
else:
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    print(c)
'''
'''
###피보나치 수
from sys import stdin
a=0
b=1
n=int(stdin.readline())
if n==1:
    print(1)
else:
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    print(c)    
'''
'''
###피보나치 수 3
from sys import stdin
n=int(stdin.readline())%(15*10**5)
print(n)
print(15*10**5)
a=0
b=1
if n==1:
    print(1)
else:
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    print(c%1000000)  
'''
'''
from sys import stdin
import time
start_time = time.time()



#recursive solution
def fib(x, y, upperLimit):
    return [x] + fib(y, (x+y), upperLimit) if x < upperLimit else [x]

#To test :

print(fib(0,1,999999999))
print("run time: " + str(time.time() - start_time))
#print(f(int(stdin.readline())%(15*10**5))%1000000)
#fibonacci(int(input()))

'''
'''
import time
from sys import stdin
n=int(stdin.readline())%(15*10**5)
start_time = time.time()
a=0
b=1
if n==1:
    print(1)
else:
    for i in range(n-1):
        a,b=b,a+b
    print(b%1000000) 
    print("run time: " + str(time.time() - start_time))
'''
'''
#import time
from sys import stdin
def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
n=int(stdin.readline())%(15*10**5)
#start_time = time.time()
print(fib(n)%1000000)
#print("run time: " + str(time.time() - start_time))
'''
'''
from sys import stdin
def f(n):
    x=1
    y=1
    z=0
    for _ in bin(n)[3:]: 
        a = y*y
        x,y,z=x*x+a,(x+z)*y, a+z*z
        if _=='1':    
            x, y, z = x+y, x, y
    return y
n=int(stdin.readline())%(15*10**5)
print(f(n)%1000000)
'''
import time
from sys import stdin
f=0;g=1
n=int(stdin.readline())%1500000
start_time = time.time()
for i in range(n):    
    f,g=g,(f+g)%1000000
print(f)
print("run time: " + str(time.time() - start_time))
