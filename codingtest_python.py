# RunTime error 이유 : 0으로 나눴을때, index에러, 선언하지않은 변수를 사용할때,
# 3차원 배열 선언시 주의 사항 : *로 배열을 늘리면, 얕은 복사때문에 한 요소가 변경되면 다른 요소도 자동으로 변경됨.
# 3차원 배열 선언 : 3d_array = [[[0 for _ in range(column)] for _ in range(row)] for _ in range(level)]
# dfs 쓸때 : sys.setrecursionlimit(10**6)
# dfs 쓸때 : nonlocal 변수 선언 필요할때 있음

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

list1.index(30)  # 요소 값이 30인 index값 리턴
list1.pop(3)  # index 3 요소 삭제, 삭제된 요소 리턴
list1.clear()  # 아예 리스트 비우기
list1.sort()  # 올림차순
list1.sort(reverse=True)  # 내림차순

list1.reverse() # 리스트 뒤집기

list2 = [[1,2],[4,3],[3,6]]
list2.sort() ## 이중리스트를 정렬하면 리스트의 첫번째 요소 숫자를 기준으로 정렬함
list2.sort(key=lambda x: (x[1],x[0])) ## 이렇게 하면 정렬기준을 리스트 2번째 요소를 기준으로 정렬함.

''.join(i for i in letters)  # 리스트 요소 사이사이에 '' 요게 들어감.
''.join(letters) # 위에랑 똑같은 말임. 위는 리스트 요소마다 변화를 줄 수 있는 것이 차이점.

min(list1)
max(list1)
sum(list1) #숫자로 이루어진 리스트의 요소들의 합

# map(함수, 리스트) : 리스트 요소를 하나씩 순회하면서 함수에 적용, 함수에 적용된 요소들이 리스트로 리턴.
lst = map(lambda x: x**2, lst)

from itertools import combinations
items = [1,2,3,4,5,6,7]
list(combinations(items,2))  # 리스트에서 요소2개를 뽑는 모든 경우의 수 # [(1,2),(1,3),.....]
for i in combinations(items,2):
    print(i)  # (1,2), (1,3), ...

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
string1.find("h") #문자열에 h가 있는지 , 있으면 index리턴 , 여러개있으면 제일 첫번째꺼 리턴, 없으면 -1 리턴
string1.rfind("h",0,6) # 오른쪽부터 h 찾기시작. 인덱스 0부터 6까지(6은미포함) 탐색, 찾은 인덱스 리턴
string1[0] # h 
list(string1) ## 문자열 한글자마다 잘라서 리스트로 만들어줌
string1.startswith("hi") #문자열이 "hi"로 시작하는지 T/F
string1.endswith("hi")
string1.split('.')  #'.' 를 기준으로 문자열 나누기 리스트로 반환
string1.isalpha()
string1.isdigit() # 문자열이 숫자로만 이루어져 있는지 T/F 판별. 양수만 판별가능
string1.replace('hi', 'hello') # 파이썬 replace는 모든 hi 를 다 바꿈 , javascript는 하나만 바꿈
# rstrip, lstrip  양쪽 or 오른쪾 or 왼쪽에 h문자열이 있으면 h문자열이 안나올때까지 h를 없앰.
string1.strip() ## 문자열 앞뒤 공백제거
string1.strip('hi') ## hi를 인자로 전달하면 문자열의 앞뒤에 있는 h,i 문자를 제거함. h,i가 안나올때까지 계속 지움.
string1.upper()
string1.isupper()
string1.lower()
string1.islower()
string1.isdecimal() # 문자가 숫자인지 아닌지 true false, isdigit도 있음.
string1[::-1] # 문자열 뒤집기
list(string1) #문자열을 한글자로 분리시켜서 리스트로 리턴
for char in string1:    #문자열 인덱스위치로 값리턴
    print(char)
    
## 딕셔너리 
obj = dict()

del obj['key']  ## 딕셔너리 key,value 삭제하기 
keylst = list(obj.keys())
valuelst = list(obj.values())
keyValuelst = list(obj.items())  ## [(key,value),(key2,value2),...]
value = obj.get('key') ## obj['key'] 와 동일하지만 get은 오류를 일으키지않고 none값을 리턴함.

## 딕셔너리안에 특정 key값이 존재하는지 확인
if 'key' in obj:
    print(True)
if 'key' not in obj:
    print(True)
    
for key,val in obj.items():
    print(key,val)





############################################################################################
############################################################################################
############################################################################################
############################################################################################

############################################################################################
############################################################################################
############################################################################################
############################################################################################

############################################################################################
############################################################################################
############################################################################################
############################################################################################
###### 코딩 테스트 ####
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
# 서로다른 n개 중에 r개를 선택하는 경우의 수 (순서 x, 중복 x) 재귀함수
def DFS(v,index):
    global cnt
    if v == m :
        print(res)
        cnt+=1
        return
    else:
        for i in range(index,n+1):
            if checkList[i]==0:  ## 아직 뽑지않은 선택지만 뽑기위한 조건
                res[v] = i
                checkList[i]=1  ##순열에서는 뽑은 선택지는 다시 뽑으면 안되기때문에 checkList에서 표시를 해준다.
                DFS(v+1,i+1)   ## 다음선택지 for문을  전에 선택한 인덱스 + 1 부터로 시작하기 위한 조건 
                checkList[i]=0 ##다시 되돌아 왔을때, 기존에 선택했던 선택지가 아닌 다른 선택지를 선택하러 for문이 넘어가기때문에 리셋해준다.
# 순열 : 서로다른 n개 중에 r개를 선택하는 경우의 수 (순서 o, 중복 x) : n!/(n-r)!, 재귀함수
def DFS(v):
    global cnt
    if v == m :
        print(res)
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            if checkList[i]==0:  ## 아직 뽑지않은 선택지만 뽑기위한 조건
                res[v] = i
                checkList[i]=1  ##순열에서는 뽑은 선택지는 다시 뽑으면 안되기때문에 checkList에서 표시를 해준다.
                DFS(v+1)
                checkList[i]=0 ##다시 되돌아 왔을때, 기존에 선택했던 선택지가 아닌 다른 선택지를 선택하러 for문이 넘어가기때문에 리셋해준다.

if __name__ == "__main__":
    n = 4
    m = 3
    cnt = 0
    checkList = [0]*(n+1)
    res = [0]*m
    
    DFS(0)
    print(cnt)
    
# 중복 순열 : n^r, 재귀함수 활용
def DFS(v):
    global cnt
    if v == m :
        print(res)
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            # 중복순열에서는 뽑은거 다시 뽑아도 되기때문에 checkList없어도 됨.
            res[v] = i
            DFS(v+1)

if __name__ == "__main__":
    n = 4
    m = 3
    cnt = 0
    res = [0]*m
    
    DFS(0)
    print(cnt)
    
# 원 순열 : 원 모양의 테이블에 n개의 원소를 나열하는 경우의 수 : (n-1)!

# 요세푸스 문제 (원 순열 java version)
# int idx = 0;
# while (!list.isEmpty()) {
#     idx = (idx + k - 1) % list.size();
#     list.append(list.remove(idx))
# }

# 조합 : 서로다른 n개 중에 r개를 선택하는 경우의 수 (순서 x, 중복 x) : n!/(n-r)!r!

#재귀함수 : 어떤 함수내에서 자기 자신함수를 호출하여 작업을 계속 수행하는 방식

#복잡도 
    # 시간 복잡도 : 알고리즘의 필요 연산 횟수 
    # 공간 복잡도 : 알고리즘의 필요 메모리 
    # 두 복잡도는 trade off 관계에 있다.

#이진 탐색 트리 : 왼쪽 자식노드는 부모보다 작고, 오른쪽 자식 노드는 부모보다 큼

# 수열
    # 등차 수열 일반항 : an = a1 + (n-1)*d       # d는 등차값 
    # 등차 수열 합 : n(a1 + an)/2
    # 등비 수열 일반항 : an = a1 * r^(n-1)
    # 등비 수열 합 : a1 * (1-r^n)/(1-r)

# 최소값 구하기 
arr = []
arrMin = float('inf')
for num in arr:
    if num<arrMin:
        arrMin = num

#10진수를 2진수로 (재귀함수 이용) 10진수를 2로 나눠서 나온 나머지와 몫을 이용.
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end= ' ')

# 정다면체
# 두 개의 정N면체와 정M면체 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성
# 정답이 여러개일 경우 오름차순으로 출력

# 두개의 주사위 값의 합은 최대 M+N이다. 
lst = [0]*(M+N)
for i in range(1,N+1):
    for j in range(1, M+1):
        lst[i+j] += 1
# 이렇게 하면 리스트의 인덱스 값이 두 숫자의 합이 되고, 인덱스에 위치해 있는 값이 그 합이 나온 횟수를 나타내게 된다.


## 자연수x의 각 자릿수의 합
sum = 0
while x>0:
    sum+=x%10
    x=x//10

## 1부터 n까지의 정수중 소수의 개수 구하기 
lst = [0]*(n+1)
cnt = 0
for i in range(2,n+1):
    if lst[i]==0:
        cnt += 1
        for j in range(i, n+1, i):
            lst[j] = 1
            
## 자연수 n을 뒤집은 자연수, 첫째자리가 0이면 생략 , 숫자 뒤집기
n = 9010
res = 0 

while n>0:
    add=n%10
    res = res*10 + add 
    n=n//10
    
## 자연수 n이 소수인지 판별
def isPrime(x):
    if x==1:
        return False 
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

## 주사위 3개를 던졌을때, 숫자 3개가 같은경우, 2개가 같은경우, 모두 다른 경우

if lst[0] == lst[1] and lst[0] == lst[2]:
    prize = 10000+lst[0]*1000
elif lst[0] == lst[1] or lst[0] == lst[2]:
    prize = 1000+lst[0]*100
elif lst[1] == lst[2]:
    prize = 1000+lst[1]*100
else:
    prize = max(lst)*100
    
## 점수 계산 : n개의 문제가 있고 한 문제당 점수 1점 연속으로 맞출수록 가산점 1점씩 추가
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
        
## 회문 문자열 검사  : 똑바로 읽어도 거꾸로 읽어도 똑같은 문자열 
str1 = "moon"
str1 = str1.upper()
str1[::-1] #문자열 뒤집기, 쉬운방법

# for문으로 돌리는 방법
for i in range(len(str1)//2):
    if str1[i] != str1[-1-i]:
        print('NO')
        break
else:
    print('YES')
    

## 스왑 
lst = [1,2,3,4,5]

lst[0],lst[4] = lst[4], lst[0]


## 이미 정렬되어있는 리스트 2개를 합쳐서 다시 정렬하기 
lst = [1,2,3,4]
lst2 = [4,7,8,9,10]

result = []

p1 = 0
p2 = 0

while p1<len(lst) and p2<len(lst2):
    if lst[p1]<lst2[p2]:
        result.append(lst[p1])
        p1+=1
    else:
        result.append(lst2[p2])
        p2+=1

if p1<len(lst):
    result += lst[p1:]
else:
    result += lst2[p2:]

print(result)


## 다이아몬드 탐색, 이중 리스트 , 이중 for문 탐색
n = 5
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

## 리스트 요소 회전시키기 (요소들 자리를 한칸씩 옮기기)
# pop(), insert(), append()
rolling = [[1,0,3],[2,1,3]]
lst = [[12,39,30,23,11],[1,4,6,2,5]]

for roll in rolling: 
    if roll[1] == 0:
        for _ in range(roll[2]):
            pop = lst[roll[0]-1].pop(0)
            lst[roll[0]-1].append(pop)
    else:
        for _ in range(roll[2]):
            pop = lst[roll[0]-1].pop()
            lst[roll[0]-1].insert(0,pop)
            
            
## 이중 리스트에서 상하좌우에 있는 값 비교 
# all() 인자로 리스트를 받고 리스트 요소들이 모두 True일때만 True 반환
n = 5
count = 0

dx=[-1,0,1,0]
dy=[0,1,0,-1]

lst = [[n for n in range(5)] for _ in range(n)]

print(lst)

for i in range(1,n):
    for j in range(1,n):
        if all(lst[i][j]>lst[i+dx[k]][j+dy[k]] for k in range(4)):
            count+=1
            
            
## 7*7 격자판에서 5개의 연속되는 수가 (가로, 세로) 회문수인 경우의 수
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
            

## 이분검색, 이분탐색 (up down할때 빨리 찾는법)
lst = [23,87,65,12,57,32,99,81,31]

lst.sort()

m = 32

lt = 0
rt = len(lst)-1

while lt<=rt:
    mid = (lt+rt)//2
    if m<lst[mid]:
        rt= mid-1
    elif m>lst[mid]:
        lt= mid+1
    else:
        result = mid+1
        break
    
print(result)

## 그리디 : 현재 단계에서 가장 좋은 선택을 하는 과정. 정렬이 동반됨, 리스트를 정렬후 순회하면서 조건대로 풀어내기

## 스택 (list) : 후입선출 나중에 들어간게 먼저 나온다, 리스트에 먼저들어간 요소가 조건에 안맞으면 pop해서 제거 
num = 5276823
m = 3

stack = []
lst = list(str(num))

for x in lst:
    while stack and m>0 and stack[-1]<x :
        stack.pop()
        m -= 1
    stack.append(x)
    
if m!= 0:
    stack = stack[:-m]
    
print(stack)

## 큐 (deque): 선입선출 , 들어간 순서대로 나옴. 먼저들어간 요소들이 popleft로 차례대로 나오면서, 다시 append로 들어감. 조건에 맞춰서 pop만 시킬 요소 가려내기

## 해시 (dict) : key, value로 이루어진 자료구조를 말한다.

## 이진 트리 : 각 노드가 최대 2개의 자식노드만 가질 수 있는 트리, 자식노드의 좌우를 구분함.
    ## 포화 이진 트리 : 모든 레벨에서 노드가 꽉차있는 트리
    ## 완전 이진 트리 : 마지막 레벨을 제외하고 노드들이 모두 채워져있는 트리
    ## 정 이진 트리 : 자식 노드를 0개 또는 2개를 가지고 있는 트리
    ## 편향 트리 : 한쪽으로 기울어진 트리
    ## 균현 이진 트리 : 모든 노드의 좌우 서브 트리 높이가 1이상 차이 나지 않는 트리 

## 힙 : 이진트리 구조. 부모노드가 자식노드값보다 크거나 작아야함. 같을 수 는 없음.

## 이진트리순회 (DFS) :깊이 우선 탐색, 부모노드부터 시작해서 왼쪽 노드로 계속 탐색. 경우의 수 같은 문제에 쓸 수 있음.
# 예제는 1부터7까지의 숫자가 적힌 이진트리를 탐색하며 숫자출력하는 재귀함수 구현
def DFS(v):
    if v>7:
        return 
    else:
        DFS(v*2) #왼쪽노드
        DFS(v*2+1) #오른쪽노드
        print(v, end= " ") #현재노드
        # print 구문이 어디 들어가냐에따라 전위순회(현재노드->왼쪽노드->오른쪽노드), 중위순회(왼쪽->현재->오른쪽), 후위순회(왼쪽->오른쪽->현재)로 나뉨. 어떤 노드부터 탐색할것이냐. 이방식은 후위순회임.

## 이진트리순회 (BFS) : 넓이 우선 탐색, level순으로 탐색