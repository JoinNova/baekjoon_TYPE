'''
###Hello World
print('Hello World!')

###등록
print(5)
print('nova9128')

###개
print('|\_/|')
print('|q p|   /}')
print('( 0 )\"\"\"\\')
print('|"^"`    |')
print('||_/=\\\__|')

print('|\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|"^"`    |\n||_/=\\\__|')

###We love kriii
print('강한친구 대한육군\n'*2,end='')
'''
'''
###그대로 출력하기
while True:
    try:
        print(input())
    except EOFError:
        break
'''
'''
###삼각김밥
from sys import stdin
x,y=map(int,stdin.readline().split())
result=1000/y*x
for i in range(int(stdin.readline().strip())):
    a,b=map(int,stdin.readline().split())
    new=1000/b*a
    if result>new:
        result=new
print('%.2f'%result)
'''
'''
###컨베이어 벨트
from sys import stdin
n,m=map(int,stdin.readline().split())
t=[]
h=[]
chk=0
for i in range(n):
    t.append(int(stdin.readline()))
f=int(stdin.readline())
for i in range(n):
    if i!=0:
        h.append(t[i]*f+h[len(h)-1])
    else:
        h.append(t[i]*f)
print(h)
for i in range(m-1):
    c=[]
    f=int(stdin.readline())
    for j in range(n):
        if :
            c.append()

    h=c
print(h)
'''
'''
from sys import stdin
n,k=map(str,stdin.readline().split())
new=str()
com=str()
result=str()
chk=0
if int(k)==1:
    if len(n)==1:
        result=n
    else:
        for i in range(len(n)):
            new+=n[0]
            com+=str(int(n[0])+1)
        if int(new)>=int(n):
            result=new
        else:
            result=com
else:
    result=0
    while chk==0:
        for i in range():
        if int(result)>=int(n):
            chk=1
        #result=str(result)

    
        
        
    
print(result)
'''           

'''
while True:
    if len(set(list(str(n))))==k:
        break            
    n+=1
'''
'''
###보물
from sys import stdin
n=int(stdin.readline().strip())
a=sorted(list(map(int,stdin.readline().split())))
b=sorted(list(map(int,stdin.readline().split())),reverse=True)
result=0
for i in range(n):
    result+=a[i]*b[i]
print(result)
'''
###막대기
print(list(str(bin(int(input()))[2:])).count('1'))
