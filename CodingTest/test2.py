from collections import defaultdict

obj = defaultdict(int)

for i in range(1,1000000):
    obj[str(i)[0]] += 1
    
print(obj)