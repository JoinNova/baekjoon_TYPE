'''
###수 정렬하기
l=[]
for i in range(int(input())):
    l.append(int(input()))
l=sorted(l)
for i in range(len(l)):
    print(l[i])

###수 정렬하기 2
from sys import stdin
l=[]
for i in range(int(stdin.readline())):
    l.append(int(stdin.readline()))
l=sorted(l)
for i in range(len(l)):
    print(l[i])
'''
'''
###수 정렬하기 3
m=10000
a=list(map(int,input().split()))
#a=[]
#for i in range(int(input())):
    #a.append(int(input()))
print(a)
n=len(a)
c=[0]*(m+1)
s=[0]*(m+1)
for i in range(n):
    c[a[i]]+=1
s[0]=c[0]
for i in range(1,m+1):
    s[i]=s[i-1]+c[i]
b=[0]*(n+1)

for i in range(n-1,-1,-1):
    b[s[a[i]]]=a[i]
    s[a[i]]=1

result=''
for i in range(1,n+1):
    if i<=n-1:
        result+=str(b[i])+"\n"
    else:
        result+=str(b[i])    
print(result)
'''
'''
def countingSort(arr, digit):
    n = len(arr)
  
    # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성한다. 
    output = [0] * (n)
    count = [0] * (10)
    
    #digit, 자릿수에 맞는 count에 += 1을 한다. 
    for i in range(0, n):
        index = int(arr[i]/digit) 
        count[ (index)%10 ] += 1
 
    # count 배열을 수정해 digit으로 잡은 포지션을 설정한다.  
    for i in range(1,10):
        count[i] += count[i-1]  
        #print(i, count[i])
    # 결과 배열, output을 설정한다. 설정된 count 배열에 맞는 부분에 arr원소를 담는다.   
    i = n - 1
    while i >= 0:
        index = int(arr[i]/digit)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    #arr를 결과물에 다시 재할당한다.  
    for i in range(0,len(arr)): 
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
    # arr 배열중에서 maxValue를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다. 
    maxValue = max(arr)  
    #자릿수마다 countingSorting을 시작한다. 
    digit = 1
    while int(maxValue/digit) > 0: 
        countingSort(arr,digit)
        digit *= 10

arr=[]
for i in range(int(input())):
    arr.append(int(input())) 
#arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
#arr = [4, 2, 1, 5, 7, 2]
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i], end="\n")
'''
'''
from sys import stdin
key = [ 0 ]
i = 1
N = int(stdin.readline())

while i < 10001:
    key += [ 0 ]
    i += 1
    
while N:
    key[int(stdin.readline())] += 1
    N -= 1

i = 1
while i < 10001:
    j = 0
    while j < key[i]:
        print(i)
        j += 1
    i += 1
'''
'''
import sys
n = int(sys.stdin.readline())
lst = [0]*10001
for i in range(n):
    lst[int(sys.stdin.readline())] += 1
for i in range(n+1):
    for j in range(lst[i]):
        print(i)
'''
'''
from sys import stdin
m=10000
p=[0]*(m+1)
t=int(stdin.readline())
for i in range(t):
    p[int(input())]+=1
for i in range(m+1):
    print('%s\n'%i*p[i],end='')
'''
'''
###통계학
from sys import stdin
import statistics as st
import numpy as np
from collections import Counter

#from math import 
l=[]
for i in range(int(stdin.readline())):
    l.append(int(stdin.readline()))
print(round(sum(l)/len(l)))
#print(int(round(np.mean(l))))
l=sorted(l)
#ll=len(l)
#if ll<2:
#    print(l[0])
#elif ll%2==0:
#    print((l[int(ll/2)]+l[int(ll/2-1)])/2)
#else:
#    print(l[int(ll/2)])
print(st.median(l))
#c=0
#chk=0
#chk2=0
#print(s)
if len(l)!=1:
    data = Counter(l)
#print(data.most_common(2))
    if (data.most_common(2)[0])[1]==(data.most_common(2)[1])[1]:
        print((data.most_common(2)[1])[0])
    else:
        print((data.most_common(1)[0])[0])  
else:
    print(l[0])
#print(data.most_common(2)[1])
print(max(l)-min(l))

'''
###소트인사이드
from sys import stdin
s=sorted(stdin.readline()[:-1])[::-1]
for _ in s:
    print(_,end='')


'''
###단어 정렬
def q(li):
    if len(li)<=1:
        return li
    p=li[len(li)//2]
    le,mo,eq = [],[],[]
    for _ in li:
        if len(_)<len(p):
            le.append(_)
        elif len(_)>len(p):
            mo.append(_)
        else:
            eq.append(_)
    return q(le)+eq+q(mo)
    

from sys import stdin
l=[]
for i in range(int(stdin.readline())):
    s=stdin.readline()[:-1]
    if l.count(s)==0:
        l.append(s)
for _ in q(sorted(l)):
    print(_)
'''

