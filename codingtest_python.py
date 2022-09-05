# 리스트 list
list1 = [1, 2, 3]
[*list1]  ##리스트 언팩킹 
letters = ["A", "B", "C"]
lst1 = ['A', 'B', 'C', 'D']
lst2 = ['C', 'D', 'E', 'F']

set(list1)
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

list1 = set(list1)  # 중복값 제거

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
string1.split()
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
