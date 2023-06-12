n = 7 # 노드 수
lst = [(1,2,8), (1,3,6), (1,5,5), (2,3,-5), (2,4,1) ,(2,6,4) ,(3,4,4) ,(4,7,3),(5,6,5),(6,2,0),(6,7,-7)] #(정점1, 정점2, 가중치)
dist = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    dist[i][i] = 0   # 자기자신에게 가는 비용은 0
    
for v in lst:
    dist[v[0]][v[1]] = v[2]  # 인접한 노드로 가는 비용 
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  # 중간에 k노드를 거쳐서 가는게 더빠르면 업데이트

print(dist)