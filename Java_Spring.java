import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

// jdk download 검색 후 설치 : java SE , java EE 따로있음. SE는 standard edition, ee는 enterprise edition. EE버전이 SE위에 더 기능을 추가한 버전이라고 생각하면 됨.
// java EE 설치 : temurin 검색후 lts 버전 설치 
// tomcat : WAS  tar파일 받은후 bin폴더 경로로 가서  ./startup.sh 실행 localhost:8080 으로 접속가능 // ./shutdown.sh 으로 종료
// gradle : brew install gradle (npm과 같은 패키지,빌드 매니저 )
// start.spring.io
// intellij settings에서 gradle 검색후 build and run을 inellij 로 변경하면 더 빨리 빌드하고 실행됨.

//class이름은 대문자로 시작, 파일이름과 동일해야함.
public class Java {
    public static void main(String[] args) {
        //입출력
        //print(), println()   println은 자동줄바꿈을 해줌.
        System.out.println("hellow world"); 

        // Scanner
        Scanner sc = new Scanner(System.in);
        System.out.print("입력1 :");
        System.out.println(sc.next()); // 입력받은값 출력, 공백단위로 자름
        System.out.println(sc.nextInt()); // 숫자만 입력가능
        System.out.println(sc.nextLine()); // 입력받은값 출력, 공백포함 
        sc.nextLine(); // 엔터키 소진

        // BufferedReader : 입력값이 많을때 Scanner보다 성능이 훨씬 뛰어남.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        String s = br.readLine();
        int i = Integer.parseInt(br.readLine()); //int형으로 받고싶을때는 형변환 필요

        // format 
        // %d 정수, %f float, %.2f 자리수조절, %s 문자열, %o %x 8진수 16진수
        System.out.printf("%d", 10);
        String.format("%d %s",i,str);

        // Random
        Random random = new Random();
        int rnd = random.nextInt(100); // 0~99 정수 랜덤

        //삼항연산자
        int integer = rnd<10 ? 1:3;

        //문자열 자르기
        String str1 = "avcdfefs";
        str1.substring(0, 3); //index 0부터 2까지 슬라이스
        String[] lst = str1.split("d");

        int num = 10;
        int bNum = 0B1010; //2진수
        int oNum = 012;    //8진수
        int hNum = 0xA;    //16진수

        // 자료형, 변수 선언
        byte n = 123;
        int n2 = 12345;
        long n3 = 12345567L;

        // 비트연산
        // & : 두 비트값이 모두 1일때만 1
        // | : 두 비트 값중 하나라도 1이면 1
        // ^ : 두개의 비트값이 다르면 1, 같으면 0
        // ~ : 하나의 비트값을 바꾸는 연산자 , 0이면 1로 1이면 0으로

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
        // int를 String으로
        String str2 = String.valueOf(numm);
        String str3 = Integer.toString(numi);
        // String을 int로 
        int intvalue2 = Integer.valueOf(str2);
        int intvalue = Integer.parseInt(str3);

        // ** String 비교 
        // String은 == 으로 비교하면안되고 equals() 로 비교해야한다
        if (str2.equals(str3)){
            System.out.println("True");
        }


        //사칙 연산
        // + - * / %  ++ -- //
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
        for(int num=1; num<=10; num++){
            sum += num;
        }
        //향상된 for문 
        String[] strArr = {"hongsa", "dev", "junior"}
        for(String s : strArr){
            System.out.println(s)
        }

        //while문
        while (num < 10){
            sum += num;
            num++;
        }
}
}

/// 클래스 , 객체지향
/// 객체 지향 클래스 만드는 규칙
// 객체를 정의
// 각 객체의 속성을 멤버변수로, 역할을 메서드로 구현
// 각 객체간의 협력을 구현

public class Student {
    // 멤버 변수 정의
    int studentID;
    String studentName;
    int grade;
    String address;

    // Array 리스트
    int[] numbers = new int[10]; // 요소10개가 들어올 수 있는 배열 생성. 0으로 모두 초기화해서 만들어짐. numbers[0] = 0;
    int[] numbers2 = new int[] { 0, 1, 2, 3 };
    int[] numbers3 = { 0, 1, 2, 3 };

    // 다차원 Array
    int[][] arr = new int[2][3]; // 2행 3열의 array 배열 {{1,2,3},{4,5,6}}

    // ArrayList : 그냥 Array는 요소를 추가, 삭제하려고 하면 새로운 배열을 만들어서 복사하고 하는 귀찮은 작업이 있어야하는데,
    // ArrayList는 자동으로 해줌.
    ArrayList<String> list = new ArrayList<String>();
    // list.add("hongsa");
    // list.get(index); list[0] 이거는 안됨.
    // list.remove(index);
    // list.size();

    // 객체 리스트
    Java[] library = new Java[2]; // library[0] = new Java();, library[1] = new Java();
    // 만약 배열을 만들고 library[0] = new Java(); 만 할당해주면, library[1] = null 값이 나오게됨.
    // 배열 복사하기 : System.arraycopy(복사할배열, 복사시작할 인덱스위치, 붙여넣을배열, 붙여넣을 첫 인덱스 위치, 복사할 요소
    // 개수)

    // 객체 배열 복사 :
    Java[] library2 = new Java[2];
    Java[] library3 = new Java[2];
    // library2 배열에는 객체형성이 모두 되어있고, library3은 객체형성이 안되어있을경우, library2를 library3로 복사를
    // 한다면, 얕은복사가 일어난다.
    // 즉 객체의 메모리 주소를 복사하기 때문에 library2의 멤버변수가 변하면, library3의 멤버변수도 같이 변하게 된다.
    // 깊은 복사를 하기 위해서는 library3에서도 인스턴스 생성을 모두 해주고, set메서드를 통해서 직접 멤버변수값을 할당해주어야한다.

    // default 생성자 : 이걸만들어주면 new Student();로 인스턴스만들때 오류가 나지않음
    public Student() {
        this(1, "hongsa"); // this: 생성자가 다른 생성자를 호출할때 쓰임, 이경우 이 생성자안에서는 다른 코드작업을 할 수 가 없다.
                           // 왜냐면 여기서 다른 생성자를 호출했다는 것은 인스턴스가 아직 만들어지지 않은 상황이기때문이다.
                           // 인스턴스는 생성자가 동작하고 나서 멤버변수가 제대로 생성되는 구조임.
    }

    // 생성자 : 이걸 만들면 new Student(100,"이순신") 이런식으로 매개변수가 꼭 들어가줘야함. 단 default생성자를 만들면
    // 매개변수없어도 오류일으키지않음.
    public Student(int id, String name) {
        studentID = id;
        studentName = name;
    }

    public void showStudent() {
        System.out.println(studentName + "," + address);
    }

    public static void main(String[] args) {
        Student studentLee = new Student();
        // studentLee 객체는 stack 메모리에 저장되고, 이 studentLee는 클래스의 멤버변수가 저장되어있는 heap메모리의 주소를
        // 가리키게된다.
        // studentLee.~ 를 할 수있는 이유가. studentLee가 멤버변수들이 저장되어있는 heap메모리주소를 가리키고 있기 때문임
        studentLee.studentName = "이순신";
    }

}

// 하나의 파일안에 클래스가 여러개 있을 수 있음. 단 public class는 하나만 만들 수 있고 클래스명은 파일이름과 같아야함. 그외
// 클래스는 그냥 class로 만들어야함.
// private으로 선언된 변수는 선언된 내부클래스안에서만 사용할수 있음. 같은 파일안에 있더라도 클래스가 다르면 private으로 선언된
// 변수를 다른 클래스에서 사용하지 못함.
// 만약 private 변수를 다른 클래스에서 사용하고 싶으면, public 메서드를 만들어서 그 메서드를 통해 접근해야함.
// protected는 상속된 클래스에서만 사용가능하고, 나머지는 private, 외부패키지에서도 접근가능.
// 아무것도 안쓴다면 default로 기능하고, 같은 패키지내에서라면 외부클래스에서 모두 사용가능하지만, 외부 패키지에서는 사용불가.
// public은 어떤 위치에서간에 모두 사용가능.

// this? : 자신(인스턴스)의 메모리를 가리킴, 생성자에서 다른 생성자를 호출할때도 쓰임

// 클래스(객체)들 간의 협업 : 특정 클래스의 메서드안에서 다른 클래스의 메서드를 호출, 사용해서 그 클래스의 멤버변수에 영향을 끼치는
// 작업들.

// static? 변수 : 클래스 변수라고도 함. 다른클래스들이 공유할 수 있는 변수. 이 변수는 인스턴스가 생성되지 않아도.
// 클래스명.변수명으로 사용이 가능함.
// static 메소드 : 마찬가지로 static으로 만들어진 메서드는 인스턴스가 생성되지않아도 사용이 가능함. 그래서 static으로 생성된
// 메서드 안에서는 인스턴스 변수, 즉 멤버변수를 사용하지 못함. 멤버변수는 인스턴스가 생성될때 메모리가 잡히기 때문
// static으로 선언된 변수는 데이터 메모리, 멤버 변수는 힙 메모리, 지역변수(메서드안에서 생성된 변수)와 인스턴스는 스택메모리에
// 저장됨.
// 순서는 객체를 생성했을때 스택메모리에 인스턴스 저장, 이후 생성자 실행되면서 멤버변수들이 힙메모리에 저장, static은 객체를
// 생성하지않아도 데이터 영역에 저장.
// 자바는 메모리 해제를 가비지컬렉터가 자동으로 해주는데, 데이터 메모리 영역은 프로그램이 끝날때까지 메모리 할당이 유지 되기 때문에,
// static으로 선언하는 변수에 너무 큰 메모리를 할당하면 안됨.

// singleton? 패턴 : 단하나의 인스턴스만 존재해야하는 경우
public class Company {
    private static Company instance = new Company(); // 클래스 내부에서 미리 인스턴스 하나 생성해놓음.

    private Company() {
    } // 이렇게되면 외부에서 new Company()로 인스턴스 생성 불가.

    public static Company getInstance() { // 외부에서 이 메서드를 통해 생성된 하나의 인스턴스를 get할 수 있음. static을 쓴 이유는 인스턴스 생성없이 이 메서드를
                                          // 사용가능하게 해주기 때문
        return instance;
    }
}

// 상속?
// 상속을 쓸때는 어떤 클래스의 기능에 더해서 좀더 구체화 된, 차별된 기능을 추가 하고 싶을때 상속을 사용한다.
// 예를들어, customer에 대한 정보, 할인율에 대한 정보가 구현되어있는 클래스가 구현되어있는 상태에서 vip customer에 대한
// 등급이 필요해졌고 추가 기능이 필요해진 상태에서
// 만약 기존에 구현되어있던 Customer class에 기능을 추가하게된다면 if 등급==vip else if 등급==gold 이런식으로
// 코드가 난잡하게 만들어지게 되고,
// vip 손님에게만 존재하는 멤버변수들이 Customer class에 존재하게 되버린다.
// 이를 위해 customer를 상속받는 새로운 Vip class를 만들면 유지관리가 훨씬 편리해진다.
// 상속 키워드 extends는 하나의 클래스만 상속받을 수 있다. 2개이상 X (다이아몬드 문제)

// 자식클래스의 객체를 생성하게 되면, 부모클래스의 생성자가 먼저 실행되고, 자식클래스의 생성자가 실행된다.

public class Customer {
    protected int customerID; // protected는 상속받은 클래스에서는 쓸 수 있지만, 다른 외부 클래스에서는 private함.
    // 만약 그냥 int Customer라고 선언하면 default가시성이고, 같은 패키지내에서는 다른 클래스에서 쓸 수 있지만, 패키지가
    // 달라지면 쓸 수 없게 된다.
    protected String customerName;

    public Customer(int customerID, String customerName) {
        this.customerID = customerID;
        this.customerName = customerName;
    }

    public int calPrice() {
    }

}

public class VipCustomer extends Customer {
    // Customer를 상속받았기 때문에, 추가로 필요한 멤버변수만 정의하면됨.
    private double saleRatio;

    public VipCustomer(int customerID, String customerName) {
        super(customerID, customerName);
        saleRatio = 0.1;
    }
    // 만약 자식클래스의 생성자를 public VipCustomer(){} 이렇게 디폴트 생성자로 만들면 오류가난다. 왜냐면 현재 부모클래스에서는
    // 디폴트생성자가 없기 때문.
    // 오류를 없애려면 부모클래스에서도 디폴트 생성자를 만들어주거나, 자식클래스 생성자를 부모클래스 생성자와 같은 구조로 만들어주고,
    // 생성자안에 super(customerID, customerName) 이렇게 부모클래스 생성자를 호출해주어야한다.

    @Override // 이렇게 표시를 해주면 컴파일러가 알아듣게됨. 그래서 상위클래스의 메서드와 구조가 달라지면 컴파일 에러체크를 해줌.
    public int calPrice() {
    }

}

// 형변환 : Customer vc = new VipCustomer(); Customer의 멤버변수들은 VipCustomer의 멤버변수들에
// 포함되기 때문에 이렇게 객체생성이 가능하다.
// 하지만 vc.saleRatio는 사용할 수 가 없다. vc는 Cumstomer 클래스형이기 때문.
// VipCustomer vc = new Customer(); 이거는 불가능함.

// 오버라이딩 : 부모클래스에서 정의된 메서드와 똑같은 구조로 자식클래스에서도 만들면 오버라이딩된다. 이때 자식클래스에서는 기능을 바꿔서
// 구현할 수 있다.
// 가상 메서드(virtual method) : Customer vc = new VipCustomer(); 이렇게 했을때
// vc.calPrice()를 해보면 VipCustomer의 calPrice가 호출이됨.
// 원래대로라면 vc는 Customer형이기 때문에 Customer의 메소드만 쓸 수 있지만, java는 기본적으로 모든 메서드가
// virtual method라서 VipCustomer의 calPrice가 호출이 된다. 이런 성질은 다형성과 연결이되는데
// 다형성 : 다형성이란 쉽게 말해 한줄의 똑같은 코드가 다른 기능들을 수행할 수 있을 때를 말한다.

public class AnimalTest {
    public static void main(String[] args) {
        AnimalTest test = new AnimalTest();
        test.moveAnimal(new Human()); // 사람이 뜁니다.
        test.moveAnimal(new Tiger()); // 호랑이가 뜁니다.
        test.moveAnimal(new Eagle()); // 독수리가 날읍니다.
        // Human, Tiger, Eagle은 모두 Animal이라는 상위클래스를 가지고 있음.
    }

    public void moveAnimal(Animal animal) {
        animal.move();
        // Animal animal = new Human()
        // Animal animal = new Tiger()
        // Animal animal = new Eagle()
        // 이런식으로 코드가 실행되고, 이는 각각의 Human Tiger Eagle 클래스에서 구현된 virtual method를 실행시키게된다.
        // 이는 animal.move()의 한줄의 코드가 각기 다른 method를 실행시키는 결과로 이어진다. 이것이 다형성이다.

        // downcasting 다운캐스팅 : 하위클래스에 상위클래스에는 없는 메서드가 있고 그걸 써야될 경우 다운캐스팅을 해야 쓸 수 있음.
        if (animal instanceof Human) { // animal이 Human객체로 생성되었다면
            Human human = (Human) animal; // 다운캐스팅
            human.readBook();
        }
    }
}

// 추상클래스 : 추상클래스는 현재 클래스에서는 어떻게 구현할지는 모르고, 하위클래스에서 구현이 가능할때 쓴다.
// 하위클래스가 추상클래스를 상속받으면 하위클래스에서는 abstract로 선언된 메서드들을 반드시 구현을 해야한다.
// 만약 메서드를 일부만 구현한다면 그 클래스도 abstract로 선언해줘야한다.
// 추상클래스는 객체를 생성할 수 없다 (new Computer() 불가)
public abstract class Computer {
    public abstract void display();

    public abstract void typing();

    public void turnOn() {
        System.out.println("computer is turned on");
    }

    public void washCar() {
    } // 여기서는 구현이 안되어있지만, 필요에 따라 하위클래스에서 구현이 가능함. 구현을 안한 하위클래스에서는
      // 밑에 run() 했을때 아무것도 실행안하고 넘어갈 것이고, 구현한 하위클래스에서는 실행이 될것임. abstract메서드는 하위클래스에서
      // 무조건 구현을 해줘야하지만
      // 이렇게 하면 구현을 해도되고 안해도 됨.

    // 만약 run() 메서드가 하위클래스에서 오버라이딩되면 안되는, 고정된 기능이어야 하면 final로 확정을 해준다. 이를 템플릿 메서드라고
    // 함.
    // 미리 메서드의 시나리오를 정해놓고, 바뀌면 안되는 메서드를 말함.
    public final void run() {
        display();
        typing();
        turnOn();
        washCar();
    }
}

// 인터페이스 : 내부적으로는 추상클래스로 동작함. 모든 메서드가 추상 메서드로 이루어진 클래스를 말함. 형식선언만 하고 구현은 없음.
// 인터페이스 키워드 implements는 여러개를 상속받을 수 있다. 인터페이스 클래스는 구현된 부분이 없어서 다이아몬드 문제가 발생하지
// 않기 때문
public interface Calc {

    double PI = 3.14;
    // 컴파일 단계에서 public static final double로 자동 선언이 됨.

    int add(int num1, int num2);
    // 얘도 public abstract가 앞에 생략이 되어있는 상태임.

    // 원래 인터페이스 클래스에서는 구현메서드가 없어야 하지만 default로 선언해주면 만들 수 있다. 오버라이딩도 가능.
    default void description() {
        System.out.println("디폴트 메서드");
    }

    // static 메서드도 가능.
    static int total(int[] arr) {

    }
}

// 인터페이스를 상속받을때는 extends가 아닌 implements를 쓴다.
public class Calculator implements Calc {

}

// 객체 class 설계하기
// 객체의 3가지 요소
// 상태유지 : 객체의 상태정보를 저장할 수 있어야하고, 이러한 속성은 변수로 정의되어진다.
// 기능제공 : 객체의 행위에 대한 method가 정의되어야 한다.
// 고유 식별자 제공 : 객체의 고유한 식별자를 가지고 있어야한다.

// 객체 설계 5원칙
// 객체간의 결합도는 낮아야한다. (객체끼리 서로 의존성이 있게되면 한 객체가 수정될때, 의존관계에 있는 객체들을 모두 수정해야됨)
// 객체의 응집도가 높아야한다.
// 개방폐쇄 원칙 : interface를 이용
// 리스코프 치환 원칙 : 자식 클래스는 언제나 부모클래스타입으로 치환이 가능해야함.
// 공중유닛 - 정찰기 o
// 아반떼 - 그랜저 x

// 자신의 코드에 if/else, switch가 난무하고있지 않은가
// 책임과 역할이 다른 코드가 하나의 클래스에 다 들어가 있지 않은가
// 절차지향적으로 한 개의 파일에 모든 코드를 넣고 있지 않은가
// 내가 만든 객체가 재사용이 가능한가

// 디자인 패턴
// 생성패턴 (객체 생성과 관련된 패턴)
// Factory Method
// Singleton : 객체를 하나만 생성해야할때
// Prototype
// Builder
// Abstract Factory
// Chaining

// 구조패턴 (프로그램 내의 자료구조나 인터페이스 구조 등 프로그램 구조를 설계할때 활용되는 패턴)
// Adapter : 파라미터 객체타입이 맞지 않아 활용을 못할때 어댑터 클래스를 만들어서 객체타입이 맞지않아도 활용할 수 있게 해줌
// Composite
// Bridge
// Decorator : 원본클래스 인터페이스는 유지하고 거기에 다양한 데코레이터 클래스를 입혀서 확장된 형태의 객체를 만드는 방식
// Facade
// Flyweight
// Proxy : interpace를 상속하는 프록시(대리인) 클래스를 만들어서 cache처럼 활용가능. AOP 접목해서 활용 많이 함.

// 행위패턴 (반복적으로 사용되는 객체들의 상호작용을 패턴화)
// Template Method
// Interpreter
// Iterator
// Observer : 변화가 일어 났을 때, 미리 등록된 다른 클래스에 통보해주는 패턴
// Strategy : 유사한 행위들을 캡슐화하여, 객체의 행위를 바꾸고 싶은 경우 직접 변경하는 것이 아닌 전략만 변경하여, 유연하게
// 확장하는 패턴
// Visitor
// Chain of responsibility
// Command
// Mediator
// State
// Memento

// Singleton
public class SocketClient {

    private static SocketClient socketClient = null;

    private SocketClient() {

    }

    public static SocketClient getInstance() {
        if (socketClient == null) {
            socketClient = new SocketClient();
        }

        return socketClient;
    }
}

// json parser, http request
public class Mission1 {

    public static Integer getTotalCount(OkHttpClient client) throws IOException {
        Request request = new Request.Builder()
                .url("http://openapi.seoul.go.kr:8088/7275616250676d7233317868675579/json/TbPublicWifiInfo/1/1/")
                .build();
        try (Response response = client.newCall(request).execute()) {
            JsonParser parser = new JsonParser();
            Object obj = parser.parse(response.body().string());
            JsonObject jsonObject = (JsonObject) obj;
            Integer totalCount = jsonObject.getAsJsonObject("TbPublicWifiInfo").get("list_total_count").getAsInt();
            return totalCount;
        }
    }
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// implementation 'org.springframework.boot:spring-boot-starter-aop'
// implementation 'org.springframework.boot:spring-boot-starter-validation'
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Spring

// @SpringBootApplication : spring boot application으로 설정
// @Controller : View를 제공하는 controller로 설정
// @RestController : REST API를 제공하는 controller로 설정
// @RequestMapping : URL 주소를 맵핑
// @GetMapping, PostMapping, PutMapping, DeleteMapping, : api method 설정
// @RequestParam : URL query parameter 맵핑.
// @RequestBody : Http Body를 parsing 맵핑
// @Valid : POJO Java class의 검증
// @Configration : 1개 이상의 Bean을 등록할때 설정
// @Component : 1개의 Class 단위로 등록할때 사용
// @Bean : 1개의 외부 library로부터 생성한 객체를 등록 시 사용 , 메소드에 사용
// @Autowired : DI를 위한 곳에 사용
// @Qualifier : @Autowired 사용시 bean이 2개 이상 일때 명시적 사용
// @Resource : @Autowired + @Qualifier 의 개념으로 이해
// @Transactional : 클래스나 메소드에 달아서 트랜잭션 생성
// @Transactional(prpagation = Required) : Required가 실무에서 가장 많이 쓰이고,
// Required-New가 가끔 쓰일수 있다.
// New는 Transactional메소드안에 다른 메소드가 존재하고 그 메소드를 Transactional New로 설정해주면 그 메소드만
// 따로 독립적인 Transaction을 갖게된다.
// @Query(value = "select b from Book b where name = :name and createdAt >=
// :createdAt and updatedAt >= :updatedAt and category is null") :
// Query는 Repository 객체에서 쿼리메소드에 대한 어노테이션으로 붙는다. 쿼리메소드 naming이 너무 길어질때 쓴다.
// jpql문에서 :name은 쿼리메소드의 파라미터에서
// List<Book> findByNameRecently(@Param("name") String name, ...) 이렇게 Param
// 어노테이션을 사용해줘야지 쓸수 있다. 안그러면 ?1 이런식으로 파라미터 순서번호로 jpql에 넣어줘야한다.

// cascade : orphanRemoval vs Remove vs Soft deleted(soft는 deleted컬럼을 생성후 이데이터가
// 삭제된 데이터인지 true false 표시, 이후 데이터를 지우려고 할때 deleted false인 데이터만 지우게 한다.)

// jdk download 검색 후 설치 : java SE , java EE 따로있음. SE는 standard edition, ee는
// enterprise edition. EE버전이 SE위에 더 기능을 추가한 버전이라고 생각하면 됨.
// java EE 설치 : temurin 검색후 lts 버전 설치
// tomcat : WAS tar파일 받은후 bin폴더 경로로 가서 ./startup.sh 실행 localhost:8080 으로 접속가능 //
// ./shutdown.sh 으로 종료
// gradle : brew install gradle (npm과 같은 패키지,빌드 매니저 )
// start.spring.io
// talend API tester : 크롬웹스토어에서 다운
// intellij settings에서 gradle 검색후 build and run을 inellij 로 변경하면 더 빨리 빌드하고 실행됨.

// TestCode 관련
// implementation 'ch.qos.logback:logback-classic:1.2.3'
// testImplementation 'org.assertj:assertj-core:3.23.1'
// testImplementation 'org.junit.jupiter:junit-jupiter-params:5.8.2'

// DB관련
// implementation 'org.springframework:spring-jdbc:5.3.22'
// implementation 'com.zaxxer:HikariCP:5.0.1'
// testImplementation 'com.h2database:h2:2.1.214'

// import static org.assertj.core.api.Assertions.*;

// new project 생성 , gradle 기반
// TDD
// ex) 학점 계산기 도메인
// 1. 도메인을 구성하는 객체에는 어떤 것들이 있는지 고민
// 이수한 과목, 학점 계산기
// 2. 객체들 간의 관계를 고민
// 학점계산기 객체가 이수한 과목들을 인스턴스 변수로 갖고 그것들을 통해 학점평균계산?
// 3. 동적인 객체를 정적인 타입으로 추상화해서 도메인 모델링 하기
// 동적인 객체 : 과목종류(자료구조, 객체지향프로그래밍, 코딩테스트) --> 정적인 타입: 과목(코스) 클래스로 구현
// 4. 협력을 설계
// 5. 객체들을 포괄하는 타입에 적절한 책임을 할당.
// 6. 구현하기

// tomcat : was, 요청올때 쓰레드를 늘려서 요청을 처리하는 방식.
// 요청이 올때마다 쓰레드를 늘리면 대규모 트래픽 상황에서 서버의 과부화가 심해진다.
// 그래서 쓰레드 갯수를 제한해놓고 쓰레드 풀을 형성하여 쓰레드를 재활용하는 방식으로 운영된다.

// CGI(Common Gateway Interface)
// 웹 서버와 was 사이에 데이터를 주고받는 규약
// 인터프리터 방식 : 웹서버 <--> script engine <--> script 파일
// 서블릿 방식 : 웹서버 <--> servlet Container <--> servlet 파일
// servlet? : 자바에서 웹 애플리케이션을 만드는 기술, 동적인 웹 페이지를 구현하기 위한 표준이다.

// JDBC
// 커넥션 풀 : 미리 디비와의 커넥션들을 연결해놓고 풀로 형성해놓음. client요청이 있을때 마다 커넥션을 사용
// Was 스레드 수와 커넥션 수를 함께 고려해야함.
// 커넥션 수를 많이 설정하면 많은 접속자의 요청을 처리할 수 있지만 메모리 소모가 큼.

// settings
// inlay - code vision - usages 해제
// gradle - build and run : intellij 사용, jdk 버전 변경

// resources.static에 index.html 파일 올리면 알아서 spring boot가 index.html을 welcome
// page로 렌더링함.
// static 폴더에 hello-static.html 를 만들고 localhost:8080/hello-static.html 하면 spring
// boot cointainer가 처음에는
// hello-static.html 컨트롤러를 찾고 없으면, static폴더의 hello-static.html파일을 찾아서 렌더링 해줌.
// file - project structure에서 jdk 버전 변경 가능.
// settings에서 gradle 검색후 gradle의 jdk 버전도 변경 가능.
// 빌드하기 : 프로젝트폴더 경로에서 ./gradlew build, 빌드하면 /build/libs 경로에 jar파일 생성됨.
// ./gradlew clean build 하면 build 폴더 싹 지웠다가 다시 빌드함.
// /build/libs 경로에서 java -jar 파일이름.jar 하면 서버가 실행됨.

// MVC (Model, View, Controller) 방식 : html 정적파일에 동적데이터들을 합쳐서 렌더링
// API 방식 : json데이터를 리턴해주는 방식

// TDD : Test code를 먼저 구현하고, 그에 맞춰 로직을 구현하는 방식.
// debug 모드 사용 : 브레이크포인트 찍고, debug모드로 test코드 실행.

// Controller -> Service -> Repository : 정형화된 DI(Denpendency Injection) 관계
// Controller에서 Service기능을 써야하고, Service에서는 Repository 기능을 써야함.
// Ex) service.MemberService 클래스는 회원가입서비스가 구현되어있고,
// repository.MemoryMemberRepository 에는 회원정보를
// DB에 저장하는 기능 구현되어있음. MemberService의 회원가입서비스에는 Repository의 DB저장기능을 가져와서 쓰고 있고,
// controller.MemberController 에서는 client에서 온 요청에 따라 MemberService의 회원가입 기능을
// 가져와서 씀.
// 즉 Controller -> Service -> Repository는 DI 관계가 형성되어있고 Spring boot는 @Controller
// @Service 클래스의
// 생성자에 @Autowired 태그를 달아서 자동의존관계로 연결을 해줌.(스프링 빈 등록)

// 일급 컬렉션(클래스) : object(딕셔너리) 라고 생각하면됨. key,value를 인스턴스변수로 갖는 클래스 A를 List<A> 변수로
// 가지고 있는 클래스

// jpa auditing : Entity에서 데이터타입이 localDatetime인 컬럼에 자동으로 시간 넣어주는 기능
// https://webcoding-start.tistory.com/53
// @EnableJpaAuditing, @EntityListeners(AuditingEntityListener.class) 으로 사용한다.

// StringBuilder
// StringBuilder는 문자열을 + 연산할때 쓰인다.
// 그냥 보통 "a" + "b" 를 써도 되지만 이렇게 하면 메모리 낭비가 심해지기때문에 StringBulider를 쓴다.
// StringBuilder로 생성된 객체에 append를 사용하여 합친후 .toString()으로 출력가능

// IoC, DI
// Ioc(Inversion of Control) : 제어의 역전. java 객체를 개발자가 new로 생성하여 관리하는 것이 아닌 Spring
// Container에 모두 맡김.
// DI(Dependency Injection) : 객체간의 결합성을 낮춰주고, 유지보수가 좋은 코드로 만들어줌. 의존성으로 부터 격리시켜
// 코드 테스트에 용이하다. Mock
// 예를 들어 DB를 연결하는 기능의 객체를 만들려고하는데, 하나는 mysql, 하나는 postgresql이 있다고 한다면 두 객체에서 모두
// connect라는 method를 만들어야함. 그러면 이때 connect method를 가진 Idb 객체를 만들고. mysql과
// postgresql 객체에서는 각자 connect 메서드를 오버라이드해서 구현을 한다.
// 그리고 DbConnector라는 DI 객체를 만들어서 DbConnector connertor = new DbConnector(new
// mysql()), connector.connect(mysql) 이렇게사용
// 즉 DbConnector라는 객체안에서 new mysql()으로 객체를 생성하는 것이 아니라 밖에서 생성한 객체를 파라미터로 전달해
// 주입하는 형태를 말함.
// Ioc 는 @Component 어노테이션으로 spring에게 객체를 관리해달라는 뜻임. Component 등록된 객체는 Spring
// container에서 관리하는 Bean이 됨.

// AOP : 로그관련 기능 @Aspect, @Pointcut, @Before, @After

// JPA
// ORM (Object Relational Mapping) : Database의 테이블과, java에서의 객체 간의 관계를 정의해줌.
// JPA는 ORM역할을 하는 표준라이브러리라고 생각하면됨.
// Hibernate : JPA의 실제 구현체들을 말함.
// Spring data jpa : Hibernate에서 자주쓰는 기능들을 좀더 사용하기 쉽게 Spring에서 제공해주는 라이브러리
// @Entity : database의 table과 java의 객체를 이어주기 위해서 자바 객체에 선언
// @Id : table의 아이디로 설정
// @GeneratedValue : auto increment

// Lombok
// @Getter
// @Setter
// @ToString // User라는 객체를 println 했을때, User의 멤버변수에 대한 값들을 출력해줌.
// @NoArgsConstructor // 인자가 없는 생성자 생성, 필수적으로 넣어줘야함
// @AllArgsConstructor // 모든 멤버변수를 인자로 갖는 생성자 생성
// @RequiredArgsConstructor // NonNull 멤버변수를 인자로 갖는 생성자 생성
// @EqualsAndHashCode // 객체끼리의 비교연산을 위한 어노테이션
// @Data // Getter + Setter + ToString + RequiredArgsConstructor +
// EqualsAndHashCode
// @Builder // User.builder().name("martin").email("11@gs").build(); 이런식으로
// 이어쓰기위한 어노테이션

// 프로젝트 구조
// package
// controller : API 로직 구현 부분. GET POST DELETE UPDATE 로직 구현
// domain : DB에서의 테이블 내용이라고 생각하면 됨.
// repository : domain과 실제 DB를 연결. CRUD를 할때 이 repository를 통해 사용함. Interface로 작성
