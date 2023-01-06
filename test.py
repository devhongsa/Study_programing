lst = [802,743,457,539]

first = 1
last = 802

n = 11

result = 0

while first<=last:
    mid = (first+last)//2
    res = sum([num//mid for num in lst])
    
    if res<n:
        last = mid-1
    else:
        first = mid + 1
        result = mid
        
print(result)