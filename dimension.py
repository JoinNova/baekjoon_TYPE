'''
###단어의 개수
print(len(input().split()))

###숫자의 개수
t=str(int(input())*int(input())*int(input()))
for _ in range(10):
    print(t.count(str(_)))

###OX퀴즈
for i in range(int(input())):
    q=input()
    r=[]
    s=0
    for j in range(len(q)):
        if q[j]=='O':
            s+=1
            r.append(s)
        else:
            s=0
    print(sum(r))

###음계
s=str(input())
if s=='1 2 3 4 5 6 7 8':
    print('ascending')
elif s=='8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')
'''
###평균 점수
a=[]
for i in range(5):
    s=int(input())
    if s<40:
        s=40
    a.append(s)
print(int(sum(a)/5))
