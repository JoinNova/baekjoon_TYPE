###K번째 수
#n,k=map(int,input().split());print(sorted(map(int,input().split()))[k-1])

###좌표 정렬하기
#l=[];k=[0,0]
#for _ in 'a'*int(input()):k=[0,0];k[0],k[1]=map(int,input().split());l.append(k)
#for _ in sorted(l):print(_[0],_[1])


###수학숙제
'''
import re;l=[]
for i in 'a'*int(input()):
 t=input();t=re.findall(r'\d+',t)
 for _ in t:l.append(int(_))
for _ in sorted(l):print(_)
'''
###ABC
'''
A,B,C=map(int,input().split());t=A+B+C;d={};r=''
d['A'],d['B'],d['C']=min(A,B,C),t-max(A,B,C)-min(A,B,C),max(A,B,C)
for _ in input():r+=str(d[_])+' '
print(r[:-1])
'''
'''
A,B,C=sorted(map(int,input().split()));print(*[eval(i) for i in input()])
'''
'''
###상근이의 체스판
r,c=map(int,input().split());a,b=map(int,input().split());k=0;p='X';t=str() 
for i in range(c*b):
 t+=p
 if (i+1)%b==0:k+=1
 if k%2==1:p='.'
 else:p='X'
for i in range(r*a):
 print(t)
 if (i+1)%a==0:t=t.replace('.','_');t=t.replace('X','.');t=t.replace('_','X')
'''
'''
###애너그램
t=[_ for _ in input()];c=0
for _ in input():
 try:t.remove(_)
 except:c+=1
print(len(t)+c)
'''
#큰수 a+b
#a=int(input());b=int(input());print(a+b,a-b,a*b)

'''
n=int(input())
while 1:
 c=int(input())
 if c==0:break
 if c%n==0:print("%d is a multiple of %d."%(c,n))
 else:print("%d is NOT a multiple of %d."%(c,n))
'''
###배수찾기
'''
n=int(input())
while(1):
 a=int(input())
 if a==0 :break
 print(str(a)+' is'+(' NOT' if a%n else '')+' a multiple of '+str(n)+ '.')
'''
#네번째 수
'''
a,b,c=sorted(map(int, input().split()))
if b-a==c-b:
 if c+c-b<=100:print(c+c-b)
 else:print(a-b+a)
elif b-a>c-b:print(a+c-b)
else:print(c-b+a)
'''
###오각형
#n=int(input())
#print((1+n+3*((n*(n+1))//2))%45678)
##최대곱
#s,k=map(int,input().split());a=s//k;b=s%k;print(a**(k-b)*(a+1)**b)





'''
###단어 수학
n=int(input());l=[];m=0
for i in 'a'*n:
    t=input().strip()
    m=max(len(t),m)
    l.append(t)
print(l,m)
'''
'''
###삼각형 만들기
n=int(input())
for i in range(n):
    l.append(int(input()))
'''


'''
###기숙사바닥
from math import gcd
r,b=map(int,input().split())
s=[]
chk=0
for i in range(3,r):
    if (r+b)%i==0:
        s.append(i)
for i in range(len(s)-1):
    for j in range(i+1,len(s)-1):
        if (r+b)==s[i]*s[j]:
            print(s[j],s[i])
            chk=1
            break
    if chk==1:
        break
'''
'''
#l*w=r+b

w=(r+b)/l

#(l-2)*(w-2)=b
l*w-2(l+w)+4=b
(r+4)/2=l+w

(r+4)/2=l+(r+b)/l
7=l+12/l
#2*l+2*(w-2)=r
l+w=(r+4)/2
'''
'''
###버블 소트
from sys import stdin;
n=int(stdin.readline());
l=list(map(int,stdin.readline().split()));
def mergeSort(A):
	### Base case ###
    if len(A) <= 1:
        return A

    ### A를 반으로 쪼개서 recursive call을 해 주고 정렬된 반쪽짜리들을 받아옵니다.  
    left = mergeSort(A[:len(A)//2])
    right = mergeSort(A[len(A)//2:])

    ### 여기서부터 두 개의 쪼개졌던 list를 합치는 Merge 부분입니다.
    ### 여기서 포인트는 정렬된 상태로 돌아왔기 때문에 앞에서부터 순차적으로 한번만 돌면 정렬시킬 수 있다는 것입니다.
    i, j, k = 0, 0, 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    if i == len(left): #만약 left의 원소를 모두 채웠고, right가 남아있을 때.
        while j<len(right):
            A[k] = right[j]
            j += 1
            k += 1
    elif j == len(right): #만약 right의 원소를 모두 채웠고, left가 남아있을 때.
        while i<len(left):
            A[k] = left[i]
            i += 1
            k += 1
    return A #마지막으로 정렬된 list를 리턴합니다.

#r=0;s=sorted(l)
print(mergeSort(l))
'''
'''
###국영수
l=[0]*4
for i in 'a'*int(input()):
    l=list(map(int,input().split()))
    print(l[0])
'''



'''
from sys import stdin
n=int(stdin.readline())
l=[]
d={}
for i in range(n):
    s=stdin.readline().strip()
    d[s]=
'''







'''
##나이순 정렬





from sys import stdin
l=[];k=[]
n=int(stdin.readline())
for _ in range(n):
    s=['0']*2
    s[0],s[1]=map(str,stdin.readline().split())
    k.append(s[0])
    l.append(' '.join(s))
s=sorted(k)
for i in range(n):
    r=k.index(s[i])
    print(l[r])
    l[r]='201 a'
    k[r]=201
'''
