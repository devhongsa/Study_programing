from collections import deque

lst = deque([1,2,3])

lst.append("a")
lst.append("b")
lst.append("c")

lst.remove("b")

print(lst)