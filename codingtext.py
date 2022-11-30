def solution(n,s,e,k):
    lst = []
    lst2 = lst[s-1:e]
    lst2.sort()
    result = lst2[k-1]