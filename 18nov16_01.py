'''
###A+B
n=list(map(int,input().split()))
print(n[0]+n[1])

###A-B
n=list(map(int,input().split()))
print(n[0]-n[1])


###터렛#########################
#import math
rl=[]
for i in range(int(input())):
    r=2
    l=list(map(int,input().split()))
    if l[0] == l[3] and l[1] == l[4]:
        r=-1
        if l[2] != l[5]:
            r=0
        elif l[2] == 0 :
            r=1
    else :
        if (l[3]-l[0])**2+(l[4]-l[1])**2>(l[2]+l[5])**2:
            r=0
        elif (l[3]-l[0])**2+(l[4]-l[1])**2==(l[2]+l[5])**2:
            r=1
    rl.append(r)
for i in range(len(rl)):
    if i==len(rl)-1:
        print(rl[i])
    else:
        print('%d '%rl[i])

###피보나치 함수
s=[1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141]
for i in range(int(input())):
    n=int(input())
    print(s[n],s[n+1])

###A/B
n=list(map(int,input().split()))
print(n[0]/n[1])
'''
'''
###수열 정렬
def soo(n,nl):
    r=[]
    l=[]
    sl=set(nl)
    for _ in sl:
        l.append(nl.count(_))
    for 
    
n=int(input())
nl=list(map(int,input().split()))
soo(n,nl)
'''
    
