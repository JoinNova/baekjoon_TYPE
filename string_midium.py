'''
###KMP는 왜 KMP일까?
from sys import stdin
t=stdin.readline().split('-')
for _ in t:
    print(_[0],end='')
'''
###찾기
from sys import stdin
import re
#t=stdin.readline().strip()
t=stdin.readline().strip()
p=stdin.readline().strip()
chk=0
r=str()
for i in range(len(t)-len(p)+1):
    if (p in t[i:i+len(p)])==True:
        chk+=1
        r+=str(i+1)
        r+=' '
print(chk)
print(r.strip())
        
    
'''
l=[]
for i in range(len(t)+1-len(p)):        
    if t[i:i+len(p)]==p:
        l.append(str(i+1))
print(len(l))
for i in range(len(l)):
    if i!=len(l)-1:
        print(l[i],end=' ')
    else:
        print(l[i])
'''
