###sys.stdin.readline()
'''
###시험 성적
import sys
n=int(sys.stdin.readline())
if n>89:
    print('A')
elif n>79:
    print('B')
elif n>69:
    print('C')
elif n>59:
    print('D')
else:
    print('F')

###세 수
#import sys
#print(sorted(list(sys.stdin.readline().split()),reverse=True)[1])
print(sorted(map(int,input().split()))[1])
print(sorted(input().split(),key=int)[1])

#X보다 작은 수
n=input().split()
r=str()
for i in [_ for _ in map(int,input().split()) if int(n[1])>_]:
    r+=str(i)+' '
print(r[:len(r)-1])

N,X=input().split();print(*(t for t in input().split()if int(t)<int(X)))

###평균
n=int(input())
nl=list(map(int,input().split()))
new=0
m=max(nl)
for _ in nl:
    new+=_/m*100
print(new/n)

###평균은 넘겠지
l=[]
for i in range(int(input())):
    n=list(map(int,input().split()))
    a=sum(n[1:])/n[0]
    c=0
    for _ in n[1:]:
        if _>a:
            print(_)
    #for j in range(n[0]):
        #if n[j+1]>a:
            c+=1
    l.append(c/n[0]*100)
for _ in l:
    print("%.3f"%_+'%')
'''
###더하기 사이클
def n(c,a,b):
    c+=1
    if len(a)==1:
        a='0'+a
    s=0
    w=str()
    for _ in a:
        s+=int(_)
    s=str(s)
    if len(s)==1:
        s='0'+s
    w=a[1]+s[1]
    w=int(w)
    if w!=b:
        w=str(w)
        return n(c,w,b)
    return c
c=0
a=str(input())
b=int(a)
print(n(c,a,b))

