#사칙연산
+ - * / 
% **
// : 나누고 나머지 뺀 정수

# 리스트 list
list1 = [1, 2, 3]
[*list1]  ##리스트 언팩킹 
letters = ["A", "B", "C"]
lst1 = ['A', 'B', 'C', 'D']
lst2 = ['C', 'D', 'E', 'F']

a= 'a'
if a == 'a' or a =='b' or a == 'c':
    print('true')

ethWalletList = [address for address in ethWalletList if(address != None)] #ethWalletList안에 요소들중 None값이 아닌것만 리스트로 리턴
lst = [int(num) for num in lst]  #lst안에 있는 스트링 숫자를 인트로바꿔서 리스트로 리턴
lst = [int(num) for num in lst if (num == '2')] #lst안에 요소에 2인것만 정수형으로 변환해서 리스트로 리턴
verb = 'buy' if amount>=0 else 'sell'

list1 = list(set(list1))  # 중복 제거
list1.index(1)
{x: 0 for x in list1}
list1.count(1)  # 요소값이 1인 갯수 세기
# 요소값이 1인 요소 삭제하기, 단 1이 여러개면  첫번째 요소만 삭제함. list1 = list1.remove(1) 이렇게 안해줘도 바뀜.
list1.remove(1)

list1.append('yellow')
list1.insert(1, 'black')  # index 1에 black 요소 추가
list1.extend(b)  # 리스트 a와 b를 합침

list1.index(30)  # 요소 값이 30인 index
list1.pop(3)  # index 3 요소 삭제
list1.clear()  # 아예 리스트 비우기

list1.sort()  # 올림차순
list1.sort(reverse=True)  # 내림차순

min(list1)
max(list1)
sum(list1) #숫자로 이루어진 리스트의 요소들의 합

round(3.12333,2)


if 'aaa' in a:          # 문자열에서 특정 문자열 찾기
    print('aaa exist')

union = (set(lst1) | set(lst2))  # 합집합, 두리스트 합집합
inter = (set(lst1) & set(lst2))  # 교집합, 두리스트에서 교집합 요소추출
complement = (set(lst1) - set(lst2))  # 차집합, lst1 기준 lst2와 다른 요소만 추출


for pair in zip(list1, letters):
    print(pair)
# (1,'A'), (2,'B') ...

for i, val in enumerate(list1):
    print(i, val)
# (0, 1), (1, 2) ...


# string 문자열
string1 = "hi hello"
string1.split('.')  #'.' 를 기준으로 문자열 나누기 리스트로 반환
string1.isalpha()
string1.isdigit()
string1.replace('hi', 'hello') # 파이썬 replace는 모든 hi 를 다 바꿈 , javascript는 하나만 바꿈
''.join(i for i in letters)  # 리스트 요소 사이사이에 '' 요게 들어감.
# rstrip, lstrip  양쪽 or 오른쪾 or 왼쪽에 h문자열이 있으면 h문자열이 안나올때까지 h를 없앰.
string1.strip('h')
string1.upper()
string1.isupper()
string1.lower()
string1.islower()
string1[::-1] # 문자열 뒤집기
list(string1) #문자열을 한글자로 분리시켜서 리스트로 리턴
for char in string1:    #문자열 인덱스위치로 값리턴
    print(char)







############################################################################################
############################################################################################
############################################################################################
############################################################################################

# 경우의 수
# 숫자가 적혀있는 N개의 카드중에 3개를 뽑아 숫자를 더한값의 모든 경우의 수 (N개중에 3개를 뽑는 모든 경우의 수)
lst = []
resultSet = set()
n = 10
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            resultSet.add(lst[i] + lst[j] + lst[m])

# 최소값 구하기 
arr = []
arrMin = float('inf')
for num in arr:
    if num<arrMin:
        arrMin = num
        

# 정다면체
두 개의 정N면체와 정M면체 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성
정답이 여러개일 경우 오름차순으로 출력

두개의 주사위 값의 합은 최대 M+N이다. 
lst = [0]*(M+N)
for i in range(1,N+1):
    for j in range(1, M+1):
        lst[i+j] += 1
이렇게 하면 리스트의 인덱스 값이 두 숫자의 합이 되고, 인덱스에 위치해 있는 값이 그 합이 나온 횟수를 나타내게 된다.


#자연수x의 각 자릿수의 합
sum = 0
while x>0:
    sum+=x%10
    x=x//10

# 1부터 n까지의 정수중 소수의 개수 구하기 
lst = [0]*(n+1)
cnt = 0
for i in range(2,n+1):
    if lst[i]==0:
        cnt += 1
        for j in range(i, n+1, i):
            lst[j] = 1
            
# 자연수 n을 뒤집은 자연수, 첫째자리가 0이면 생략 
n = 9010
res = 0 

while n>0:
    add=n%10
    res = res*10 + add 
    n=n//10
    
# 자연수 n이 소수인지 판별
def isPrime(x):
    if x==1:
        return False 
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

# 주사위 3개를 던졌을때, 숫자 3개가 같은경우, 2개가 같은경우, 모두 다른 경우

if lst[0] == lst[1] and lst[0] == lst[2]:
    prize = 10000+lst[0]*1000
elif lst[0] == lst[1] or lst[0] == lst[2]:
    prize = 1000+lst[0]*100
elif lst[1] == lst[2]:
    prize = 1000+lst[1]*100
else:
    prize = max(lst)*100
    
# 점수 계산 : n개의 문제가 있고 한 문제당 점수 1점 연속으로 맞출수록 가산점 1점씩 추가
lst = [1,0,1,1,1,0,0,1,1,0]
n = 10
score = 1
res = 0
for i in range(n):
    if lst[i] == 0:
        score = 1
        continue
    else:
        res += score
        score += 1
        
# 회문 문자열 검사  : 똑바로 읽어도 거꾸로 읽어도 똑같은 문자열 
str1 = "moon"
str1 = str1.upper()
str1[::-1] #문자열 뒤집기, 쉬운방법

# for문 돌리는 방법
for i in range(len(str1)//2):
    if str1[i] != str1[-1-i]:
        print('NO')
        break
else:
    print('YES')