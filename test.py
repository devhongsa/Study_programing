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