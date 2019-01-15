

'''
from sys import stdin
n=stdin.readline().strip()
t=stdin.readline().strip()
for i in range(len(t)):
    #print(t[i],n.count(t[i]))
    if n.count(t[i])==1:
        n=n.replace(t[i],'')
    else:
        l=[]
        for j in range(len(n)):
            #print(j,n[j],t[i])
            if n[j]==t[i]:
                if j==0:
                    l.append(int(n[1:]))
                else:
                    l.append(int(n[:j]+n[j+1:]))
        n=str(max(l))
    #print(n)
print(n)
'''

'''
###1360
from sys import stdin
n=int(stdin.readline())
l=[];r='';k=0;
for i in range(n):
    t=stdin.readline().split()
    if t[0]=='type':
        r+=t[1]
'''
'''
from sys import stdin
n,m=map(int,stdin.readline().split())
l=list(map(int,stdin.readline().split()))
k=[0]*1000000001
for _ in l:
    k[_]+=1
r=0;p=max(l)
for i in range(max(l),-1,-1):
    if r>=m:break
    r+=k[i]
    if i-1<0:break
    k[i-1]+=k[i]
    p=i-1
print(p)
'''
for i in 'a'*int(input()):
 t='';c=0;h=0
 while 1:
  k=input().strip('\n')
  if k=='':break
  t+=k
 l=len(t);r=(l-t.count('#'))/l*100
 if r!=int(r):
  for _ in str(r):
   if h==2:
    if int(_)>=5:
     d=k.split('.');b=d[1];f=d[0]
     if int(b)+1==10:k=str(int(f)+1)
     else:k=f+'.'+str(int(b)+1)
     break
   if _=='.':c=1
   if c==1:h+=1
   k+=_
 else:k=str(int(r))
 print('Efficiency ratio is %s'%k+'%.')
