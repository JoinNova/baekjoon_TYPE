'''
###농구 경기
#a='abcdefghijklmnopqrstuvwxyz'
#l=[0]*26
l=str();c=0
for i in range(int(input())):l+=input()[0]
for _ in sorted(set(l)):
    if l.count(_)>=5:print(_,end='');c=1
if c==0:print('PREDAJA')
'''
'''
###나무 조각
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    for j in range(1,len(l)-i):
        if l[j-1]>l[j]:
            l[j-1],l[j]=l[j],l[j-1]
            print(l[0],l[1],l[2],l[3],l[4])
        if l==[1,2,3,4,5]:
            c=1
            break
    if c==1:
        break       
'''
'''
a = list(map(int,input().split()))
while a != [1,2,3,4,5]:
    for i in range(4):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            print(' '.join(map(str,a)))
'''
'''
a=input().split();i=3
while[*'12345']<a:
 i=-~i%4;z=a[i+1]
 if a[i]>z:a[i:i+2]=z,a[i];print(*a)
'''
'''
###날짜 계산
l=list(map(int,input().split()));e,m,s=0,0,0;i=0
while True:
    i+=1;e+=1;m+=1;s+=1
    if [e,m,s]==l:break
    if e==15:e=0
    if m==28:m=0
    if s==19:s=0
print(i)
'''
'''
###유니코드
print(chr(44031+int(input())))
'''
'''
###한글2
print(ord(input())-44031)
'''

import re
"""
    초성 중성 종성 분리 하기
	유니코드 한글은 0xAC00 으로부터
	초성 19개, 중상21개, 종성28개로 이루어지고
	이들을 조합한 11,172개의 문자를 갖는다.

	한글코드의 값 = ((초성 * 21) + 중성) * 28 + 종성 + 0xAC00
	(0xAC00은 'ㄱ'의 코드값)

	따라서 다음과 같은 계산 식이 구해진다.
	유니코드 한글 문자 코드 값이 X일 때,

	초성 = ((X - 0xAC00) / 28) / 21
	중성 = ((X - 0xAC00) / 28) % 21
	종성 = (X - 0xAC00) % 28

	이 때 초성, 중성, 종성의 값은 각 소리 글자의 코드값이 아니라
	이들이 각각 몇 번째 문자인가를 나타내기 때문에 다음과 같이 다시 처리한다.

	초성문자코드 = 초성 + 0x1100 //('ㄱ')
	중성문자코드 = 중성 + 0x1161 // ('ㅏ')
	종성문자코드 = 종성 + 0x11A8 - 1 // (종성이 없는 경우가 있으므로 1을 뺌)
"""
# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


if __name__ == '__main__':
    test_keyword = input()
    split_keyword_list = list(test_keyword)
    print(split_keyword_list)

    result = list()
    for keyword in split_keyword_list:
        # 한글 여부 check 후 분리
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(CHOSUNG_LIST[char1])
            #print('초성 : {}'.format(CHOSUNG_LIST[char1]))
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(JUNGSUNG_LIST[char2])
            #print('중성 : {}'.format(JUNGSUNG_LIST[char2]))
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            result.append(JONGSUNG_LIST[char3])
            #print('종성 : {}'.format(JONGSUNG_LIST[char3]))
        else:
            result.append(keyword)
    # result
    print("".join(result))
s=re.sub('\\','\\x98',str(s))
print(s)


'''
###4와7
from re import sub;print(sub('1','7',sub('0','4',bin(int(input())+1)[3:])))
'''
'''
4,7,44,47,74,77,444,447,474,477,744,747,774,777
1 2  3 4  5  6   7   8   9   10  11  12 13   14
  2         2+4                             2+4+8
n%2
1 10 11 100 101 110 111
'''
'''
###Sort Me
from sys import stdin
chk2=0
result=str()
while True:
    chk2+=1
    l=[]
    t=stdin.readline().strip().split()
    if t[0]=='0':
        break
    p=t[1]
    for i in range(int(t[0])):
        s=stdin.readline().strip()
        l.append(s)
    for i in range(int(t[0])):
        for j in range(1,int(t[0])-i):
            chk=0
            a=l[j-1]
            b=l[j]
            for k in range(min(len(a),len(b))):
                if p.index(a[k])==p.index(b[k]):
                    chk+=1
                elif p.index(a[k])>p.index(b[k]) and chk==k:
                    l[j-1],l[j]=l[j],l[j-1]
                    break
                else:
                    break
    result+='year '+str(chk2)+'\n'
    for _ in l:
        result+=_+'\n'
                
                
print(result[:-1])           
'''
