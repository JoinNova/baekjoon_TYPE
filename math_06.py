###
#x=0;exec('x+=1;a,b=map(int,input().split());print("Case #%d:"%x,a,"+",b,"=",a+b);'*int(input()))

'''
while 1:
 a,b=map(int,input().split())
 if a==0:break
 print(a+b)
'''
#exec('print(eval(input().replace(",","+")));'*int(input()))

#print(eval(a))
#print(sum(map(int,input().split())))
t='''Cube = 6, Triple = (3,4,5)
Cube = 12, Triple = (6,8,10)
Cube = 18, Triple = (2,12,16)
Cube = 18, Triple = (9,12,15)
Cube = 19, Triple = (3,10,18)
Cube = 20, Triple = (7,14,17)
Cube = 24, Triple = (12,16,20)
Cube = 25, Triple = (4,17,22)
Cube = 27, Triple = (3,18,24)
Cube = 28, Triple = (18,19,21)
Cube = 29, Triple = (11,15,27)
Cube = 30, Triple = (15,20,25)
Cube = 36, Triple = (4,24,32)
Cube = 36, Triple = (18,24,30)
Cube = 38, Triple = (6,20,36)
Cube = 40, Triple = (14,28,34)
Cube = 41, Triple = (2,17,40)
Cube = 41, Triple = (6,32,33)
Cube = 42, Triple = (21,28,35)
Cube = 44, Triple = (16,23,41)
Cube = 45, Triple = (5,30,40)
Cube = 46, Triple = (3,36,37)
Cube = 46, Triple = (27,30,37)
Cube = 48, Triple = (24,32,40)
Cube = 50, Triple = (8,34,44)
Cube = 53, Triple = (29,34,44)
Cube = 54, Triple = (12,19,53)
Cube = 54, Triple = (6,36,48)
Cube = 54, Triple = (27,36,45)
Cube = 56, Triple = (36,38,42)
Cube = 57, Triple = (9,30,54)
Cube = 58, Triple = (22,30,54)
Cube = 58, Triple = (15,42,49)
Cube = 60, Triple = (21,42,51)
Cube = 60, Triple = (30,40,50)
Cube = 63, Triple = (7,42,56)
Cube = 66, Triple = (33,44,55)
Cube = 67, Triple = (22,51,54)
Cube = 69, Triple = (36,38,61)
Cube = 70, Triple = (7,54,57)
Cube = 71, Triple = (14,23,70)
Cube = 72, Triple = (34,39,65)
Cube = 72, Triple = (8,48,64)
Cube = 72, Triple = (36,48,60)
Cube = 75, Triple = (12,51,66)
Cube = 75, Triple = (38,43,66)
Cube = 76, Triple = (12,40,72)
Cube = 76, Triple = (31,33,72)
Cube = 78, Triple = (39,52,65)
Cube = 80, Triple = (28,56,68)
Cube = 81, Triple = (25,48,74)
Cube = 81, Triple = (9,54,72)
Cube = 82, Triple = (4,34,80)
Cube = 82, Triple = (19,60,69)
Cube = 82, Triple = (12,64,66)
Cube = 84, Triple = (28,53,75)
Cube = 84, Triple = (42,56,70)
Cube = 84, Triple = (54,57,63)
Cube = 85, Triple = (50,61,64)
Cube = 87, Triple = (33,45,81)
Cube = 87, Triple = (20,54,79)
Cube = 87, Triple = (38,48,79)
Cube = 87, Triple = (26,55,78)
Cube = 88, Triple = (25,31,86)
Cube = 88, Triple = (21,43,84)
Cube = 88, Triple = (32,46,82)
Cube = 89, Triple = (17,40,86)
Cube = 90, Triple = (25,38,87)
Cube = 90, Triple = (10,60,80)
Cube = 90, Triple = (45,60,75)
Cube = 90, Triple = (58,59,69)
Cube = 92, Triple = (6,72,74)
Cube = 92, Triple = (54,60,74)
Cube = 93, Triple = (32,54,85)
Cube = 95, Triple = (15,50,90)
Cube = 96, Triple = (19,53,90)
Cube = 96, Triple = (48,64,80)
Cube = 97, Triple = (45,69,79)
Cube = 99, Triple = (11,66,88)
Cube = 100, Triple = (16,68,88)
Cube = 100, Triple = (35,70,85)'''
#print(t)
#import random;print(*random.sample(range(1,46),6))
#for i in range(1000,1050):
#    print(int(12,i))
'''
from datetime import datetime
print(str(datetime.today())[:10])
'''
'''
for a in range(2,101):
    for b in range(a,1,-1):
        for c in range(b,1,-1):
            for d in range(c,1,-1):
                if a**3==b**3+c**3+d**3:
                    print('Cube = %d, Triple = (%d,%d,%d)'%(a,d,c,b))
        
'''
#while 1:
# t=input()
# if t=='END':break
# print(t[::-1])
'''
for i in 'a'*int(input()):
 l=[];n=int(input());k=2
 for j in range(n):
  if n%k==0:l.append(k);n=n//k
  else:k+=1
 for i in range(2,max(l)+1):
  if l.count(i)!=0:print(i,l.count(i))
'''    
'''
n=int(input())
for i in range(n):
    print(' '*(n-i-1)+('*'*(2*i+1)))
for i in range(n-2,-1,-1):
    print(' '*(n-i-1)+('*'*(2*i+1)))
이문제는 예제를 채점하지 않습니다.
데이터는 한개입니다
입력을 받을 필요는 없다.
'''
#print('�')
#n=int(input());exec('print("*"*n);'*n)
#import base64
#code = "7Z6M7Yq464qUIGh0dHBzOi8vc3RhcnRsaW5rLmlvLyDsl5Ag7J6I64qUIOOFiOOFjuOFguOFjg==" # Unencrypt is 202cb962ac59075b964b07152d234b70
#print(base64.b64decode(code).decode('utf-8'))

#7Z6M7Yq464qUIGh0dHBzOi8vc3RhcnRsaW5rLmlvLyDsl5Ag7J6I64qUIOOFiOOFjuOFguOFjg==
#02-521-0487
'''
n=int(input())
#for i in range(n):print(' '*(n-i-1)+('*'*(2*i+1)))
for i in range(n-2,-2,-1):
    print((' '*(2*i+2)).center(2*n,'*'))
for i in range(n-1):
    print((' '*(2*i+2)).center(2*n,'*'))
'''
#n=int(input())
#for i in range(n-1,0,-1):print(' '*(n-i-1)+('*'*(2*i+1)))
#for i in range(n):print(' '*(n-i-1)+('*'*(2*i+1)))
'''
###별 찍기 - 11
def byul(n,k,bl):
    if k==0:
        return bl
    else :
        for i in range(len(bl)):
            bl.append(bl[i]+' '+bl[i])
            bl[i]=(bl[i]).center(len(bl[len(bl)-1]),' ')
        k-=1
        return byul(n,k,bl)
    
n=int(input())
w=n
k=0
if n!=3:
    for i in range(11):
        k+=1
        if int(n/2)==3:
            break
        n=n/2
bl=['***','* *','***']
byul(n,k,bl)
for _ in bl:
    print(_)
'''
'''
n=int(input())
for i in range(n):
    s=str()
    k=('*'*(2*i+1))
    if i!=0:
        for j in range(len(k)):
            if j%2==0:
                s+=k[i]
            else:
                s+=' '
        print(' '*(n-i-1)+s)
    else:
        print(' '*(n-i-1)+k)
'''
'''
n=int(input())
for i in range(n):
    k=('*'*(2*i+1))
    if i==n-1:
        print(k)
    elif i!=0:
        print(' '*(n-i-1)+'*'+k[1:-1].replace('*',' ')+'*')
    else:
        print(' '*(n-i-1)+k)
'''
n=int(input())
u=str()
d=str()
for i in range(n*2):
    if i%2==0:
        u+='*';d+=' '
    else:
        u+=' ';d+='*'
u=u[:-1]
for i in range(n):
    if i%2==0:
        print(u)
    else:
        print(d)
