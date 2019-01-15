
'''
###직사각형을 만드는 방법
n=int(input());t=0
for i in range(int(n**0.5)):
    for j in range(i,n):
        if ((i+1)*(j+1))<=n:
            t+=1
print(t)
    
'''

###캔디 구매

c,k=map(int,input().split())
if c<10**(k-1):
    print(0)
else:
    if int(str(c//(10**(k-1)))[-1])>=5:
        r=str(c//(10**k)+1)+'0'*k
    else:
        r=str(c//(10**k))+'0'*k
    print(r)
