'''
###아스키 코드
print(ord(str(input())))

###알파벳 찾기
l=[]
c=0
a=input()
for _ in 'abcdefghijklmnopqrstuvwxyz':
    try:
        l.append(a.index(_))
    except:
        l.append('-1')
for _ in l:
    c+=1
    if c==26:
        print(_)
    else:
        print(_,end=' ')

###문자열 반복
for i in range(int(input())):
    s=input().split()
    n=s[1]
    for j in range(len(n)):
        print(n[j]*int(s[0]),end='')
    print()

###단어 공부
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b='abcdefghijklmnopqrstuvwxyz'
t=input()
l=[]
for _ in a:
    l.append(t.count(_))
for i in range(len(b)):
    l[i]+=t.count(b[i])
m=max(l)
if l.count(m)==1:
    print(a[l.index(m)])
else:
    print('?')

###그룹 단어 체커
r=0
for i in range(int(input())):
    t=input()
    c=t[0]
    for j in range(1,len(t)):
        if t[j-1]!=t[j]:
            c+=t[j]
    if len(set(t))==len(c):
        r+=1
print(r)

###상수
a,b=input().split()
c,d=str(),str()
for i in range(3,0,-1):
    c+=a[i-1]
    d+=b[i-1]
print(max(c,d))

###다이얼
n=str()
r=0
for _ in input():
    k=ord(_)
    if k<68:
        r+=3
    elif k<71:
        r+=4
    elif k<74:
        r+=5
    elif k<77:
        r+=6
    elif k<80:
        r+=7
    elif k<84:
        r+=8
    elif k<87:
        r+=9
    else:
        r+=10
print(r)
'''
###크로아티아 알파벳
t=input()
t=t.replace('c=','_')
t=t.replace('c-','_')
t=t.replace('dz=','_')
t=t.replace('d-','_')
t=t.replace('lj','_')
t=t.replace('nj','_')
t=t.replace('s=','_')
t=t.replace('z=','_')
print(len(t))
