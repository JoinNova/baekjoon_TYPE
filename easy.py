'''
###수 찾기
from sys import stdin
n=int(stdin.readline().strip())
nl=set(map(int,stdin.readline().split()))
m=int(stdin.readline().strip())
ml=list(map(int,stdin.readline().split()))
for _ in ml:
    print(len(nl.intersection({_})))
'''
'''
###16진수
print(int(input(),16))
'''
'''
###2진수 8진수
print(oct(int(input(),2))[2:])
'''
'''
###8진수 2진수
print(bin(int(input(),8))[2:])
'''
'''
###사파리월드
from sys import stdin
n,m=map(int,stdin.readline().split())
print(abs(n-m))
'''
'''
###분산처리
from sys import stdin
for i in range(int(stdin.readline().strip())):
    a,b=map(str,stdin.readline().split())
    aa=a[len(a)-1:]
    if aa=='1':
        print(1)
    elif aa=='2':
        l=[2,4,8,6]
        if int(b)%4-1==-1:
            print(l[3])
        else:
            print(l[int(b)%4-1])
    elif aa=='3':
        l=[3,9,7,1]
        if int(b)%4-1==-1:
            print(l[3])
        else: 
            print(l[int(b)%4-1])
    elif aa=='4':
        l=[4,6]
        if int(b)%2-1==-1:
            print(l[1])
        else:
            print(l[int(b)%2-1])
    elif aa=='5':
        print(5)
    elif aa=='6':
        print(6)
    elif aa=='7':
        l=[7,9,3,1]
        if int(b)%4-1==-1:
            print(l[3])
        else:
            print(l[int(b)%4-1])
    elif aa=='8':
        l=[8,4,2,6]
        if int(b)%4-1==-1:
            print(l[3])
        else:
            print(l[int(b)%4-1])
    elif aa=='9':
        l=[9,1]
        if int(b)%2-1==-1:
            print(l[1])
        else:
            print(l[int(b)%2-1])
    else :
        print(10)
'''



'''
###달팽이
from sys import stdin
n=int(stdin.readline().strip())
#f=int(stdin.readline().strip())
for i in range(n):
    l=[]
    for j in range(n):
        if j==0:
            l.append(str(n**2-i))
        elif j==n-1:
            l.append(str())
        else:
            l.append(str())
    print(' '.join(l))
 '''   

