'''
###5와 6의 차이
from sys import stdin
from re import sub
a,b=map(str,stdin.readline().split())
a=sub('6','5',a)
b=sub('6','5',b)
print(int(a)+int(b),end=' ')
a=sub('5','6',a)
b=sub('5','6',b)
print(int(a)+int(b))
'''
'''
###접미사 배열
from sys import stdin
t=stdin.readline().strip()  
l=set()
for i in range(len(t)):
    l.add(t[i:])
l=sorted(l)
print('\n'.join(l))
'''
'''
###모음의 개수
from sys import stdin
p=['a','e','i','o','u']
chk=0
for _ in (stdin.readline().strip()):
    if p.count(_)==1:
        chk+=1
print(chk)
'''
'''
###카이사르의 암호
from sys import stdin
p='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t=stdin.readline().strip()
n=str()
for _ in t:
    if p.index(_)<2:
        n+=p[26+p.index(_)-3]
    else:
        n+=p[p.index(_)-3]
print(n)
'''
'''
###문자열
from sys import stdin
a,b=stdin.readline().split()
r=50
for i in range(len(b)-len(a)+1):
    c=0
    n=str()
    n=b[:i]+a+b[len(a)+i:]
    for j in range(len(n)):
        if n[j]!=b[j]:
            c+=1
    r=min(c,r)
print(r)
'''
'''
###유학 금지
from sys import stdin
from re import sub
print(sub(r'[CAMBRIDGE]','',stdin.readline().strip()))
'''
'''
###알파벳 거리
from sys import stdin
p='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(stdin.readline().strip())):
    a,b=map(str,stdin.readline().split())
    l=[]
    for j in range(len(a)):
        if p.index(b[j])>=p.index(a[j]):
            l.append(str(p.index(b[j])-p.index(a[j])))
        else:
            l.append(str((p.index(b[j])+26)-p.index(a[j])))
    print('Distances:',' '.join(l))
'''
'''
###JOI와 IOI
from sys import stdin
j='JOI'
i='IOI'
t=stdin.readline().strip()
a=0
b=0
for k in range(len(t)-2):
    if t[k:k+3]==j:
        a+=1
    elif t[k:k+3]==i:
        b+=1
print('%s\n%s'%(a,b))
'''
'''
###민균이의 비밀번호
from sys import stdin
l=[]
for i in range(int(stdin.readline().strip())):
    t=stdin.readline().strip()
    l.append(t)
    if l.count(t[::-1])==1:
        break
print(len(t),t[int(len(t)/2)])
'''
'''
###FBI
from sys import stdin
from re import sub
l=[]
c='FBI'
for i in range(5):
    t=stdin.readline().strip()
    a=sub(c,'',t)
    if t!=a:
        l.append(str(i+1))
if len(l)==0:
    print('HE GOT AWAY!')
else:
    print(' '.join(l))
'''
'''
###8진수
print(oct(int(input(),2))[2:])
'''
'''
###지영공주님의마법거울
from sys import stdin
l=[]
for i in range(int(stdin.readline().strip())):
    l.append(stdin.readline().strip())
n=int(stdin.readline().strip())
if n==1:
    print('\n'.join(l))
elif n==2:
    ll=[]
    for _ in l:
        ll.append(_[::-1])
    print('\n'.join(ll))
else:
    print('\n'.join(l[::-1]))
'''
'''
###가장 많은 글자
from sys import stdin
p='abcdefghijklmnopqrstuvwxyz'
s={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
#t=stdin.readline()
while True:
    try:
        l = input()
    except EOFError:
        break
    for i in range(len(p)):
        s[p[i]]+=l.count(p[i])

for _ in p:
    if s[_]==max(s.values()):
        print(_,end='')
'''
'''
###행복한지 슬픈지
from sys import stdin
from re import findall as f
t=stdin.readline().strip()
h=f(r'[:][\-][)]',t)
u=f(r'[:][\-][(]',t)
if len(h)==len(u):
    if len(h)==0:
        print('none')
    else:
        print('unsure')
elif len(h)>len(u):
    print('happy')
else:
    print('sad')
'''
'''
###컵홀더
from sys import stdin
from re import sub
a=int(input())
t=stdin.readline().strip()
t=sub('S','*S*',t)
t=sub('LL','*LL*',t)
t=sub('[*]{2}','*',t)
print(min(a,t.count('*')))
'''
'''
###크로스워드 만들기
from sys import stdin
a,b=stdin.readline().split()
ai=0
bi=0
chk=str()
for i in range(len(a)):
    if b.count(a[i])!=0:
        ai=i
        chk=a[i]
        break
for i in range(len(b)):
    if b[i]==chk:
        bi=i
        break
for i in range(len(b)):
    l=str()
    if i!=bi:
        for j in range(len(a)):
            if j!=ai:
                l+='.'
            else:
                l+=b[i]
        print(l)
    else:
        print(a)
'''
'''
###한국이 그리울 땐 서버에 접속하지
from sys import stdin
n=int(stdin.readline().strip())
p=stdin.readline().strip().split('*')
for i in range(n):
    t=stdin.readline().strip()
    #print(t[:len(p[0])],p[0])
    #print(t[len(t)-len(p[1]):],p[1])
    if t[:len(p[0])]==p[0]:
        if t[len(t)-len(p[1]):]==p[1]:
            if len(p[0])+len(p[1])-1<=len(t):
                print('DA')
            else:
                print('NE')
        else:
            print('NE')
    else:
        print('NE')
#    if bool(search(p[0],t))==True:
#        print((t.split(p[0]))[1])
#        if bool(search(p[1],(t.split(p[0]))[1]))==True:
#            print('DA')
#        else:
#            print('NE')
#    else:
#        print('NE')
'''
'''
###문서검색
from sys import stdin
from re import sub
t=stdin.readline().strip()
p=stdin.readline().strip()
print((sub(p,'_',t)).count('_'))
'''
'''
###블라인드
from sys import stdin
n,m=map(int,stdin.readline().split())
chk=0
s={0:0,1:0,2:0,3:0,4:0}
l=[0]*m
chk=0
for i in range(n*5+1):
    t=stdin.readline().strip()
    if i%5!=0 and i!=n*5:
        #print(t)
        for j in range(1,m*5,5):
            if t[j]=='*':
                #print(chk)
                #print(l[chk])
                l[chk]+=1
            chk+=1
        chk=0
        #print(l)
    if (i+1)%5==0:
        for _ in l:
            s[_]+=1
        l=[0]*m
for i in range(5):
    if i==4:
        print(s[i])
    else:
        print(s[i],end=' ')
'''

###밑 줄
from sys import stdin
n,m=map(int,stdin.readline().split())
l=[]
tt=0
for i in range(n):
    t=stdin.readline().strip()
    tt+=len(t)
    l.append(t)
s=(m-tt)%(n-1)  ###밑줄 추가갯수
d=(m-tt)//(n-1) ### 공평한 밑줄
result=str()
for i in range(n):
    if i==n-1:
        if s>0:
            print('_',end='')
            print(l[i])
        else:
            print(l[i])
        #result+=n[i]
    else:
        if l[i][0].isupper()==True and s<(n-i):
            print(l[i],end=('_'*d))
        else:
            if s!=0:
                print('_',end='')
                s-=1            
            print(l[i],end=('_'*d))
        #result+=n[i]
        #result+='_'*d
#print(result)


'''
###가르침
from sys import stdin
n,k=map(int,stdin.readline().split())
for i in range(n):
    t=stdin.readline().strip()

'''

'''
###IOIOI
from sys import stdin
from re import sub
n=int(stdin.readline().strip())
p=int(stdin.readline().strip())
s=stdin.readline().strip()
chk=0
r=0
rr=0
for i in range(len(s)-1):
    print(s[i:i+2])
    if s[i:i+2]=='IO':
        chk=1
    else:
        r=0
        chk=0
    if chk==1 and (s[i+1:i+3]=='IO' or s[i+1]=='I'):
        r+=1
    if r==n:
        r-=1
        rr+=1
print(rr)

'''




'''
###암호
from sys import stdin
p='abcdefghijklmnopqrstuvwxyz'
n=stdin.readline().strip()
k=stdin.readline().strip()
r=str()
for i in range(len(n)):
    try:
        #print(n[i],k[(i+1)%len(k)-1])
        #print(p.index(n[i]),p.index(k[(i+1)%len(k)-1]))
        if p.index(n[i])>=p.index(k[(i+1)%len(k)-1]):
            r+=p[p.index(n[i])-p.index(k[(i+1)%len(k)-1])-1]
        else:
            r+=p[26+p.index(n[i])-p.index(k[(i+1)%len(k)-1])-1]                        
    except:
        r+=' '
print(r)
'''
'''
###애너그램 만들기
from sys import stdin
r=0
a=list(stdin.readline().strip())
b=list(stdin.readline().strip())
chk=set(a).intersection(b)
chka=set(a).symmetric_difference(b)
chkb=set(b).symmetric_difference(a)
r=len(chka)+len(chkb)
for _ in chk:
    if a.count(_)!=b.count(_):
        r+=abs(a.count(_)-b.count(_))
print(r)
'''
'''
###문자열 폭발
from sys import stdin
from re import sub
t=stdin.readline().strip()
d=stdin.readline().strip()
s=re.sub(" \&\& ", " and ", s)
print(t)
'''
