x = []

x[0:3]   #index 0부터 2까지 
x[5:]    #index 5부터 끝까지 
x[-1]    #index 맨뒤 
x[-3:]   #index 끝에서 3번째 부터 끝까지 
x[-4:-2] # index 끝에서 4번째부터 끝에서 3번째 까지 .

# + - * / % // **
# // 7//2 는 3   소수점 절삭  **는 제곱 

포맷팅
name = 'hongsa'
a = '나는 %s 입니다'% name
a = '이름 : {}'.format(name)

문자열 메소드
str.format()
str.count()
str.find()
str.upper()
str.lower()
str.replace()
str.split()    #문자열 분리하기
str.isspace()  #문자열에 공백있는지 확인하기

print(year,month,day, sep='/')   #문자열 중간중간 / 삽입

\n 
\t 
\\ 
\' 
\"


print(a, end='')  #다음 print하면 같은 줄에 출력 

you = 2
if you == 3 or you ==2 :
    print(you)

or and not

for i in range(1,10,2)          #1부터 2씩 증가
for i in range(20, 0, -2)       #20부터 -2 감소 


리스트 list 

a.append('yellow')
a.insert(1,'black')  #index 1에 black 요소 추가 
a.extend(b)    #리스트 a와 b를 합침

a.index(30)  # 요소 값이 30인 index 
a.pop(3) #index 3 요소 삭제 
a.remove(90)  # 요소 중 90인 요소 삭제 
a.clear()  #아예 리스트 비우기 

a.count('aaa')   # 요소값이 aaa인 요소 개수 
a.sort()          #올림차순
a.sort(reverse=True)  #내림차순

튜플
리스트보다 반복문에서 조금더 빠름 
요소를 변경할 수 없음 보안 굿
딕셔너리의 키로 쓸수있음 


딕셔너리 (object)
del diction['hongsa']


함수 매개변수 갯수를 정해놓지 않을때 
def hongsa(*names):
    sum = 0 
    for i in range(len(names)):
        print(names[i])

hongsa('hi','hello','bye')   #이때 매개변수는 튜플형태로 함수안에 들어가게되고 호출할때도 names[i]의 형태로 호출해야함.

파이썬에서 매개변수에 튜플을 제외한, 리스트나 딕셔너리를 매개변수로 전달하면 레퍼런스(메모리주소)로 전달하게 된다.


익명함수 람다 p.240

x= lambda a : a+2


파일다루기 

file = open('sample.txt', 'w', encoding='utf8')
lines = file.readlines()  #리스트 형태로 한줄씩 저장.


w : 쓰기모드 #기존 파일에 새 내용을 덮어씀 
r : 읽기모드 
a : 수정모드  #기존 파일에 새 내용 추가.

file.write('gg')
file.close()


import math             #모듈 전체 임포트
math.sqrt(100)

import math as m        #모듈 별명 정해서 임포트
m.sqrt(100)

from math import sqrt   # math 모듈에서 sqrt 만 가져오기 
sqrt(100)

from math import *      # 모듈 전체 임포트
sqrt(100)


math.floor()
math.ceil()
round()
math.factorial()