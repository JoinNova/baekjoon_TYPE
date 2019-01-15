'''
###이항 계수 1
from sys import stdin
from math import factorial as f
n,k=map(int,stdin.readline().split())
result=int(f(n)/(f(k)*f(n-k)))
print(result)
'''
'''
###팩토리얼 0의 개수
from sys import stdin
from math import factorial as f
r=0
for _ in str(f(int(stdin.readline())))[::-1]:
    if _!='0':
        break
    r+=1
print(r)
'''
'''
###팩토리얼
from sys import stdin
from math import factorial as f
print(f(int(stdin.readline())))
'''
###
from sys import stdin
n,m=map(int, stdin.readline().split())
l=['81','64','49','36','25','16','09','04','01','00']
li=[]
chk=0
for i in range(n):    
    t=stdin.readline().strip()
    for _ in t:
        li.append(_)
li=sorted(li,reverse=True)
result=str()
for _ in li:
    for __ in li:
        if _!=__:
            result=_+__
            for ___ in l:
                if ___==result:
                    chk=1
                    break
        if chk==1:
            break
    if chk==1:
        break
print(result)

