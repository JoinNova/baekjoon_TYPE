'''
###큐
from sys import stdin
n=int(stdin.readline())
q=[]
for i in range(n):
    com=stdin.readline().split()

    if com[0]=='push':
        q.append(int(com[1]))
    elif com[0]=='pop':
        try:
            print(q[0])
            del(q[0])
        except:
            print(-1)
    elif com[0]=='size':
        print(len(q))
    elif com[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif com[0]=='front':
        try:
            print(q[0])
        except:
            print(-1)
    else:
        try:
            print(q[-1])
        except:
            print(-1)
'''
'''
###DFS와 BFS
from sys import stdin
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

#dfs(graph, 'A')
n=list(map(int,stdin.readline().split()))
print(n)
graph=[]
for i in range(n[1]):
    m=list(map(int,stdin.readline().split()))
    graph[i]=(m[0],m[1])
dfs(graph,n[2])
'''
'''
###조세퍼스 문제 0
from sys import stdin
n,m=map(int, stdin.readline().split())
l=list(range(1,n+1))
result='<'
idx=0
for i in range(n):
     idx+=m
     while idx>len(l):
         idx=idx-len(l)
     result+=str(l[idx-1])
     result+=', '
     del(l[idx-1])
     idx-=1
result=result[:-2]
result+='>'
print(result)    
'''
'''
n, m = map(int, input().split())
l = list(range(1, n + 1))
r = []
index = 0
while len(l):
    index = (index + m - 1) % len(l)
    r.append(str(l.pop(index)))
    print(len(l))

print('<', ', '.join(r), '>', sep='')
'''
'''
###프린터 큐
from sys import stdin
for i in range(int(stdin.readline())):
    n,m=map(int,stdin.readline().split())
    l=list(map(int,stdin.readline().split()))
    nl=sorted(l,reverse=True)
    imp=l[m]
    del(l[m])
    l.insert(m,'X')
    result=0
    idx=0
    if n==1:
        result=1
    else:
        while True:
            #print('돌아갑니다.',l,idx)
            if l[idx]==nl[0]:
                del(l[idx])
                del(nl[0])
                if idx==0:
                    idx=len(l)
                else:
                    idx-=1
                result+=1
            elif max(nl)==imp and l[idx]=='X':
                result+=1
                break
            if idx<len(l)-1:    
                idx+=1
            elif l==[]:
                break
            else:
                idx=0
    print(result)
'''
'''
for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [*map(int, input().split())]
    order = 1

    while l:
        first = l.index(max(l))
        if first == 0:
            if m == 0:
                print(order)
                break
            else:
                l.pop(0)
                order += 1
        else:
            l.append(l.pop(0))
        m = (m - 1) % len(l)
'''
from sys import stdin
n,m,v=map(int,stdin.readline().split())
al=[]
result=[]
for i in range(m):
    al.append(list(map(int,stdin.readline().split())))
result.append(str(v))
#dfs
while True:
    if len(result)==n:
        break
    for i in range(len(al)):
        sub=al[i]
        if sub[0]==v and result.count(sub[1])==0:
            v=sub[1]
            result.append(str(v))
        elif sub[1]==v and result.count(sub[0])==0:
            v=sub[0]
            result.append(str(v))
        elif len(result)==n:
            break
print(' '.join(result))
#BFS
v=int(result[0])
result=[]
node=[]
result.append(str(v))
idx=0
chk=0
while True:
    if len(result)==n:
        break
    if node!=[] and chk==0:
        v=node[0]
        del(node[0])
        chk=1
    else:
        for i in range(len(al)):
            sub=al[i]
            if sub[0]==v and result.count(sub[1])==0:
                chk+=1
                result.append(str(sub[1]))
                node.append(sub[1])
            else:
                chk=0
                break
print(' '.join(result))
