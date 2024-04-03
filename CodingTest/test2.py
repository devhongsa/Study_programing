import copy

lst = [
    [2,1,0,0,0,0,1,0],
    [1,2,0,0,0,0,1,0],
    [0,1,0,0,2,0,0,1],
    [0,0,2,1,0,1,0,0],
    [0,0,1,0,0,0,2,1],
    [0,1,0,0,0,0,2,1],
    [0,1,0,0,1,0,2,0],
    [1,0,0,0,0,0,2,1],
    [1,0,1,0,0,0,2,0],
    [0,1,1,0,0,0,2,0],
    [0,0,0,1,1,0,2,0],
    [2,0,1,0,0,0,0,1],
    [2,0,0,0,1,0,1,0],
    [2,0,0,0,0,1,0,1],
    [1,1,0,2,0,0,0,0],
    [0,1,0,2,1,0,0,0],
    [0,0,0,2,0,0,1,1],
    [0,0,0,2,0,1,0,1],
    [0,0,2,1,1,0,0,0],
    [0,0,2,0,0,0,1,1],
    [0,0,2,0,0,1,0,1],
    [0,1,2,0,1,0,0,0],
    [0,1,2,1,0,0,0,0],
    [0,0,2,0,0,1,1,0],
    [1,0,2,0,0,1,0,0],
    [0,2,0,0,1,0,1,0],
    [0,2,1,0,0,0,1,0],
    [0,2,0,1,0,0,1,0],
    [0,0,1,0,2,0,1,0],
    [0,0,0,1,1,0,0,2],
    [0,0,1,0,0,0,1,2],
    [1,0,0,0,0,1,0,2],
    [1,0,1,0,0,0,0,2],
    [1,0,0,1,0,0,0,2],
    [0,0,0,1,0,1,0,2],
    [0,0,1,0,1,0,0,2],
    [0,0,0,0,0,1,1,2],
    [0,0,0,0,0,2,1,1],
    [0,0,0,1,0,2,1,0],
    [0,0,0,0,1,2,1,0],
    [0,0,0,1,0,2,0,1],
    [0,1,0,0,0,2,1,0],
    [1,0,1,0,0,2,0,0],
    [2,0,1,0,0,0,1,0],
    [0,0,0,2,1,1,0,0],
    [0,1,2,0,0,0,0,1],
    [0,0,2,0,1,0,0,1],
    [1,0,0,0,1,0,0,2],
    [0,0,1,1,0,0,2,0],
    [1,0,0,0,0,1,2,0],
    [2,0,0,0,1,1,0,0],
    [2,0,0,1,0,0,1,0],
    [2,0,0,0,1,0,0,1],
    [2,0,0,0,0,0,1,1],
    [0,1,0,2,0,0,1,0],
    [0,1,0,2,0,1,0,0],
    [0,0,2,0,1,0,1,0],
    [1,2,0,0,0,0,0,1],
    [0,1,1,0,2,0,0,0],
    [0,1,0,0,2,1,0,0],
    [0,0,0,1,2,0,1,0],
    [0,1,0,0,0,0,1,2],
    [0,1,0,0,0,1,0,2],
    [0,0,1,0,0,1,0,2],
    [0,1,0,0,1,0,0,2],
    [0,0,1,1,0,2,0,0],
    [0,0,1,0,0,2,0,1],
    [0,0,1,0,1,2,0,0]
]
# lst  = list(set(map(tuple, lst)))
# print(lst)
res = [0,0,0,0,0,0]
coreCheck = [0,0,0,0,0,0,0,0]
totalRes = [0,0,0,0,0,0,0,0]
cnt = 0
result = [0,0,0]

need = []
needCore = []

def DFS(v,index):
    global cnt
    if v == 5 :
        if ((totalRes[0] == 2 or totalRes[0] == 3) and (totalRes[1] == 2 or totalRes[1] == 3)):
            for i in range(2,8):
                if totalRes[i] != 1 and totalRes[i] != 2:
                    return
                
            nlst = [0,0,0,0,0,0,0,0]
            for i in range(8): 
                if i == 0 or i == 1:
                    nlst[i] = 3-totalRes[i]
                else :
                    nlst[i] = 2-totalRes[i]
                if nlst[i] == 1 and coreCheck[i] == 0:
                    nlst[i] = 2
            
            res2 = copy.deepcopy(res)
            
            if nlst[0] == 2 :
                cnt += 1
                print(cnt)
                
                need.append(nlst)
                needCore.append(res2)
                print("result",res)
                print("tr",totalRes)
                
                for i in res:
                    print(lst[i])
                
                

            
            
            # print("cc",coreCheck)
            # print("tr",totalRes)
            
                
    else:
        for i in range(index,len(lst)):
            l = lst[i]
            core = 0
            idx = [0,0,0,0,0,0,0,0]
            # print("list",l)
            # print("cc",cc)
            # print("tr",tr)
            
            for j in range(8) :
                if l[j] == 2:
                    if coreCheck[j] == 1:
                        return
            for j in range(8):
                if l[j] == 2:
                    coreCheck[j] = 1
                    totalRes[j] += 1
                    idx[j] += 1
                    core = j
                elif l[j] == 1:
                    totalRes[j] += 1
                    idx[j] += 1
                    
            # for n in range(2,8):
            #     if totalRes[n] > 2 :
            #         return
            
            # bcc = copy.deepcopy(cc)
            # btr = copy.deepcopy(tr)
            
            # print("totalRes",totalRes)
            res[v] = i
            DFS(v+1,i+1)
            coreCheck[core] = 0
            for q in range(8):
                totalRes[q] = totalRes[q]-idx[q]
            
DFS(0,0)

answer = sum(needCore, []) # 남겨둬야하는 코어
answer= list(set(answer))
# print(len(lst))
# print(answer)

last = []  # 남겨둬야하는 코어 

for i in answer :
    last.append(lst[i])
    
last.sort()

#print(need) # 필요한 코어 (잊 메인)
# for l in need:
#     print(l)

    

# need.sort()
# print(need)

# obj = {
#     0 : 0,
#     1 : 0,
#     2 : 0,
#     3 : 0,
#     4 : 0,
#     5 : 0,
#     6 : 0,
#     7 : 0
# }

# for needList in need:
#     for i in range(8):
#         if needList[i] == 2:
#             obj[i] += 1

# print(obj)

# for needList in need:
#     if needList[0] == 2:
#         print(needList)

