'''
###스택
from sys import stdin
l=[]
for i in range(int(stdin.readline())):    
    n=stdin.readline().split()
    #print(n[0])
    if n[0]=='push':
        l.append(int(n[1]))
    elif n[0]=='pop':
        if len(l)==0:
            print(-1)
        else:
            print(l[len(l)-1])
            l.pop()
    elif n[0]=='size':
        print(len(l))
    elif n[0]=='empty':
        if len(l)==0:
            print(1)
        else:
            print(0)
    else:
        if len(l)==0:
            print(-1)
        else:
            print(l[len(l)-1])
    #print(l)   
'''
'''
###스택수열
from sys import stdin
from collections import deque
n=int(stdin.readline())
#initl=list(range(n,0,-1))
initl=deque(range(n,0,-1))
pivot=deque()
result=deque()
makel=deque()
err=0
printl=deque()
'''
'''
ml=[]
chkc=0
for i in range(n):
    mm=int(stdin.readline())
    ml.append(mm)
    if n==mm:
        chkc=1
    elif chkc==1:
        if kk<mm:
            err=1
            break
    if err==1:
        break
    kk=mm
if err==0:
'''
'''
for i in range(n):
    try:
        m=int(stdin.readline())
        result.append(m)
        while makel!=result:
            while pivot.count(m)!=1:
                pivot.append(initl[len(initl)-1])
                initl.pop()
                printl.append('+')
            makel.append(pivot[len(pivot)-1])
            pivot.pop()
            printl.append('-')
    except:
        err=1
        break
    #print('initl={0},pivot={1},result={2},makel={3}'.format(initl,pivot,result,makel))
if err==1:
    print('NO')
else:
    for _ in printl:
        print(_)
'''
'''
from sys import stdin
from collections import deque
n = int(stdin.readline())
pivot = deque(maxlen=n)
result = deque(maxlen=n*2)
des = 0
chk = 0
for i in range(n):
    num = int(stdin.readline())
    if num > des:
        for i in range(des,num):
            pivot.append(i+1)
            result.append('+')
        pivot.pop()
        result.append('-')
        des = num
    else:
        if num == pivot[-1]:
            pivot.pop()
            result.append('-')
        else:
            chk = 1
            break        
if chk == 0:
    for _ in result:
        print(_)
else:
    print("NO")
'''
'''
###괄호
from sys import stdin
from re import compile
pattern = compile('[(][([)]')
for i in range(int(stdin.readline())):
    t = stdin.readline()
    #print(t)
    result= pattern.findall(t)
    for _ in result:
        if _==t[:-1]:
            if _.count('(')==_.count(')'):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
'''
'''
from sys import stdin
from re import match
for _ in range(int(stdin.readline())):
    regex = stdin.readline()
    try:
        test = match(regex,'')
        print('YES')
    except:
        print('NO')
'''
'''
###괄호의 값
from sys import stdin
from re import sub
t = stdin.readline().strip()
chka=0
chkb=0
if len(t)%2==0:
    if t.count('[')==t.count(']') and t.count('(')==t.count(')'):    
        t=sub(r'[\]]{1}[\[]{1}',']+[',t)
        t=sub(r'[\]]{1}[(]{1}',']+(',t)
        t=sub(r'[)]{1}[\[]{1}',')+[',t)
        t=sub(r'[)]{1}[(]{1}',')+(',t)
        t=sub(r'[\[]{1}[\]]{1}','3',t)
        t=sub(r'[(]{1}[)]{1}','2',t)
        t=sub(r'[(]{1}[2][)]{1}','2*2',t)
        t=sub(r'[(]{1}[3][)]{1}','2*3',t)
        t=sub(r'[\[]{1}[2][\]]{1}','2*3',t)
        t=sub(r'[\[]{1}[3][\]]{1}','3*3',t)
        new=str()
        for _ in t:
            if _=='(':
                new+='2*('
                chka+=1
            else:
                new+=_
        t=new
        new=str()
        for _ in t:
            if _=='[':
                new+='3*('
                chkb+=1
            else:
                if _==']':
                    new+=')'
                else:
                    new+=_
        try:
            if eval(new)!=():
                print(eval(new))
            else:
                print(0)
        except:
            print(0)
    else:
        print(0)
else:
    print(0)
'''
'''
t = []
for c in input():
    if c == ')':
        if not t:
            break
        elif t[-1] == '(':
            num = 1
        elif isinstance(t[-1], int):
            num = t.pop()
            if not t or t[-1] != '(':
                break
        else:
            break

        t.pop()
        if t and isinstance(t[-1], int):
            t.append(t.pop() + 2 * num)
        else:
            t.append(2 * num)
    elif c == ']':
        if not t:
            break
        elif t[-1] == '[':
            num = 1
        elif isinstance(t[-1], int):
            num = t.pop()
            if not t or t[-1] != '[':
                break
        else:
            break

        t.pop()
        if t and isinstance(t[-1], int):
            t.append(t.pop() + 3 * num)
        else:
            t.append(3 * num)
    elif c == '(' or c == '[':
        t.append(c)
    else:
        break
else:
    if len(t) == 1 and isinstance(t[0], int):
        print(t[0])
        exit(0)

print(0)
'''
'''
import sys

stack = []
error = False
res = 0
tmp = 1
ss = sys.stdin.readline().strip()
for i in range(len(ss)):
    s = ss[i]
    if i+1 < len(ss):
        n = ss[i+1]
    else:
        n = ""
    if s == "(":
        stack.append(s)
        tmp *= 2
        if n == ")":
            res += tmp
    elif s == "[":
        stack.append(s)
        tmp *= 3
        if n == "]":
            res += tmp
    elif s == ")":
        if not stack or stack[-1] != "(":
            error = True
            break

        stack.pop()
        tmp /= 2
    elif s == "]":
        if not stack or stack[-1] != "[":
            error = True
            break

        stack.pop()
        tmp /= 3

if error or len(stack) != 0:
    print(0)
else:
    print(int(res))
'''
