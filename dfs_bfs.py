'''
visit={}
load={}
N,M,V=map(int,input().split())

for i in range(M):
    fromN, toN = map(int, input().split())
    visit[fromN]=0
    visit[toN]=0
    if load.get(fromN)==None:
        load[fromN]=[]
    if load.get(toN)==None:
        load[toN]=[]
    load[fromN].append(toN)
    load[toN].append(fromN)
for a in load:
    load[a].sort()
    
way=[]
def DFS(startV):
    way.append(startV)
    visit[startV]=1 
    for toN in load.get(startV):
        if visit.get(toN) == 0:
            DFS(toN)

bfsWay=[]
def BFS(startV):#1
    flag=0
    for toN in load.get(startV):
        if visit.get(toN)==0:
            bfsWay.append(toN)
            visit[toN]=1
            flag=1
    if flag!=0:
        for nextN in bfsWay:
            BFS(nextN)

DFS(V)

for i in visit.keys():#visit초기화
    visit[i]=0
bfsWay.append(V)
visit[V] = 1
BFS(V)

result=''
for i in way:
    result+=str(i)+' '
print(result[:len(result)-1])
result=''
for i in bfsWay:
    result+=str(i)+' '
print(result[:len(result)-1])
'''



'''
####
#백준 - DFS와 BFS (1260번)
# 인접 리스트로 구현된 그래프에 DFS와 BFS 적용

from collections import deque

# 정점 개수(N), 간선 개수(M), 시작 정점(start) 입력 
n, m, start = map(int, input().split())
# 인접 리스트 생성
adj = [[] for _ in range(n+1)]
# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
# (조건) 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
# 리스트의 sort()는 리스트 그 자체를 소팅함
for i in range(n+1):
    adj[i].sort()

# 1) dfs 구현 - 재귀호출
def dfs(x):
    # 함수 안에서 전역변수 수정하기 위해서는 global로 명시
    global check
    # 탈출 조건
    if check[x]:
        return
    # check 배열에 True 입력 후 방문 출력
    check[x] = True
    print(x, end=" ")
    # 이어진 정점 중 방문하지 않은 곳 방문
    for y in adj[x]:
        if check[y] == False:
            dfs(y)

# 2) bfs 구현 - 큐
def bfs(start):
    # 큐 생성
    q = deque()
    # 첫 방문시 큐에 삽입 후 체크 배열에 True 표시
    q.append(start)
    check[start] = True
    # 큐가 비어있지 않는 동안 루프를 돌며
    while q:
        x = q.popleft() # 큐의 맨 앞에서 요소를 뺌
        print(x, end=" ")
        for y in adj[x]:
            # 이어진 정점 중 방문하지 않았다면 큐에 넣고 check를 True로 
            if check[y] == False:
                check[y] = True
                q.append(y)


# 1) dfs 적용
# 체크 배열 생성
check = [False] * (n+1)
dfs(start)
print()

# 2) bfs 적용
# 체크 배열 생성
check = [False] * (n+1)
bfs(start)
print()

'''
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    for i in range(50):
        for j in range(len(s)-1):
            p=str()
            try:
                if s[j]==s[j+1]:
                    p=s[j]*2
                    s=re.sub(p,'',s)
            except:pass
    if len(s)==0:
        s='Empty String'
    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = superReducedString(s)
    print(result)
    #fptr.write(result + '\n')
    #fptr.close()
'''
'''
import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    return len(re.sub(r'[a-z]','',s))+1
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
'''

'''
import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, p):
    result=0
    if p==re.sub(r'[a-z]','',p):
        result+=1
    if p==re.sub(r'[A-Z]','',p):
        result+=1
    if p==re.sub(r'[0-9]','',p):
        result+=1
    if p==re.sub(r'[!@#$%^&*()\-+]','',p):
        result+=1
    if 6-(len(p)+result)>0:
        result+=6-(len(p)+result)
    return result
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)
    #fptr.write(str(answer) + '\n')
    #fptr.close()
'''

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    p='abcdefghijklmnopqrstuvwxyz'
    l=[];result=0
    t=list(set(list(s)))
    for i in range(len(t)-1):
        for j in range(1+i,len(t)):
            l.append(t[i]+t[j])
    for _ in l:
        pp=re.sub(r'[%s]'%_,'',p)
        k=re.sub(r'[%s]'%pp,'',s)
        chk=0
        for i in range(len(k)-1):
            if k[i]!=k[i+1]:chk+=1
            else:break
        if chk==len(k)-1:
            result=max(len(re.sub(r'[%s]'%pp,'',s)),result)           
            
    return result
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input().strip())
    s = input()
    result = alternate(s)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
