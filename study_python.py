https://senticoding.tistory.com/49      ##docker 개념 
https://github.com/amamov/teaching-async-python     ##비동기 async 교육 소스코드
https://github.com/amamov/teaching-type-python-oop/tree/main/00%20%EC%B2%AB%20%EC%8B%9C%EC%9E%91    # 파이썬 개발환경 설정.
https://seong6496.tistory.com/68       ## 가상환경 생성 및 삭제 
https://tempdev.tistory.com/26?category=845382     ##멀티프로세싱
https://tempdev.tistory.com/27?category=845382     ##멀티프로세싱 이게 좋네
https://wikidocs.net/85603              ##멀티프로세싱 
https://niceman.tistory.com/145         ##멀티프로세싱

#pip install 패키지명 --upgrade
#python -m pip install --upgrade pip
#pip --version
#pip freeze    설치된 패키지 확인
#pip freeze > requirements.txt    내가 설치한 패키지들 txt 파일로 만들어줌.
#pip install -r requirements.txt   txt파일에 있는 패키지들 install
#/usr/local/bin/python3.7 -m pip install psutil  원하는 interpreter에 패키지 설치 

# 현재 경로 pwd

x = [1,2,3,...]

x[0:3]   #index 0부터 2까지 
x[5:]    #index 5부터 끝까지 
x[-1]    #index 맨뒤 
x[:-1]   #처음부터 끝에서 2번째까지 
x[-3:]   #index 끝에서 3번째 부터 끝까지 
x[-4:-2] # index 끝에서 4번째부터 끝에서 3번째 까지 .

y= [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

y[0,:]   # y의 0번째 리스트에서 모든요소 


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
str.split(',')    #문자열 분리하기     ','기준으로 스트링을 나누고 리스트로 반환.
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

if 'aaa' in a:
    print('aaa exist')
    
*list1 : 리스트 언패킹 


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

hongsa(('hi','hello','bye'))   #이때 매개변수는 튜플형태로 함수안에 들어가게되고 호출할때도 names[i]의 형태로 호출해야함.

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
math.pow(10,8)      #10의 8승

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
##만일 자식의 생성자가 부모생성자와 똑같으면 굳이 자식클래스에서 생성자를 안만들어줘도 됨.
##super().getInfo() 부모클래스의 메소드를 사용






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


url = "https://restapi.nftscan.com/gw/token?apiKey=zfd"
headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
headers2 = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*','Access-Token' : ""}


url2 = "https://restapi.nftscan.com/api/v1/getAllNftPlatformInformation"


#res = requests.get(url, headers=headers)

res = requests.post(url2, headers=headers2, json={'erc':'erc721','page_index':1,'page_size':100,'user_address':"0x98e711f31e49c2e50c1a290b6f2b1e493e43ea76"})
#post에서 json = 부분은 파라미터라고 보면됨. json형태로 파라미터 작성. 
#get이면 url에 파라미터 작성. 

print(res.json())




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
stringTime = dt.strftime("%Y-%m-%d")   #인자는 어떤 포맷으로 바꿀 것인지.

#datatime 형식 바꾸기
df['timestamp'].dt.strftime('%Y-%m-%d %H:%M')  #datetime을 원하는 형식으로 변경 

######################################### dataframe #########################################

#단일 인덱싱에서는 at, iat이 작업 시간 상 유리하고, 여러 row/column을 인덱싱해야하는 상황에서는 loc, iloc을 사용해야한다. 
# at, iat은 df.at[3:100, 'column'] 이런게 안된다. 


import pandas as pd

#dataframe timestamp 날짜로 변경, dataframe timedelta (DateOffset)
pd.to_datetime(df['timestamp'], unit='s') + pd.DateOffset(hours=8)

#dataframe 만들기
pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
df = pd.DataFrame(columns=['timestamp', 'buy', 'sell'])
df = pd.DataFrame({'timestamp' : timestamp, 'price' : price})
df = pd.DataFrame([])
df = pd.DataFrame(np.random.randint(1,100,size=(100,4)))

#index값 추출
df.index   # return index list
df.index[i]

#loop 돌때 빠른 at
df.at[index, 'timestamp']
#loop 돌때 loc보다 빠른 행 넣기 
https://dowtech.tistory.com/39          

#행 위치 데이터 추출
df['timestamp'].iloc[-1]
#인덱스 위치 데이터추출   
df['timestamp'].loc[0]


#지수표기법 변경
pd.options.display.float_format = '{:.2f}'.format
pd.reset_option('display.float_format')

#데이터프레임 합치기
df = pd.concat([df1, df2], axis=1) # axis=1로 하면 옆으로 붙이기, 설정안하면 밑으로 붙이기 

#데이트프레임 열 평균
df['buy'].iloc[:2].mean()       # 행 0부터 1까지 평균
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
df.drop(columns=['name'])       #컬럼 삭제하기
df.drop('timestamp', axis=1)   # column 삭제하기 

df.loc[df["Salary"] >= 5000]
df.loc[(df["Salary"] >= 5000)&(df["Salary"] < 7000)]

df.loc[df['def'] == 1,'ghi'] = 100    # def칼럼의 값이 1인 행들에서, ghi 값을 100으로 바꾼다.
#특정 값 바꾸기
df["Gender"] = df["Gender"].replace({"M": "male", "F": "female"})

#데이터프레임 행 추가하기 
df.loc[len(df)] = ['2022',3,4] #행 전체를 추가하기 

for key,value in 딕셔너리.items() 
    df.loc[key] = value

#필요한 column만 추출하기 
df = df.loc[:,['exchange','local_timestamp','asks[0].price','asks[0].amount','bids[0].price','bids[0].amount']] 
## : 모든행에 대해, [] 안에 있는 컬럼만 추출.
df = df[['exchange','local_timestamp']]

#column 이름바꾸기 
# 전체 열 이름 입력하기
df.columns = ['col', 'col', 'col']
# 선택하여 열 이름 변경하기
df.rename(columns={'Before':'After'})
# 특정 열을 리스트로 바꾸기
timestampList = df['timestamp'].values.tolist()




#정렬하기 
df.sort_values('timestamp', ascending=False)   #timestamp값으로 내림차순 정렬  최근시간이 위로 오는 정렬 

df.reset_index(drop=True)   #index 다시 설정 drop=true는 이전의 index열 삭제함. 


#중복값 제거하기 
df.drop_duplicates(['timestamp'], keep='first', ignore_index =True)     #timestamp 값중에 중복되는 것을 찾고 첫번째놈 남기고 지워, 그리고 인덱스 다시 설정.
                                                                        #first, last ,False(중복값 모두 제거)
#중복값 확인하기
df.value_counts(normalize=True)   #normalize True로 하면 비율로 보여줌.

#groupby 
https://ponyozzang.tistory.com/291
df = df.groupby('local_timestamp').tail(1)                  ##timestamp컬럼 데이터들 중 똑같은애들끼리 묶어서 그룹화하고 마지막행만 모아서 리턴
df.groupby(['city', 'fruits'],as_index=False).mean()        ##그냥 groupby하면 인덱스가 바뀌는데, 바꾸고싶지않으면 False로


#excel로 저장
df.to_excel('bal.xlsx')    # 실행하는 위치에 저장
df.to_excel(excel_writer = './Balance/bal.xlsx')  #현재위치에서 폴더만들고 저장 
df = pd.read_excel('경로/파일이름.xlsx')

df.to_csv('./경로/bal.csv', columns =['city', 'fruits'], index=True)   #index True면 인덱스도 같이 내보냄.
df = pd.read_csv('경로/파일이름.csv', encoding='UTF-8'or'cp949', skiprows=(1,2,3))  

#리스폰스 바로 데이터프레임으로 만들기 
#pd.DataFrame() 가로안에 들어간 json 파일이 list로 이루어져있으면 실행되는데, 단일 딕셔너리면 ([requests..]) 리스트로 감싸줘야함.
pd.DataFrame(requests.get("https://api.opensea.io/api/v1/collections?offset=300&limit=300").json()['collections'])




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
##try except는 try 안에 있는 코드 실행중 오류가 발생하면 except로 넘어가서 코드를 실행한뒤 
##try 안에있는 남아있는 코드를 실행하지않고 밖으로나와 프로그램을 끝까지 끝내는역할을함.


try:
    print('hi')
except:
    pass            #어떤 오류든 그냥 pass 

except Exception as e:
    print(e)        #오류 내용을 출력해줌

except 오류이름:
    특정오류가 발생하면 실행 .
else: 
    오류가 발생하지않으면 else로 와서 코드 실행 , except와 같이 사용해야함.
finally:
    오류가 발생하든 안하든 finally로 넘어오고 코드실행. except 없어도 됨. 단 except가 없으면 오류발생으로 인한 비정상 종료 


#########################################  #########################################
삼항연산자 

[trueValue] if [condition] else [falseValue]
#########################################  #########################################
크롤링 스크래핑 
import requests 
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
res = requests.get('view-source:https://opensea.io/rankings?sortBy=seven_day_volume',headers=headers)
print(res.text)


soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())


######################################### 비동기 async  #########################################
https://github.com/amamov/teaching-async-python     ##소스코드 

# pip install aiohttp~=3.7.3     #비동기 http requests


import asyncio 

async def hello_world():
    print("hello world")
    return 123
    
    
if __name__ == "__main__":
    asyncio.run(hello_world)            
    
#async로 선언된 함수 hello_world를 실행시키려면 await hello_world로 실행시켜줘야함
#근데 await는 async로 선언된 함수내에서만 쓸수있음.
#async 밖에서 await를 사용하려면 asyncio.run(hello_world) 이렇게 실행시켜주면 됨.


def main():
    url = "https://naver.com"
    
    session = requests.Session()
    session.get(url)
    session.close()
    
    with requests.Session() as session:             #위에 세줄이 이 with 구문과 똑같은 코드임.
        session.get(url)



if __name__ == "__main__":
    main()
    
    
### 기본 버전
import asyncio
import requests
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
     
    with requests.Session() as session:
        result = [fetcher(session,url) for url in urls]             #결과값이 리스트로 담김.
        print(result)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()


### async 버전
import aiohttp 

async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()            #text뒤에 () 붙여줘야함. awaitable 한 함수여야되서.
        
async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
     
    async with aiohttp.ClientSession() as session:
        #result = [fetcher(session,url) for url in urls]             #결과값이 리스트로 담김.
        #print(result)
        result = await asyncio.gather(*[fetcher(session,url) for url in urls])
        #result = await fetcher(session, urls[0])
        print(result)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end-start)
    
    
    
### multithreading 버전

import requests
import time 
import os
import threading 
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session = params[0]                 ##map으로부터 params가 튜플형태로 전달되서 이런식으로 따로 변수를 만들어줌.
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
     
    executor = ThreadPoolExecutor(max_worker=10) 
    
    with requests.Session() as session:
        params = [(session,url) for url in urls]                ##
        result = list(executor.map(fetcher, params))            ## map은 fetcher라는 함수를 multithread로 실행시켜줌 params는 파라미터 전달.
        print(result)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

### cpu bound basic 
import time
import os
import threading

# nums = [50, 63, 32]
nums = [30] * 100


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    results = [cpu_bound_func(num) for num in nums]
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 49.37, 34
    
    
### cpu bound multithreading 버전 
# cpu bound 에서는 multithreading의 효과가 없음.
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor

nums = [30] * 100
# nums = [50, 63, 32]


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 50, 36


### multiprocess 버전
## cpu bound (연산에서 발생하는 bound)에서는 multithread 방식은 효과가 거의없고, multiprocess 방식으로 해야 효과가있음.

import time
import os
import threading
from concurrent.futures import ProcessPoolExecutor

nums = [30] * 100


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    executor = ProcessPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 22

######################################### 웹 스크래핑 #########################################
#pip install beautifulSoup

from bs4 import BeautifulSoup
import aiohttp
import asyncio

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install beautifulsoup4

"""
웹 크롤링 : 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑 : 웹에서 데이터를 수집하는 프로그램
"""


async def fetch(session, url, i):
    print(i + 1)
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        cont_thumb = soup.find_all("div", "cont_thumb")             #div 블록안에 cont_thumb 클래스를 가진 모든 태그 리스트로 불러와줌.
        for cont in cont_thumb:
            title = cont.find("p", "txt_thumb")
            if title is not None:
                print(title.text)


async def main():
    BASE_URL = "https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C"
    urls = [f"{BASE_URL}?page={i}" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])

#enumerate(list)  => [(index, value),(index,value), ...]

if __name__ == "__main__":
    asyncio.run(main())


#########################################  #########################################
## numpy 

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



import numpy as np

#1차원 배열
arr = np.array([1,2,3])
print(arr)

#2차원 배열 
arr2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr)

#shape 몇행몇열 
arr.shape 
#ndim 차원
arr.ndim
#size 요소몇개 
arr.size 
#dtype 요소들의 데이터타입
arr.dtype 

#요소들 dtype 정해주기 
arr = np.array([1,2,3], dtype=np.int)
arr = arr.astype(np.float32)
#ndarray는 요소들의 데이터타입이 무조건 같아야 함. 다른 데이터타입을 넣어도 
#알아서 똑같은 데이터형으로 바꿈, 똑같이 바꿀수 없는 경우면 에러가 발생


# np.zeros()  가로안에는 shape , shape은 (2,2) [2,2] 아무거나 써도 됨.
arr = np.zeros([2,2])

# np.ones()
arr = np.ones([3,5])

# np.full()
arr = np.full((2,3), 5)

# np.eye()  대각원소가 1이고, 나머지 원소는 0인 행렬생성. k는 대각원소의 시작지점을 정해주는 파라미터
arr = np.eye(3, 4, k=0)


# np.zeros_like()   모든 원소를 0으로 만들어버림
np.zeros_like(arr)   
# np.ones_like()    모든 원소 1로 만들어버림.

# np.full_like()
np.full_like(arr,9)

#########################################  #########################################

arr = np.arange(9)      # 0~8
arr = np.arange(3,12)   # 3~11
arr = np.arange(3,13,3) # 3, 6, 9, 12

arr = np.linspace(0,100,11)  # 11개 요소가 0부터 100사이 숫자로 모두 같은 간격으로 생성됨.

arr = np.logspace(1, 10, 10, base=2)

#########################################  #########################################

#랜덤함수 rand(), randn() - 정규분포형태로 랜덤값 리턴, randint()
#loc 평균, scale 표준편차, size 표본개수
arr = np.random.normal(loc=0, scale=1, size=10 )
arr = np.random.normal(loc=0, scale=1, size=(2,3) )

import matplotlib.pyplot as plt 

arr = np.random.normal(0, 1, 1000)
plt.hist(arr, bins=100)  # bins는 몇구간으로 나눠서 볼지 
plt.show()


arr = np.random.rand(1000)  #표본개수1000개 0부터 1사이의 랜덤숫자 
arr = np.random.randn(1000)

arr = np.random.randint(low=1, high=5, size=10) #1부터 5미만 값이 10요소 리스트로 랜덤
arr = np.random.randint(low=1, high=5, size=(2,3))
arr = np.random.randint(5)   # 0부터 5미만 사이의 정수 랜덤 리턴 


# seed값을 똑같이 해서 난수를 생성하면, 똑같은 난수가 생성됨. 
np.random.seed(10)
arr = np.random.rand(10)
print('난수발생 1',arr)

np.random.seed(10)
arr = np.random.rand(10)
print('난수발생 2',arr)
#########################################  #########################################
#indexing 

arr = np.array([1,2,3,4,5,6,7])
arr[[0,2,4]]    # 0, 2, 4번째 인덱스 요소 

arr2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr2[[0,2],2:]    # 0,2 번째 인덱스 리스트에서 2번째 인덱스 요소부터 끝까지 

arr2[arr2>4]    #4보다 큰 요소 리스트로 리턴 

#########################################  #########################################
#연산

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr2 = np.array([[2,2,2],
                [2,2,2],
                [2,2,2]])
                
arr+arr2 
np.add(arr,arr2)

arr-arr2 
np.subtract(arr,arr2)

arr*arr2 
np.multiply(arr,arr2)

arr/arr2 
np.divide(arr,arr2)

arr**2 
np.square(arr)

np.sqrt(arr) #제곱근

arr // 2 # 몫 

arr % 2 #나머지 

np.dot(arr,arr2)  #진짜 행렬 계산 

np.abs(arr)   #절대값 

np.ceil(arr) #올림
np.floor(arr)#내림
np.round(arr)#반올림 
np.trunc(arr)#버림 



#########################################  #########################################


#########################################  #########################################

#########################################  #########################################

#########################################  #########################################

#########################################  #########################################

#########################################  #########################################





