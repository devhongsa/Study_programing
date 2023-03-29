import sys
import heapq

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2,end='')
        
def solution10():
    n = int(sys.stdin.readline())
    L = [int(sys.stdin.readline()) for i in range(n)]
    
    lst = [0]*20
    
    for i in L:
        k = i
        cnt = 0
        while k > 0:
            lst[cnt] += k%2
            k//=2
            cnt+=1
    
    answer = 0
    for i in range(len(lst)):
        answer += lst[i] * (n-lst[i]) * 2**i

    print(answer)
    
def solution2(jobs):
    jobs.sort()
    heap = []
    
    jobsIdx = 0
    doneJob = 0
    end = 0
    workTime = 0
    
    while doneJob != len(jobs):
        while jobsIdx<len(jobs) and jobs[jobsIdx][0]<=end:
            heapq.heappush(heap,(jobs[jobsIdx][1],jobs[jobsIdx][0]))
            jobsIdx += 1
            
        if len(heap) == 0:
            end = jobs[jobsIdx][0]
        
        if len(heap) > 0:
            wt, a = heapq.heappop(heap)
            workTime += wt + end - a
            end += wt
            doneJob += 1
    
    return int(workTime/doneJob)
    
def solution4():
    answer = 0
    c = "+"
    while True:
        n = input()
        if n.isdigit():
            n = int(n)
            if c == "+":
                answer += n 
            elif c == "-":
                answer -= n 
            elif c == "*":
                answer *= n 
            else:
                answer /= n
            answer = int(answer)
        else:
            c = n
        
        if c == "=":
            return answer
# DFS
def solution11():
    for _ in range(n-1):
        n1, n2 = map(int,sys.stdin.readline().split())
        obj[n1].append(n2)
        obj[n2].append(n1)
        
    dfs(1)
    
    for i in range(2,n+1):
        print(parent[i], end='\n')

def dfs2(index):
    isVisit[index] = True
    for n in obj[index]:
        if not isVisit[n]:
            parent[n] = index
            dfs(n)
            
# BOJ 2251 물통, BFS 
def solution():
    a, b, c = map(int,input().split())
    
    visit = [[[False for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
    limit = [a,b,c]
    answer = []
    
    def bfs(x,y,z):
        visit[x][y][z] = True
        que = []
        que.append([x,y,z])
        
        while len(que)!=0:
            st = que.pop(0)
            if st[0] == 0 : answer.append(st[2])
            for f in range(3):
                for t in range(3):
                    if f==t or st[f]==0: continue
                    nxt = move(f,t,st)
                    if not visit[nxt[0]][nxt[1]][nxt[2]] : 
                        visit[nxt[0]][nxt[1]][nxt[2]] = True 
                        que.append(nxt)
            
    def move(f,t,st_):
        st = [x for x in st_]
        if st[f]+st[t]>=limit[t]:
            st[f] = st[f]-(limit[t]-st[t])
            st[t] = limit[t]
        else:
            st[t] += st[f]
            st[f] = 0
        return st
        
    bfs(0,0,c)
    answer.sort()
    for a in answer:
        print(a, end='\n')
        
if __name__ == "__main__":
    # n = int(input())
    # obj = {}
    # for i in range(1,n+1): obj[i]=[]
    # isVisit = [False]*(n+1)
    # parent = [0]*(n+1)
    # solution()
    sys.setrecursionlimit(10**6)
    
    solution()
    