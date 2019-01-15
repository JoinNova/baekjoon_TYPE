#print(int(input())-1946)

#n=input();print(input().count(n))
#print(input().upper())

#exec('print(int(input(),2));'*int(input()))
#import re;exec('t=input().replace(" ","");r=len(re.findall(r"[AEIOUaeiou]",t));print(len(t)-r,r);'*int(input()))
'''
d=r=0
for _ in input():
 if _!=d:r+=10
 else:r+=5
 d=_
print(r)
'''
'''
p='/-\(@?>&%'
while 1:
 r=0;t=input();k=len(t)-1
 if t=='#':break
 for _ in t:r+=(p.index(_)-1)*8**k;k-=1
 print(r)
       
'''
'''l
while 1:
 t=input();r='yes'
 if t=='0':break
 if t!=t[::-1]:r='no'
 print(r)
'''
#input();print(*sorted(map(int,input().split()))[:1000])
#r=0;exec('r+=int(input());print(r);'*int(input()))
'''
a='ABC';b='BABC';c='CCAABB';input();x=y=z=i=0
for _ in input():
 if _==a[(i+3)%3]:x+=1
 if _==b[(i+4)%4]:y+=1
 if _==c[(i+6)%6]:z+=1
 i+=1
r=max(x,y,z);print(r)
if x==r:print('Adrian')
if y==r:print('Bruno')
if z==r:print('Goran')
'''
'''
t=input()
while t!='0 W 0':
 e=eval(t.replace('W','-').replace('D','+'))
 if e>=-200:print(e)
 else:print('Not allowed')
 t=input()
'''
'''
t=input()
if t==t[::-1]:print('true')
else:print('false')
'''
'''
n,k=map(int,winput().split());r=[]
l=list(range(n*k,n,-n))
for _ in l:
    r.append(int(str(_)[::-1]))
print(max(r))
'''
'''
r=0
for _ in sorted(map(int,input().split()))[::-1]:
 if _>0:r+=1
 else:break
print(r)
'''
#print(len([0 for _ in input().split() if int(_)>0]))
'''
i=0;f='Pizza';e='on the table.'
while 1:
 try:
  r,w,l=map(int,input().split());i+=1
 except:break
 if (2*r)**2>=w*w+l*l:print(f,i,'fits',e)
 else:print(f,i,'does not fit',e)
 
'''
'''
n=int(input());a=n//300;n=n%300;b=n//60;n=n%60
if n//10==n/10:print(a,b,n//10)
else:print(-1)
'''
#input();l=list(map(int,input().split()));r=i=0;exec('if i+1!=l[i]:r+=1\ni+=1\n'*len(l));print(r)
#from math import *;print(ceil(sqrt(int(input()))))
'''
for i in 'a'*(int(input())):
 t=list(map(str,input().split()));r='god'
 for j in range(len(t)):
  if j!=0:r+=t[j]
 print(r)
'''
'''
for i in range(int(input())):
 t=input();h=len(t)//2
 if t[h-1]==t[h]:print('Do-it')
 else:print('Do-it-Not')
'''
'''
a,b=sorted(map(int,input().split()))
if abs(a-b)<=1:print(0)
else:print(b-a-1);print(*list(range(a+1,b)))
'''
#print(int(input())*4)

#print(input()+'??!')
#if input()=='0':print('YONSEI')
#else:print('Leading the Way to the Future')
#exec('print("="*int(input()));'*int(input()))
#exec('print(["even","odd"][int(input())%2]);'*int(input()))
#print(sorted(map(int,input().split())))
#l=[int(input())for i in range(9)];r=max(l);print(r,l.index(r)+1,sep='\n')
#m=0;a=b=i=0;exec('n=list(map(int,input().split()));m=max(m,max(n))\nif n.count(m)!=0:\n a=i+1;b=n.index(m)+1\ni+=1;'*9);print('%d\n%d %d'%(m,a,b))
'''
l=[]
for i in range(7):
 n=int(input())
 if n%2==1:l.append(n)
if l==[]:print(-1)
else:print(sum(l),min(l),sep='\n')
'''
#A65 Z90 a97 z122
'''
for _ in input():
 k=ord(_)
 if k<91:print(chr(k+32),end='')
 else:print(chr(k-32),end='')
'''
'''
while 1:
 r=eval(input().replace(' ','+'))
 if r==0:break
 print(r)
'''
#exec('t=input();print(t[0].capitalize()+t[1:]);'*int(input()))
'''
a,b=map(int,input().split())
if a>b:print('>')
elif a<b:print('<')
else:print('==')
a,b = map(int, input().split())
print('>' if a>b else '==' if a==b else '<')
'''

a,b=map(int,input().split());exec('input();'*a);print('비와이')
