https://senticoding.tistory.com/49      ##docker 개념 


#pip install 패키지명 --upgrade


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

a = set(a)          #중복값 제거 


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

import random
random 

random.random() 
random.randrange(1,11,2)        #1부터 10까지 숫자 랜덤 추출, 증가값 2  1,3,5,7,9 중에 랜덤 추출
random.randint(1,11)            #1부터 11까지 숫자 랜덤 추출
random.choice(list_tuple)       #리스트, 튜플을 넣으면 그중에 한 요소 랜덤 추출.
random.shuffle(list_tuple)      #리스트, 튜플을 넣으면 요소 순서 무작위로 바꿈.





클래스 속성 

class MyClass:
    number = 100

    def inc_10(self):
        MyClass.number += 10        ## 클래스명.변수명 이렇게 하면 클래스 속성

    def inc_20(self):
        MyClass.number += 20 

obj1 = MyClass() 
obj2 = MyClass() 

## 클래스 속성은 어떤 객체든 간에 number가 공유가 됨.  

인스턴스 속성 

class MyClass :
    def __init__(self, number):
        self.number = number        ##self.변수명 이렇게 하면 인스턴스 속성

    def inc_10(self):
        self.number += 10 

    def inc_20(self):
        self.number += 20 

## 이때는 객체마다 number가 공유되지 않음. 

상속 

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def printInfo(self):
        print()

    def getInfo(self):
        return self.name + ',' + str(self.age)

class Student(Person):
    def __init__(self, name, age, department, id):
        super().__init__(name, age)
        self.department = department 
        self.id = id 

    def printStudentInfo(self):
        name_age = super().getInfo()
        print(name_age)
        print()


##super().__init__() 은 부모클래스의 생성자를 그대로 사용하겠다는 뜻 
##super().getInfo() 부모클래스의 메소드를 사용


Numpy 

import numpy as np 

np.array([1,2,3])
data = np.random.randn(2,3)    #2행 3열로 리스트 생성  요소 3개짜리 리스트 2개 생성 
data.dtype 
data.shape 

np.zeros(10)            # 요소 10개인 리스트 생성 값은 0으로 
np.zeros((2,3), dtype=np.int32)  #int타입으로 생성 2행 3열
np.ones                 #요소값 1로 생성

data = np.arange(10,121,10)        #10부터 10씩 증가시킨 값을 리스트로 생성
data.reshape(2,6)               #2행 6열 구조로 다시 생성

data.sum()
data.mean()
data.max()
data.min()

data.max(axis=0)        #세로 방향으로 max
data.max(axis=1)        #가로 방향으로 max
np.argmax(data,axis=0)  #index 리턴 
np.argmax(data,axis=1)

np.where(data>0,1,-1)  #data가 양수이면 1, 아니면 -1인 np 리턴 
np.where(data>0,5,data)  #data의 값이 양수일경우 5, 아니면 data값인 np 리턴



## with문 ##

with Hello() as h :
    h.sayHello('obama')
    h.sayHello('trump')


# 클래스의 객체를 바로 만들고 
# 만든 객체를 이용하여 인사를 하고
# 만든 객체를 소멸시킵니다.

## 객체의 라이프사이클(생성 >> 사용 >> 소멸)을 설계할 수 있습니다.



############ API requests ##############
import requests

url = ""

response = requests.get(url).json()   #.json()으로 받아오기/// .text  // .content

############ datetime ##############
import time
from datetime import datetime, timedelta 

today = datetime.now() 

today.year
today.month 
today.day 
today.hour 
today.minute 
today.second 

today.strftime('%Y/%m/%d %H:%M:%S')

%Y #4자리 연도 
%y #2자리 연도  
%m #월
%d #일
%A #요일
%a #간단 요일
%H #시(24시 기준)
%I #시(12시 기준)
%p #AM 또는 PM 
%M #분
%S #초


#현재 unix time 
unixTime = time.time()
#unix time을 datetime으로 
date = datetime.fromtimestamp(unixTime)
#time delta 
date = date + timedelta(hours=3)  #days, seconds... 

#string시간을 datetime으로 
date = datetime.strptime(stringTime, '%Y-%m-%d %H:%M:%S')  #2번째 인자는 stringTime의 시간 포맷이 어떻게 되있나 알려주는 역할.

#datetime을 unixtime으로 
unixTime = datetime.timestamp(date)

#datetime을 string으로 
stringTime = time.strftime("%Y-%m-%d")   #인자는 어떤 포맷으로 바꿀 것인지.

#datatime 형식 바꾸기
df['timestamp'].dt.strftime('%Y-%m-%d %H:%M')  #datetime을 원하는 형식으로 변경 

######################################### dataframe #########################################

#단일 인덱싱에서는 at, iat이 작업 시간 상 유리하고, 여러 row/column을 인덱싱해야하는 상황에서는 loc, iloc을 사용해야한다. 
# at, iat은 df.at[3:100, 'column'] 이런게 안된다. 


import pandas as pd

#dataframe 만들기
pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
df = pd.DataFrame(columns=['timestamp', 'buy', 'sell'])
df = pd.DataFrame({'timestamp' : timestamp, 'price' : price})

#index값 추출
df.index   # return index list
df.index[i]

#loop 돌때 빠른 at
df.at[index, 'timestamp']

#인덱스 위치 데이터 추출
df['timestamp'].iloc[-1]   

#지수표기법 변경
pd.options.display.float_format = '{:.2f}'.format
pd.reset_option('display.float_format')

#데이터프레임 합치기
df = pd.concat([df1, df2])

#데이트프레임 열 평균
df['buy'].iloc[:2].mean()       # 인덱스 0부터 1까지 평균
(df['buy'].iloc[:2]*df['sell'].iloc[:2]).mean()  #.sum()

#데이터프레임 nan 확인
pd.isna(df.at[i,'timestamp'])   #nan이면 True 반환
pd.notna(df.at[i,'timestamp'])  #nan이 아니면 True 반환 

#inplace
데이터프레임에서 inplace=True 값을 주면 원본객체를 함께 변경한다는 뜻임.
즉 df = df.sort_value() 이런식으로 원본 변수에 다시 지정안해줘도 된다는 뜻.

#조건으로 데이터프레임 행 추출하기 
timestamp = datetime.now()
df = df[timestamp<=df['timestamp']]

df = df[df['name']!='hongsa']   #name이 hongsa인 칼럼 지우기 

df_index = df[df['name']=='hongsa'].index
df.drop([df_index])            #index로 행 삭제하기.

#데이터프레임 행 추가하기 
df.loc[len(df)] = ['2022',3,4] #행 전체를 추가하기 

for key,value in 딕셔너리.items() 
    df.loc[key] = value

#필요한 column만 추출하기 
df = df.loc[:,['exchange','local_timestamp','asks[0].price','asks[0].amount','bids[0].price','bids[0].amount']]


#정렬하기 
df.sort_values('timestamp', ascending=False)   #timestamp값으로 내림차순 정렬  최근시간이 위로 오는 정렬 

df.reset_index(drop=True)   #index 다시 설정 drop=true는 이전의 index열 삭제함. 


#중복값 제거하기 
df.drop_duplicates(['timestamp'], keep='first', ignore_index =True)     #timestamp 값중에 중복되는 것을 찾고 첫번째놈 남기고 지워, 그리고 인덱스 다시 설정.
                                                                        #first, last ,False(중복값 모두 제거)

#groupby 
https://ponyozzang.tistory.com/291
df = df.groupby('local_timestamp').tail(1)                  ##timestamp컬럼 데이터들 중 똑같은애들끼리 묶어서 그룹화하고 마지막행만 모아서 리턴



#########################################  #########################################
mlflow 
pip install mlflow 
mlflow ui 

mlflow.set_tracking_uri('http://127.0.0.1:5000')
mlflow.create_experiment('Test')
mlflow.set_experiment('Test')

param = {'spreadIn':spreadFrom, 'spreadOut':outSpread}
mlflow.log_params(param)

log_metric("profitRate", round(pnlDf['총수익률'].iloc[-1],4))
log_metric("tradingCount", len(pnlDf))
#########################################  #########################################
asyncio 비동기함수 

비동기함수란 함수 완료 여부와 상관 없이 호출자에게 리턴하며, 작업이 완료되면 호출자에게 완료를 통보한다. 

#########################################  #########################################

try:
    print('hi')
except:
    pass            #어떤 오류든 그냥 pass 

except Exception as e:
    print(e)        #오류 내용을 출력해줌

except 오류이름:
    특정오류가 발생하면 실행 .
finally:
    오류가 발생해서 코드 진행이 멈추기 직전에 마지막으로 실행하는 함수. 


#########################################  #########################################
#########################################  #########################################
#########################################  #########################################
#########################################  #########################################
#########################################  #########################################
#########################################  #########################################
#########################################  #########################################

