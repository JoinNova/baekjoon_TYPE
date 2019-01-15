'''
###X보다 작은 수
from sys import stdin
n,m=map(int,stdin.readline().split())
l=list(map(int,stdin.readline().split()))
result=[]
for _ in l:
    if _<m:
        result.append(str(_))
print(' '.join(result))
'''
'''
###윷놀이
from sys import stdin
for i in range(3):
    n=list(map(int,stdin.readline().split()))
    if n.count(0)==1:
        print('A')
    elif n.count(0)==2:
        print('B')
    elif n.count(0)==3:
        print('C')
    elif n.count(0)==4:
        print('D')
    else:
        print('E')
'''
###정수 삼각형
from sys import stdin
l=[]
for i in range(int(stdin.readline())):
    f=list(map(int,stdin.readline().split()))
    fibot=[]
    #print('===============')
    #print('시작점',l)
    #print('초기화',fibot)
    idx=0
    idx2=0
    if i==0:
        l.append(f[0])
    else:
        for j in range(2*i):
            #if j<=len(fibot)-1:
            #print("idx={0},idx2={1},fivot={2}".format(idx,idx2,fibot))
            fibot.append(l[idx]+f[idx2])
            if j%2==0:
                idx2+=1    
            if (j+1)%2==0:
                idx+=1
            #else:
                #print("idx={0},j={1},fivot={2}".format(idx,j,fibot))
                #fibot.append(l[idx]+f[j])
                #print(fibot)
                #if (j+1)%2==0:
                    #idx+=1
        #print(fibot)
        l=fibot
print(max(l))    
            
    
