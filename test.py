while True:
    st={0,1,2,3,4,5,6,7,8,9}

    x=input()
    x=x.split(' ')
    a=int(x[0])
    b=int(x[1])

    A=[0]*len(str(a))
    for i in range(len(str(a))):
        A[i]=int(str(a)[i])
    p=0
    for i in range(len(A)+1):
        aa=A[:i] #남은 숫자 len(A)-i 개
        t=set(aa)
        n=b-len(t)
        nn=st-t
        nn=list(nn)
        nn.reverse()
        nn=nn[:n]
        t.update(set(nn))
        k=nn+[max(t)]*(len(A)-i-n)
        k.sort()
        k.reverse()
        aa+=k
        if len(aa)>len(A):
            c=i
            break
        s=''
        for j in range(len(aa)):
            s+=str(aa[j])
        s=int(s)
        if s<a:
            c=i
            break
        elif s==a:
            ans=[]
            for w in str(s):
                ans+=[int(w)]
            p=1
            break
        else:
            continue
        
    if p==0:
        if c==0:
            m=list(st)[:b]
            m=[0]*(len(A)+1-b)+m
            if m[0]==0:
                m[0]=1
                for e in range(1,len(m)):
                    if m[e]==1:
                        m[e]=0
            s=''
            for j in range(len(m)):
                s+=str(m[j])
            ans=m
        elif c==len(A):
            m=A[:]
            while len(set(m))!=b:
                m[len(m)-1]+=1
            ans=m
        else:
            m=A[:c]
            m[len(m)-1]+=1
            while b-len(set(m))>(len(A)-c) or len(set(m))>b:
                m[len(m)-1]+=1
            
            n1=b-len(set(m))
            n2=st-set(m)
            n3=list(n2)[:n1]
            n4=set(m)
            n4.update(n3)
            m=m+[min(n4)]*(len(A)-c-n1)+n3
            ans=m
    Ans=''

    for i in ans:
        Ans+=str(i)
    break
print(int(Ans))
