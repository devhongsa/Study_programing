def solution(heights):
    
    move = [[1,0],[0,1],[-1,0],[0,-1]]

    minEffort = float("inf")

    visit = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]

    def dfs(x,y,res):
        nonlocal minEffort

        if x==len(heights)-1 and y == len(heights[0])-1:

            if max(res)<minEffort:
                minEffort = max(res)
            return

        for m in move:
            nx = x + m[0]
            ny = y + m[1]

            if 0<=nx<len(heights) and 0<=ny<len(heights[0]) and visit[nx][ny] == 0:
                res.append(abs(heights[x][y]-heights[nx][ny]))
                visit[nx][ny] = 1
                dfs(nx,ny,res)
                res.pop()
                visit[nx][ny] = 0
    
    visit[0][0] = 1 
    dfs(0,0,[])

    return minEffort

print(solution([[1,2,2],[3,10,2],[5,3,5]]))