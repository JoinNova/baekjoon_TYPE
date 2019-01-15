#exec('n,m=input().split();print(bin(int(n,2)+int(m,2))[2:]);'*int(input()))

    
#print(int(int(input()),10))
#from sys import stdin
#for i in range(int(stdin.readline())):
#    b,d=map(int,stdin.readline().strip().split())
#    print(int(str(d),b)%(b-1))
from sys import stdin
l='0'*20;d='1'*20;z='0'*20
for i in 'a'*int(stdin.readline()):
    x=stdin.readline().strip()
    if x.count(' ')==1:x=x.split();x,y=x[0],int(x[1])
    if x=='add':l=l[:y-1]+'1'+l[y:]
    elif x=='remove' and l[y-1]!='0':l=l[:y-1]+'0'+l[y:]
    elif x=='check':print(int(l[y-1]=='1'))
    elif x=='toggle':
        if l[y-1]=='0':l=l[:y-1]+'1'+l[y:]
        else:l=l[:y-1]+'0'+l[y:]
    elif x=='all':l=d
    else:l=z
    #print(x,l)                            
'''
from sys import stdin
n,m=map(int,stdin.readline().split())
l=[0]*n;i=0
while n-i:    
    l[i]=int(stdin.readline());i+=1
while m:
    a,b=map(int,stdin.readline().split())
    print(min(l[a-1:b]));m-=1
'''
'''
from sys import stdin
l=[0]*10001
n=int(stdin.readline())
for i in range(n):
    l[int(stdin.readline())]+=1
for i in range(10001):
    print('%s\n'%i*l[i],end='')
'''
