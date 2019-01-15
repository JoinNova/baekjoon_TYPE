'''
###A×B
n=list(map(int,input().split()))
print(n[0]*n[1])

###사칙연산
n=list(map(int,input().split()))
print('{0}\n{1}\n{2}\n{3}\n{4}'.format(n[0]+n[1],n[0]-n[1],n[0]*n[1],int(n[0]/n[1]),n[0]%n[1]))

###나머지
n=list(map(int,input().split()))
print('{0}\n{1}\n{2}\n{3}'.format((n[0]+n[1])%n[2],(n[0]%n[2]+n[1]%n[2])%n[2],(n[0]*n[1])%n[2],(n[0]%n[2]*n[1]%n[2])%n[2]))

###A+B - 2
print(int(input())+int(input()))
'''
###설탕 배달
n=int(input())
if n==4 or n==7:
    print(-1)
else:
    for i in range(5):
        if (n-3*i)%5==0:
            print(i+(n-3*i)//5)          
            break
