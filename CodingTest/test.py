import sys
import heapq
import math
import copy
from collections import deque

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
    

def solution222():
    lst = [3,1,2,4]
    ch = [0]*5
    res = [0]*4
    answer = 0
    def dfs(l):
        nonlocal answer
        if len(l) == 1 :
            answer =  l[0]
        else:
            lst_ = []
            for i in range(len(l)-1):
                lst_.append(l[i]+l[i+1])
            dfs(lst_)
            
    
    def dfs2(v):
        if v==4:
            dfs(res)
            if answer == 16:
                print(res)
            return
        else:
            for i in range(1,5):
                if ch[i] == 0:
                    res[v] = i 
                    ch[i] = 1
                    dfs2(v+1)
                    ch[i] = 0
    dfs2(0)


def solution13134():
    n = int(input())
    lst = []
    res = 0
    for i in range(n):
        lst.append(list(map(int,input().split())))
    print(lst)
    
    def dfs(v, sum):
        nonlocal res
        if v >= n :
            if sum>res:
                res = sum
            
        else:
            dfs(v+lst[v][0], sum+lst[v][1])
            dfs(v+1, sum)
            
    dfs(0,0)
    print(res)

#동전 바꿔주기(DFS)
def solution9876():
    m = int(input())
    n = int(input())
    lst = []
    
    for i in range(n):
        lst.append(list(map(int,input().split())))
    
    def dfs(v,sum):
        if sum==m:
            print('20 done')
        elif v==n:
            return
        else:
            for i in range(lst[v][1]+1):
                dfs(v+1,sum+lst[v][0]*i)
    
    dfs(0,0)

#동전 분배하기(DFS)
def solution33443():
    n = int(input())
    lst = []
    sumList = [0,0,0]
    for i in range(n):
        lst.append(int(input()))
        
    subMin = float("inf")
    
    def dfs(v):
        nonlocal subMin
        if v == n:
            if len(list(set(sumList))) == 3 and subMin>max(sumList)-min(sumList) :
                subMin = max(sumList)-min(sumList)
        else:
            for i in range(3):
                sumList[i] += lst[v]
                dfs(v+1)
                sumList[i] -= lst[v]
    
    dfs(0)
    print(subMin)

#알파코드(DFS)
def solutionAlpha():
    code = str(input())
    lst = []
    
    def dfs(s):
        if s=="":
            print(lst)
        else:
            if int(s[:2]) <= 26 and len(s)>=2:
                lst.append(int(s[:2]))
                dfs(s[2:])
                lst.pop()
            lst.append(int(s[0]))
            dfs(s[1:])
            lst.pop()
            
    dfs(code)
    

def solution2255():
    s, e = map(int,input().split())
    
    visit = [False for _ in range(e+1)]
    move = [-1,1,5]
    L = 0 
    
    def bfs(v):
        nonlocal L
        que = []
        que.append(v)
        visit[v] = True
        
        while que:
            for i in range(len(que)):
                x = que.pop(0)
                if x == e:
                    print(L)
                    return
                
                for m in move:
                    nx = x + m 
                    if nx<=e and nx>=1 and not visit[nx]:
                        que.append(nx)
                        visit[nx] = True
            L += 1
    
    bfs(s)
    

# 사격연습 BOJ 27958 (제로베이스 미니 코딩 대회)
def solution27958():
    n = int(input())
    b = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int,input().split())))
        
    bullet = list(map(int,input().split()))
    
    #lst = [[0,0,7,0,0],[0,0,5,20,20],[0,6,7,0,0],[0,1,0,0,0],[0,0,2,0,0]]
    #lst = [[0,0,0,0,0],[10,0,4,0,0],[0,0,7,0,0],[0,0,0,0,0],[0,0,2,0,0]]
    #bullet = [2,3,1,1,1]
    #bullet = [1,5,1]
    maxSum = 0
    
    def shot(b, index, startTarget, scoreBoard):
        target = copy.deepcopy(startTarget)
        newScoreBoard = copy.deepcopy(scoreBoard)
        move = [[1,0],[-1,0],[0,1],[0,-1]]
        score = 0
        for i in range(len(target[index])):
            if target[index][i] != 0:
                if target[index][i] >= 10 :
                    score = target[index][i]
                    target[index][i] = 0
                    newScoreBoard[index][i] = 0
                else:
                    if target[index][i]-b <= 0:
                        target[index][i] = 0
                        score = newScoreBoard[index][i]
                        
                        for m in move:
                            nx = index + m[0]
                            ny = i + m[1]
                            if 0<= nx < n and 0<= ny < n and target[nx][ny] == 0:
                                target[nx][ny] = lst[index][i]//4
                                newScoreBoard[nx][ny] = newScoreBoard[index][i]//4
                                newScoreBoard[index][i] = 0

                    else:
                        target[index][i] -= b
                break
        return score, target, newScoreBoard
    
    def dfs(v, startTarget, sum, scoreBoard):
        nonlocal maxSum
        #target = copy.deepcopy(startTarget)
        if v == len(bullet):
            if sum>maxSum:
                maxSum = sum
        else:
            for i in range(len(lst)):
                score, newTarget, newScoreBoard = shot(bullet[v], i, startTarget, scoreBoard)
                dfs(v+1, newTarget, sum+score, newScoreBoard)
                
        
    dfs(0,lst,0,lst)
    print(maxSum)
    
# LIS 최대증가수열
def solutionLIS():
    lst = [2,7,5,8,6,4,7,12,3]
    lst = [5,3,7,8,6,2,9,4]
    d = [0]*len(lst)
    
    d[0] = 1
    d[1] = 1
    
    for i in range(2,len(lst)):
        maxLen = 0
        for j in range(i):
            if lst[j] < lst[i]:
                if maxLen<d[j]+1:
                    maxLen = d[j] + 1
        d[i] = maxLen

    print(max(d))

# LIS 최대증가수열
def solutionLIS2():
    lst = [[25,3,4],[4,4,6],[9,2,3],[16,2,5],[1,5,2]]
    d = [0]*len(lst)
    
    d[0] = 3
    d[1] = 4
    
    for i in range(2,len(lst)):
        maxHigh = 0
        for j in range(i):
            if lst[i][0]<lst[j][0] and lst[i][2] < lst[j][2] and maxHigh < d[j] + lst[i][1]:
                maxHigh = d[j] + lst[i][1]
        d[i] = maxHigh
    
    print(max(d))
    
# 알리바바 40인 
def solutionAli():
    lst = [[3,7,2,1,9],[5,8,3,9,2],[5,3,1,2,3],[5,4,3,2,1],[1,7,5,2,4]]
    
    d = [[0 for _ in range(5)] for _ in range(5)]
    d[0][0] = 3
    
    for i in range(5):
        for j in range(5):
            up = i - 1
            left = j - 1
            if i==0 and j==0:
                d[i][j] = lst[i][j]
                continue
                
            if up>=0 and left>=0 : 
                d[i][j] = min(d[up][j],d[i][left]) + lst[i][j]
            elif up<0 :
                d[i][j] = d[i][left] + lst[i][j]
            else:
                d[i][j] = d[up][j] + lst[i][j]
    
    print(d[4][4])
    

def solution22113():
    d = [0]*12
    lst = [[5,12],[3,8],[6,14],[4,8]]
    
    for v in lst:
        d[v[0]] = v[1]
    
    for i in range(1,12):
        maxW = 0
        for j in range(i//2+i%2,i+1):
            if d[j] + d[i-j] > maxW:
                maxW = d[j] + d[i-j]
        d[i] = maxW
        
    print(d[11])
 
# 냅색알고리즘  선택지 중복선택 O
def solutionNS():
    N = 11 # 무게 제한
    d = [0]*(N+1)
    lst = [[5,12],[3,8],[6,14],[4,8]] # 가치, 무게
    
    for v in lst:
        for i in range(v[1], N+1):
            d[i] = max(d[i],d[i-v[1]] + v[0])
    
    print(d[N])

# 냅색알고리즘 최대점수 구하기, 선택지 중복선택 X
def solution9987():
    N = 20 # 무게 제한
    lst = [[10,5],[25,12],[15,8],[6,3],[7,4]] # [가치,무게]
    
    d = [0]*(N+1)
    
    for q in lst:
        for i in range(N, q[1]-1, -1):
            d[i] = max(d[i], d[i-q[1]]+q[0])
                
    print(d[N])
    
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution12321(S):
    opStack = ArrayStack()
    answer = ''
    for s in S:
        if s == '+' or s == '-' or s == '*' or s == '/':
            if opStack.size()!=0 and prec[opStack.peek()]>=prec[s]:
                answer += opStack.pop()
                opStack.push(s)
            else:
                opStack.push(s)
        elif s == '(':
            opStack.push(s)
        elif s == ')':
            while True:
                p = opStack.pop()
                if p == '(':
                    break
                else:
                    answer += p
        else:
            answer += s
            
    if opStack.size() != 0:
        while opStack.size() != 0:
            answer += opStack.pop()
                
    return answer

# BOJ 11725
def solution11725():
    n = int(input())
    lst = [[] for _ in range(n+1)]
    parent = [0]*(n+1)
    visit = [0]*(n+1)
    for _ in range(n-1):
        p, c = map(int,input().split())
        lst[p].append(c)
        lst[c].append(p)
    
    def dfs(v):
        visit[v] = 1
        for i in lst[v]:
            if visit[i] == 0:
                parent[i] = v
                dfs(i)
            
    dfs(1) 
    for i in range(2,len(parent)):
        print(parent[i])
            
# BOJ 1068 
def solution1068():
    n = int(input())
    if n==1:
        print(0)
        return
    lst = list(map(int,input().split()))
    node = int(input())
    leaf = [x for x in range(n)]
    obj = {}
    
    for i in range(len(lst)):
        if lst[i] == -1:
            continue
        if lst[i] in obj:
            obj[lst[i]].append(i)
        else:
            obj[lst[i]] = [i]
            
    for k in obj.keys():
        leaf.remove(k)

    deleteNode = [node]
    
    for key,value in obj.items():
        if node in value and len(value) == 1:
            leaf.append(key)
        
    def dfs(v):
        if v not in obj:
            return 
        else:
            for c in obj[v]:
                deleteNode.append(c)
                dfs(c)
    
    dfs(node)
    result = list(set(leaf)-set(deleteNode))
    print(len(result))
    
def solutionpp():
    code = "2{l2{e}l}"
    def dfs(num,index):
        string = ""
        while code[index]!="}":
            if code[index].isdigit():
                str_, index2 = dfs(code[index],index+2)
                string += str_
                index = index2
            else:
                string += code[index]
                index += 1
        return string*int(num), index+1
    answer = ""
    check = 0
    for i in range(len(code)):
        if code[i].isdigit() and i>=check:
            mid, index_ = dfs(code[i],i+2)
            answer += mid
            check = index_
        elif i>=check:
            answer += code[i]
    return answer

def solution(delay, capacity, times):
    answer = 0
    time = 0
    que = 0
    
    for t in times:
        if time == delay:
            que -= 1
            time = 0
        if t==0:
            que += 1
            if que-capacity >0:
                answer += que-capacity
                que = capacity
        else:
            time += t
            que += 1
            if que-capacity >0:
                answer += que-capacity
                que = capacity
        

    return answer

# boj1260 :DFS BFS
def solution1260():
    n, m, vv =  map(int,input().split())
    lst = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int,input().split())
        lst[a].append(b)
        lst[b].append(a)
    
    for l in lst:
        l.sort()
        
    visitD = [False]*(n+1)
    visitB = [False]*(n+1)
    dfsList = []
    bfsList = []
    
    def dfs(v):
        visitD[v] = True
        dfsList.append(v)
        for i in lst[v]:
            if not visitD[i]:
                dfs(i)
    
    def bfs(v):
        que = deque([])
        que.append(v)
        visitB[v] = True
        
        while que:
            x = que.popleft()
            bfsList.append(x)
            for i in lst[x]:
                if visitB[i]:
                    continue 
                que.append(i)
                visitB[i] = True
    
    dfs(vv)
    bfs(vv)
    
    print(" ".join([str(x) for x in dfsList]))
    print(" ".join([str(x) for x in bfsList]))


def solution2667():
    n = int(input())
    mapList = []
    for _ in range(n):
        lst = [int(x) for x in list(input())]
        mapList.append(lst)
    
    visit = [[False for _ in range(n)] for _ in range(n)]
    danji = 0
    numList = []
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    
    def bfs(x,y):
        que = deque([])
        que.append(x)
        que.append(y)
        visit[x][y] = True
        total = 0
        
        while que:
            a = que.popleft()
            b = que.popleft()
            total += 1
            for m in move:
                nx = m[0] + a
                ny = m[1] + b
                if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and mapList[nx][ny]==1:
                    que.append(nx)
                    que.append(ny)
                    visit[nx][ny] = True
 
        return total
    
    for i in range(n):
        for j in range(n):
            if mapList[i][j]!=0 and not visit[i][j]:
                numList.append(bfs(i,j))
                danji += 1
    
    
    print(danji)
    numList.sort()
    for n in numList:
        print(n)
        

def solution3055():
    r, c = map(int,input().split())
    map1 = []
    dist = [[0 for _ in range(c)] for _ in range(r)]
    visit = [[0 for _ in range(c)] for _ in range(r)]
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    D = []
    S = []
    
    for _ in range(r):
        map1.append(list(input()))
    for i in range(r):
        for j in range(c):
            if map1[i][j] == "S":
                S = [i,j]
            elif map1[i][j] == "D":
                D = [i,j]
                
    
    def spread(lst):
        water = []
        
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                if lst[i][j] == "*":
                    water.append([i,j])
        
        for w in water:
            for m in move:
                ni = w[0]+m[0]
                nj = w[1]+m[1]
                if 0<=ni<r and 0<=nj<c and lst[ni][nj]==".":
                    lst[ni][nj] = "*"
        return lst 
    
    def bfs():
        nonlocal map1
        visit[S[0]][S[1]] = 1
        que = []
        que.append(S)
        
        while que:
            map1 = spread(map1)
            for _ in range(len(que)):
                l = que.pop(0)
                x = l[0] 
                y = l[1]
    
                if [x,y] == D:
                    return 
                for m in move:
                    nx = x + m[0]
                    ny = y + m[1]
                    if 0<=nx<r and 0<=ny<c and visit[nx][ny] == 0 and (map1[nx][ny] == "." or map1[nx][ny] == "D"):
                        que.append([nx,ny])
                        visit[nx][ny] = 1
                        dist[nx][ny] = dist[x][y] + 1
    bfs()
    if dist[D[0]][D[1]] == 0:
        print("KAKTUS")
    else: print(dist[D[0]][D[1]])
    

def solution11057():
    n = int(input())
    lst = [[1 for _ in range(10)] for _ in range(n+1)]
    
    for i in range(2,n+1):
        for j in range(1,10):
            lst[i][j] = (lst[i][j-1] + lst[i-1][j])%10007
            
    print(sum(lst[n])%10007)


def solution1949():
    n = int(input())
    people = list(map(int,input().split()))
    people.insert(0,0)
    lst = [[] for _ in range(n+1)]
    dy = [[0 for _ in range(n+1)] for _ in range(2)]

    for _ in range(n-1):
        a, b = map(int,input().split())
        lst[a].append(b)
        lst[b].append(a)
        
    def dfs(x, prev):
        dy[0][x] = 0
        dy[1][x] = people[x]
        
        for y in lst[x]:
            if y == prev:
                continue
            dfs(y,x)
            dy[0][x] += max(dy[0][y],dy[1][y])
            dy[1][x] += dy[0][y]
    
    dfs(1,-1)
    print(max(dy[0][1],dy[1][1]))
    

def solution14502():
    N, M = map(int,input().split())
    maplst = []
    for _ in range(N):
        lst = list(map(int,input().split()))
        maplst.append(lst)
    
    virus = []
    safe = []
    wall = [0]*3
    
    answer = 0
    
    for i in range(N):
        for j in range(M):
            if maplst[i][j] == 2:
                virus.append([i,j])
            elif maplst[i][j] == 0:
                safe.append([i,j])
    
    def bfs(before):
        move = [[1,0],[-1,0],[0,1],[0,-1]]
        after = [lst[:] for lst in before]
        que = []
        for v in virus:
            que.append(v)
        
        while que:
            v = que.pop(0)
            x = v[0]
            y = v[1]
            
            for m in move:
                nx = x + m[0]
                ny = y + m[1]
                
                if 0<=nx<N and 0<=ny<M and after[nx][ny] == 0:
                    after[nx][ny] = 2
                    que.append([nx,ny])
                    
        return after

    def dfs(v,index):
        nonlocal answer
        nonlocal wall
        if v == 3:
            newMap = [lst[:] for lst in maplst]
            
            for w in wall:
                newMap[w[0]][w[1]] = 1
                
            resMap = bfs(newMap)
            total = 0
            
            for s in resMap:
                total += s.count(0)
                
            if total>answer:
                answer = total
            return
        
        else:
            for i in range(index,len(safe)):
                wall[v] = safe[i]
                dfs(v+1,i+1)
    
    dfs(0,0)
    print(answer)
    
def solution1991():
    N = int(input())
    obj = {}
    for i in range(N):
        n,l,r = input().split()
        
        obj[n] = [l,r]
        
    def dfs(v, node, type):
        if v == N:
            return 
        else:
            if type==1:
                print(node, end="")
                if obj[node][0] != ".":
                    dfs(v+1, obj[node][0],type)
                if obj[node][1] != ".":
                    dfs(v+1, obj[node][1],type)
            elif type ==2:
                if obj[node][0] != ".":
                    dfs(v+1, obj[node][0],type)
                print(node, end="")
                if obj[node][1] != ".":
                    dfs(v+1, obj[node][1],type)
            else:
                if obj[node][0] != ".":
                    dfs(v+1, obj[node][0],type)
                if obj[node][1] != ".":
                    dfs(v+1, obj[node][1],type)
                print(node, end="")
        
    dfs(0,'A',1)
    print("")
    dfs(0,'A',2)
    print("")
    dfs(0,'A',3)
    

def solution1012():
    N1 = int(input())
    
    def bfs(a,b):
        nonlocal map1
        nonlocal visit
        
        move = [[1,0],[-1,0],[0,1],[0,-1]]
        que = [a,b]
        visit[a][b] = 1
        
        while que:
            a = que.pop(0)
            b = que.pop(0)
            
            for m in move:
                na = a + m[0]
                nb = b + m[1]
                
                if 0<=na<n1 and 0<=nb<m1 and visit[na][nb] == 0 and map1[na][nb] == 1:
                    que.append(na)
                    que.append(nb)
                    visit[na][nb] = 1
                    
    for _ in range(N1):
        n1, m1, g1 = map(int,input().split())
        map1 = [[0 for _ in range(m1)] for _ in range(n1)]
        visit = [[0 for _ in range(m1)] for _ in range(n1)]
        answer = 0
        for _ in range(g1):
            x, y = map(int,input().split())
            map1[x][y] = 1
            
        for i in range(n1):
            for j in range(m1):
                if map1[i][j] == 1 and visit[i][j] == 0:
                    bfs(i,j)
                    answer += 1
                    
        print(answer)
                    

def solution7795():
    tc = int(input())
    for _ in range(tc):
        an, bn = map(int,input().split())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        
        B.sort()
        
        ans = 0
        
        for num in A:
            left = 0
            right = len(B)-1
            
            result = left - 1
            while left<=right:
                middle = (left+right)//2
                
                if B[middle]>=num:
                    right = middle-1
                else:
                    left = middle+1
                    result = middle

            ans += result+1

        print(ans)
        

def solution2470():
    N = int(input())
    lst = list(map(int,sys.stdin.readline().split()))
    
    lst.sort()
    
    absv = float("inf")
    result = []
    
    for i in range(N):
        a = lst[i]
        left = 0
        right = N-1
        
        while left<=right:
            mid = (left+right)//2
            if mid==i: break

            res = a + lst[mid]
            absv_ = abs(res)
            
            if absv_<absv:
                absv = absv_ 
                result = [a,lst[mid]]
            
            if res<0 :
                left = mid+1
            elif res>0:
                right = mid-1
            else:
                print(a,lst[mid])
                return
    
    result.sort()
    print(result[0], end=' ')
    print(result[1])
        

def solution2805():
    N, M = map(int,input().split())
    lst = list(map(int, sys.stdin.readline().split()))
    
    maxLen = max(lst)
    
    left = 0
    right = maxLen
    
    result = -1
    
    while left<=right:
        mid = (left+right)//2
        
        total = 0
        for wood in lst:
            if wood>mid:
                total += wood-mid
        
        if total>=M:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
            
    print(result)
                

def solution2110():
    N, C = map(int,input().split())
    lst = []
    
    for i in range(N):
        lst.append(int(sys.stdin.readline()))
    lst.sort()
    
    left = 1
    right = lst[-1]-lst[0]
    
    result = 0
    
    while left <= right:
        mid = (left+right)//2
        c = 1
        
        a = lst[0]
        
        for i in range(1,len(lst)):
            if lst[i] - a < mid:
                continue
            else:
                c += 1
                a = lst[i]
                
                if c >= C :
                    left = mid + 1
                    result = mid
                    break
        
        if c < C:
            right = mid - 1
    
    print(result)


def solution15651():
    
    N, M = map(int,input().split())
    
    result = [0]*M
    def dfs(v):
        nonlocal result
        if v == M:
            for n in result:
                print(n, end=" ")
            print("")
            return
        else:
            for i in range(1,N+1):
                result[v] = i
                dfs(v+1)
    
    dfs(0)
    
def solution15649():
    
    N, M = map(int,input().split())
    
    result = [0]*M
    ch = [0]*(N+1)
    
    def dfs(v):
        nonlocal result
        if v == M:
            for n in result:
                print(n, end=" ")
            print("")
            return
        else:
            for i in range(1,N+1):
                if ch[i] == 0:
                    result[v] = i
                    ch[i] = 1
                    dfs(v+1)
                    ch[i] = 0
    
    dfs(0)
    

def solution15652():
    N, M = map(int,input().split())
    
    res = [0] * M
    def dfs(v,index):
        if v == M:
            for n in res:
                print(n, end=" ")
            print("")
            return
        else:
            for i in range(index,N+1):
                res[v] = i 
                dfs(v+1,i)
    dfs(0,1)


def solution15650():
    N, M = map(int,input().split())
    
    res = [0] * M
    def dfs(v,index):
        if v == M:
            for n in res:
                print(n, end=" ")
            print("")
            return
        else:
            for i in range(index,N+1):
                res[v] = i 
                dfs(v+1,i+1)
    dfs(0,1)


def solution14888():
    N = int(input())
    numList = list(map(int,sys.stdin.readline().split()))
    add, sub, mul, div = map(int,input().split())
    minNum = 1000000001
    maxNum = -1000000001
    
    def dfs(v, result):
        nonlocal minNum, maxNum, add, sub, mul, div
        if v == N-1:
            minNum = min(result,minNum)
            maxNum = max(result,maxNum)
            return 
        else:
            if add>0:
                add -= 1
                dfs(v+1, result + numList[v+1])
                add += 1
            if sub>0:
                sub -= 1
                dfs(v+1, result - numList[v+1])
                sub += 1
            if mul>0:
                mul -= 1
                dfs(v+1, result * numList[v+1])
                mul += 1
            if div>0 :
                div -= 1
                dfs(v+1, int(result/numList[v+1]))
                div += 1
    dfs(0,numList[0])      
    print(maxNum)
    print(minNum)
    

def solution9663():
    N = int(input())
    cnt = 0
    rowList = [0]*N
    
    def check(x):
        for i in range(x):
            if rowList[x] == rowList[i] or abs(rowList[x] - rowList[i]) == abs(x - i):
                return False
        return True 
        
    def dfs(row):
        nonlocal cnt
        if row == N:
            cnt += 1
        else:
            for i in range(N):
                rowList[row] = i
                if check(row):
                    dfs(row+1)
                    
    dfs(0)
    print(cnt)
    

def solution1182():
    N, S = map(int,sys.stdin.readline().split())
    lst = list(map(int,sys.stdin.readline().split()))
    
    cnt = 0
    ch = [0]*N
    
    def dfs(v,sum):
        nonlocal cnt
        if v==N:
            if 1 not in ch:
                return
            if sum==S:
                cnt += 1
        else:
            ch[v] = 1
            dfs(v+1,sum+lst[v])
            ch[v] = 0
            dfs(v+1,sum)
    dfs(0,0)
    print(cnt)


def solution10825():
    N = int(input())
    lst = []
    for i in range(N):
        lst_ = list(sys.stdin.readline().split())
        for i in range(1,4):
            lst_[i] = int(lst_[i])
        lst.append(lst_)
        
    lst.sort(key=lambda x : (x[1],-x[2],x[3],x[0]), reverse=True)
    
    for name in lst:
        print(name[0])


def solution1015():
    N = int(input())
    lst = list(map(int,sys.stdin.readline().split()))
    lst2 = []
    for i in range(N):
        lst2.append([lst[i],i])
    lst2.sort(key=lambda x:(x[0],x[1]))
    
    for i in range(N):
        lst2[i].append(i)

    lst2.sort(key=lambda x : x[1])
    
    for n in lst2:
        print(n[2], end=" ")


def solution11652():
    N = int(input())
    obj = {}
    for _ in range(N):
        n = int(sys.stdin.readline())
        if n in obj:
            obj[n] += 1
        else:
            obj[n] = 1
    result = 0
    ans = float("inf")
    for k,v in obj.items():
        if v>result:
            result = v
            ans = k 
        elif v==result:
            if k<ans:
                ans = k
        
    print(ans)
    

def solution15970():
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int,sys.stdin.readline().split())))
    lst.sort(key=lambda x : (x[1],x[0]))
    
    total = 0
    total += (lst[1][0]-lst[0][0]) + (lst[-1][0]-lst[-2][0])
    
    for i in range(1,N-1):
        if lst[i+1][1] == lst[i][1] and lst[i-1][1] == lst[i][1]:
            total += min(lst[i][0]-lst[i-1][0],lst[i+1][0]-lst[i][0])
        elif lst[i-1][1] != lst[i][1]:
            total += lst[i+1][0]-lst[i][0]
        else:
            total += lst[i][0]-lst[i-1][0]
    
    print(total)
    
def solution(ingredients, items):
    obj = {}
    for ing in ingredients:
        obj[ing] = []
    for i,v in enumerate(items):
        if v in obj:
            obj[v].append(i)

    print(obj)
    
    keys = list(obj.keys())
    minimum = len(items) + 1
    res = [0]*len(keys)
    def dfs(v):
        nonlocal minimum
        if v == len(obj):
            ma = max(res)
            mi = min(res)
            if ma-mi+1 < minimum:
                minimum = ma-mi+1
                print(res)
            return
        else:
            for i in range(len(obj[keys[v]])):
                res[v] = obj[keys[v]][i]
                dfs(v+1)
    dfs(0) 
    print(minimum)   
    return minimum


def solution11726():
    n = int(input())
    
    if n == 1:
        print(1)
        return
    
    d = [0] * (n+1)
    d[1] = 1 
    d[2] = 2
    
    for i in range(3,n+1):
        d[i] = (d[i-2] + d[i-1])%10007
    
    print(d[n])
    
def solution2579():
    n = int(input())
    c = [0]
    for i in range(n):
        c.append(int(sys.stdin.readline()))
    if n == 1:
        print(c[1])
        return
    
    d = [[0]*(n+1),[0]*(n+1)]
    
    d[0][1] = c[1]
    d[0][2] = c[1] + c[2]
    d[1][2] = c[2]
    
    for i in range(3,n+1):
        d[0][i] = d[1][i-1] + c[i]
        d[1][i] = max(d[0][i-2],d[1][i-2]) + c[i]
        
    print(max(d[0][n],d[1][n]))
    

def divideSubArray(lst, left, right):
    if (left == right) : return lst[left]
    
    mid = (left+right)//2
    maxLeft = divideSubArray(lst,left,mid)
    maxRight = divideSubArray(lst,mid+1,right)
    
    maxarr = getMaxSubArray(lst, left, mid, right)
    
    print(left, right)
    print(maxLeft, maxRight, maxarr)
    return max(maxLeft, max(maxRight,maxarr))

def getMaxSubArray(lst, left, mid, right):
    sumLeft = 0
    maxLeft = float("-inf")
    
    for i in range(mid,left-1,-1):
        sumLeft += lst[i]
        maxLeft = max(maxLeft, sumLeft)
        
    sumRight = 0
    maxRight = float("-inf")
    
    for i in range(mid+1,right+1):
        sumRight += lst[i]
        maxRight = max(maxRight, sumRight)
        
    return maxLeft + maxRight

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    
    print(divideSubArray([-5,0,4,-3,-1,3,1,-5,8], 0, 8))
    #print(divideSubArray([5,4,0,7,8], 0, 4))

    
