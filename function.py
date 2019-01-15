'''
###셀프 넘버
al=list(range(1,10000))
for i in range(10000):
    try :
        t=str(i+1)
        l=len(t)
        n='0'*(4-l)+t
        s=0
        for _ in n:
            s+=int(_)
        s+=int(n)
        al.remove(s)
    except:
        pass
for _ in al:
    print(_)

###한수
n=str(input())
l=list(range(1,1000))
chk=99
if len(n)<3:
    print(n)
else:
    for i in range(100,int(n)+1):
        i=str(i)
        if int(i[1])-int(i[0])==int(i[2])-int(i[1]):
            chk+=1
    print(chk)
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
w=n*2-1
k=0
if n!=3:
    for i in range(11):
        k+=1
        if int(n/2)==3:
            break
        n=n/2
bl=['  *  ',' * * ','*****']
byul(n,k,bl)
for _ in bl:
    print(_)
    
