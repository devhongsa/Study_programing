import java.util.*;
public class JavaCondingTest{
    String str = "apple";

    // String 비교는 .equals()로 
    // char 비교는 == '' 이거로 비교

    for (int i = 0; i < str.length(); i++) {
        char c = s.charAt(i);
        ...
    }

    for (char c : str.toCharArray()) {
        ...
    }

    //길이 반환
    str.length();

    //빈 문자열 체크
    str.isEmpty();

    //문자 찾기
    str.charAt(0);            // 'a' -> 문자 반환
    str.indexOf("a");         // 0 -> 인덱스 반환
    str.lastIndexOf("p")      // 2 -> 마지막으로 문자가 속한 인덱스 반환

    //문자 자르기
    str.substring(1, 3);      // "pp" -> 인덱스 1 이상 3 미만 위치의 문자열 반환
    str.substring(3);         // "app" -> 인덱스 3 미만 위치의 문자열 반환

    //문자 치환(바꾸기)
    //replace([기존문자],[바꿀문자])
    str.replace('p', 'e');      // "aeele" -> 모든 [기존 문자]를 [바꿀 문자]로 치환

    //replaceAll([정규식],[바꿀문자])
    str.replaceAll(".", "/");   // "/////" -> 정규식에 맞춰 문자 치환 (정규식 "." 은 모든 문자를 의미)

    //replaceFirst([기존문자],[바꿀문자])
    str.replaceFirst('p', 'e');	// "aeple" -> 여러 문자 중 첫번째만 치환

    //문자 동일 여부 판단
    //자바 string의 경우, 클래스로써 Call by Reference형태로 생성 시 주소값이 부여된다.
    //그렇기에 String타입을 선언했을때는 같은 값을 부여하더라도 서로간의 주소값이 다르다.
    //따라서 값 비교로는 equals를 사용한다.
    str.equals("apple");

    //문자 비교
    /**
    * str과 applf가 같으면 0
    * str이 applf보다 사전순으로 앞이면 -1
    * str이 applf보다 사전순으로 뒤면 1
    * str과 applf가 마지막 문자만 다르면, 마지막 문자의 사전순 차이 반환
    */
    str.compareTo("applp"); // -1 -> 위 내용 참고

    //문자 포함 여부 판단
    str.contains("app");

    //문자열 분리
    str.split(" ");    //공백으로 구분된 문자열 str을 분리하여 String[] 배열로 반환
    str.split();       //띄어쓰기 없는 문자열 str을 한 문자씩 분리하여 String[] 배열로 반환

    //문자 앞뒤 공백 제거
    str.trim();        // str의 앞뒤 공백을 제거한다. 문자열 사이의 공백은 제거하지 않는다.

    //문자 <-> 숫자 변환
    Integer.parseInt("100")    //문자열 "100"을 숫자 100으로 변환
    Integer.toString(100)      //숫자 100을 문자열 "100"으로 변환

    //문자열 곱하기 
    str.repeat(3); // 문자열 3번반복

    StringBuilder sb = new StringBuilder();

    //문자열 추가
    sb.append("apple");    // "apple"

    //특정 인덱스에 문자 삽입
    sb.insert(2, "oo");    // "apoople"

    //문자열 삭제
    sb.delete(0, 2);       // "oople"

    //특정 인덱스의 문자 삭제
    sb.deleteCharAt(2);    // "oole"

    //특정 인덱스의 문자를 변경
    sb.setCharAt(1, 'p');  // "ople"

    //문자열 뒤집기
    sb.reverse();          // "elpo"

    //문자열 절대길이 줄이기
    sb.setLength(2);       // "el"

    //문자열 절대길이 늘이기
    sb.setLength(4);       // "el  " -> 뒤가 공백으로 채워짐

    // 대소문자 바꾸기
    str.toLowerCase();
    str.toUpperCase();

    //삼항연산자
    int max = (a > b) ? a : b;
    System.out.println("더 큰 값: " + max); 








    int[] lst = new int[3];
    String[] lst2 = {"a","b","c"};

    lst[0] = 3;

    // 원시타입 배열을 리스트로 
    int[] arr = {1, 2, 3};
    List<Integer> list = Arrays.stream(arr).boxed().collect(Collectors.toList());

    // 원시타입 배열 깊은 복사 
    int[] copied = Arrays.copyOf(arr, arr.length);

    // 원시타입 배열 출력 
    System.out.println(Arrays.toString(arr));

    // String 배열을 리스트로
    List<String> list2 = new ArrayList<>(Arrays.asList(lst2));

    // 리스트 선언 
    List<String> list = new ArrayList<>();

    //깊은 복사
    List<String> list3 = new ArrayList<>(list2);

    //얕은 복사
    List<String> list3 = list2;

    //요소 가져오기 
    list.get(0);

    //인덱스 범위 
    list.subList(1,3);  //원본 배열과 아직 연결되어 있음. 원본 배열이 바뀌면 더이상 사용못함. 깊은 복사로 사용하든가 해야됨. 

    //요소 삽입
    list.add("one");

    //특정 인덱스에 요소 삽입
    list.add(0, "zero");

    //특정 인덱스 요소를 바꿈 
    list.set(0, "zero");

    //리스트 병합 (추가되는 리스트가 뒤로 온다)
    list.addAll(list2);

    //특정 요소의 첫번째 인덱스 반환
    list.indexOf("zero");        // 0

    //특정 요소의 마지막 인덱스 반환
    list.lastIndexOf("zero");

    //특정 인덱스의 값 삭제, 인자로 int 원시타입들어감
    list.remove(0);

    //첫번째 값 삭제, 인자로 객체가 들어감
    list.remove("one");

    //리스트 차집합
    list.removeAll(list2);        // list에서 list2에 있는 모든 값을 삭제

    //리스트 교집합
    list.retainAll(list2);        // list에서 list2에 있는 값을 제외한 모든 값을 삭제

    //리스트 비우기
    list.clear();

    //리스트 비어있는지 체크
    list.isEmpty();

    //리스트 길이
    list.size();

    //리스트 특정 요소 포함여부 체크
    list.contains("one");

    //리스트에 다른 리스트 요소가 전부 포함되어있는지 여부 체크
    list.containsALL(list2);          // list에 list2의 모든 값이 포함되어 있으면 true

    //람다식 사용하여 요소들 제거
    list.removeIf(x -> x % 2 == 0)    // list에서 짝수인 수를 모두 제거

    //문자열 타입 배열을 List로 변환
    String[] temp = {"apple", "banana", "lemon"};
    List<String> list = new ArrayList<>(Arrays.asList(temp));

    //List를 문자열 배열로 변환
    List<String> list = new ArrayList<>();
    String[] temp = list.toArray(new String[list.size()]);

    //정수 배열을 List로 변환
    int[] b = {1, 2, 3, 4};
    List<Integer> a = Arrays.stream(b).boxed().collect(Collectors.toList());

    //List를 정수 배열로 변환
    List<Integer> list = new ArrayList<>();
    int[] temp = list.stream().mapToInt(x -> x).toArray();


    //reduce
    T result = stream.reduce(초기값, (누적값, 현재값) -> 새로운값);
    //누적곱 구하기 
    int product = nums.stream().reduce(1, (a, b) -> a * b);
    //누적합 구하기
    int product = nums.stream().reduce(0, (a, b) -> a + b);

    //map
    List<Integer> result = list.stream()
    .map(n -> n + 1)
    .collect(Collectors.toList());

    Arrays.stream(arr).map(num->{
           
        if(num>=50 && num%2 == 0){
            return num/2;
        } else if(num<50 && num%2 == 1){
            return num*2;
        } else{
            return num;
        }
    }).toArray();



    int[] temp = {1, 2, 3, 10, 20};
    List<Integer> list = new ArrayList<>(Arrays.asList(arr));

    //정수형 List 원소 중 최대, 최소값 
    Collections.max(list);
    Collections.min(list);

    //List 정렬
    Collections.sort(list);                               // 오름차순 (ASC)
    Collections.sort(list, Collections.reverseOrder())    // 내림차순 (DESC)

    //List 뒤집기
    Collections.reverse(list);

    //List 내 원소의 갯수 반환
    Collections.frequency(list, 3);

    //List 내 원소를 이진탐색을 이용해 찾기
    Collections.binarySerch(list, 10);    // 3



    Stack<Integer> stack = new Stack<>();

    //요소 추가
    stack.push(1);

    //요소 제거(꺼내기)
    stack.pop();

    //스택 비우기
    stack.clear();

    //스택 크기 체크
    stack.size();

    //스택이 비어있는지 유무 확인
    stack.empty();

    //스택에 요소 존재하는지 확인
    stack.contains(1);

    //스택 최상단 요소 확인, pop()과 다름
    stack.peek();



    Queue<Integer> queue = new LinkedList<>();

    //큐에 요소 추가(enqueue)
    queue.add(1);            // 추가성공시 true리턴, 문제 상황에서 예외 발생
    queue.offer(2);          // 문제 상황에서 false 리턴

    //큐에서 요소 제거(dequeue)
    queue.remove();          // 문제 상황에서 예외 발생
    queue.pool();            // 문제 상황에서 null 리턴

    //큐 비우기
    queue.clear();

    //큐의 최전방 요소 확인
    queue.element();         // 문제 상황에서 예외 발생
    queue.peek();            // 문제 상황에서 null 리턴




    // HashSet : 중복 허용 X, 순서 X
    // LinkedHashSet : 중복 허용 X, 순서 O (삽입순)
    // TreeSet : 중복 허용 X, 이진탐색트리 형태로 데이터 저장, 정렬 O

    HashSet<Integer> hashSet = new HashSet<>();
    HashSet<Integer> hashSet2 = new HashSet<>();

    //요소 추가
    hashSet.add(1);

    //요소 삭제
    hashSet.remove(1);    // 값이 1인 요소 삭제

    //차집합
    hashSet.removeAll(hashSet2);    //hashSet의 데이터 중 hashSet2과 중복된 데이터를 모두 삭제

    //교집합
    hashSet.retainAll(hashSet2);    //hashSet의 데이터 중 hashSet2과 중복된 데이터만 남기고 나머지 모두 삭제

    //데이터 초기화
    hashSet.clear();

    //hashSet 사이즈 확인
    hashSet.size();

    //특정 요소 포함 여부 확인
    hashSet.contains(1);

    //요소 전체 출력
    //Iterator 사용
    Iterator tempIterator = hashSet.iterator();
    while (tempIterator.hasNext()){
        System.out.println(tempIterator.next());
    }

    //for-each문 사용
    for (String item : hashSet){
        System.out.println(item);
    }

    list.forEach(item -> System.out.println(item));

    // filter
    list.stream()
    .filter(item -> item.startsWith("a"))
    .forEach(System.out::println);


    // HashMap : <key, value>쌍, value의 중복 허용 O, 순서 X
    // LinkedHashMap : <key, value>쌍, value의 중복 허용 O, key 순서 O (삽입순)
    // TreeMap : <key, value>쌍, key 순서가 오름차순(알파벳순) 으로 정렬됨

    HashMap<Integer, String> hashMap = new HashMap<>();

    //요소 추가
    hashMap.put(1, "딸기");
    hashMap.put(2, "바나나");
    hashMap.put(1, "사과");    // (1. "딸기")의 value가 "사과"로 대체됨

    //요소 삭제
    hashMap.remove(1);    // key 가 1인 요소 삭제

    //전체 삭제
    hashMap.clear();

    //key 포함 여부 확인
    hashMap.containsKey(1);

    //모든 value를 Collection에 담아 리턴
    hashMap.values();

    //value 포함 여부 확인
    hashMap.containsValue("사과");

    //key - value 출력
    for (Integer key : hashMap.keySet()){
        System.out.println(key + " " + hashMap.get(key))
    }

    for (Entry<Integer, String> temp : hashMap.entrySet()){
        System.out.println(temp.getKey() + " " + temp.getValue());
    }


}