lst = [1,2,3,4]
lst2 = ["a","b","c","d"]

for i, pair in enumerate(zip(lst,lst2)):
    print(i, pair[0],pair[1])