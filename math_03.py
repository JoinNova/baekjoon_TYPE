#조합
#from math import factorial as f;n,m=map(int,input().split());print(f(n)//f(m)//f(n-m))
#중앙이동 알고리즘
#3*3 5*5 9 17
#()**2
#print((2**int(input())+1)**2)
'''
#핸드폰 요금
n=input();l=list(map(int,input().split()));y,m=0,0
for _ in l:y+=(_//30+1)*10;m+=(_//60+1)*15
if y<m:print('Y',y)
elif y>m:print('M',m)
else:print('Y','M',m)
'''
'''
###세로읽기
r=str();l=[]
for i in 'a'*5:t=input();l.append(t)
while 1:
 ll=[]
 for _ in l:
   if len(_)!=0:r+=_[0];_=_[1:];ll.append(_)
 l=ll        
 if len(l)==0:break
print(r)
'''
'''
t=int(input())
for i in 'a'*9:t-=int(input())
print(t)
'''
'''
###에라토스테네스의 체
n,k=map(int,input().split());l=[_ for _ in range(2,n+1)];h=0;r=0
while 1:
 c=[]
 for _ in l:
  if _%l[0]==0:h+=1
  else:c.append(_)
  if h==k:r=_;break
 if h==k:break
 l=c
print(r)
'''
'''
###0 = not cute / 1 = cute
n=int(input());k=0
for i in 'a'*n:k+a=int(input())
print('Junhee is '+'not '*(n//2>=k)+'cute!')
'''
'''
###거스름돈
r=0;p=1000-int(input());
r+=p//500;p=p%500;
r+=p//100;p=p%100;
r+=p//50;p=p%50;
r+=p//10;p=p%10;
r+=p//5;p=p%5;
r+=p//1;print(r)
'''
'''
###심부름 가는 길
a=sum([int(input()) for _ in 'a'*4]);print('%d\n%d'%(a//60,a%60))
#print(*divmod(eval('+int(input())'*4),60))
s=sum([int(input()) for i in'i'*4]);print(s//60);print(s%60)
'''
'''
###타임 카드
for i in 'a'*3:
 l=list(map(int,input().split()));s=l[5]-l[2]
 if s<0:
  s+=60;m=l[4]-l[1]-1
  if m<0:m+=60;h=l[3]-l[0]-1
  else:h=l[3]-l[0]
 else:
  m=l[4]-l[1]
  if m<0:m+=60;h=l[3]-l[0]-1
  else:h=l[3]-l[0]     
 print(h,m,s)
'''
'''
###수빈이와 수열
n=int(input());t=[];a=0;b=list(map(int,input().split()))
for i in range(n):r=b[i]*(i+1)-a;t.append(str(r));a+=r
print(' '.join(t))
'''
'''
##POT
r=0;exec('t=input();r+=int(t[:-1])**int(t[-1]);'*int(input()));print(r)
'''   
###10부제
#n=input();print(list(map(str,input().split())).count(n))
##3콘테스트
#w=[];k=[]
#for i in range(10):w.append(int(input()))
#for i in range(10):k.append(int(input()))
#w.sort(reverse=True);k.sort(reverse=True)
#print(sum(w[:3]),sum(k[:3]))
###시험 점수
#print(max(sum(map(int,input().split())),sum(map(int,input().split()))))
'''
###STROJOPIS
p=['1QAZ','2WSX','3EDC','45RFVBGT','67YHNMJU','8IK,','9OL.','0P;/-[\'=]'];t=input()
for _ in p:
 r=0
 for __ in _:r+=t.count(__)
 print(r)
'''
'''

###기상캐스터
h,w=map(int,input().split());l=[]
for i in 'a'*h:
    t=input()
    if t.count('c')!=0:
        r=[];chk=-1
        for _ in t:
            if _=='c':
                chk=0
                r.append(str(chk))
            elif chk>=0:
                chk+=1
                r.append(str(chk))
            else:
                r.append(_)
        t=r    
    t=' '.join(t)
    #print(t)
    t=t.replace('.','-1')
    l.append(t)
#print(l)
print('\n'.join(l))

'''
'''
###앵그리 창영
n,w,h=map(int,input().split())
for i in 'a'*n:
 if int(input())>(w*w+h*h)**0.5:print('NE')
 else:print('DA')

'''
'''
###점수계산 
s=[0];l=[]
for i in 'a'*8:
    a=int(input())
    s.append(a)
t=sorted(s)
for i in range(5):
    if t[len(t)-i-1]!=0:
        l.append(s.index(t[len(t)-i-1]))
print(sum(t[-5:]))
l.sort()
for i in range(len(l)):
    if i==len(l)-1:
        print(l[i])
    else:
        print(l[i],end=' ')
'''
###수도요금
#a=int(input());b=int(input());c=int(input())
#d=int(input());p=int(input())
#if (p-c)*d>0:print(min(a*p,(p-c)*d+b))
#else:print(min(a*p,b))


###상근날드9
#a=int(input());b=int(input());c=int(input());d=int(input());e=int(input())
#print(min(a,b,c)+min(d,e)-50)
'''
#TGN
for i in 'a'*int(input()):
 r,e,c=map(int,input().split());
 if e-c>r:print('advertise');
 elif e-c==r:print("does not matter");
 else:print("do not advertise");
'''
'''
###유니크
n=int(input());a=[0]*n;b=[0]*n;c=[0]*n;s=[0]*n
for i in range(n):a[i],b[i],c[i]=map(int,input().split())
for i in range(n):
    if a.count(a[i])==1:
        s[i]+=a[i]
for i in range(n):
    if b.count(b[i])==1:
        s[i]+=b[i]
for i in range(n):
    if c.count(c[i])==1:
        s[i]+=c[i]
for _ in s:print(_)
'''
'''
##공약수
from math import gcd
n=int(input())
l=list(map(int,input().split()))
if n==2:
    for i in range(1,gcd(l[0],l[1])+1):
        if gcd(l[0],l[1])%i==0:
            print(i)
else:
    k=gcd(l[0],l[1])
    k=gcd(k,l[2])
    for i in range(1,k+1):
        if k%i==0:
            print(i)
'''
###과제
#l=[str(_) for _ in range(1,31)];exec('del(l[l.index(input())]);'*28);print('\n'.join(l))
'''
##직각삼각형
while 1:
 l=sorted(map(int,input().split()));
 if l[2]==0:break
 print(['wrong','right'][l[0]**2+l[1]**2==l[2]**2])
'''   
###방학 숙제
#import math;l=int(input());a=int(input());b=int(input());c=int(input());d=int(input());print(l-max(math.ceil(a/c),math.ceil(b/d)))

###내 학점을 구해줘
#exec('t,a=0,0;exec(\'c,s=map(float,input().split());t+=c;a+=c*s;\'*int(input()));print(\'%d %.1f\'%(t,a/t));'*int(input()))
'''      
###알람시계
h,m=map(int,input().split());m=m-45
if m<0:m+=60;h-=1
if h<0:h+=24
print(h,m)
'''
t=input();l=len(t);r=''
for i in range(l-1):
 if int(t[-1])>=5:t=str(int(t[:-1])+1);r+='0'
 else:t=t[:-1];r+='0'
print(t+r)
    


        




'''
t=input();r=0
for i in range(len(t)):
    if int(t)//10!=0:
        r+=9*10**i
        t=t[:-1]
    if t=='':
        break
print(r)
'''
        
'''
###음식평론가
n,m=map(int,input().split())
1/m
1/3
'''



'''
###책 페이지
k=0
for i in range(int(input())):
    k+=str(i+1).count('0')
    print('%d'%(i+1),k)
'''
