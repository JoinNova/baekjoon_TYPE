'''
###카약
from sys import stdin
s=[0,0,0,0,0,0,0,0,0]
r,c=map(int,stdin.readline().split())
score=0
for i in range(r):
    t=stdin.readline().strip()[1:-1]
    if t.count('.')!=c-2:
        for j in range(len(t)):
            if t[j]=='.':
                score+=1
            else:
                s[int(t[j])-1]=score
                break
        score=0
rank=list(sorted(set(s),reverse=True))
for i in range(9):
    print(rank.index(s[i])+1)
'''
'''
###여우는 어떻게 울지?
from sys import stdin
#n=int(stdin.readline().strip())
for k in range(int(stdin.readline().strip())):
    t=list(map(str,stdin.readline().split()))
    s=set()
    while True:
        a=list(map(str,stdin.readline().split()))
        if a==['what','does','the','fox','say?']:
            break
        #l[a[0]]=a[2]
        s.add(a[2])
    #print(s)
    for i in range(len(t)):
        if t[i] not in s:
            if i!=len(t)-1:
                print(t[i],end=' ')
            else:
                print(t[i])
'''
'''
###Java vs C++
from sys import stdin
p='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t=stdin.readline().strip()
if t.count('__')==0 and p.count(t[0])==0 and t[len(t)-1]!='_' and t[0]!='_':
    if t.count('_')==0:
        for i in range(len(t)):
            if t[i].isupper()==True:
                print('_',end='')
            if i!=len(t)-1:
                print(t[i].lower(),end='')
            else:
                print(t[i].lower())
    else:
        for _ in t:
            if p.count(_)>0: 
                print('Error!')
                break
        else:
            chk=0
            for i in range(len(t)):
                if i==len(t)-1:
                    if chk==1:
                        print(t[i].upper())
                    else:
                        print(t[i])
                elif t[i]=='_':
                    chk=1
                elif chk==1:
                    print(t[i].upper(),end='')
                    chk=0
                else:
                    print(t[i],end='')
else:
    print('Error!')
'''
'''
###반지
from sys import stdin
p=stdin.readline().strip()
r=0
for i in range(int(stdin.readline().strip())):
    chk=0
    t=stdin.readline().strip()
    for i in range(10):
        pivot=t[0]
        t=t[1:]+t[0]
        if t.count(p):
            chk=1
    if chk==1:
        r+=1
print(r)
'''
'''
###균형잡힌 세상
from sys import stdin
from re import sub
while True:
    t=str(stdin.readline())
    t=sub(r'[\n]','',t)
    if t=='.' and len(t)==1:
        break
    c=sub(r'[ .\w\n]','',t)
    for i in range(50):
        c=sub(r'[(]{1}[)]{1}','',c)
        c=sub(r'[[]{1}[]]{1}','',c)
    if len(c)!=0:
        print('no')
    else:
        print('yes')
'''
'''
###데이트
from sys import stdin
a=stdin.readline().strip()
ini=0
r=[]
for i in range(int(stdin.readline().strip())):
    b=stdin.readline().strip()
    s=a+b
    l=s.count('L')
    o=s.count('O')
    v=s.count('V')
    e=s.count('E')
    #print(l,o,v,e)
    chk=((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100
    if i==0:
        ini=chk
        #print(b)
        r.append(b)
    else:
        if chk>ini:
            r[0]=b
            ini=max(chk,ini)
        elif chk==ini:
            r.append(b)
            #print(r)
            r.sort()
            #print(r)
            r.pop()
            #print(r)
print(''.join(r))
'''
'''
###Miscalculation
from sys import stdin
t=stdin.readline().strip()
a=int(stdin.readline().strip())
c=eval(t)
#print(c)
r=0
n=str()
#print('len(t)',len(t))
for i in range(0,len(t)-2,2):
    #print(t[i])
    if i==0:
        n+=t[i]
    n+=t[i+1]
    n+=t[i+2]
    r=eval(n)
    n=str(r)
    #print(r)
#print(r)
r=int(r)
if len(t)!=1:
    if a==c:
        if a==r:
            print('U')
        else:
            print('M')
    else:
        if r==a:
            print('L')
        else:
            print('I')
else:
    if a==int(t):
        print('U')
    else:
        print('I')
'''
'''
###HTML
import sys
#from re import sub
su=str()
result=str()
chk=0
chk2=0
b='<br>'
h='<hr>'
while True:
    try:
        t=input().split()
    except EOFError:
        break
    for i in range(len(t)):
        chk2+=1
        if t[i]==b:
            su+='\n'
            chk=0
            chk2=0
        elif t[i]==h:
            if t[i-1].isalnum()==True:
                su+='\n'
                chk=0
                chk2=0
            su+='--------------------------------------------------------------------------------\n'
            chk=0
            chk2=0
        else:
            chk+=len(t[i])
            if chk+chk2>80:
                su+='\n'
                chk=0
                chk2=0
                chk+=len(t[i])
            su+=t[i]+' '
                
    
            
print(su)
    #sys.stdout.write(t)
'''
'''
###문자열
from sys import stdin
for i in range(int(stdin.readline().strip())):
    t=stdin.readline().strip()
    n=str()
    if len(t)==1:
        n=t+t
        print(n)
    else:
        n=t[0]+t[len(t)-1]
        print(n)
'''
'''
###사이클 단어
from sys import stdin
l=[]
for i in range(int(stdin.readline().strip())):
    t=stdin.readline().strip()
    chk=0
    if i==0:
        l.append(t)
    else:
        n=str()
        for i in range(len(t)):
            n=t[i:]+t[:i]
            if l.count(n)!=0:
                chk=1
                break
            
        if chk==0:
            l.append(t)
print(len(l))
'''

'''
l=[]
for i in range(int(input())):
    s=input()
    f=True
    for j in range(len(s)):
        if s[j:]+s[:j] in l:
            f=False
            break
    if f:l.append(s)
print(len(l))
'''
'''
###추월
from sys import stdin
n=int(stdin.readline().strip())
l=[]
chk=0
for i in range(n):
    l.append(stdin.readline().strip())
for i in range(n):
    c=stdin.readline().strip()
    if l[i]!=c:
        del(l[l.index(c)])
        l.insert(0,c)
        chk+=1
print(chk)
'''
'''
###출력 형식이 잘못되었습니다
from sys import stdin
from re import sub
n=int(stdin.readline().strip())
for i in range(n):
    a=stdin.readline().strip().lower()
    b=stdin.readline().strip().lower()
    for j in range(max(a.count(' '),b.count(''))):
        a=sub(r'[ ]{2}?',' ',a)
        b=sub(r'[ ]{2}?',' ',b)
    a=sub(r'[{]','(',a)
    b=sub(r'[{]','(',b)
    a=sub(r'[}]',')',a)
    b=sub(r'[}]',')',b)
    a=sub(r'[[]','(',a)
    b=sub(r'[[]','(',b)
    a=sub(r'[]]',')',a)
    b=sub(r'[]]',')',b)
    a=sub(r'[;]',',',a)
    b=sub(r'[;]',',',b)
    a=sub(r'[:]{1} ',':',a)
    b=sub(r'[:]{1} ',':',b)
    a=sub(r' [:]{1}',':',a)
    b=sub(r' [:]{1}',':',b)
    a=sub(r'[,]{1} ',',',a)
    b=sub(r'[,]{1} ',',',b)
    a=sub(r' [,]{1}',',',a)
    b=sub(r' [,]{1}',',',b)
    a=sub(r'[.]{1} ','.',a)
    b=sub(r'[.]{1} ','.',b)
    a=sub(r' [.]{1}','.',a)
    b=sub(r' [.]{1}','.',b)
    a=sub(r'[(]{1} ','(',a)
    b=sub(r'[(]{1} ','(',b)
    a=sub(r' [)]{1}',')',a)
    b=sub(r' [)]{1}',')',b)
    a=sub(r'[(]{1} ','(',a)
    b=sub(r'[(]{1} ','(',b)
    a=sub(r' [)]{1}',')',a)
    b=sub(r' [)]{1}',')',b)

    
    #print(a)
    #print(b)

    if i!=n-1:
        if a==b:
            print('Data Set {}: equal\n'.format(i+1))
        else:
            print('Data Set {}: not equal\n'.format(i+1))
    else:
        if a==b:
            print('Data Set {}: equal'.format(i+1))
        else:
            print('Data Set {}: not equal'.format(i+1))    
'''
'''
###문장
from sys import stdin
from re import sub
p1=['one','two','three','four','five','six','seven','eight','nine','ten']
p2=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
p3=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
p4=['onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred']
n=int(stdin.readline().strip())
l=[]
a=str()
chk=0
for i in range(n):
    t=stdin.readline().strip()
    chk+=len(t)
    if t=='$':
        idx=i
    l.append(t)
    
#print(chk)
#print(idx)
#print(' '.join(l))
chk3=0
for i in range(999):    
    if i+1<=10:
        t=p1[i]
    elif i+1<=19:
        t=p2[i%10]
    elif (i+1)%10==0 and len(str(i+1))==2:
        t=p3[(i+1)//10-2]
    elif len(str(i+1))==2:
        t=p3[i//10-2]+p1[i%10]
    elif (i+1)%100==0:
        t=p4[i//100-1]
    else:
        t=p4[i//100-1]
        j=int(str(i+1)[1:])
        if j<=10:
            t+=p1[j-1]
        elif j<=19:
            t+=p2[(j-1)%10]
        elif j%10==0 and len(str(j))==2:
            t+=p3[j//10-2]
        elif len(str(j))==2:
            t+=p3[(j-1)//10-2]+p1[(j-1)%10]
    #print(t)
    if i+1==(len(t)+chk-1):
        del(l[idx])
        l.insert(idx,t)
        break
#print(chk)

print(' '.join(l))
'''

###Unreliable Messengers
'''J rotates
“aB23d” to “B23da”.
C rotates
“aB23d” to “daB23”
E swaps the left half of the message
“aB23d” to “3d2aB”
“e3ac” to “ace3”
A reverses
“aB23d” to “d32Ba”
P increments by one all the digits
“aB23d” to “aB34d”
“e9ac” to “e0ac”
M decrements by one
 “aB23d” to “aB12d”,
“e0ac” to “e9ac”.'''
'''
#from sys import stdin
for i in range(int(input())):
    c=input().strip()[::-1];f=input();l=len(f);k=int(l/2)
    for _ in c:
        if _=='C':f=f[1:]+f[0]
        if _=='J':f=f[len(f)-1]+f[:-1]
        if _=='E':
            if l%2==0:f=f[k:]+f[:k]
            else:f=f[k+1:]+f[k]+f[:k]
        if _=='A':f=f[::-1]
        if _=='P':
            for j in range(l):
                if f[j].isnumeric()==True:
                    f=f[:j]+str((int(f[i])-1)%10)+f[i+1:]
        if _=='M':
            for i in range(l):
                if f[i].isnumeric()==True:
                    f=f[:i]+str((int(f[i])+1)%10)+f[i+1:]
    print(f)
'''
from sys import stdin
from fractions import Fraction as f
a=1
b=1
for i in range(int(stdin.readline().strip())):
    t=stdin.readline().strip().split('/')
    a*=int(t[0])
    b*=int(t[1])
print(f(a,b))





'''
###유성
from sys import stdin
r,s=map(int,stdin.readline().split())
l=[]
dl=[]
for i in range(r):
    t=stdin.readline().strip()
    if t.count('.')==s:
        l.insert(0,t)
    else:
        l.append(t)
    for j in range(s):
        t[j]=
print('\n'.join(l))

'''



'''
###36진수
l=[]
c=[]
for i in range(int(input())):
    nn=input()
    c.append(nn)
    l.append(str(int(nn,36)))
n=int(input())
print(' '.join(c))
print(' '.join(l))
#print((1019108*7))
#print(int(7133756,36))  

'''
'''
#ZUCK
print(1672292*7)

def convert(n, base):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


print(convert(1672292*5, 16))
'''



'''
###가로 세로 퍼즐
from sys import stdin
l=[]
for i in range(6):
    t=stdin.readline().strip()
    l.append(t)
s=list(set(l))
chk=0
for i in range(6):
'''    
    


'''
###괄호 제거
from sys import stdin
from re import sub
t=stdin.readline().strip()
l=[]
m=sub(r'\w?(\w?)\w?','',t)
print(m)
print()
n=sub(r'[/\+\-\*]','',m)
print(n)
'''

'''
###올바른 바이너리 문자열
from sys import stdin
from re import sub
for i in range(int(stdin.readline().strip())):
    t=stdin.readline().strip()
    if len(t)%2==0 and abs(t.count('1')-t.count('0'))<=t.count('.'):
        n=t.split('.')
        chk2=0
        for _ in n:
            print(_)
            if _!='':
                chk1=0
                for j in range(len(_)-1):
                    #print(chk2)
                    if _[j]==_[j+1]:
                        chk1+=1
                    else:
                        chk1=0
                    if chk1==2:
                        chk2=1
        if chk2==1:
            print('no')
        else:
            print('yes')
                    
                
    else:
        print('no')
'''

'''
    result=str()
    t=sub(r'\n','',HTML)
    t=sub(r'[<][b][r][>]','\n',t)
    #print(t)
    t=sub(r'[<][h][r][>]','\n--------------------------------------------------------------------------------\n',t)
    #print(t)
    #flen=len(t)
    print(t)
'''








'''
###괄호 문자열
from sys import stdin
from re import sub
n,m=map(int,stdin.readline().split())
l=[]
result=[]
for i in range(2**n):
    t=str()
    b=bin(i)[2:]
    if len(b)<n:
        b='0'*(n-len(b))+b
    #t=sub('0','(',b)
    #t=sub('1',')',t)
#    for _ in b:
#        if _=='0':
#            t+='('
#        else:
#            t+=')'
    chk=sub(r'[0]{1}[1]{1}','',b)
    for i in range(50):
        chk=sub(r'[0]{1}[1]{1}','',chk)
    if len(chk)!=0:
        result.append(b)
        
    #l.append(b)
    #print(b)
#print(l)
        
#for _ in l:
    #print(_)
    #chk=sub(r'[0]{1}[1]{1}','',_)
    #for i in range(25):
        #chk=sub(r'[0]{1}[1]{1}','',chk)
    #print(chk)
    #if len(chk)!=0:
        #result.append(_)
try:
    print(result[m])
except:
    print(-1)
'''            

'''
###민식어
from sys import stdin
p=['a','b','k','d','e','g','h','i','l','m','n','ng','o','p','r','s','t','u','w','y']
for i in range(int(stdin.readline().strip())):
    t=stdin.readline().strip()
    for i in :
'''



'''
###
t='abc efg'
a='0120123'
tl=[]
al=[]
for _ in t:
    print(_,hex(ord(_))[2:],end=' ')
    tl.append(int(hex(ord(_))[2:]))
print()
for _ in a:
    print(_,hex(ord(_))[2:],end=' ')    
    al.append(int(hex(ord(_))[2:]))
print()
for i in range(len(t)):
    print(t[i],ord(str((tl[i]+al[i])%2)),end=' ')
'''
'''
###놀라운 문자열
from sys import stdin
while True:
    t=stdin.readline().strip()
    if t=='*':
        break
    l=[]
    for i in range(len(t)-1):
        
        
    print(t)
'''















'''
###배부른 마라토너
from sys import stdin
from collections import OrderedDict
#d=deque()
#l=[]
#s=set()
o=OrderedDict()
print(type(o))
n=int(stdin.readline().strip())
for i in range(n):
    o[stdin.readline().strip()]+=1
    #d[i]=stdin.readline().strip()
    #l.append(stdin.readline().strip())
    print(o)
for i in range(n-1):
    o.move_to_end(stdin.readline().strip())
    #print(d.get(stdin.readline().strip()))
    #del(d[d.get(stdin.readline().strip())])
    print(o)

    #l.remove(stdin.readline().strip())
#print(''.join(l))
print(o)
'''   


 
