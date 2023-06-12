# RunTime error 이유 : 0으로 나눴을때, index에러, 선언하지않은 변수를 사용할때,
# 3차원 배열 선언시 주의 사항 : *로 배열을 늘리면, 얕은 복사때문에 한 요소가 변경되면 다른 요소도 자동으로 변경됨.
# 3차원 배열 선언 : 3d_array = [[[0 for _ in range(column)] for _ in range(row)] for _ in range(level)]
# dfs 쓸때 : sys.setrecursionlimit(10**6)
# dfs 쓸때 : nonlocal 변수 선언 필요할때 있음
# 깊은복사 import copy , copy.deepcopy(lst), or 2차원 리스트 깊은복사 : [lst[:] for lst in lsts]
from collections import deque
from collections import Counter
lst = deque()
lst.append(1)
lst.appendleft(2)
lst.popleft()
lst.pop()
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

L = [{'name':'John','score':83},{'name':'hong','score':93}]
list1.sort(key=lambda x: x['score'], reverse= True) ## lambda x에서 x는 리스트의 각 요소를 말함. key를 지정할때 x['score']를 기준으로 정렬해주는것임.

list1.reverse() # 리스트 뒤집기

list2 = [[1,2],[4,3],[3,6]]
list2.sort() ## 이중리스트를 정렬하면 리스트의 첫번째 요소 숫자를 기준으로 정렬함
list2.sort(key=lambda x: (x[1],x[0])) ## 이렇게 하면 정렬기준을 리스트 2번째 요소를 기준으로 정렬함.
lst.sort(key=lambda x : (x[1],-x[2],x[3],x[0]), reverse=True) ## 여기서 x[0]은 문자열이라서 -를 못붙인다. 이때 reverse를 활용해야함.

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

obj = dict(sorted(obj.items(),reverse=True))  # 딕셔너리 정렬
obj = dict(sorted(obj.items(), key= lambda x: x[1],reverse=True))  # value기준 정렬, 딕셔너리 정렬

counter = Counter(obj)
counter2 = Counter(lst)
counter.most_common(10) # value값이 가장 큰 10개 리스트로 출력 [(key,value),....]
counter2.most_common(10) # value값이 가장 큰 10개 딕셔너리로 출력 {요소값:나온횟수}

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
   




########################################################################################################        
########################################################################################################        
################################################ 자료구조 ################################################
########################################################################################################   
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

  
########################################################################################################        
########################################################################################################        
################################################ 알고리즘 ################################################
########################################################################################################        
########################################################################################################        
########################################################################################################        
########################################################################################################  
# 이분탐색
# 트라이
# 우선순위큐 
# 그리디
# 완전탐색
# 분할정복
# DFS, BFS
# 백트래킹
# 최단경로
# 투포인터
# 동적계획법
# 냅색 알고리즘
# 최소신장트리 (크루스칼, 프림)
# 최단경로 (다익스트라, 벨만포드, 플로이드워셜)
# 기타


## 이분탐색? (정렬된 리스트에서 특정값을 찾고싶을때, 결과 빨리 찾기// 꼭 완전히 정렬되어있지않아도됨. 결과값을 기준으로 특정 규칙으로 정렬되어있으면 이분탐색 가능)
left = 0              #리스트 첫 인덱스
right = len(lst)-1    #리스트 마지막 인덱스

num = 8  # 이값보다 작으면 조건 만족

result = left - 1     #결과 초기값
while left<=right:
    middle = (left+right)//2
    
    if lst[middle]>=num:  #조건에 만족하지 않을때
        right = middle-1
    else:                 #조건에 만족할때
        left = middle+1
        result = middle   #조건에 만족할때 그때의 인덱스 result에 저장, 경우에 따라 결과값이 최선의 선택이면 break로 while문 탈출


## 트라이? (문자열 검색에 응용, 문자열검색을 엄청많이 반복해야될때 유용)
def solution(words, queries):
    trie_dict = dict()

    ## 문자열 길이에 따라서 트라이를 여러개 만들어냄.
    for idx, word in enumerate(words):
        n = len(word)
        if n not in trie_dict:
            trie_dict[n] = Trie()
        trie_dict[n].add_word(word, idx)
    
    result = []
    for query in queries:
        n = len(query)
        if n not in trie_dict:
            result.append([])
        else:
            result.append(trie_dict[n].get_result(query))

    result = [[words[idx] for idx in r] for r in result]
    return result

class Node:
    def __init__(self, val):
        self.val = val      # 필수
        self.children = dict()      # 필수
        self.words = []     # 추가 기능


class Trie:
    def __init__(self):
        self.head = Node(None)  # 필수
    
    def add_word(self, word, idx):
        curr = self.head    # 필수
        curr.words.append(idx) # 추가 기능
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c) # 필수
            curr = curr.children[c] # 필수
            curr.words.append(idx) # 추가 기능

    def get_result(self, query):
        curr = self.head

        for c in query:
            if c == '?':
                return curr.words
            if c not in curr.children:
                return []
            curr = curr.children[c]
        return curr.words

# words = ["hello", "hear", "hell", "good", "goose", "children", "card", "teachable"]
# queries = ["he??", "g???", "childre?", "goo????"]


## 우선순위큐? (작업순서 문제에 적용)
from queue import PriorityQueue
pq = PriorityQueue()
pq.put((priority, data1, data2))
pq.get()

import heapq 
heapq.heapify(lst)
heapq.heappush(lst,(priority,data1,data2)) ## priority 기준으로 최소힙정렬함.
heapq.heappop(lst)


## 그리디? : 현재 단계에서 가장 좋은 선택을 하는 과정. 정렬이 동반됨, 리스트를 정렬후 순회하면서 조건대로 풀어내기

## 깊이우선탐색 (DFS?) : 이진트리의 경우 부모노드부터 시작해서 왼쪽 노드로 계속 탐색. 경우의 수 같은 문제에 쓸 수 있음.
# 그래프에서의 DFS 탐색 (인접리스트 탐색) : 모든 정점을 방문하는 방법, 만약 visit리스트에 False가 남아있다면 출발지점에서 시작해서 그 정점에 방문할수 없다는뜻.
lst = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]] # 0번 정점은 없다고 가정한것임.
visit = [False]*(n+1)
def dfs(v):
    visit[v] = True
    print(v) # 정점에 방문하면 정점출력
    for i in lst[v]:
        if not visit[i]:
            dfs(i)
            
# 1부터7까지의 숫자가 적힌 이진트리를 탐색하며 숫자출력하는 재귀함수 구현 (트리구조가 표현된 리스트에서)
def DFS(v):
    if v>7:
        return 
    else:
        DFS(v*2) #왼쪽노드
        DFS(v*2+1) #오른쪽노드
        print(v, end= " ") #현재노드
        # print 구문이 어디 들어가냐에따라 전위순회(현재노드->왼쪽노드->오른쪽노드), 중위순회(왼쪽->현재->오른쪽), 후위순회(왼쪽->오른쪽->현재)로 나뉨. 어떤 노드부터 탐색할것이냐. 이방식은 후위순회임.

## 완전탐색? 경우의 수 DFS
# 모든경우의 수 (모든 부분집합 구하기)
ch = [0]*(n+1)
def dfs(v,sum):
    if v == n+1:
        print(sum)
        for c in ch:
            "doSometing"
    else:
        ch[v] = 1
        DFS(v+1,sum+addsometing) # 원소를 선택했을때 sum값을 바꾸고 넘김
        ch[v] = 0 
        DFS(v, sum) # 원소를 선택하지 않았을땐 sum값을 그대로 넘김
    
# 서로다른 n개 중에 r개를 선택하는 경우의 수 조합 (순서 x, 중복 x) 
def DFS(v,index):
    global cnt
    if v == m :
        print(res)
        cnt+=1
        return
    else:
        for i in range(index,n+1):
            res[v] = i
            DFS(v+1,i+1)   ## 다음선택지 for문을  전에 선택한 인덱스 + 1 부터로 시작하기 위한 조건 , 그냥 i 넣으면 중복 허용 (순서x,중복o)
            
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

    
# 중복 순열 : n^r, 서로다른 n개 중에 r개를 선택하는 경우의 수 (순서 o, 중복 o) 재귀함수 활용
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


## 넓이우선탐색 (BFS) : level순으로 탐색
# 그래프에서의 BFS 탐색 (인접리스트) : 모든 정점 방문하는 방법
lst = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]] # 0번 정점은 없다고 가정한것임.
visit = [False]*(n+1)
def bfs(v):
    que = deque([])
    que.append(v)
    visit[v] = True # 중요 
    
    while que:
        x = que.popleft()
        
        for i in lst[x]: #여기서 lst[x]는 다음선택지들의 리스트
            if visit[i]: #그 선택지들이 이미 갔던곳인지, 갈수있는곳인지 체크
                continue 
            que.append(i) #que에 작업추가
            visit[i] = True ## 이 부분이 중요
            
## 분할정복?
# 기본원리
def divide(lst, left, right):
    # 최대로 분할했을때(left == right): 리턴할 값 
    # 분할도중 더이상 분할하지않아도 될때가 있으면 그때의 조건과 리턴 값.
    # 분할해야할때 left, right 인덱스값 수정해서 재귀함수 호출 
    # 재귀함수가 리턴한 값들을 통해 자신이 얻고자 하는 값을 리턴 
    
# 최대값 찾기
def getMax(lst, left, right):
    mid = (left+right)//2 
    if (left == right): return lst[left]
    
    left = getMax(lst, left, mid)
    right = getMax(lst, mid+1, right)
    
    return left if left>right else right

# 부분수열의 최대 합 
def divideSubArray(lst, left, right):
    if (left == right) : return lst[left]
    
    mid = (left+right)//2
    # 단일 요소 값
    maxLeft = divideSubArray(lst,left,mid) 
    maxRight = divideSubArray(lst,mid+1,right)
    
    # 요소 2개 이상인 부분수열의 합
    maxarr = getMaxSubArray(lst, left, mid, right)
    
    return max(maxLeft, max(maxRight,maxarr))

def getMaxSubArray(lst, left, mid, right):
    sumLeft = 0
    maxLeft = float("-inf")
    
    for i in range(mid,left-1,-1):
        sumLeft += lst[i]
        maxLeft = max(maxLeft, sumLeft)
        
    sumRight = 0
    maxRight = float("-inf")
    
    for i in range(mid+1,right+1):
        sumRight += lst[i]
        maxRight = max(maxRight, sumRight)
        
    return maxLeft + maxRight


## 백트래킹? : 트리탐색 (DFS)에서 재귀호출 for문(다음노드 후보군)에서 if문으로 조건을 정해서 조건에 만족하는 노드만 재귀호출 하는 것.
## 투포인터? 
def twoPointer(lst, target):
    p1 = 0
    p2 = 0
    total = 0
    result = [-1,-1]
    
    while True:
        if total>target:
            total -= lst[p1]
            p1 += 1
        elif total<target:
            total += lst[p2]
            p2 += 1
        
        if total == target:
            result[0] = p1 
            result[1] = p2 - 1
            break 
        elif total<target and p2 == len(lst): break
    
    return result

## 최단경로?
# 다익스트라 
    # 출발점에서 목표점까지 최단경로를 구함
    # 한노드에서 다른 모든 노드까지의 최단경로를 모두 구함
    # 간선에 음의 가중치가 없어야함
visit = [0] * N
res = [float("inf")] * N
obj = {
    1 : [[2,2],[3,3]],  # 노드1에서 노드2, 3이 연결되어있고 그에따른 가중치 
    2 : [[3,4],[4,5]],
    3 : [[4,6]],
    5 : [[1,1]]
}
res[1] = 0 # 노드1에서 1로 가는 비용은 0

while True:
    ## 아직 방분하지 않은 곳들 중에서 가장 res값이 낮은곳 선택
    startNode = -1
    minValue = float("inf")
    for i,v in enumerate(res):
        if visit[i] == 0:
            if v<minValue:
                startNode = i
                minValue = v
    if startNode == -1 :
        break
    visit[startNode] = 1
    # startNode에서 연결된 노드들까지 가는데 드는 최소비용 
    for l in obj[startNode]:
        if visit[l[0]] == 0:
            res[l[0]] = min(res[l[0]],res[startNode]+l[1])

## 동적계획법? : dfs로 모든 경우의 수를 파악하기에는 경우의 수가 너무 많고, 최대값 최소값과 관련된 얘기가 나오면 동적계획법을 생각해야한다.
    # 동적계획법에서 리스트 형태가 나온다면, 그 리스트사이즈인 d리스트를 생성해서 요소요소마다 값을 채우는법을 먼저 생각한다.
    # 동적계획법은 d[N] 값을 구하는 것이기 때문에 d[0]부터 d[N]까지 어떤식으로 채워서 넣어야할지 부터 생각해야한다.

## 냅색 알고리즘?
# 냅색알고리즘  선택지 중복선택 O
def solutionNS():
    N = 11 # 무게 제한
    d = [0]*(N+1)
    lst = [[5,12],[3,8],[6,14],[4,8]] # 가치, 무게
    
    for v in lst:
        for i in range(v[1], N+1):
            d[i] = max(d[i],d[i-v[1]] + v[0])
    
    print(d[N])

# 냅색알고리즘 최대점수 구하기, 선택지 중복선택 X
def solution9987():
    N = 20 # 무게 제한
    lst = [[10,5],[25,12],[15,8],[6,3],[7,4]] # [가치,무게]
    
    d = [0]*(N+1)
    
    for q in lst:
        for i in range(N, q[1]-1, -1):
            d[i] = max(d[i], d[i-q[1]]+q[0])
                
    print(d[N])
# 중복선택 X 버전, 이중리스트로 구현하는법
    # d[선택지갯수+1][가방무게+1] 만들기
    # d[0][0~end] 까지 모두 0으로 초기화
    # d[1][0~end] d[1]은 우선 d[i-1]꺼 복사 
    # 이후 비교참조는 d[i-1] 부분과 비교 -> 중복선택하지 않기 위한 로직
    
    
## 최소신장트리? : 최소 비용으로(선택된 모든 간선비용의 합) 모든 노드들을 연결하는 방법
# 크루스칼 
    # 간선 중 최소 값을 가진 간선부터 연결 ( 가중치 기준 정렬 필요)
    # 사이클 발생시 다른 간선 선택 
        # Union-find 방식 
graph = [(1,3,1), (1,2,9), (1,6,8), (2,4,13), (2,5,2) ,(2,6,7) ,(3,4,12) ,(4,7,17),(5,6,5),(5,7,20)] #(정점1, 정점2, 가중치) / 중복간선정보있어도됨.
graph.sort(key=lambda x: x[2]) 

mst = []
n = 7 # 정점 개수 
parent = [0] 

for i in range(1,n+1):
    parent.append(i) # 각 정점의 부모를 자기자신으로 일단 표기
    
def find(u):
    if u!=parent[u]:
        parent[u] = find(parent[u])
        
    return parent[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    
    if u<v:
        parent[root2] = root1
    else:
        parent[root1] = root2
    
mst_cost = 0 # 가중치 합 

for l in graph:
    a, b, w = l
    if find(a) != find(b): ## 부모노드가 같다는건 사이클이 발생했다는 뜻.
        union(a,b)
        mst.append((a,b))
        mst_cost += w
        
print(mst_cost, mst)

# 프림 
    # 임의의 노드에서 시작
    # 간선정보 리스트를 -> 딕셔너리 형태로 바꿔야함. {노드 : [(가중치, 노드, 노드2), (가중치2, 노드, 노드3)]}
    # 연결된 노드들의 간선 중 낮은 가중치를 갖는 간선 선택 (최소 heap으로 구현)
    # 추가된 노드가 가지고 있는 간선들(방문하지 않은 쪽 간선만) heap에 추가
    # 즉 갈수있는 경로(간선)에서 최소 가중치를 가진 간선을 계속 선택하는 과정
    # 간선의 개수가 많을 때 크루스칼보다 유리 

import heapq
import collections

n = 7 # 정점개수
lst = [(1,3,1), (1,2,9), (1,6,8), (2,4,13), (2,5,2) ,(2,6,7) ,(3,4,12) ,(4,7,17),(5,6,5),(5,7,20)] #(정점1, 정점2, 가중치)
graph = collections.defaultdict(list)
visit = [0] * (n+1)

for l in lst: # 간선 정보 입력 받기 (중복간선정보가 들어있지 않은 간선정보리스트)
    u, v, weight = l
    graph[u].append([weight, u, v]) # heapify 할때 첫번째 인자를 기준으로 정렬하기 때문에 weight를 맨앞으로 넣어줌.
    graph[v].append([weight, v, u]) # 만약 중복간선정보가 있는 리스트면 이 줄을 빼주면 됨 


def prim(graph, start_node):
    visit[start_node] = 1
    candidate = graph[start_node]
    heapq.heapify(candidate)
    
    mst = []
    total_weight = 0
    
    while candidate:
        w, u, v = heapq.heappop(candidate)
        if visit[v] == 0:
            visit[v] = 1
            mst.append((u,v))
            total_weight += w 
            
            for edge in graph[v]:
                if visit[edge[2]] == 0:
                    heapq.heappush(candidate,edge)
                    
    return total_weight

print(prim(graph,1))


## 최단경로 : 출발점에서 목표점까지 최소비용으로 가는 방법
# 다익스트라 
    # 출발점에서 도착점까지의 최소비용(간선 가중치의 합이 최소가 되는)으로 가는방법 구함
    # 출발점에서 모든 노드들 까지의 최소비용을 모두 구할 수 있음.
    # 간선 가중치가 음수가 없어야함.
    # 1. 노드들 간의 간선 정보 graph로 표현 (단방향)
    
import heapq
import collections

n = 7 # 정점개수
lst = [(1,3,1), (1,2,9), (1,6,8), (2,4,13), (2,5,2) ,(2,6,7) ,(3,4,12) ,(4,7,17),(5,6,5),(5,7,20)] #(정점1, 정점2, 가중치)
graph = collections.defaultdict(list)
visited = [False] * (n+1)
distance = [float("inf")] * (n+1)

for l in lst:
  u, v, w = l                           # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
  graph[u].append((v, w))              # 거리 정보와 도착노드를 같이 입력합니다.

def get_smallest_node():
  min_val = float("inf")
  index = 0
  for i in range(1, n+1): # 0노드는 없으니까 1번노드부터 시작
    if distance[i] < min_val and not visited[i]: 
      min_val = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0 # 시작 노드는 0으로 초기화
  visited[start] = True

  for i in graph[start]:
    distance[i[0]] = i[1] # 시작 노드와 연결된 노도들의 거리 입력
  
  for _ in range(n-1): 
    now = get_smallest_node() # 거리가 구해진 노드 중 가장 짧은 거리인 것을 선택
    visited[now] = True       # 방문 처리

    for j in graph[now]:
      if distance[now] + j[1] < distance[j[0]]: # 기존에 입력된 값보다 더 작은 거리가 나온다면,
        distance[j[0]]= distance[now] + j[1]    # 값을 갱신한다.

dijkstra(1)
print(distance)


# 벨만포드
    # 음수 간선이 포함되어 있어도 가능
    # 음수 사이클이 있으면 동작안함
    # 매번 모든 간선을 확인하기 때문에 다익스트라에 비해서 느림

start = 1 #출발점
n = 7 # 정점개수
lst = [(1,2,8), (1,3,6), (1,5,5), (2,3,-5), (2,4,1) ,(2,6,4) ,(3,4,4) ,(4,7,3),(5,6,5),(6,2,0),(6,7,-7)] #(정점1, 정점2, 가중치)
distance = [float("inf")] * (n+1)

distance[start] = 0

isMinusCycle = False 
for i in range(n+1): # n+1 만큼 반복실행
    for v in lst:
        if distance[v[0]] == float("inf"): continue
        
        if distance[v[1]] > distance[v[0]] + v[2] :
            distance[v[1]] = distance[v[0]] + v[2]
            
            if i==n:
                isMinusCycle = True # n+1번째때 최소비용이 갱신된다면 음수사이클이 존재하는 것임.

print(distance)


# 플로이드워셜 
    # 각각의 정점에서 모든 정점으로의 최단거리(최소비용)를 구함
    # 이차원 리스트의 distance
    # 음수있어도 가능, 음수싸이클이 있으면 불가 
n = 7 # 노드 수
lst = [(1,2,8), (1,3,6), (1,5,5), (2,3,-5), (2,4,1) ,(2,6,4) ,(3,4,4) ,(4,7,3),(5,6,5),(6,2,0),(6,7,-7)] #(정점1, 정점2, 가중치)
dist = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    dist[i][i] = 0   # 자기자신에게 가는 비용은 0
    
for v in lst:
    dist[v[0]][v[1]] = v[2]  # 인접한 노드로 가는 비용 

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  # 중간에 k노드를 거쳐서 가는게 더빠르면 업데이트

print(dist)
    
    
    
                    
## 기타?
## 누적합을 이용한 부분수열 합구하기 : 효율성을 크게 높임.
lst = [0]*N # N은 주어진 리스트의 길이 
lst[0] = givenList[0]
for i in range(1,N): 
    lst[i] = givenList[i] + lst[i-1]

#인덱스 i부터 j까지의 부분수열의 합 
lst[j]-lst[i-1]




            