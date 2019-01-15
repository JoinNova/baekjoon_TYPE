p,w=map(int,input().split())
t=input().strip()
l=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
r=0;chk='';chk2=0
for _ in t:
    r+=p;
    for sub in l:
        if sub.count(_)!=0:
            chk=sub
            break
