'''
###농구 경기
#a='abcdefghijklmnopqrstuvwxyz'
#l=[0]*26
l=str();c=0
for i in range(int(input())):l+=input()[0]
for _ in sorted(set(l)):
    if l.count(_)>=5:print(_,end='');c=1
if c==0:print('PREDAJA')
'''
'''
###나무 조각
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    for j in range(1,len(l)-i):
        if l[j-1]>l[j]:
            l[j-1],l[j]=l[j],l[j-1]
            print(l[0],l[1],l[2],l[3],l[4])
        if l==[1,2,3,4,5]:
            c=1
            break
    if c==1:
        break       
'''
'''
a = list(map(int,input().split()))
while a != [1,2,3,4,5]:
    for i in range(4):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            print(' '.join(map(str,a)))
'''
'''
a=input().split();i=3
while[*'12345']<a:
 i=-~i%4;z=a[i+1]
 if a[i]>z:a[i:i+2]=z,a[i];print(*a)
'''
'''
###날짜 계산
l=list(map(int,input().split()));e,m,s=0,0,0;i=0
while True:
    i+=1;e+=1;m+=1;s+=1
    if [e,m,s]==l:break
    if e==15:e=0
    if m==28:m=0
    if s==19:s=0
print(i)
'''
'''
###유니코드
print(chr(44031+int(input())))
'''
'''
###한글2
print(ord(input())-44031)
'''
'''
import re
b,c,j=44032,588,28
l=['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
m=['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
n=[' ','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
s=[input()]
r=[]
for _ in s:
    if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', _) is not None:
        h = ord(_)-b
        a=int(h/c)
        r.append(l[a])
        b=int((h-(c*a))/j)
        r.append(m[b])
        d=int((h-(c*a)-(j*b)))
        r.append(n[d])
    else:
        r.append(_)
print("\n".join(r))
'''
'''
a='ㄱ'
aa='ㄴ'
b='ㅗ'
c='ㄴ'
d='곤'
print(a.encode("utf-8"))
print(aa.encode("utf-8"))
print(b.encode("utf-8"))
print(c.encode("utf-8"))
print(d.encode("utf-8"))
print((a+b+c).encode("utf-8"))
print((a+b+c).encode("utf-8").decode("utf-8"))
'''
###소인수분해
a=2;c=0;n=int(input())
for i in range(n):
    if n%a==0:
        print(a)
        n=n/a
        if n==1:c=1;break
    else:a+=1
    #if c==1:
        #break




'''
###4와7
from re import sub;print(sub('1','7',sub('0','4',bin(int(input())+1)[3:])))
'''
'''
4,7,44,47,74,77,444,447,474,477,744,747,774,777
1 2  3 4  5  6   7   8   9   10  11  12 13   14
  2         2+4                             2+4+8
n%2
1 10 11 100 101 110 111
'''
'''
###Sort Me
from sys import stdin
chk2=0
result=str()
while True:
    chk2+=1
    l=[]
    t=stdin.readline().strip().split()
    if t[0]=='0':
        break
    p=t[1]
    for i in range(int(t[0])):
        s=stdin.readline().strip()
        l.append(s)
    for i in range(int(t[0])):
        for j in range(1,int(t[0])-i):
            chk=0
            a=l[j-1]
            b=l[j]
            for k in range(min(len(a),len(b))):
                if p.index(a[k])==p.index(b[k]):
                    chk+=1
                elif p.index(a[k])>p.index(b[k]) and chk==k:
                    l[j-1],l[j]=l[j],l[j-1]
                    break
                else:
                    break
    result+='year '+str(chk2)+'\n'
    for _ in l:
        result+=_+'\n'
                
                
print(result[:-1])           
'''
