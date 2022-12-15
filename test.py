n = 5

lst = [[10,13,10,12,15],[12,39,30,23,11],[11,25,50,53,15],[19,27,29,37,27],[19,13,30,13,19]]

result = []

print(result)

column = [0 for _ in range(n)]
x = 0
x2 = 0

for i in range(n):
    result.append(sum(lst[i]))
    for j in range(n):
        column[j] += lst[i][j]
        
    x += lst[i][i]
    x2 += lst[i][-1-i]
    
result.append(x)
result.append(x2)
result += column

print(result)
    