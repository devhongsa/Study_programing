//for문
int sum=0;
for(int num=1; num<=10; num++){
    sum += num;
}

//향상된 for문 
String[] strArr = {"hongsa", "dev", "junior"}
for(String s : strArr){
    System.out.println(s);
}

public String solution(int[] numbers){
    StringBuilder sb = new StringBuilder();
    Arrays.stream(numbers)
        .boxed()
        .sorted((x,y)->{
            int a = Integer.parseInt(String.valueOf(x)+String.valueOf(y));
            int b = Integer.parseInt(String.valueOf(y)+String.valueOf(x));
            return b-a;
        })
        .forEach(sb::append);

    return sb.toString();

}