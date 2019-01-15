n=int(input())
a=[]
chk=0
# 1 1 2 2 3  3  4  4  5
for i in range(n):
    chk+=1
    #print(int(i/2)+1)
    a.append(int(i/2)+1)
    #print(sum(a))
    if sum(a)>=n:
        break
print(chk)
'''    
#1,2,3,5,7,10,13,17,21,26
print(a)
k=0
l=[]
for i in range(n):
    k+=a[i]
    l.append(k)
print(l)
#1,2,3,4,5, 6, 7, 8, 9,10
'''
