'''
n=int(input());p=' *'
if n==1:print('*')
else:
    u='*'+(p*int((n-1)/2));d=(p*int(n/2));
    for i in range(2*n):
        if i%2==0:
            print(u)
        else:print(d)
'''        
'''    
n=int(input());p='*';b=' '
for i in range(n-1):
    if i==0:
        print(p*n+b*(2*n-3)+p*n)
    else:
        print(b*i+p+b*(n-2)+p+b*(2*(n-i)-3)+p+b*(n-2)+p)
print(b*(n-1)+p+b*(n-2)+p+b*(n-2)+p)
for i in range(n-2,-1,-1):
    if i==0:
        print(p*n+b*(2*n-3)+p*n)
    else:
        print(b*i+p+b*(n-2)+p+b*(2*(n-i)-3)+p+b*(n-2)+p)
'''
'''
n=int(input());p='*';b=' ';c=str();pb='* ';r=str()
if n==1:print(p)
else:
    k=p*(4*n-3)
    for i in range(2*n-2):
        if i%2==0:
            print(pb*((i+1)//2)+k+(pb*((i+1)//2))[::-1])
            r+=pb*((i+1)//2)+k+(pb*((i+1)//2))[::-1]+'\n'
            k=k[2:len(k)-2]
            
        else:
            print(pb*((i+1)//2)+b*len(k)+(pb*((i+1)//2))[::-1])
            r+=pb*((i+1)//2)+b*len(k)+(pb*((i+1)//2))[::-1]+'\n'
    for i in range(4*n-3):
        if i%2==0:c+=p
        else:c+=b
    print(c)
    print((r[::-1])[1:])
'''
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
w=n*2-1
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


