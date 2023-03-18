import math
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
    lst = [0,2,3]
    print(lst.count(1))