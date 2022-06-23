### list 
list1 = [1,2,3]
letters = ["A", "B", "C"]
lst1 = ['A', 'B', 'C', 'D']
lst2 = ['C', 'D', 'E', 'F']

set(list1)
list1.index(1) 
{x : 0 for x in list1}
list1.count(1)  ##요소값이 1인 갯수 세기 
list1.remove(1)  ##요소값이 1인 요소 삭제하기, 단 1이 여러개면  첫번째 요소만 삭제함. list1 = list1.remove(1) 이렇게 안해줘도 바뀜.

union = (set(lst1) | set(lst2))   ## 합집합, 두리스트 합집합 
inter = (set(lst1) & set(lst2))   ## 교집합, 두리스트에서 교집합 요소추출 
complement = (set(lst1) - set(lst2))  ## 차집합, lst1 기준 lst2와 다른 요소만 추출 


for pair in zip(list1, letters):
    print(pair)
## (1,'A'), (2,'B') ... 

for i, val in enumerate(list1):
    print(i, val)
## (0, 1), (1, 2) ...



## string 문자열 
string1 = "hi hello"
string1.split()
string1.isalpha() 
string1.isdigit()
string1.replace('hi', 'hello')
''.join(i for i in letters)  ##리스트 요소 사이사이에 '' 요게 들어감.
string1.strip('h')    ## rstrip, lstrip  양쪽 or 오른쪾 or 왼쪽에 h문자열이 있으면 h문자열이 안나올때까지 h를 없앰.
string1.upper()
string1.isupper()
string1.lower()
string1.islower()


