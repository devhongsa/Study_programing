//jdk download 검색 후 설치

//class이름은 대문자로 시작, 파일이름과 동일해야함.
public class Java{
    public static void main(String[] args) {
        System.out.println("hellow world");

        int num = 10;
        int bNum = 0B1010; //2진수
        int oNum = 012;    //8진수
        int hNum = 0xA;    //16진수

        // 자료형, 변수 선언
        byte n = 123;
        int n2 = 12345;
        long n3 = 12345567L;

        //Unicode : 한글과 같은 복잡한 언어를 표현하기 위한 표준 인코딩 , java에서는 표준인코딩 utf-16 사용 

        char a = 'A';
        double dNum = 3.14;
        float fNum = 3.14F;

        boolean b = true;

        String str = 'hongsa'; //String은 java가 정의해놓은 클래스이름임.

        // 상수(const)는 대문자로 표현 
        final int MAX_NUM = 100;

        // 형변환
        // 덜 정밀한 수에서 더 정밀한 수로 형변환은 묵시적으로 자동 형변환이됨.
        long numm = 3;
        // 정밀한 수에서 덜 정밀한 수로 형변환 할때는 자료형을 명시해줘야함(long->int)
        int numi = (int)numm;


        //사칙 연산
        // + - * / %  ++ -- 
        // < > <= == !=
        // && || !
        // += -= *= /= %=

        // ++num은 num에 먼저 1을 더함, num++은 나중에 1을 더함
        // println(++num)하면 1일 더해진 값이 나오고 num++이면 num숫자가 나오고 그 뒤에 1이 더해짐.

        //삼항연사자  조건 ? 결과1 : 결과2

        //if문
        if (num == 3){
            num = 1;
        }else if(num==5){
            num = 2;
        }else{
            num = 10;
        }
        //위 if문과 동일한 switch문
        switch(num){
            case 3 : num = 1;
                    break;
            case 5 : num = 2;
                    break;
            default: num=10;
        }

        //for문
        int sum=0;
        for(num=1; num<=10; num++){
            sum += num;
        }

        //while문
        while (num < 10){
            sum += num;
            num++;
        }
}
}





/// 클래스 

public class Student{
    //멤버 변수 정의
    int studentID;
    String studentName;
    int grade;
    String address;

    //default 생성자 : 이걸만들어주면 new Student();로 인스턴스만들때 오류가 나지않음
    public Student(){}

    // 생성자 : 이걸 만들면 new Student(100,"이순신") 이런식으로 매개변수가 꼭 들어가줘야함. 단 default생성자를 만들면 매개변수없어도 오류일으키지않음.
    public Student(int id, String name){
        studentID = id;
        studentName = name;
    }

    public void showStudent(){
        System.out.println(studentName + "," + address);
    }

    public static void main(String[] args) {
        Student studentLee = new Student();
        // studentLee 객체는 stack 메모리에 저장되고, 이 studentLee는 클래스의 멤버변수가 저장되어있는 heap메모리의 주소를 가리키게된다.
        // studentLee.~ 를 할 수있는 이유가. studentLee가 멤버변수들이 저장되어있는 heap메모리주소를 가리키고 있기 때문임
        studentLee.studentName = '이순신';
    }


    
}