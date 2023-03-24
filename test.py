import sys
import heapq

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2,end='')
        
def solution():
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
    
if __name__ == "__main__":
    print(solution2([[0,3],[1,9],[2,6]]))
    