|                | python                                      | java                                                      |   |   |
|----------------|---------------------------------------------|-----------------------------------------------------------|---|---|
| calculate      | + - * / %                                   | + - * / %                                                 |   |   |
|                | //                                          | int a , a/n                                               |   |   |
|                | 2**3                                        | Math.pow(2,3)                                             |   |   |
| List           | lst = [1,2,3]                               | List<String> s = new ArrayList<>(Arrays.asList(1,2,3))    |   |   |
|                |                                             | int[] lst = {1,2,3}                                       |   |   |
|                | [*list]                                     |                                                           |   |   |
|                | list(set(lst))                              | HashSet<Integer> hashset = new HashSet<Integer>(lst)      |   |   |
|                |                                             | ArrayList<Integer> arr = new ArrayList<Integer>(hashset)  |   |   |
|                | lst.index(value:1)                          | arrList.indexOf(1)                                        |   |   |
|                | if value in lst:                            |                                                           |   |   |
|                | lst.count(1)                                | Collections.frequency(arrList,1)                          |   |   |
|                | lst.remove(value:1)                         | arrList.remove(Integer.valueOf(1))                        |   |   |
|                | lst.pop(index:1)                            | arrList.remove(1)                                         |   |   |
|                | lst.append(2)                               | arrList.add(2)                                            |   |   |
|                | lst.insert(index:1, value:4)                | arrList.add(index:1, value:4)                             |   |   |
|                | lst.extend(lst2), lst + lst2                | arrList.addAll(arrList2)                                  |   |   |
|                | lst.clear()                                 | arrList.clear()                                           |   |   |
|                | lst.sort()                                  | arrList.sort(Comparator.naturalOrder())                   |   |   |
|                |                                             | arrList.sort(String.CASE_INSENSITIVE_ORDER)               |   |   |
|                | lst.sort(reverse=True)                      | arrList.sort(Comparator.reverseOrder())                   |   |   |
|                | lst.sort(key=lambda x: (x[1],x[0]))         | Collections.sort(arrList)                                 |   |   |
|                |                                             | Collections.sort(arrList, Collections.reverseOrder())     |   |   |
|                |                                             | Collections.sort(list, (c1, c2) -> c1.n - c2.n );         |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                | lst.reverse()                               | Collections.reverse(arrList)                              |   |   |
|                | ','.join(lst)                               | String.join(",", arrList)                                 |   |   |
|                | min(lst)                                    | Collections.min(arrList)                                  |   |   |
|                | max(lst)                                    | Collections.max(arrList)                                  |   |   |
|                | sum(lst)                                    | arrList.stream().mapToInt(Integer::intValue).sum();       |   |   |
|                | round(3.12333,2)                            | Math.round(3.12333)/100.0;                                |   |   |
|                | math.ceil                                   |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                | if 'aaa' in str                             | str.contains("aaa")                                       |   |   |
|                |                                             | str.indexOf("aaa")                                        |   |   |
|                | inter = (set(lst1) & set(lst2))             | arrList.retainAll(arrList2)                               |   |   |
|                | complement = (set(lst1) - set(lst2))        | arrList.removeAll(arrList2)                               |   |   |
|                | union = (set(lst1) \| set(lst2))            | arrList.addAll(arrList2)                                  |   |   |
|                |                                             | HashSet<Integer> hashset = new HashSet<Integer>(arrList)  |   |   |
|                |                                             |                                                           |   |   |
| hashTable      | dict(sorted(obj.items()))                   |                                                           |   |   |
|                | dict(sorted(obj.items(),reverse=True))      |                                                           |   |   |
|                | len(obj)                                    |                                                           |   |   |
|                | obj.pop(key,None)                           |                                                           |   |   |
|                | del obj[key]                                |                                                           |   |   |
|                |                                             |                                                           |   |   |
| String         | str.find("h")                               | str.indexOf("h")                                          |   |   |
|                | str.rfind("h")                              | str.lastIndexOf("h")                                      |   |   |
|                | str[0]                                      | str.charAt(0)                                             |   |   |
|                | str.startswith("h")                         | str.startsWith("h")                                       |   |   |
|                | str.endswith("h")                           | str.endsWith("h")                                         |   |   |
|                | str.split(",")                              | str.split(",")                                            |   |   |
|                | str.replace("h","s",1)                      | str.replaceFirst("h","s")                                 |   |   |
|                | str.strip() #delete vacant space            | str.strip()                                               |   |   |
|                | str.strip("hi")                             |                                                           |   |   |
|                | str.isupper()                               | str.isUpperCase()                                         |   |   |
|                | str.upper()                                 | str.toUpperCase()                                         |   |   |
|                | str.lower()                                 | str.toLowerCase()                                         |   |   |
|                | str[::-1]                                   | StringBuffer sb = new StringBuffer(str)                   |   |   |
|                |                                             | str = sb.reverse().toString()                             |   |   |
|                | list(str)                                   | str.toCharArray()                                         |   |   |
|                | str * 3                                     | str.repeat(3)                                             |   |   |
|                | s[:i] + s[i+1:]                             | StringBuffer sb = new StringBuffer()                      |   |   |
|                |                                             | sb.deleteCharAt(index)                                    |   |   |
|                |                                             |                                                           |   |   |
|                | str(123)                                    | String.valueOf(123)                                       |   |   |
|                |                                             | Integer.toString(123)                                     |   |   |
|                | int("string")                               | Integer.parseInt("string")                                |   |   |
|                |                                             | Integer.valueOf("string")                                 |   |   |
|                |                                             |                                                           |   |   |
| binary         | int(String: binary, 2)                      | Integer.parseInt(String: s, 2)                            |   |   |
|                | bin(1024), oct(),hex()                      | Integer.toBinaryString(1024)                              |   |   |
|                |                                             |                                                           |   |   |
| ASCII          | chr(65), ord("A")                           | (char)num, (int)ch                                        |   |   |
|                |                                             |                                                           |   |   |
| deque          | from collections import deque               |                                                           |   |   |
|                | q = deque(lst)                              |                                                           |   |   |
|                | q.appendleft, q.popleft, q.rotate(2 or -2)  |                                                           |   |   |
|                |                                             |                                                           |   |   |
| Priority Queue | import heapq                                | PriorityQueue<Integer> pq = new PriorityQueue<>()         |   |   |
| heap           | heapq.heappush(lst,value)                   | New PriorityQueue<>(Collections.reverseOrder())           |   |   |
|                | heapq.heappush(lst, -value)                 | PriorityQueue<int[]> pq =                                 |   |   |
|                | heapq.heappush(lst,(priority,value))        | new PriorityQueue<>((o1, o2) -> o1[0] - o2[0])            |   |   |
|                | heapq.heappop(lst)                          |                                                           |   |   |
|                | heapq.heapify(lst)                          |                                                           |   |   |
|                |                                             |                                                           |   |   |
| binary search  |                                             | Arrays.binarySearch(arr, value) : return index(or -index) |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
| Input          | lst = list(map(int,input().split()))        | Scanner sc = new Scanner(System.in)                       |   |   |
|                |                                             | int n = sc.nextInt()                                      |   |   |
|                | import sys                                  |                                                           |   |   |
|                | lst = map(int,sys.stdin.readline().split()) | BufferedReader br =                                       |   |   |
|                | data = sys.stdin.readline().rstrip()        | new BufferedReader(new InputStreamReader(System.in));     |   |   |
|                |                                             | int i = Integer.parseInt(br.readLine())                   |   |   |
|                |                                             | StringTokenizer st = new StringTokenizer(br.readLine())   |   |   |
|                |                                             | int N = Integer.parseInt(st.nextToken())                  |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |
|                |                                             |                                                           |   |   |