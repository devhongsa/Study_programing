import sys
import heapq
import math

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
def solution2251():
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
        
# BOJ 2178 미로 탐색 BFS
def solution2178():
    n, m = map(int,input().split())
    lst = []
    visit = [[False for _ in range(m)] for _ in range(n)]
    dist = [[1 for _ in range(m)] for _ in range(n)]
    direct = [[0,1],[1,0],[0,-1],[-1,0]]
    
    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        lst.append(list(s))
    
    print(lst)
    
    def bfs(x,y):
        que = []
        que.append(x)
        que.append(y)
        visit[x][y] = True
        
        while len(que)!=0:
            x = que.pop(0)
            y = que.pop(0)
            for k in range(4):   
                nx = x + direct[k][0]
                ny = y + direct[k][1]
                print(nx,ny)
                if nx < 0 or ny < 0 or nx>=n or ny>=m : 
                    print('continue')
                    continue
                if lst[nx][ny] == '0' : continue
                if visit[nx][ny] : continue
                visit[nx][ny] = True 
                que.append(nx)
                que.append(ny)
                dist[nx][ny] = dist[x][y] + 1
    
    bfs(0,0)
    print(dist[n-1][m-1])


# BOJ 1697 숨바꼭질 BFS
def solution1697():
    n, k = map(int,input().split())
    visit = [False for _ in range(100003)]
    dist = [0 for _ in range(100003)]
    
    def bfs(n):
        que = []
        que.append(n)
        
        while len(que) != 0:
            x = que.pop(0)
            
            if x == k: 
                print(dist[x])
                break
            
            for nx in (x-1, x+1, x*2):
                if 0<= nx <= 100000 and not dist[nx]:
                    dist[nx] = dist[x] + 1
                    que.append(nx)
    bfs(n)

# BOJ 3055 탈출 BFS
def solution3055():
    r, c  = map(int, input().split())
    m = []
    dist = [[-1 for _ in range(c)] for _ in range(r)]
    locS = [0,0]
    locD = [0,0]
    direct = [[0,1],[1,0],[-1,0],[0,-1]]
    wDist = [[-1 for _ in range(c)] for _ in range(r)]
    wVisit = [[False for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        s = sys.stdin.readline().rstrip()
        lst = list(s)
        if 'S' in lst:
            index = lst.index('S')
            locS[0] = i 
            locS[1] = index
        if 'D' in lst:
            index = lst.index('D')
            locD[0] = i 
            locD[1] = index
            
        m.append(lst)
        
    wDist[locD[0]][locD[1]] = 999999
        
    def wBfs():
        wQue = []
        for i in range(r):
            for j in range(c):
                if m[i][j] == '*':
                    wQue.append(i)
                    wQue.append(j)
                    wDist[i][j] = 0
                    wVisit[i][j] = True
                    
        while len(wQue) != 0:
            i = wQue.pop(0)
            j = wQue.pop(0)
            for k in range(4):
                ni = i + direct[k][0]
                nj = j + direct[k][1]
                if 0<= ni < r and 0<= nj < c and (m[ni][nj] == '.' or m[ni][nj]=='S') and not wVisit[ni][nj]:
                    wDist[ni][nj] = wDist[i][j] + 1
                    wVisit[ni][nj] = True
                    wQue.append(ni)
                    wQue.append(nj)            

    def bfs(x, y):
        que = []
        que.append(x)
        que.append(y)
        visit = [[False for _ in range(c)] for _ in range(r)]
        visit[x][y] = True
        dist[x][y]=0
        
        while len(que) != 0:
            x = que.pop(0)
            y = que.pop(0)
            
            if x == locD[0] and y == locD[1]:
                print(dist[x][y])
                return
            
            for k in range(4):
                nx = x + direct[k][0]
                ny = y + direct[k][1]
                if nx< 0 or nx>=r or ny <0 or ny>=c : continue 
                if m[nx][ny]!= 'X' and m[nx][ny] != '*' and (dist[x][y]+1)<wDist[nx][ny] and not visit[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    visit[nx][ny] = True
                    que.append(nx)
                    que.append(ny)
            
        print("KAKTUS")
    wBfs()
    print(wDist)
    bfs(locS[0],locS[1])
    
def solution333(S):
    stack = []
    lst = []

    while S != "":
        for i in range(len(S)):
            if S[i] == "+" or S[i]=="-" or S[i]=="/" or S[i]=="*":
                num = S[:i]
                lst.append(float(num))
                lst.append(S[i])
                S = S[i+1:]
                break
        if S.find("+") == -1 and S.find("-") == -1 and S.find("/") == -1 and S.find("*") == -1:
            lst.append(float(S))
            S = ""

    while lst:
        v = lst.pop(0)
        print(stack, "시작")
        if type(v) is float:
            stack.append(v)
        elif v=="+" or v=="-":
            stack.append(v)
        elif v=="*":
            num = float(stack.pop())*float(lst.pop(0))
            stack.append(num)
        else:
            num = float(stack.pop())/float(lst.pop(0))
            stack.append(num)
    
    answer = 0
    if len(stack) == 1:
        return int(100*stack[0])/100
    else:
        while stack:
            n = stack.pop(0)
            if n == "+":
                answer += stack.pop(0)
            elif n == "-":
                answer -= stack.pop(0)
            else:
                answer += n
        return int(answer*100)/100


def solution1313():
    lst = ["+","-","*","/"]
    answer = []
    choice = [""]*6
    cnt = 0
    
    def dfs(k):
        nonlocal cnt
        if k==6:
            #answer.append(choice)
            cnt += 1
            return
        
        for i in range(len(lst)):
            choice[k] = lst[i]
            dfs(k+1)
    dfs(0)
    print(cnt)
    
def solution2004():
    n, m = map(int,input().split())
    lst = list(map(int,sys.stdin.readline().split()))
    answer = 0
    for i in range(len(lst)):
        sum = lst[i]
        if sum == m:
            continue
        elif sum > m :
            continue
        for j in range(1+i,len(lst)):
            sum += lst[j]
            if sum==m:
                answer += 1
                break
            elif sum>m :
                break
    print(answer)


def solution1890():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int,sys.stdin.readline().split())))
        
    obj = {"33":1}
    
    def bfs(x,y,cnt):
        que = []
        que.append(x)
        que.append(y)
        
        while que:
            a = que.pop(0)
            b = que.pop(0)
            if str(a)+str(b) in obj:
                cnt += obj[str(a)+str(b)]
                continue
            j = lst[a][b]
            if j == 0:
                if a == n-1 and b == n-1:
                    cnt += 1
                continue
            nx = a + j 
            ny = b + j
            
            if nx<n:
                que.append(nx)
                que.append(b)
            if ny<n:
                que.append(a)
                que.append(ny)
        obj[str(x)+str(y)] = cnt
                
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            bfs(i,j,0)
    print(obj["00"])
    
def solution11047():
    n, k = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append(int(input()))
    
    cnt = 0
    lst.sort(reverse=True)
    for coin in lst:
        if k//coin > 0 :
            cnt += k//coin
            k %= coin
    print(cnt)
        

def solution1254():
    a = input()
    
    if a == a[::-1]: 
        print(len(a))
        return
    
    for i in range(1, len(a)):
        if a[i:] == a[i:][::-1]:
            print(len(a[:i])+len(a))
            return


def solution12345():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(int(input()))
    dList = [[0 for _ in range(n)] for _ in range(2)]
    
    if n == 1:
        print(lst[0])
        return
    dList[0][0] = lst[0]
    dList[1][0] = lst[0]
    dList[0][1] = lst[0] + lst[1]
    dList[1][1] = lst[1]
    
    for i in range(2,n):
        dList[0][i] = dList[1][i-1] + lst[i]
        dList[1][i] = max(dList[0][i-2],dList[1][i-2]) + lst[i]
    
    print(max(dList[0][n-1],dList[1][n-1]))
    

def solution():

    def dfs(n):
        if n // 2 == 0:
            print(n%2, end='')
            return 
        dfs(n//2)
        print(n%2, end='')
    
    dfs(11)
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    solution()
    
