def DFS(v):
    global cnt
    if v == m :
        print(res)
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            if checkList[i]==0:
                res[v] = i
                checkList[i]=1
                DFS(v+1)
                checkList[i]=0
                print("checkList reset")

if __name__ == "__main__":
    n = 4
    m = 3
    cnt = 0
    checkList = [0]*(n+1)
    res = [0]*m
    
    DFS(0)
    print(cnt)