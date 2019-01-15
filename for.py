'''
###N 찍기
for _ in range(int(input())):
    print(_+1)

###기찍 N
for _ in range(int(input()),0,-1):
    print(_)

###구구단
n=int(input())
for _ in range(9):
    print('{0} * {1} = {2}'.format(n,_+1,n*(_+1)))

###별 찍기 - 1
for i in range(int(input())):
    print('*'*(i+1))  

###별 찍기 - 2
n=int(input())
for i in range(n):
    print(' '*(n-(i+1))+'*'*(i+1))    

###별 찍기 - 3
for i in range(int(input()),0,-1):
    print('*'*i)

###별 찍기 - 4
n=int(input())
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*i)  

###2007년
n=list(map(int,input().split()))
if n[0]==1:
    y=n[1]%7
elif n[0]==2:
    y=(n[1]+31)%7
elif n[0]==3:
    y=(n[1]+31+28)%7
elif n[0]==4:
    y=(n[1]+31+28+31)%7
elif n[0]==5:
    y=(n[1]+31+28+31+30)%7
elif n[0]==6:
    y=(n[1]+31+28+31+30+31)%7
elif n[0]==7:
    y=(n[1]+31+28+31+30+31+30)%7
elif n[0]==8:
    y=(n[1]+31+28+31+30+31+30+31)%7
elif n[0]==9:
    y=(n[1]+31+28+31+30+31+30+31+31)%7
elif n[0]==10:
    y=(n[1]+31+28+31+30+31+30+31+31+30)%7
elif n[0]==11:
    y=(n[1]+31+28+31+30+31+30+31+31+30+31)%7
else:
    y=(n[1]+31+28+31+30+31+30+31+31+30+31+30)%7

if y==1:
    print('MON')
elif y==2:
    print('TUE')
elif y==3:
    print('WED')
elif y==4:
    print('THU')
elif y==5:
    print('FRI')
elif y==6:
    print('SAT')
else:
    print('SUN')

###합
print(sum(range(int(input())+1)))

###숫자의 합
n=input()
print(sum(list(map(int,input()))))

###열 개씩 끊어 출력하기
T=str()
c=0
t=list(map(str,input()))
for _ in t:
    T+=_
    c+=1
    if c==10:
        print(T)
        T=str()
        c=0
print(T)
'''
###빠른 A+B
import sys
for i in range(int(sys.stdin.readline())):
    n=sys.stdin.readline().split()
    print(int(n[0])+int(n[1]))
