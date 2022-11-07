
/////////////////////////////////////////////////////////////////////////////////////////

#include <iostream>

int main()
{


	return 0;
}


1.1 프로그램 구조


int main(    )
{
							///// 빈칸이나 빈줄은 컴파일러가 무시
	int x = 2;				//// 2는 리터럴
	x = 5;
	int y = x + 3; 

	std::cout << 1 + 2 << std::endl;  //// std는 namespace ,  :: 은 std 안에있는 cout 함수 쓰게 하는것

	return 0;				//// syntax error는 문법오류
}

/////////////////////////////////////////////////////////////////////////////////////////

1.3 변수

객체 objects					///// 객체가 메모리에 저장되고 메모리에 저장된 객체를 부르는 이름을 변수라고 함
변수 variables

left-values , right-values		///// x라는 메모리를 가지고 있는 것이 l-value, 123같이 한번있고 사라지는게 r-value
초기화 initialization , 대입 assignment 


int main()
{
	int x = 123;  /// 초기화 initializtion
	int x(123);

	int x;
	x = 123; // assignment       초기화와 어싸인먼트는 좀 다르다.

	return 0;
}

///////////////////////////////////////////////////////////////////////////////////////

1.4 std::cin, std::cout, std::endl;

\t : tab 키 cout으로 출력하면 tab 공간 출력
\n : 줄바꿈   endl;과 거의 같은 기능이지만 살짝 다름
\a : 오디오 소리 출력

int main()
{

	int x;
	cin >> x;     //// 사용자로 부터 x 값 입력 받기 

	cout << "your input is" << x << endl;
	return 0;
}


using namespace std; /// std:: 뺄수 있음

///////////////////////////////////////////////////////////////////////////////////////

1.5 함수


#include <iostream>

using namespace std;

int addTwoNumbers(int num_a, int num_b)    ///// 값 2개를 입력받아서 기능 하는 함수
{
	int sum = num_a + num_b;

	return sum;     ////// sum 은 int 형  add 함수도 int 형 함수  //// 출력 자료형과 함수 자료형은 같아야 함

}

void printHelloworld()
{
	cout << "Hello World" << endl;    ////////  이 함수같은경우 return 값이 없기 때문에 함수 앞에 void라고 쳐줌

	return;    ///// return을 쳐줘도 됨  return 0; 을 하면 0 (int 형) void 형이랑 다르기 때문에 에러남

	cout << "Hello World" << endl;   /////// return 뒤에 있는 것들은 실행되지 않음
}



int main()
{
	cout << addTwoNumbers(1, 2) << endl;    ////// 함수 이름 클릭하면 이름 같은 곳 모두 표시됨, 오른쪽 클릭 rename 하면 똑같은이름 전부 바꿈
	
	return 0;
}



****함수 안에 함수 선언은 불가능

void printa()
{
	void printb()
	{

	}
}

///////////////////////////////////////////////////////////////////////////////////////

1.6 키워드와 식별자

변수 명 숫자로 시작 금지, 띄어쓰기 금지
함수 명 main() 금지 , 대분자로 주로 시작 (동사 + 명사 ex. GetNumber())


///////////////////////////////////////////////////////////////////////////////////////

1.7 지역범위 local scope

int main()
{
	int x(0);    /////// x라는 변수는 main() 함수에서 벗어나면 사라짐

	{
		int x = 1;   /////// 이 영역에서의 x와 위에서의 x는 다른 변수임, 메모리 주소가 다름// 단 영역 밖으로 가면 없어짐

	} 
	
	{
		x = 2;    ///// 이렇게 하면 제일 바깥에 있던 x의 값이 달라짐 
	}


	return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////

1.8 연산자

+ -/ *


#include <iostream>

using namespace std;

int main()
{
	int x = 2;

	int y = (x > 0) ? 1 : 2;  // 삼항 연산자  x>0 이면 1 실행  아니면 2 실행

	cout << "my home" << endl;  // 문자열도 리터럴
}

// 하드 코딩 : 프로그래머가 변수에 직접 고정값들 넣어주면서 하는 방식
// 소프트 코딩 : 실행중 사용자의 입력이나 , 인터넷 통신등 으로 값을 받아와서 하는 방식


/////////////////////////////////////////////////////////////////////////////////////////

1.10 선언과 정의 declaration, definition

#include <iostream>

using namespace std;

int add(int a, int b);    /// 전방선언해주면 main함수가 앞으로 와도 add 함수 인식  세미콜론 찍어주기

int main()                /// main 함수가 코드 맨 앞으로 이동하면 add 함수를 모르기 때문에 컴파일 에러
{
	cout << add(1, 2) << endl;

	return 0;
}


int add(int a, int b)
{
	return a + b;
}

/////////////////////////////////////////////////////////////////////////////////////////

1.11 헤더파일 만들기

// add 함수를 다른 cpp 파일로 옮기기 , 헤더파일만들고 거기에 전방선언하기, main cpp에서 인클루드 헤더파일 해주기
// 헤더파일에 선언과 정의 모두 해줘도 되지만, cpp 파일이랑 헤더로 나누는걸 추천
#include "add.h" or "Myheaders/add.h" // myheader 라는 하위폴더에 헤더파일 있을때 

#include <iostream>

using namespace std;

int add(int a, int b);

int main()
{
	cout << add(1, 2) << endl;

	return 0;
}


int add(int a, int b)
{
	return a + b;
}

/////////////////////////////////////////////////////////////////////////////////////////

1.12 헤더 가드

헤더가드는 헤더파일들을 include 하다가 같은 함수가 2번 정의되는 것을 막아주는 역할

함수가 정의되어있는 파일에서
#ifndef MY_ADD   // MY_ADD 는 그냥 아무 이름 붙인거임 만약 이 파일에서 MY_ADD가 정의되어있지 않으면
#define MY_ADD   // MY_ADD를 정의한다

함수 정의

#endif      // #ifndef or #ifdef 를 하면 마지막에 #endif 써줘야함

이렇게 해주면 헤더 가드 역할 해줌

// 보통 헤더파일에서 #pragma once 가 이미 선언되어있음 이것만 있으면 헤더가드 역할해줌

/////////////////////////////////////////////////////////////////////////////////////////

1.13 네임스페이스 namespace

#include <iostream>

using namespace std;

namespace Myspace1
{
	namespace Myspace2     /// namespace 안에 namespace 가능 이때 이거 쓰려면 Myspace1::Myspace2::function()
	{
		int function()
		{
			return 0;
		}
	}
	int doSomething(int a, int b)
	{
		return a + b;
	}

	int doAnything(int a, int b)
	{
		return a * b;
	}
}

int doSomething(int a, int b)
{
	return a + b;
}

int main()
{
	cout << doSomething(1, 2) << endl;   // doSomething 이름 같아도 밖에 있는 doSomething 실행함
	cout << Myspace1::doSomething(1, 2) << endl;  // namespace로 만든거는 이렇게 해줘야 실행 가능

	using namespace Myspace1;   // Myspace1 안에 여러개 함수 있으면 using namespace 써서 Myspace1:: 생략 가능

	doSomething(1, 2);  // using namespace 쓰면 또 다시 doSomething 이름 같기때문에 에러발생
}


/////////////////////////////////////////////////////////////////////////////////////////


1.14 전처리기

#include <iostream>
using namespace std;

#define MY_NUMBER 9    /// 매크로  코드에서 MY_NUMBER를 만나면 9로 자동으로 바꿔줌
#define MY_NUMBER "Hello, World"  // 문자열도 가능

#define MAX(a,b) ((a>b) ? a : b)  


#define PRINT_JOE

#ifdef PRINT_JOE				//만약 print_joe가 define 되있으면
cout << "Joe" << endl;			//코드실행
#endif							// 조건 끝나면 무조건 endif 써주기

#ifndef PRINT_BOB
cout << "Bob" << endl;
#endif

#undef PRINT_JOE  // def 했던거를 undef함. 

int main()
{
	cout << MY_NUMBER << endl; // 9
	cout << MAX(1, 2) << endl;
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

2.1 기본 자료형

char
char16_t    // 이모티콘 같은 문자를 저장할때 쓰는
char32_t
wchar_t		// 잘 안씀

integer types
signed/unsigned  //  unsigned가 계산이 더 빠름 
short			 // 16 bits
int				// 16 bits
long			// 32 bits
long long		// 64 bits

floating-point types
float			// 32 bits
double			// 64 bits
long double

bool

void

decltype     // null pointer


#include <iostream>

int main()
{
	using namespace std;

	bool bValue = false;
	char chValue = 65;
	char chValue2 = "A";

	float fValue = 3.141592f;  //float 는 뒤에 f 붙이기  // f 빼면 double로 인식하는데 float는 더 작은그릇이므로 짤리는부분있음
	double dValue = 3.141592;  

	auto aValue = 3.141592;		//  자료형 알아서 정해줌

	sizeof(aValue);				//size of 메모리를 얼마큼 차지 하는지 알려줌 
	sizeof(int);				// 자료형도 넣을 수 있음

	int a(123);  // direct initialization
	int b{ 123 }; // uniform intitialization   조금 더 엄격하게 컴파일 데이터 타입 안맞으면 안댐;
	int c = 123;  // copy initialization

	cout << bValue << endl;   // 0, true는 1 
	cout << chValue << endl;  // A
	cout << (int)chValue2 << endl; // 65
}



//////////////////////////////////////////////////////////////////////////////////////////////////////////

2.4 무치형 (보이드 , void)

#include <iostream>

void my_function()
{

}


int main()
{

	void my_void;   /// void는 메모리가 없기때문에 변수선언 불가
	int i = 123;
	float f = 123.456f;

	void* my_void;  /// 이런 형태는 가능

	my_void = (void*)&i;
	my_void = (void*)&f;
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

2.6 불리언 자료형 , bool 

#include <iostream>


bool isEqual(int a, int b)
{
	bool result = (a == b);			// a와 b가 같으면 true 리턴

	return result;
}



int main()
{
	using namespace std;

	bool b1 = true;
	bool b2(false);
	bool b3{ true };

	b3 = false;


	cout << std::boolalpha;   /// true false를 출려할때 1, 0 이 아닌 true false 로 출력
	cout << b3 << endl;		  // 0   !b3 하면 true
	cout << b1 << endl;		  // 1   
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

2.7 문자형 char type


static_cast<char>(65)     // char(65) 와 같음   < > 여기에는 변환할 타입을 넣음
static_cast<int>('A')     // int('A') 와 같음   static_cast는 컴파일러한테 미리 체크받는 느낌 

endl; 이랑 \n 이랑 차이점은 endl; 은 버퍼에 있는 내용까지 다출력하고 줄바꿈해라의 의미도 포함되어있음
std::flush 는 버퍼에 있는 내용 다 출력하고 줄바꿈 안함
 "출력하고 싶으면 \" " 이렇게 하면 출력됨


//////////////////////////////////////////////////////////////////////////////////////////////////////////

2.8 리터럴 상수 literal

decimal 10진수 : 0 1 2 3 4 5 6 7 8 9
octal 8진수 : 0 1 2 3 4 5 6 7 10 11 12
hexa 16진수 : 0 1 2 3 4 5 6 7 8 9 A B C D E F


int x = 012; // 앞에 0 붙이면 8진수라는 뜻 
int x = 0xF;  // 16진수는 앞에 0x 붙임
int x = 0b1010; // 2진수는 앞에 0b


//////////////////////////////////////////////////////////////////////////////////////////////////////////

2.9 심볼릭 상수 const

const double gravity(9.8);		// const를 쓰면 반드시 선언과 동시 초기화를 해주어야함

double const gravity(9.8);   // 단순 변수 선언할때는 const가 앞에 붙든 뒤에 붙든 상관 없음 , 하지만 포인터로 가면 의미가 달라질수 있음



void printNumber(const int my_number)  // 파라미터에 const를 붙이는 이유는 , my_number가 함수안에서 바뀌지 않게 막는 용도.
{
	int n = my_number;     // 바꿀라면은 새로운 변수 선언해서 바꿔줘야함
	n = 134; 

	cout << my_number << endl;
}

constexpr // 이거는 컴파일 타임에 결정되서 바뀔 수 없다는 걸 체크하는 의미 , 런타임때 결정되는 변수는 constexpr 로 선언 못함.



//////////////////////////////////////////////////////////////////////////////////////////////////////////


3.3 증감 연산자++ --

++x 와 x++ 의 차이는 ++x 는 먼저 1더하고 x 출력하고, x++ 는 먼저 x 출력하고 1을 더함



//////////////////////////////////////////////////////////////////////////////////////////////////////////


3.4 size of, 쉼표 연산자, 조건부 연산자(삼항 연산자)

int x = 3;
int y = 4;
int z = (++x, ++y); //콤파 연산자는 ( )를 해줘야함 , 뜻은 ++x를 하고 ++y 이값을 z에 대입   주로 for문에서 쓰인다고 함


//////////////////////////////////////////////////////////////////////////////////////////////////////////

3.5 관계 연산자 

부동소수점 오차에 대해서 오차 무시하고 크기 비교하는 법 


//////////////////////////////////////////////////////////////////////////////////////////////////////////

3.6 논리 연산자

if (a==1 && b==2)            // &&는 만약에 a가 1이 아니면은 b==2를 보지도 않고 그냥 넘어감. 
{
	dosomething;       
}

//XOR 은 두개가 같으면 false 다르면 true

//////////////////////////////////////////////////////////////////////////////////////////////////////////
4.1 지역변수, 범위, 지속기간

#include <iostream>	


using namespace std;

int main()
{
	int apple = 5;

	cout << apple << endl;

	{
		int apple = 1;				// 이때 위에 apple과 안에 apple은 다른 메모리 주소를 갖는다. 
		cout << apple << endl;		// 근데 만약 int apple 이 아니고 그냥 apple 만 썼으면 위에 apple 변수를 말하는 것임.

	}

	cout << apple << endl;
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////
4.2 전역변수, 정적 변수, 내부연결, 외부연결

#include <iostream>

using namespace std;

int value = 123;    /// 전역변수앞에 static int value = 123; 하면 다른 cpp 파일에서 이 변수는 접근을 못함
					/// extern을 앞에 붙이면 다른 파일 어딘가에 있는 value를 가져와서 씀. 이때 이 파일에서 다시 초기화하면 에러걸림

extern void doSomething();  ////  void doSomething이라는 함수는 다른 cpp 파일에 선언되어있고 여기 메인 cpp에서 전방선언을 해주면 
							////  이 cpp 파일에서 doSomething 함수 사용 가능. 이때 앞에 extern이라고 써주는게 좋음(외부에 있다는걸 알려줌)


void doSomething()
{
	static int a = 1;     /// static으로 변수 선언을 하면 같은 메모리 주소를 계속 쓰기 때문에 함수밖으로 나갔다와도 a =1로 초기화 안함.
	++a;
	cout << a << endl; 
}


int main()
{
	int value = 1;

	cout << ::value << endl;   // :: 붙이면 global scope operator 전역변수 사용가능
	cout << value << endl;

}


// 헤더파일에서 namespace some 쓰고 안에 const int a = 123;  불변 상수 선언하고, 다른 여러 cpp 파일에서 some::a 쓰면 메모리가 
// 계속 다른 메모리를 생성해내서, 메모리 낭비가 심함. 이때는 헤더파일에 namespace에서는 a를 초기화 하지말고 다른 cpp 파일을 만들어서
// 똑같이 namespace some을 만들고 extern const int a =123 ; 초기화 해주면 여러 cpp파일에서 a를 사용해도 메모리가 하나로 고정되있음.


//////////////////////////////////////////////////////////////////////////////////////////////////////////

4.3 using문

using namespace std;
using std::cout; //  std안에있는 cout 함수만 using 하고 싶으면 namespace는 빼


//////////////////////////////////////////////////////////////////////////////////////////////////////////

4.4 auto 

auto add(int x, int y)   /// 함수 앞에는 auto 쓸수 있지만 파라미터에는 auto를 쓸 수 없음. 템플릿을 써야됨
{
	return x + y;
}

auto a = add(1, 2); 

//////////////////////////////////////////////////////////////////////////////////////////////////////////

4.5 형변환

int i = 30000;
char c = i;

cout << static_cast<int>(c) << endl;   // 30000은 char가 담을 수 없는 데이터크기, 이거를 출력을 하면 엉뚱한 숫자가 나오게됨.
										// 근데 2를 넣으면 제대로 나오긴 함.

cout << 5u - 10u;		// unsigned 끼리 연산해서 signed 값이 나오면 이상한 값을 출력하게됨.

									
//////////////////////////////////////////////////////////////////////////////////////////////////////////

4.6 std string

#include <string>

using std::string;

int main()
{
	const char my_strs[] = "hello, world";   // 이 경우 마지막에 안보이는 문자하나 있음
	const string myt_s = "hello, world";     //  이 경우는 보이는 스트링 개수만큼 

	string name;

	
	std::getline(std::cin, name);			// getline 쓰는 이유는 cin을 쓰게되면 띄어쓰기가 나올때 입력받는걸 멈추기때문, 띄어쓰기
	cin.getline(name, 255);					// 뒤에 있는 내용은 버퍼로 남겨두고, 나중에 출력시킴.

	std::cin.ignore(32767, '\n');			// 이거는 \n 이거를 만나기 전까지 32767길이까지 string을 입력받아라



	string a("hello,");
	string b( "world");

	string c = a + b;		 // string 끼리 더할수 있음

	int d = c.length();		// length() 함수는 string 안에 있는 기능 함수 string의 문자열 개수 알려줌


//////////////////////////////////////////////////////////////////////////////////////////////////////////

4.7 열거형 enum

#include <iostream>
#include <string>
#include <typeinfo>

using std::string;

enum Color			//사용자정의 자료형 , 요소들은 내부적으로 int 형 숫자로 바뀌어짐. 보통 0부터시작해서 1, 2, 3, 이렇게 올라감.
					// 이로인해 다른 enum 에 있는 요소와 값자체가 같은 경우가 있기때문에, 문제가 생길수있음. 이때는 enum class를 씀
{
	COLOR_BLACK,	// 다른 enum에서 똑같은 COLOR_BLACK 이름 쓰면 안됨
	COLOR_RED = 3,	// 값 할당도 가능
};

Color AA = COLOR_BLACK;

enum class Fruit
{
	BANANA,
	APPLE,
};

Fruit A = Fruit::BANANA;   // 그냥 enum 과는 달리 enum class 에서는 Fruit::BANANA 이렇게 초기화 해줘야함.   




void my_function()
{

}


int main()
{
	using namespace std;

	Color paint = COLOR_BLACK;



}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

4.9 자료형에게 가명 붙이기

int main()
{
	using namespace std;

	typedef double distance_t;  // double 이라는 자료형을 distance_t 라고도 쓸수있게 함.
	using distance_t = double;  // 같은 얘기임. using을 쓰는 방법도 있다.

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

4.10 구조체 struct

struct Person
{
	double height = 3;     // 디폴트값으로 초기화해줄 수있음. 근데 다른 곳에서 Person me{5,...} 이렇게 다시 초기화해주면 5로 바뀜
	float weight;
	int age;
	string name;
};

void printPerson(Person ps)				// 2. person 자료형이 파라미터이기 때문에  me가 들어갈 수 있음.
{
	cout << ps.height << " " << ps.weight << endl;     //  3. me의 height, weight를 출력함.
}

// printPerson이라는 함수를 구조체 안에 넣어서 사용도 가능함. 이때는 Person ps라는 파라미터를 함수안에 넣어줄 필요도 없음.
// me.printPerson() 이렇게만 해주면 출력함. 


struct Family			// 구조체안에 구조체를 넣을 수 도 있음.
{
	Person me;
	Person mom;
	Person dad;

};

Person getMe()			// Person 구조체 자료형을 리턴해주는 함수를 만들 수 도 있음.
{
	Person me{ 2.0, 100.0, 20, "jack jack" };

	return me;


}



int main()
{ 
	using namespace std;

	person me{2.0,100.0,20, "jack jack"}  // 1. me 라는 person을 정의 초기화해줌
	printPersone(me);						


}


//////////////////////////////////////////////////////////////////////////////////////////////////////////
5.2 조건문 if

#include<cstdlib>

exit(0);			//어느 곳에 있던지 함수 리턴타입과 상관없이 그냥 나가버림.


if (x = 1)			//이거는 x=1 로 초기화하고 나서, if (x) 이거랑 똑같아짐.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
5.3 switch-case 

int main()
{
	int x;
	cin >> x;

	switch (x)
	{
		int a;
		int b = 5;					// switch문 안에서 변수 선언은 가능한데 초기화는 해줄수 없음. 할라면 case문 안에서 해줘야함.
	case 0:
		cout << "zero";				// 만약 case 마다 break를 안넣게 되면 x = 0 이 들어왔을때 case 1,2,3를 다 실행함.
		break;
	case 1:
		cout << "one";				
		break;
	case 2:
		cout << "two";
		break;

	default:
		cout << "??";				// case에 맞는 경우의 수가 하나도 없을때 default 실행
		break;
	}
	cout << endl;
}



//////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.1 배열 기초 array

struct Rectangle
{
	int length;
	int width;
};



int main()
{
	using namespace std;

	int one_student;   // sizeof 4바이트
	int students[5];	// sizeof 20바이트 , array 크기는 컴파일 타임때 정해져 있어야함, cin으로 입력받아서 결정할 수 없음.
						// 나중에 동적할당을 배우면 가능함

	students[0] = 100;

	Rectangle hi[10];    // 스트럭처 변수에도 array를 쓸 수 있음
	hi[0].length = 23;
	hi[0] = { 23, 43 }

	// array 초기화 방법
	int my_array[5] = { 1,2,3,4,5 };
	int my_array[5] = { 1,2,3, };   // 나머지 값은 0으로 초기화됨.
	int my_array[] = { 1,2,3,4,5 }; // 개수가 정해져있으면 [] 이렇게 해도 됨
	int my_array[]{ 1,2,3,4,5 };	// = 안써도 됨.

}

///

void doSomething(int student_scores[20])   // 여기서 파라미터는 배열을 파라미터로 받는게 아니고, 포인터를 파라미터로 받고 있음.
											// 즉 , 배열을 복사해서 가져오는 것이 아닌, 포인터만 가져와서 쓰는거. 배열의 메모리는 같음
											// 그래서, 뒤에 [20] 이것도 그냥 [] 이렇게 써도됨
{
	cout << &student_scores << endl;       // 여기서의 주소와 메인함수에서의 주소는 다름. 여기서의 주소는 파라미터로 받은 포인터의 주소값임.
	cout << &student_scores[0] << endl;	  //  이거는 메인함수에서 첫번째 요소의 주소값과 같음.

}


int main()
{
	int student_scores[20] = { 1,2,3,4,5 };

	cout << &student_scores << endl;
	cout << student_scores << endl;     // array는 그자체가 주소이기 때문에 &를 안써도 주소가 나옴
	cout << &student_scores[0] << endl;  // 배열의 첫번째 요소의 값의 주소는 array 주소랑 같음.
	


}


std::swap(array[0], array[3]) // array index 0,과 3의 값을 서로 바꿈

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.5 다차원 배열


int array[2][5] =			// row값은 안써줘도 컴파일러가 계산할 수 있는데, column 값은 써줘야함.
{
	{1,2,3,4,5},
	{6,7,8,9,10}
}; 

int array[2][5] = { 0 }; // 전부 0으로 초기화 ,

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.7 포인터의 기본적인 사용법

(*) de-reference  이 표시는  포인터가 저쪽 주소에 가면 이 데이터가 있어요 라고 간접적으로 가리키기만 하는 것에 대해서,
그럼 거기에 진짜 뭐가 있는지 내가 들여다볼게 라며 직접적으로 접근하겠다는 의미.

int main()
{
	using namespace std;

	int x = 5;
	double d = 1.0;

	typedef int* pint;		// 포인터 변수도 사실 데이터형이기 때문에, 이런식으로 정의할 수 있음

	int* ptr_x = &x;
	int* ptr_y = &d;		// 이때 d는 double 형인데 포인터는 int 형이므로 에러가 난다. / 그리고 포인터의 메모리는 항상 4바이트

	cout << typeid(ptr_x).name() << endl;   // int * 가 출력됨   int * 가 데이터타입


}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.7 null pointer


void doSomething(double* ptr)
{
	cout << &ptr << endl;	   // 여기서의 ptr 주소는 main에서의 &ptr과 다름. 함수의 파라미터로 ptr이 들어올때는 ptr2를 만든다고 생각하면됨.
								// 즉 main의 x 변수가 갖는 주소값은 똑같지만 포인터 변수가 2개가 되는거임. 포인터 변수가 갖는 주소값은 같기
								// 때문에 역참조를 하면 x의 값이 나옴

}



int main()
{
	using namespace std;

	double x = 5;

	double* ptr = 0;
	double* ptr = NULL;
	double* ptr = nullptr;    //모던 cpp 스타일

	double * ptr = &x

	if (ptr != nullptr)
	{
		//do something
	}

	else
	{
		//do nothing   
	}



}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.8 포인터와 정적 배열(둘은 같다)


void printArray(int my_array[])				// 이거는 printArray(int *my_array) 이거랑 같음. 즉 포인터를 파라미터로 받는다는 얘기
{
	cout << sizeof(my_array) << endl;		// 4

	*my_array = 100;						// 이렇게 하면 함수 밖에서도 my_array 값을 바꿀 수 있음.

}



int main()
{
	using namespace std;

	int my_array[5] = { 1,2,3,4,5 };

	cout << sizeof(my_array) << endl;   // 20

	int* ptr = array;

	cout << sizeof(ptr) << endl; //  정적배열과 포인터의 다른점은 사이즈를 찍었을때 정적배열은 그 배열의 사이즈가 나오고 포인터는
								// 포인터 변수의 사이즈인 4가 나온다.

	cout << *(ptr + 1) << endl;  //  이렇게 하면 2 가 나옴, my_array[1] 값 

}


cout << my_array << endl; // 이때 주소값이 나온다. 즉 포인터랑 같은 역할을 하고있음.


//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.9 포인터 연산과 배열 인덱싱


int main()
{
	int value = 7;
	int* ptr = &value;

	cout << uintptr_t(ptr - 1) << endl; // int size인 4가 빼져서 나옴
	cout << uintptr_t(ptr) << endl;
	cout << uintptr_t(ptr + 1) << endl;// int size 4가 더해져서 나옴 . double로 하면 8이 더해져서 나옴



}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

6.10 문자열 심볼릭 상수

int main()
{
	char name[] = "jack jack";
	char* name = "jack jack"; //  기본적으로 포인터에는 리터럴 값이 들어갈 수 없다. 주소만 들어갈 수 있음
	const char* name = "jack jack";  // 하지만 앞에 const를 붙여주면 되긴 함.

	int int_arr[5] = { 1,2,3,4,5 };
	char char_arr[] = "hello, world";
	const char* name = "jack jack";

	cout << int_arr << endl;	//  주소가나옴
	cout << char_arr << endl;	// hello, world    문자열 배열은 주소가 아닌 문자열을 출력함./ 이때 &char_arr 를 출력하면 이상한값이 나옴.
	cout << name << endl;		// jack jack		
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.11 메모리 동적 할당 new, delete

int main()
{
	int my_array[10000000000];  // 정적메모리 할당은 stack 메모리를 쓰기때문에 오류생김 stack 메모리는 작음 heap은 메모리가 큼, 동적메모리할당

	int* ptr = new int(7);		// int 사이즈의 메모리를 하나 할당해주세요의 뜻임. new를 쓰면 주소를 주기때문에 포인터로 값을 받아야함

	int* ptr = new (std::nothrow) int(7);		// nothrow는 다른프로그램이 메모릴를 다쓰고있어서 메모리를 할당받지못할때 오류를 안일으키고
												// nullptr을 넣어주는 기능.

	delete ptr;					// delete는 os가 프로그램이 끝날때 메모리를 가져가는게 아닌, 스스로 메모리를 반납하는거임.

	cout << *ptr << endl;		// delete를 해주고나서 다시 ptr의 값을 불러오려고하면 쓰레기값이 나옴.

	ptr = nullptr;				// 그래서 쓰레기값으로 인한 오류를 발생시키지 않기 위해 nullptr을 써줘서 방지해줌

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.12 동적 할당 배열

int main()
{
	int length;

	cin << length;

	int* my_array = new int[length]();     // new로 메모리를 동적 할당 받는 경우에는 주소를 받기 때문에 *array 포인터로 받아야함.
										// () 이거는 모든 값을 0으로 초기화 해주겠다는 뜻.
										// {11, 22, 33,44 } 이렇게 하면 차례로 값을 넣어준뒤 나머지는 0으로 초기화



	delete[] my_array;						// 배열은 [] 이걸로 delete를 해주어야함.


}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.13 포인터와 const

int main()
{

	int value = 5;
	const int* ptr = &value;		// 포인터가 가리키는 디레퍼런스값을 못바꿈
	int* const ptr2 = &value;		// 포인터가 가지고 있는 주소값을 못바꿈.
	const int* const ptr = &value;   // 아무것도 바꿀 수 없음.

	int value2 = 8;

	*ptr = 6;		// 불가능
	ptr = &value2;	// 가능

	*ptr2 = 6;		// 가능
	ptr2 = &value2;	// 불가능 
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.14 참조 변수 reference variable


void doSomething(int& v)			// 만약 파라미터에 const int& v 이렇게 하면 v의 값을 바꿀 수 없게 됨.
{									// 단 const 에 레퍼런스 쓰면, doSomething(5) 이렇게 파라미터 안에 상수를 넣을 수 있게 됨.
	v = 10;							// 레퍼런스가 아닌 int * v 이거는 상수값을 넣을 수가 없음.

}


int main()
{
	int value = 5;
	int* ptr = nullptr;
	ptr = &value;

	int& ref = value;				// 레퍼런스는 선언할때 반드시 초기화를 해줘야함. 그리고 리터럴도 못들어감

	cout << ref << endl;			//5

	ref = 10;						// 마치 변수 value랑 똑같음.

	cout << &value << endl;			// 주소1     value 와 ref는 그냥 변수이름만 다른 똑같은 놈임. ref는 그냥 별명이라고 보면됨.
	cout << &ref << endl;			// 주소1
	cout << ptr << endl;			// 주소1
	cout << &ptr << endl;			// 주소2 


	doSomething(value);				// doSomething의 파라미터는 레퍼런스이기 때문에 value의 값이 10으로 바뀌게됨. 
									// 파라미터를 레퍼런스가 아닌 그냥 int v 로 받았으면 value의 값은 달라지지 않음.

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.16 포인터와 참조의 멤버 선택

struct Person
{
	int age;
	double weight;

};

int main()
{
	Person person;

	person.age = 5;
	person.weight = 30;

	Person& ref = person;			// person을 레퍼런스로 선언해주면 별명생기는거임
	ref.age = 15;					// 그래서 person.age = ref.age  똑같음.

	Person* ptr = &person;			// 근데 포인터로 선언할때는 person의 주소가 들어가야되므로 &person으로 초기화

	ptr->age = 30;					// ptr은 ref와는 다르게 주소이기때문 ptr->age 이렇게 접근해야함
	(*ptr).age = 30;				// 마찬가지로 역참조 *ptr를 해서 접근하는방법도 가능

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.17 for each 반목문


int main()
{

	const int fibo[] = { 0,1,2,3,4,5,6 };

	for (int number : fibo)
		cout << number << " ";    // 0 1 2 3 4 5 6  출력

	for (auto number : fibo)		// auto &number 레퍼런스로 해주면 fibo의 값을 바꿔 줄 수 있음
	{								
		number = 10;
		cout << number << " "
	}

	for (int number : fibo)
		cout << number << " ";   // 위에서 auto &number 이렇게 안해주면 10으로 안바뀌고 그대로 0 1 2 .. 출력 

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////
6.18 void 포인터

int main()
{
	int i = 5;
	float f = 3.0;
	char c = 'a';

	void* ptr = nullptr;

	ptr = &i;					// void 포인터는 어떤 데이터형이든지 포인터로 선언할 수 있음
	ptr = &f;
	ptr = &c;

	cout << *ptr << endl;		// 하지만 void 포인터는 역참조를 할 수 가 없음 왜냐하면 어떤 데이터타입인지 모르기 때문에 
	cout << *static_cast<float*>(ptr) << endl;   // 이때는 ptr을 float* 이렇게 캐스트해주고 나서 앞에 * 역참조를 해줘야함.
												// 이 얘기는 float * ptr = &f 이렇게 선언을 다시 해주는 거와 같음.



}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.19 다중 포인터와 동적 다차원 배열

이중 포인터 용법

int main()
{
	int col = 5;
	int row = 3;

	int** matrix = new int* [row];

	for (int r = 0; r < row; ++r)
		matrix[r] = new int[col];
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.20 std:: array   배열 정적할당

int main()
{
	int my_array[5] = { 1, 2, 3 ,4, 5 };				// 기본적인 배열 정적할당.

	std::array<int, 5> my_arr = { 1, 2, 3, 4, 5 };    // 이거는 배열 요소 개수를 꼭 써줘야함 5 

	cout << my_arr[4] << endl;
	cout << my_arr.at(10) << endl;				// .at 을 쓰면 배열요소개수를 체크해보고 초과하는 숫자면 예외처리 발동.
	cout << my_arr.size() << endl;				// 요소 개수 알려줌
	cout << my_arr.begin() << " " << my_arr.end() << endl;		// 제일 첫번째 요소, 제일 마지막 요소

	std::sort(my_arr.begin(), my_arr.end());
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

6.21 std::vector        배열 동적할당.

int main()
{
	std::vector<int> my_arr = {1,2,3,4,5};

	cout << my_arr.size() << endl;

	cout << my_arr[1] << endl;
	cout << my_arr.at(1) << endl;  

	my_arr.resize(10);			// resize도 자유롭게 가능

}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.1 매개변수와 인자  parameter , argument

int foo(int x, int y)		// 함수 정의 할때 나오는 변수는 파라미터
{
	return x + y;
}

int main()
{
	int x = 1, y = 2;

	foo(6, 7);				// 실제로 함수를 사용할 때 쓰는게 argument

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.2 값에 의한 전달

void doSomething(int y)				// doSomething(5) 하면, int y = 5; 이거를 함수안에서 새롭게 하는 것과 같음.
{
	cout << "In func" << y << " " << &y << endl;
}

int main()
{
	doSomething(5);

	int x = 6;

	cout << "In main" << x << " " << &x << endl;

	doSomething(x);
	doSomething(x + 1);

	return 0;

}


//////////////////////////////////////////////////////////////////////////////////////////////////////////
7.3 참조에 의한 인수 전달

void getSinCos(const double degrees, double &sin_out, double &cos_out)    // 보통 입력값을 파라미터 앞에, 출력 값을 뒤쪽에 넣음. 입력값은
																		 // const로 해주면 알아보기도 쉬움.


void addOne2(int*&y)						//
void addOne(int& y)
{
	y = y + 1;
	cout << &y << endl;					//주소 1
}


int main()
{
	int x = 5;

	cout << x << " " << &x << endl;		// 주소 1

	addOne(x);

	cout << x << " " << &x << endl;		// 주소1   참조에 의한 인수 전달은 모두 주소 같음.

	int* ptr = &x;						// 포인터를 addOne(ptr) 하면 에러뜸 , 이때는 함수 addOne2 에서처럼 파라미터에 * 를 추가해주어야함

}


배열을 참조 인수로 넣기

// void Do(int (&arr)[4])		// 이때는 배열 요소개수를 꼭 써줘야함
void Do(vector<int>& arr)
{}

int main()
{

	//int arr[] = {1,2,3,4};
	vector<int> arr{ 1,2,3,4 };
	Do(arr);

}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.4 주소(포인터)에 의한 인수 전달

void foo(int* ptr2)					//이 얘기는 int* ptr2 = ptr  이렇게 선언해주는거랑 똑같음.
{									// 그래서 &ptr2 와 &ptr은 다른 주소를 가짐 , 다른 변수라는 뜻. 단지 가지고 있는 주소값이 같기때문에
									// 역참조를 하면 같은 메모리장소가 나오는 것일 뿐.
}


int main()
{
	int value = 5;

	cout << value << " " << &value << endl;

	int* ptr = &value;

	foo(ptr);
	foo(&value);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

다양한 반환 값들 (값, 참조, 주소, 구조체, 튜플)




//int getValue(int x)
//int* getvalue(int x)			// 포인터로 return할때는 main 함수에서 받을 때 조심해야됨 value값이 getvalue 함수밖을 나가면 사라지기 때문.
int& getvalue(int x)
{
	int value = x * 2;
	return value;
}


std::tuple<int, double> getTuple()  //  <> 여기 안에 내가 받을 자료형들 넣기
{
	int a = 10;
	double d = 3.14;
	
	return std::make_tuple(a, d);
}

int main()
{
	std::tuple<int, double> my_tp = getTuple();		// std::tuple<int,double> 이거 자체가 자료형이라고 생각하면됨 

	cout << std::get<0>(my_tp) << endl;				// get<n번째요소>
	cout << std::get<1>(my_tp) << endl;

	//cpp 17 이상에서는

	auto [a, d] = getTuple();
	cout << a << endl;
	cout << d << endl;


	return 0;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.6 인라인 함수 inline

inline int min(int x, int y)
{
	return x > y ? y : x;
}

int main()
{
	cout << min(5, 6) << endl;
	cout << min(3, 2) << endl; 

	cout << (5 > 6 ? 6 : 5) << endl;   // inline 함수를 쓰면 함수를 호출하지도 않고 min 함수에서 int x, y를 선언하지도 않고
										// 바로 이렇게 대입해서 쓰게 해주게 함. 속도가 빨라지는 장점
										// 근데 다 이렇게 해주는게 아니고 함수를 봤을 때 이렇게 대입할 수 있으면 컴파일러가 해줌
										// 심지어 inline을 쓰지 않아도 요즘 컴파일러들은 알아서 판단해서 해줌.

}
 
//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.7 함수 오버로딩

// 함수 오버로딩은 비슷한 기능을 하는 함수를 이름을 같게 해서 편하게 쓰려는 목적

int add(int x, int y)				// 함수는 이름이 같아도 파라미터가 다르면 다른 함수로 판단한다. 그리고 
{									// 함수의 리턴값이 다른것만 가지고는 오버로딩이 안됨.
	return x + y;
}

double add(double x, double y)
{
	return x + y;
}

int main()
{
	add(1, 2);	
	add(3.0, 4.0);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////
7.8 매개변수의 기본값 default 

void print(int x, int y = 20, int z)   // 왼쪽값은 디폴트값이 있는데 오른쪽값이 없으면 안됨, 그리고 전방선언이 있을 경우에는 전방선언 부분에만
void print(int x = 0)					// 디폴트값을 설정해주던가, 정의 부분에만 설정해주던가 둘중에 하나만 디폴트값을 설정해주어야함 보통 
										//전방선언에 설정.
{
	cout << x << endl; 
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.9 함수 포인터

int func(int x)
{
	return 5;
}

int goo()
{
	return 10;
}

int main()
{
	cout << func << endl;   // 주소값이 나옴. func() 을 했으면 5가 나왔겠지만, 그냥 func을 하면 주소값이 나옴. 
							// 즉 함수도 포인터다. 마치 my_arr[3] 배열 my_arr가 포인터인 것 처럼.

	int(*fcnptr)(int) = func;  // 함수포인터를 선언하는 방법.  func 파라미터의 자료형이 int니까  (*fcnptr)(int) 이렇게 넣어줘야함
								// const int 면 const int 넣어줘야함. 앞에 int는 함수의 리턴값의 자료형
	cout << fcnptr(1) << endl;		// 5   () 이거의 뜻은 어떤 함수의 기능을 실행하라 라는 뜻임.

	fcnptr = goo;

	cout << fcnptr() << endl;		// 10

}

함수 파라미터에 함수 포인터를 넣을 수 있음.또 파라미터로 들어간 함수 포인터에도 디폴트값을 넣어 줄 수 있음.

파라미터로 들어간 함수가 예를들어 bool (*fcnptr)(int) 이거였을때

typedef bool(*fcnptr_t)(int);  //이런식으로 줄일 수 있음.파라미터로 쓸때 fcnptr_t fcnptr 이렇게 쓰면됨.
using fcnptr_t = bool(*)(int);  //bool 자료형의 함수포인터 선언을 요약해준 것이 fcnptr_t 이다.
#include <functional> 
std::function<bool(int)>;		//마찬가지로 std::function<bool(int)> = fcnptr_t 이거랑 같음.

//////////////////////////////////////////////////////////////////////////////////////////////////////////
7.10 스택과 힙 

전역변수같은 것들이 가장 밑에서 부터 메모리가 쌓임. 가장먼저 생겨나고 가장 늦게 지워짐.
그다음 main() 함수 부터 실행이되기 때문에 main() 함수에 있는 변수들이 메모리에 쌓이기 시작
main 함수에서 다른 함수를 호출하면 그 함수로 가서 그 함수에 있는 변수들이 메모리에 쌓이기 시작.
그렇게 가다가 끝나면 제일 위에 쌓인 메모리부터 차례로 지워지기 시작.

스택은 속도는 빠르지만 메모리가 작아서 많은 메모리를 쌓진 못함. 스택오버플로우 발생가능 stack overflow

동적메모리 할당은 힙메모리에 쌓임. 힙 메모리는 사이즈가 큼.

이때 메모리 할당을 해도 지워줘야함.



//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.11 std::vector 더 잘 사용하기.

int main()
{
	std::vector<int> v{ 1,2,3 };

	v.resize(2);      // vector의 resize는 작은사이즈로 옮겨갈때는  현 3 size의 메모리를 그대로 쓰되, 2 size 인것처럼
				// 사용하게 만들어놓는다. 그래서 capacitiy를 찍어보면 여전히 3이 나옴.
				// 이렇게 하는 이유는 2 size의 메모리를 새로 받아서 복사해서 넣고 기존 3 size를 지우게 하면 너무 느리기때문

	v.reserve(1024);    // reserve는 미리 메모리를 확보해 놓는 것임. v.resize(1024) 랑 다른점은 resize는 0으로 모든 메모리를 
				// 채워넣지만 reserve는 capacity 만 높여놓고 실제로 size는 3인채로 냅둠.

	v.push_back(7);      // 배열 맨뒤에 요소 넣기,  reserve 해놓으면 메모리 복사 삭제 과정없이 쉽게 요소 추가 가능
	v.push_back(5);
	v.push_back(3);

	v.pop_back();      // 배열 맨뒤부터 요소 삭제, capacity 유지한채로 size만 줄임
	v.pop_back();
	v.pop_back();

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.12 재귀적 함수 호출

함수가 자기 자신함수를 또 부름 .


//////////////////////////////////////////////////////////////////////////////////////////////////////////
7.14 assert

int main()
{
	const int number = 5;

	assert(number == 5);					// assert는 디버그 모드에서만 작동. 어디서 오류났는지 알려줌. 5가 아니면 오류나면서 알려줌

	static_assert(x == 5, "x should be 5"); // static_assert는 컴파일타임때 오류를 알려줌. 문구도 삽입가능, 단 컴파일때 알려주기 때문에 x ==5 이런거 쓰려면
											// const int number = 5; 이렇게 초기화해줘야 사용가능.

	return 0;

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

7.16 생략부호 ellipsis

double findAverage(int count, ...)					// 인자가 몇개 들어갈 건지 파라미터로 써주고, 그다음 ... 쓰면 동적으로 인자 파라미터 생성가능.
{
	double sum = 0;

	va_list list;									

	va_start(list, count);

	for (int arg = 0; arg < count; ++arg)
		sum += va_arg(list, int);				// 인자로 들어올 타입을 정의를 해주어야함. 같은 타입의 데이터만 들어올 수 있음.

	va_end(list);

	return sum / count;

}

int main()
{
	cout << findAverage(1, 1, 2, 3, "hello", 'c') << endl;		// 이때는 인자 개수를 1로 설정했기때문에 뒤에 2 3 hello 는 무시하게됨
	cout << findAvergae(10, 1, 2, 3, 4, 5) << endl;				// 이 경우는 10개 인자를 넣는다 했는데 5개 밖에 안넣어서 오류가 나게됨.
	
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////

8.1 객체 지향 프로그래밍, 클래스


class Friend
{

public:								// class 와 struct 는 기능이 거의 비슷하지만 클래스에서만  access spectifier가 들어감.
									// public을 안해주면 이 클래스 밖에서는 클래스 멤버들을 사용할 수 없게됨. 
									// private: 해주면 밖에서 사용 불가. 
	string name;
	string address;
	int age;
	double height;
	double weight;

	void print()
	{
		cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
	}


};

int main()
{
	Friend jj{ "jack jack", "uptown", 2, 40, 10 };			// Frined 라는 클래스의 객체 jj 생성.

	jj.print();												// jj 객체의 기능 실행.

	vector<Friend> my_friends;
	my_friends.resize(2);									// 배열 { jj, jj2 } 로 생성 

	my_friends[0].print();									// jj.print()

	for (auto& ele : my_friends)
		ele.print();										



}

//////////////////////////////////////////////////////////////////////////////////////////////////////////



class Date
{

private:
	int m_month;
	int m_day;
	int m_year;

public:
	void setDate(const int& month_input, const int& day_input, const int& year_input)       // private 멤버들은 밖에서 사용못하기때문에
	{																						// 이렇게 public 함수를 사용해서 간접적으로 바꿔주는 방법.	
		m_month = month_input;
		m_day = day_input;
		m_year = year_input;
	}

	//const int& getDay()     이렇게 하면 복사하지 않고 레퍼런스를 가져오기때문에 메모리 사용 덜함.
	int getDay()
	{
		return m_day;
	}

	void copyFrom(const Date& original)
	{
		m_month = original.m_month;
		m_day = original.m_day;
		m_year = original.m_year;
	}


};


int main()
{
	Date today;
	today.setDate(8, 4, 2021);
	cout << today.getDay() << endl;

	Date yesterday;
	yesterday.copyFrom(today);			// 원래는 yesterday.setDate(today.getMonth(), today.getDay(), today.getYear()); 
										// 이렇게 해야되는거를 copyFrome 함수덕분에 줄일 수 있음.
										// 보통 class 함수의 멤버를 private으로 해놓고 이런식으로 간접적으로 접근할 수 있게
										// 하는 이유는, 만약 클래스 멤버의 변수명을 바꿔야할때가 오면 , public으로 해놧을때
										// 클래스 밖에 여기저기 다 돌아다니면서 바꿔줘야하지만, 이러한 방식은
										// 클래스 내에서만 변수 명을 바꿔주면 되므로 코드 관리측면에서 좋다.


}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

8.3 생성자 constructors

class Fraction
{
private:
	int m_n;
	int m_d;

public:
	//Fraction(const int& num_in, const int& den_in = 1)    //생성자에 파라미터 입력가능, 생성자 파라미터에서 디폴트값 넣기 가능
	Fraction()												// 클래스 이름과 같으면 생성자. 기본 디폴트값을 설정할 수 있음
	{														// Fraction frac; 으로 객체를 형성함과 동시에 생성자를 바로 실행하게됨.
															// 만약 생성자 함수를 안만들어도 컴파일러가 Fraction() {} 이거를 알아서 만들어줌.
		//m_n = num_in;
		//m_d = den_in;

		m_n = 0;
		m_d = 1;	
	}


	void print()
	{
		cout << m_n << " / " << m_d << endl;
	}

};

int main()
{
	
	Fraction frac;						// 클래스 객체를 선언할때, 생성자 함수에 파라미터가 하나도 없을 경우에는 frac 이렇게 객체 형성가능.
										// 근데 생성자 함수에 파라미터가 있으면 frac(1,3) 이런식으로 객체 생성해주어야함.

	//Fraction frac(1, 3);				// frac(1) 만 넣을 경우 생성자 함수 파라미터에 있는 디폴트 값으로 적용
	//Fraction frac{1, 3};				// () {} 이거 차이는 {} 이게 더 엄격해서 데이터 형변환을 자동으로 시켜주지 않음. {1.0, 3} 안됨
	frac.print();

	return 0;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

8.4 생성자 멤버 초기화 목록


class B
{
private:
	int m_b;

public:
	B(const int& m_b_in)
		: m_b(m_b_in)
	{}

};


class something
{
private:
	int m_i;
	double m_d;
	char m_c;
	int m_arr[5]
	B  m_b;
public:
	something()
		: m_i(1), m_d(3.14), m_c('a'), m_arr(1, 2, 3, 5, 6), m_b(m_i -1)		// () 대신에 {} 이거 써도 됨 , 배열도 초기화 가능, 다른 클래스의 객체도
	{																			// 초기화 가능, 만약 위에 private 멤버에서도 초기화햇을 경우에 생성자의 초기화가	
																				// 우선순위가 더 높다.
		int m_i = 4;															// {} 여기 안에서 초기화해주면 {}안에서 초기화해준 값이 최종 값이 된다.

	}

	void print()
	{
		cout << m_i << " " << m_d << " " << m_c << endl;

	}

};


int main()
{
	something som;

	som.print();
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////

8.5 위임 생성자 

class Fraction
{
private:
	int m_n;
	int m_d;

public:
	Fraction(const int& den_in)
		:Fraction(0, den_in)						// 이렇게 하면 main 함수에서 Fraction frac(1); 이렇게 했을때  m_n의 값을 0 으로 초기화해주고, den_in 만 
	{}												// 해주면 됨. 이거 왜하냐면 num_in이 똑같은 값이 많을때, 계속 0을 써주는게 귀찮아서 이렇게 하는거임.
													// 또는 초기화를 생성자에서 하지말고 초기화함수를 클래스안에 따로 만들어서 하는 방법도 있음.
	Fraction(const int& num_in, const int& den_in)   					
	{														
		m_n = num_in;
		m_d = den_in;
	}


	void print()
	{
		cout << m_n << " / " << m_d << endl;
	}

};

int main()
{

	Fraction frac(1);															

				
	frac.print();

	return 0;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////
8.6 소멸자 destructor

class IntArray
{
private:
	int* m_arr = nullptr;
	int m_length = 0;

public:
	IntArray(const int length_in)
	{
		m_length = length_in;
		m_arr = new int[m_length];

		cout << "constructor" << m_id << endl;
	}

	~IntArray()// 소멸자
	{
		if (m_arr != nullptr)					// nullptr을 지우려 할때도 문제가 생기기때문에 nullptr이 아닐때 지워라
			delete[] m_arr;						// 근데 그냥 vector 쓰면 이런거 할필요 없음

		cout << "destructor" << m_id << endl;
	}

};

int main()
{
	while (true)
	{
		IntArray my_int_arr(10000);				// 이렇게하면 동적할당시 메모리 leak이 일어남 , 이를 방지하기 위해서 소멸자를 사용
	}
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////
8.7 this 포인터

class Simple
{
private:
	int m_id;

public:
	Simple(int id)
	{
		setID(id);          // s1 객체가 형성되고 생성자가 실행될때 사실 this->setID(id) 이렇게 작동하는거임.
		//(*this).setID(id);    // 앞에 저렇게 숨어져 있는거임, this는 s1객체의 포인터
		//this->setID(id);
		cout << this << endl;  // 여기서 this는 객체 s1의 주소 즉 s1의 포인터임.
	}

	void setID(int id) { m_id = id; }    // 클래스 안에서의 함수는 모든 객체들이 공유하는 함수 이기때문에 객체마다
	int getID() { return m_id; }      // 함수의 메모리를 따로 생성하지 않음. 함수 메모리는 하나고, 각 객체의 정보를 가지고
}                                           // 함수를 실행하는 것임.  반대로 멤버 변수(m_id)는 각 객체마다 주소가 다름 

int main()
{
	Simple s1(1), s2(2);

	cout << &s1 << " " << &s2 << endl;

}


class Calc
{
private:
	int m_id;

public:
	Calc(int m_id)
		: m_id(m_id)
	{}

	Calc& add(int m_value)              // 리턴값을 자기 자신의 레퍼런스를 리턴함
	{
		m_id += m_value;
		return *this;                   // this는 주소이고 이거에 역참조는 Calc의 객체
	}

	void print() { cout << m_id << endl; }
};


int main()
{
	Calc cal(10);

	cal.add(2).add(10);                 // cal.add(2) 이거의 리턴값이, cal 객체를 리턴하니까 다시 .add(10) 이렇게 하는게 가능.
	cal.print();

	return 0;
}




/////////////////////////////////////////////////////////////////////////////////////////////////////

8.9 클래스와 const

class Something
{
public:
	int m_value = 0;

	void setValue(int in_value) { m_value = in_value; }     // setValue 함수는 애초에 멤버값을 바꾸는 함수 이기때문에 const 함수로 못만듬.
	int getValue() { return m_value; }
	int getValue() const { return m_value; }     // 함수 뒤에 const를 붙여주면 const로 생성한 객체가 함수 사용가능. 그리고 뒤에 const를 쓰냐 안쓰냐에 따라서
												// getValue 함수를 오버로딩 할 수 있음. const로 된 getValue 함수를 쓰려면 객체 생성할때 const Something st; 이런식으로
												// const로 객체를 생성해주면  st.getValue() 쓰면 const getValue 함수를 자동으로 호출함.
												// const를 함수 맨뒤에 붙이는 이유는 멤버를 바꾸지 않겠다는 뜻.
};

void print(const Something& st)                 // 파라미터를 레퍼런스로 안받아오면 복사가 되기때문에 이런식으로 많이씀
{
	cout << &st << endl;
}


int main()
{
	const Something som;

	som.getvalue(3);            // som 객체를 생성할때 const로 생성했기때문에 som 객체안에있는 m_value 값을 바꾸려하면 안됨.

	cout << som.getValue() << endl;     // 그냥 값을 출력하는 함수라고 해도 안됨. 그 이유는 컴파일러가 값을 바꾸냐 안바꾸냐를
										// 보는게 아닌, 함수가 const 함수인지 아닌지를 보기 때문.

}

/////////////////////////////////////////////////////////////////////////////////////////////////////

8.10 정적멤버 변수 static

class Something
{
public:
	static int s_value;                     // 클래스 멤버 변수는 static으로 했을 때 바로 초기화 할 수 없음. 밖에서 초기화해줘야됨
};

int Something::s_value = 1;                 // 이런식으로 밖에서 초기화해줘야함. 객체 형성을 안해도 쓸 수 있음. 그리고 static 선언은 cpp 파일에서 만 해야댐

int main()
{
	cout << &Something::s_value << endl;        // 객체를 형성 안해도 s_value의 주소가 있음. 그 이유는 동적이 아닌, 정적 static으로 생성된 변수이기 때문.

}

/////////////////////////////////////////////////////////////////////////////////////////////////////

8.11 정적멤버 함수

class Something
{
private:
	static int s_value;

public:

	Something()
		: s_value(123)                          // staitc 멤버 변수는 생성자에서 초기화가 불가능하다 
	{}                                          // class 안에서 static 멤버 변수를 초기화 하려면 Something 클래스 안에 새로운 클래스를 하나 더 만들고
												// 새로만든 클래스의 생성자를 통해서 초기화를 해주는 방법이 있다.
	int getValue()
		//static int getValue()                     
	{
		return s_value;                         // 만약에 얘가 static 함수였으면 this -> s_value 이렇게 못씀. 객체없이 접근 가능하기때문에
	}                                           // 특정 개체에 대한 this 를 쓰지 못하게 되는거임. 


};

int Something::s_value = 1024;

int main()
{
	cout << Something::s_value << endl;         // 이때 클래스 멤버 s_value는 private 으로 막혀져 있기 때문에 접근 불가
	cout << Something::getValue() << endl;      // 이때 클래스 안에 static 함수를 선언해주면 객체를 생성안해도 함수에 접근해서 멤버에 접근가능.

	int (Something:: * fptr)() = &Something::getValue;        // 이렇게 하면 Something 안에 있는 getValue 라는 함수의 주소를 함수 포인터에 저장 가능.
	int (*fptr2)() = &Something::getValue;                    // 이 경우는 getValue 함수가 static 함수일때 이렇게 함수포인터로 선언할 수 있다.

	Something s1;

	cout << (s1.*fptr)() << endl;                             // 이렇게 사용 가능. s1.getValue() 이렇게 사용한거랑 같음.
	cout << fptr2() << endl;


}


/////////////////////////////////////////////////////////////////////////////////////////////////////

8.12 친구 함수와 클래스 friend

class B;                                    // 전방선언 

class A
{
private:
	int m_value = 1;

	friend void doSomething(A& a, B& b);      // 클래스안에서 함수 친구를 선언해 주면 private 멤버 변수를 doSomething 함수에서 접근가능.
											  // 이때 클래스 A는 클래스 B에 대해서 모르는 상태이기 때문에 class B의 전방선이 필요하다.

	friend class B;                           // 클래스 B의 멤버함수에서 클래스 A의 멤버변수에 접근 허용해주기 위해 쓰임.
};

class B
{
private:
	int m_value = 2;

	friend void doSomething(A& a, B& b);

public:
	void doSomething2(A& a)
	{
		cout << a.m_value << endl;          // 클래스 A 에서 클래스 B 친구선언을 해주었기 때문에 A클래스 멤버변수 접근가능.
	}
};

void doSomething(A& a, B& b)
{
	cout << a.m_value << " " << b.m_value << endl;
}

int main()
{
	A a;
	doSomething(a);

	return 0;
}


/////////////////////////////////////////////////////////////////////////////////////////////////////

8.13 익명객체

class A
{
private:
	int m_value = 1;

public:
	
	void print()
	{
		cout << m_value << endl;
	}
};

int main()
{
	A a;
	a.print();

	A().print();    // 객체를 안만들고 이렇게도 사용가능. 생성자에 파라미터가 잇으면 익명객체 생성불가.

	A(1).print();   // 이 경우는 클래스 A의 멤버변수를 1로 초기화해주고 실행하는 경우, 물론 초기화해주는 생성자가 있어야함.
}

////////

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents) { m_cents = cents; }

	int getCents() const { return m_cents; }

};

Cents add(const Cents& a, const Cents& b)                   //Cents 클래스를 리턴하는 함수. Cents(어쩌고)를 리턴함.
{
	return Cents(a.getCents() + b.getCents())
}


int main()
{
	cout << add(Cents(6), Cents(8)).getCents() << endl;     // add(Cents(6), Cents(8)) = Cents(14) 이기때문에

	cout << Cents(14).getCents() << endl;                   // 이거랑 똑같음.

	return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

8.14 클래스 안에 포함된 자료형


//특정 클래스 안에서만 사용되는 자료형이라면 클래스 밖이 아닌 안에서 선언해주는 것이 좋다.

class Fruit
{
public:
	enum FruitType
	{
		APPLE, BANNA, CHERRY,

	};

	struct A
	{

	};

	class B                     // 이런식으로 inner 타입으로 만드는것도 요즘 많다.
	{

	};
};


/////////////////////////////////////////////////////////////////////////////////////////////////////
9.1 산술 연산자 오버로딩(x + y, x - y, ...)

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents) { m_cents = cents; }
	int getCents() const { return m_cents; }
	
	friend Cents operator + (const Cents& c1, const Cents& c2);  // 이렇게 하면 operator + 함수에서 c1.getCents() 를 c1.m_cents로 쓸수 있음.


	Cents operator + (const Cents& s2)						// 연산자 오버로딩을 클래스 멤버 펑션으로도 구현 가능, ( =, [], (), ->) 이것들은
	//friend Cents operator + (const Cents& c1, const Cents& c2)
	{														// 멤버 펑션으로만 구현이 가능하다고 함.
		return Cents(this->m_cents + c2.m_cents);			//friend를 안붙인 오퍼레이터에서는 파라미터에 객체 2개를 넣으면 객체 너무많다고 컴파일러가 불평
	}														// 그래서 파라미터에 객체 하나 넣고, this를 활용해야함.
};

Cents operator + (const Cents& c1, const Cents& c2)
{
	return Cents(c1.getCents() + c2.getCents());
}

int main()
{
	Cents cents1(6);
	Cents cents2(8);
	Cents cents3(10);


	cout << (cents1 + cents2 + cents3).getCents() << endl;		// cents1 + cents2 먼저하고 그다음 이 값에 + cents3을 함 연쇄적으로.


}


/////////////////////////////////////////////////////////////////////////////////////////////////////

9.2 입출력 연산자 오버로딩 (<< , >>)

class Point
{
private:
	double m_x, m_y, m_z;


public:
	Point(double x = 0.0, double y = 0.0, double z = 0.0)
		:m_x(x), m_y(y), m_z(z)
	{}

	double getX() { return m_x; }
	double getY() { return m_y; }
	double getZ() { return m_z; }

	void print()
	{

	}

	friend std::ostream& operator << (std::ostream& out, const Point& point)		//이거는 외워봐
	{
		out << point.m_x << " " << point.m_y << " " << point.m_z << endl;			// 객체자체를 출력하면 뭐를 출력할지 설정해주는거임.

		return out;			// 이거 써줘야 연쇄적으로 출력가능.
	}

	friend std::istream& operator >> (std::istream& in, Point& point)		//in operator, 입력받는거이기때문에 const 붙이면 안댐
	{
		in >> point.m_x >> point.m_y >> point.m_z;

		return in;			// 이거 써줘야 연쇄적으로 출력가능.
	}

};

int main()
{
	ofstream of("out.txt");				// include <fstream> 해주고 사용,  "out.txt" 라는 파일을 만들어줌.

	Point p1(0.0, 0.1, 0.2), p2(3.4, 1.5, 2.0);

	cout << p1 << " " << p2 << endl;	// 원래는 클래스멤버print() 함수로 출력해야되는데 << 오퍼레이터 쓰면 이렇게 출력가능.
	of << p1 << " " << p2 << endl;		// out.txt 파일에 p1 << " " << p2 << endl; 기록해줌

	of.close();							// main 함수 빠져나가면 알아서 닫아주지만 이렇게 닫아주면 더 좋음.


	cin >> p1 >> p2;

	return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

9.3 단항 연산자 오버로딩  (-x , !x)

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int doubleCents() const { return 2 * m_cents; }

	Cents operator -() const						// 단항 연산자 operator 클래스 안 멤버함수이기 때문에 파라미터 없음.
	{
		return Cents(-m_cents);
	}

	bool operator !() const
	{
		return (m_cents == 0) ? true : false;
	}
};

int main()
{
	Cents s1(5);

	cout << -s1 << endl;				// - 단항연산자 오퍼레이터로 이렇게 출력가능해짐.

	cout << !s1 << endl;				// s1은 5이기때문에 원래는 true 지만 !이 붙어서 false
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

9.4 비교 연산자 오버로딩 ( ==, != , > , >=)

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int doubleCents() const { return 2 * m_cents; }

	friend bool operator ==(const Cents& c1, const Cents& c2)	// == 자리에 != 이것도 넣을 수 있음.
	{
		return c1.m_cents == c2.m_cents;						// 같으면 true를 리턴, 다르면 false를 리턴.
	}

	friend bool operator < (const Cents& c1, const Cents& c2)	// 이때 중요한건 > 이거를 쓰면 에러나고 < 이거를 써야 정상작동.
	{
		return c1.m_cents < c2.m_cents;							// 여기서 > 이걸로 바꾸면 std::sort 할때 반대로 정렬.
	}

};


int main()
{
	Cents cents1(6);
	Cents cents2(0);

	if (cents1 == cents2)
		cout << "Equal" << endl;

	vector<Cents> arr(20);
	for (unsigned i = 0; i < 20; ++i)
		arr[i].getCents() = i;

	std::shuffle(begin(arr), end(arr));

	for (auto& e : arr)
		cout << e << " ";

	std::sort(begin(arr), end(arr));		// < 비교연산자가 없으면 안됨. 사용자 정의 타입인 Cents를 비교할 수 없기 때문.


	return 0;
}


/////////////////////////////////////////////////////////////////////////////////////////////////////

9.5 증감 연산자(++, --)

class Digit
{
private:
	int m_digit;

public:
	Digit(int digit = 0) : m_digit(digit) {}

	//prefix  ++x 
	Digit& operator ++()
	{
		++m_digit;

		return *this;
	}

	//postfix x++
	Digit operator ++(int) // 위에 오퍼레이터와 구분할 수 있게 int 더미형 파라미터 하나 넣어줌.
	{
		Digit temp(m_digit);

		++(*this);			// ++m_digit을 해줌.
		//++m_digit;

		return temp;		// x++ 이거를 출력하면 처음에는 그냥 x 값이 나오고 그다음에 반영이 되기때문에
							// return은 우선 temp로 해준다.
	}
};

/////////////////////////////////////////////////////////////////////////////////////////////////////

9.6 첨자 연산자 오버로딩[]

class IntList
{
private:
	int m_list[10];
public:
	void setItem(int index, int value)
	{
		m_list[index] = value;
	}

	int getItem(int index)
	{
		return m_list[index];
	}

	int& operator[] (const int index)		// 레퍼런스로 리턴하는 이유는 my_list[3] = 5; 이런식으로 할 수 있게 하는것. L-value 리턴
	{
		assert(index >= 0);					//index가 10보다 크면 안되고, 0보다 크거나 같아야 함으로 assert를 써주면 index잘못넣을때,
		assert(index < 10);					// 어디서 에러가 났는지 찾아줌.
		return m_list[index];			
	}

};

int main()
{

	IntList my_list;

	my_list[3] = 10;


	return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

9.7 괄호 연산자 오버로딩() functor

class Accumulator
{
private:
	int m_counter = 0;

public:
	int operator()(int i) { return (m_counter += i); }

};


int main()
{
	Accumulator acc;

	cout << acc(10) << endl;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

9.8 형변환 오버로딩

class Cents
{
private:
	int m_cents;
public:
	Cents(int cents = 0)
	{
		m_cents = cents;
	}

	int getCents() { return m_cents; }
	void setCents(int cents) { m_cents = cents; }

	operator int()					// 형변환 오퍼레이터 Cents 객체를 int 형인 m_cents 로 인식하게끔 만듬.
	{
		return m_cents;
	}
};

void printInt(const int& value)
{
	cout << value << endl;
}

class Dollar
{
private:
	int m_dollars = 0;
public:
	Dollar(const int& input) : m_dollars(input) {}

	operator Cents()						// Dollar 객체를 Cents 형인 m_dollar*100 으로 인식하게끔 만듬.
	{
		return Cents(m_dollars * 100);
	}

};


int main()

{

	Dollar dol(2);				// 얘는 Cents(2*100) 이거랑 똑같음. 오퍼레이터 덕분에.

	Cents cents = dol;

	printInt(cents);			// 형변환 오퍼레이터가 없으면 cents의 데이터 형이 int형인지 구분을 못해줌.
								// 오퍼레이터로 형변환을 해줘야함. 즉 여기서 cents는 int(m_cents) 랑 똑같은거.
}

/////////////////////////////////////////////////////////////////////////////////////////////////////
9.9 복사생성자.


/////////////////////////////////////////////////////////////////////////////////////////////////////

9.10 변환 생성자 explicit, delete

class Fraction
{
private:
	int m_numerator;
	int m_denominator;

public:
	Fraction(char) = delete;		// fraction 객체가 char type을 가지려고 할때 막음.

	explicit Fraction(int num = 0, int den = 1)			// explicit은 파라미터에 Fraction 객체가 들어가는 함수에서 doSomething(Fraction f)
		: m_numerator(num), m_denominator(den)			// doSomething(Fraction 객체) 이렇게 들어가야되는데
	{}													// doSomething(7) 이딴식으로 들어가도 컴파일러가 자동으로 컨버트해주는거를 막아줌.


	
};

/////////////////////////////////////////////////////////////////////////////////////////////////////

9.11 대입연산자 오버로딩, 깊은 복사, 얕은 복사

얕은복사는 포인터 주소만 주는것. 그외 포인터가 가르키고있는 데이터들에 대해서는 복사 하지 않음. 그래서 만약 주소를 갖고있는 애가 여러명인데
이 중 한명이 그 메모리 주소를 삭제해버리면 , 나머지 놈들은 그 주소안에 있는 값에 대해서 접근이 불가능해짐. 

깊은 복사는 포인터 주소는 복사하지 않고 포인터 주소가 가르키는 값만 복사를 해주는것.즉 다른 메모리 주소를 새로 만들고, 값을 그곳에 복사해줌.
이렇게 되면, 복사해간 놈이 그 메모리 주소를 지우던 말던, 기존에 메모리주소는 상관없음.

/////////////////////////////////////////////////////////////////////////////////////////////////////

11.1 상속

class Mother
{
private:
	int m_i;				// private 으로 선언된 멤버 변수는 자식 클래스도 쓸 수 없음. protected 쓰면 자식클래스에게만 허용.

public:

};   

class Child : public Mother
{
	
};

int main()
{
	Mother mother;
	Child son;

	son.getValue()				// 만약에 mother 클래스에도 getValue 가 있으면 자식 클래스로 실행됨. 

}

//////////

만약에 student 와 teacher에 공통되는 m_name이 있으면 이거를 class person으로 따로 만들어서 각 클래스에 상속해줌
근데 자식 클래스의 생성자에서 m_name을 초기화하려하면 안됨.감히 부모클래스의 멤버변수를 자식이 초기화하려들어 ? 이느낌
그래서 생성자에서의 m_name 초기화는 부모클래스가 담당해야되고 자식클래스는 부모클래서의 생성자를 호출해서 초기화하는
간접적인 방법으로 가야됨.

보통 상속을 사용할때는 클래스가 여러개 있는 상태에서 공통된 멤버변수나 공통된 함수가 있을때 공통된 부분들을 부모클래스로 모아서 만들어놓고
추가적인 멤버변수나 함수가 있는 클래스를 자식클래스로 해서, 공통된 부분들을 상속받는것이 좋은 사용방법이다.

class student : public person
{
private:
	//std::string m_name;				// person 부모클래스로 옮겨

public:
	student(const std::string& name_in = "no Name")
		//:m_name(name_in)							//  : 초기화 방식은 부모클래스에서 public으로 풀어놔도 m_name에 접근불가능함.
		:Person(name_in)							// 부모클래스 생성자를 간접적으로 불러오는 형식으로 초기화 가능
													// 그 이유는 student의 객체를 형성할때, 구조상 student의 생성자가 아닌 부모클래스인 person의
													// 생성자를 먼저 실행을 함. 그렇기 때문에 자식클래스에서 먼저 초기화하려고 하면 안됨.
	{
		m_name = "jack jack";						// 반면 함수안에서 초기화해주는거는 가능함. 그 이유는 부모클래스의 생성자가 먼저실행되고
													// 그 후에 함수에 들어오기 때문에 이때는 초기화가 가능한거임. 단 public으로 풀어져있을경우
	}
};

class teacher : public person
{
private:
	//std::string m_name;
};

class person			// person 클래스는 따른 파일에 만들고, stdent , teacher 클래스 파일에서 person 인클루드
{
private:
	std::string m_name;

public:
	person(const std::string& name_in = "no name")
		:m_name(name_in)
	{}
};

// 클래스 A B C 가 있었다고 가정했을때 B는 A클래스를 상속받고 C는 B클래스를 상속받으면 C c; 객체를 형성했을때
// 생성자가 실행되는 순서는 A B C 순으로 생성이 된다. 반면 소멸자는 C B A 순으로 실행이 된다.



sizeof(person)
sizeof(student)					//이때 자식클래스는 부모클래스에게서 상속받아야 하기 때문에 메모리가 더큼
								// person 클래스의 사이즈 + 자식클래서의 사이즈 + 페딩  이렇게 됨.



/////////////////////////////////////////////////////////////////////////////////////////////////////

11.7 상속받은 함수를 오버라이딩 하기.

class Base
{
protected:
	int m_i;

public:
	Base(int value)
		:m_i(value)
	{}

	void print()
	{
		cout << "I'm Base" << endl;
	}
};

class Derived : public Base
{
private:
	double m_d;

public:
	Derived(int value)
		:Base(value)
	{}

	void print()
	{
		//Base::print();				// 이렇게 하면 베이스클래스에 있는 print함수 실행후에 자기 꺼 실행.(이걸 오버라이딩이라고 함)
		cout << "I'm derived" << endl;
		//print()					// 이렇게 하면 재귀함수 발동되버림.
	}
};

int main()
{
	Derived d;
	Base b;

	b.print();			// im base
	d.print();			// im derived 부모클래스와 자식클래스의 함수 이름이 같을때는 자식클래스에서 print하면
						// 자기 함수를 실행함.
}


/////////////////////////////////////////////////////////////////////////////////////////////////////
11.8 상속받은 함수를 감추기

class Base
{
protected:
	int m_i;

public:
	Base(int value)
		:m_i(value)
	{}

	void print()
	{
		cout << "im base" << " " << m_i << endl;
	}
};


class derived : public Base
{
private:
	double m_d;

public:
	derived(int value)
		:Base(value)
	{
		m_i = 5;
	}


	using Base::m_i;				// 자식 클래스 derived의 public: 안에서 이거 써주면 m_i를 public으로 바꿔줌

private:
	using Base::print;				// 이렇게 하면 Base 클래스의 print함수를 private으로 바꿔서, 자식클래스가 사용못함.
									// print 뒤에 () 붙이면 안댐.
	void print() = delete;			// 이렇게 해도 자식클래스에서 print 함수 사용 불가.
};

int main()
{
	derived d(7);
	d.Base::print();

	d.m_i = 1024;			// base 클래스의 m_i 는 protected 이기 때문에 밖에서는 사용 불가.
							// 근데 자식 클래스 안에서는 m_i 사용가능
							// using Base::m_i; 써주면 여기서도 사용 public으로 사용가능

}
/////////////////////////////////////////////////////////////////////////////////////////////////////
11.9 다중 상속


/////////////////////////////////////////////////////////////////////////////////////////////////////
12.1 다형성의 기본 개념		virtual 

# 이개념은 자식 클래스의 객체에 부모 클래스의 포인터를 사용할 때 virtual 키워드를 사용하면 
자식 클래스가 부모클래스를 따르지 않고 마치 자기클래스인 것처럼 실행을 하는 성질.

class Animal
{
protected:
	string m_name;

public:
	Animal(std::string name)
		:m_name(name)
	{}

	string getName() { return m_name; }

	virtual void speak() const
	{
		cout << m_name << " ??? " << endl;
	}
};

class Cat : public Animal
{
public:
	Cat(string name)
		:Animal(name)
	{}

	void speak() const
	{
		cout << m_name << "Meow" << endl;
	}
};


int main()
{
	Cat cat("my cat");

	Animal* ptr_animal = &cat;

	ptr_animal->speak();			// 이렇게 하면 my cat Meow 가 아니라 my cat ??? 이 출력이됨.
									// 즉 Animal 클래스의 포인터에 자식 객체주소를 넣으면 마치 부모클래스 인 것처럼 작동함.

									//이때 Animal 부모 클래스의 speak() 함수 앞에 virtual 을 쓰면 my cat Meow를 출력함.


}


/////////////////////////////////////////////////////////////////////////////////////////////////////

12.2 가상함수와 다형성

class A
{
public:
	virtual void print() { cout << "A" << endl; }
};

class B : public A
{
public:
	void print() { cout << "B" << endl; }
};

class C : public B
{
public:
	void print() { cout << "C" << endl; }
};

int main()
{
	C c;
	B& ref = c;

	c.print();			// C 출력  virtual을 A클래스에 붙이던 B에 붙이던 C에 붙이던 , 오버라이딩된 print() 함수에 virtual 
						// 붙이기만 하면 모두 다형성 성질을 갖게 된다.
}

/////////////////////////////////////////////////////////////////////////////////////////////////////
12.3 override, final, 공변 반환값

class A
{
public:
	virtual void print(int a) { cout << "A" << endl; }
};

class B : public A
{
public:
	void print(short a) override;								// override 라고 붙이기 되면 부모클래스에 있는 함수와 override가 
																// 제대로 override 됬는지 컴파일 타임에서 확인시켜줌.
																// 지금 클래스 B의 print함수의 파라미터가 다르기 때문에 오류발생시킴.
};																// override 말고 final을 붙이면 클래스 B 밑에있는 클래스 함수들은
																// override 하지 못하게 막는다.

void B::print(short a)
{
	cout << "B" << endl;					// 이런식으로 class B에서는 선언만 해주고 정의는 밖에서 해도 됨.
}
									
class C : public B
{
public:
	void print() { cout << "C" << endl; }
};

int main()
{
	C c;
	B& ref = c;

	c.print();			
}
/////////////////////////////////////////////////////////////////////////////////////////////////////

12.4 가상 소멸자

virtual ~A()

base 클래스인 A를

A a;

delete a 해줄 때 자식 클래스까지 소멸자를 실행시켜줌 virtual 안쓰면 부모클래스만 소멸되고 
자식 클래스는 소멸이 되지 않아서 메모리 leak이 발생할 수 있음.

/////////////////////////////////////////////////////////////////////////////////////////////////////
12.5 동적 바인딩과 정적 바인딩

입력받은거를 포인터에 넣고 그 주소를 활용해서 뭔가를 하게 하는게 동적 바인딩.

이 방법은 정적바인딩보다 느리긴 하지만 유연성이 높기 때문에 잘 사용하면 좋음.
/////////////////////////////////////////////////////////////////////////////////////////////////////

12.6 가상 (함수) 표

virtual 키워드를 붙이게 되면 가상 함수 표를 만들게 된다.

부모클래스와 자식 클래스 모두 각자의 클래스에 맞는 가상 함수 표를 만들게 되고, 
가상함수표의 주소인 포인터를 하나 만들게 되고, 함수를 실행할때 포인터에 있는 주소를 따라간다음에
거기에 맞는 함수를 실행시키게 된다. 

그래서 각 클래스의 override 된 함수를 실행시킬때 각 클래스에 맞는 함수를 실행시킬수있게되는것임. 

/////////////////////////////////////////////////////////////////////////////////////////////////////
12.7 순수 가상 함수, 추상 기본 클래스, 인터페이스 클래스

class Animal
{
protected:
	string m_name;

public:
	Animal(std::string name)
		:m_name(name)
	{}

	string getName() { return m_name; }

	virtual void speak() const = 0;		// virtual을 붙이고 함수 바디를 없애버린것을 순수 가상 함수라고 부른다.
										// 이러면 Animal ani; 같은 Animal 객체를 생성할 수가 없게됨.
										// 이렇게 순수 가상 함수를 만드는 뜻은 부모클래스에서는 어떻게 할지 모르겠고, 자식 클래스에서는
										// 꼭 제대로된 override 함수를 구현해라 라는 뜻임. 만약 자식클래스에서 speak() 함수를 구현안하면
										// 컴파일 에러가 떠서 만들라고 강제함.
	
};

class Cat : public Animal
{
public:
	Cat(string name)
		:Animal(name)
	{}

	void speak() const
	{
		cout << m_name << "Meow" << endl;
	}
};


인터페이스 클래스란 부모클래스인데 클래스 안에 순수가상함수밖에 없는 클래스를 말한다. 
즉 자식클래스는 어떤 함수를 구현해야된다라는 정보만 전달하고 있는 인터페이스 클래스이다.

이때 void doSomething(인터페이스 클래스& c) {} 이런 함수를 만들게 되면, 자식 클래스가 많더라도 
일일히 파라미터에 자식클래스 타입을 적지 않고 부모클래스(인터페이스클래스) 레퍼런스만 파라미터로 넣게되면

파라미터에 자식클래스의 객체를 넣어도 , override 함수가 다 구현이 되어있기때문에 편리하게 사용할 수 있다.

///////////////////////////////////////////////////////////////////////////////////////////////////// 

12.8 다이아몬드 상속 문제와 virtual 상속

다이아몬드 상속에서는 . 가장 상위 부모 클래스가 2개가 생길 수 있는 문제가 있다.

이를 막기 위해서는 중간 부모 클래스들이 가장 상위 클래스를 상속할때 앞에 virtual 키워드를 붙이면 문제가 해결된다.
class A
class B : virtual public A 
class C : virtual public A 
class D : public B, public C 

다이아몬드 상속 문제가 안좋은 것만은 아닌 것이  이러한 문제를 활요하는 코드법도 있기 때문에 ,
쓸모가 있을 수도 있다. 

/////////////////////////////////////////////////////////////////////////////////////////////////////
12.9 객체 잘림과 reference wrapper 


int main()
{
	Derived d;
	Base& b = d;			/// 원래는 이렇게 레퍼런스나 , 포인터로 받아줘야 다형성이 형성되는데
	Base b = d;				/// 이렇게 실수로 해버리면, 객체잘림형성이 나타나게 됨.
							/// 자식 클래스는 부모클래스보다 많은 정보를 갖고 있는데 이렇게 하면 
							/// 부모클래스가 자식 클래스의 정보를 다 못담게 됨.  다형성도 무너짐. 
							/// 그리고 다형성이 형성된다고해서 Base 레퍼런스로 형성된 b는 자식 클래스의 멤버변수에 접근못함.
	/////////////
	Derived d;
	Base b;

	std::vector<Base&> my_vec;								// vector는 데이터형에 & 못씀
	std::vector<std::reference_wrapper<Base>> my_vec;		//그래서 이런형태로 써줘야 Base의 레퍼런스 형인 vector를 쓸수있음.

	my_vec.push_back(b);								   
	my_vec.push_back(d);

	for (auto& ele : my_vec)
		ele.get().print();						// reference_wrapper의 get() 함수를 써야 레퍼런스 쓸 수 있음.

	return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////
12.10 동적 형변환

class Base
{
public:
	int m_i = 0;

	virtual void print()
	{
		cout << "im base" << endl;
	}
};

class Derived1 : public Base
{
public:
	int m_j = 1024;

	virtual void print()
	{
		cout << "im derived" << endl;
	}
};

class Derived2 : public Base
{
public:
	string m_name = "Dr. Two";

	virtual void print()
	{
		cout << "im derived2" << endl;
	}
};

int main()
{
	Derived1 d1;
	Base* base = &d1;

	base->m_j;          // base는 Base 포인터이기 때문에 Derived1 의 멤버 변수인 m_j 에 접근불가 

	auto* base_to_d1 = dynamic_cast<Derived1*>(base);        // base를 Derived1* 포인터형으로 동적 형변환.
	base_to_d1->m_j;										 // 이러면 m_j 접근가능

	auto* base_to_d2 = dynamic_cast<Derived2*>(base);        // 이거는 불가능, base자체가 d1의 주소로 시작했기 때문에, Derived2 데이터형으로 못바꿈.
															// 자식끼리는 아무런 관계가 없기 때문. 
															 //다이나믹 캐스트는 형변환에 실패하면 nullptr 값을 넣어버림.
															// 근데 여기서 static_cast를 하면 또 됨. static_cast는 강제로 할 수 있는건 억지로
															// 다 해버리는 느낌. dynamic_cast는 이상하는거는 일단 안하고 에러 띄움.
}


/////////////////////////////////////////////////////////////////////////////////////////////////////

13.1 함수 템플릿 

template<typename T>			// 템플릿은 자료형만 다르고 함수들의 기능들이 동일할때 씀
T getMax(T x, T y)				// typename 자리에 class 써도 되고, T 는 다른 아무이름 붙여도 됨.
{								// 함수 파라미터에 다양한 자료형이 들어올 수 있을때 사용.
	return (x > y) ? x : y;
}

int main()
{
	cout << getMax(1, 2) << endl;
	cout << getMax(3.14, 1.592) << endl;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

13.2 클래스 템플릿

template<typename T>
class MyArray
{
private:
	int m_length;			// 이거는 배열의 길이이므로 int로 고정 T로 바꾸지 않음.
	T	* m_data;			// 이거는 m_data 포인터에 여러가지 자료형의 데이터가 들어갈 수 있으므로 T로 일반화

public:
	MyArray()
	{
		m_length = 0;
		m_data = nullptr;
	}

	MyArray(int length)					// length는 배열 길이이므로 int로 고정
	{
		m_data = new T[length];			// m_data에 여러가지 자료형의 데이터가 들어갈 수 있으므로 T로 일반화
		m_length = length;
	}

	~MyArray()
	{
		reset();
	}

	void reset()
	{
		delete[] m_data;
		m_data = nullptr;
		m_length = 0;
	}

	T& operator[](int index)			// 리턴되서 나가는 값이 m_data의 레퍼런스 이므로  T로 일반화
	{
		assert(index >= 0 && index < m_length);
		return m_data[index];
	}

	int getLength()
	{
		return m_length;
	}

	void print()
	{
		for (int i = 0; i < m_length; ++i)		// 여기서 i는 배열길이의 n번째 요소를 말하는 것이므로 int로 고정.
			cout << m_data[i] << " ";
		cout << endl;
	}
};

template<typename T>							// 만약에 위에 print 함수정의를 다른곳으로 옮겨서 정리하단다고하면
void MyArray<T>::print()						// 이런식으로 밖으로 나오게 되는데, 이때 이 정의가 다른 cpp 파일에 들어가면
{												// main 함수에서 print 함수를 템플릿화 하지 못하게 된다.
	for (int i = 0; i < m_length; ++i)		
		cout << m_data[i] << " ";
	cout << endl;
}

template class MyArray<int>;					// 그때는 이런식으로 정의가 있는 cpp파일에서 직접 데이터자료형을 써줘야한다.
template void MyArray<int>::print()				// print 함수만 템플릿화 해주려면 이렇게 . 보통 위에꺼를 많이씀.

int main()
{
	MyArray<int> my_array(10);				// 템플릿으로 일반화한 클래스는 객체를 생성할때 데이터타입을 정해줘야하니까
											// <int> 이렇게 하면 T가 들어갔던 자리가 모두 int로 바뀌어서 코드 진행.

	for (int i = 0; i < my_array.getLength(); ++i)
	{
		my_array[i] = i * 10;
	}

	my_array.print();
}

/////////////////////////////////////////////////////////////////////////////////////////////////////
13.3 자료형이 아닌 템플릿 매개변수


template<typename T, unsigned int T_SIZE>	
class MyArray
{
private:
	//int m_length;			// 파라미터에 int 형 T_SIZE를 넣어서 이거는 필요없게됨.
	T* m_data;			

public:
	MyArray()
	{
		//m_length = 0;
		m_data = nullptr;
	}

	MyArray(int length)					
	{
		m_data = new T[T_SIZE];			// 
		//m_length = length;
	}

	~MyArray()
	{
		reset();
	}

	void reset()
	{
		delete[] m_data;
		m_data = nullptr;
		//m_length = 0;
	}

	T& operator[](int index)			
	{
		assert(index >= 0 && index < m_length);
		return m_data[index];
	}

	int getLength()
	{
		//return m_length;
		return T_SIZE;
	}

	void print()
	{
		for (int i = 0; i < T_SIZE; ++i)		// 
			cout << m_data[i] << " ";
		cout << endl;
	}
};

int main()
{
	MyArray<int, 100> my_array;				
											

	for (int i = 0; i < my_array.getLength(); ++i)
	{
		my_array[i] = i * 10;
	}

	my_array.print();
}
/////////////////////////////////////////////////////////////////////////////////////////////////////

13.4 함수 템플릿 특수화

template<typename T>
T getMax(T x, T y)
{
	return(x > y) ? x : y;
}

template<>					// char 타입이 들어오는경우 이 함수를 실행하게됨. 함수 특수화
char getMax(char x, char y)
{
	cout << "warnig" << endl;

	return(x > y) ? x : y;
}

int main()
{
	cout << getMax('a', 'b') << endl;		//특수화한 템플릿으로 실행
}

만약 클래스안의 함수를 특수화하고 싶으면

class A
{
public:
	void print()
	{}

};

template<>						// 클래스 밖에다가 함수 템플릿 특수화 정의 따로 해줘야함.
void A<int>::print()			// 클래스가 int형으로 템플릿되서 객체가 형성되면 print()함수를 실행할때 이 함수로 실행.
{}

/////////////////////////////////////////////////////////////////////////////////////////////////////
13.5 클래스 템플릿 특수화 

template<typename T>
class A
{
public:
	void doSomething()
	{
		cout << typeid(T).name() << endl;
	}

	void test()
	{}
};

template<>
class A<char>							// char 타입에 대해서 반응해서 클래스 실행. 거의 새로운 클래스를 만든다고 보면됨.
{
public:
	void doSomething()
	{
		cout << "specialization" << endl;
	}

}

int main()
{
	A<int> i;
	A<double> d;
	A<char> c;

	i.doSomething();			// int
	d.doSomething();			// double
	c.doSomething();			// specialization

	c.test();					// 이때는 특수화된 클래스에 test 함수가 없기 때문에 실행 불가. 
}
/////////////////////////////////////////////////////////////////////////////////////////////////////
13.6 템플릿 부분적으로 특수화

함수 템플릿 같은경우 그냥 따로 특수화 함수 템플릿 만들면되지만

클래스 안에 있는 멤버펑션의 특수화는 클래스자체를 거의 하나 복사하는 형식으로 특수화를 해야되는데
이때 상속을 활용하면 편하게 특수화 할 수 있다.

template<typename T, int size>
class A_base
{
	어쩌고;
	저쩌고;

	void print()
	{}
};

이때 print() 함수만 특수화를 하고 싶으면 원래는 클래스 전체를 새롭게 만들어서 특수화를 해야되는데

template<typename T, int size>
class A : public A_base<T, size>		//A_base를 상속하고 뒤에 <T, size> 붙여줘야 함.
{
};										// 클래스안은 아무것도 구현안해도됨 상속받았으니깐.


template<int size>						// 그리고 이 클래스 A를 특수화하고 print() 함수만 새롭게 짜주면 끝.
class A<char, size> : public A_base<char, size>   // 여기도 마찬가지로 상속 다 써줘야함.
{
	void print()
	{
		새로운 기능
	}
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

13.7 포인터에 대한 템플릿 특수화

template<typename T>
class A
{
private:
	T m_data;
};

template<>
class A<T*>
{
private:
	T* m_data;
};
/////////////////////////////////////////////////////////////////////////////////////////////////////

13.8 템플릿화된 클래스 안에서의 멤버함수를 한번더 템플릿화 하기.

template<typename T>
class A
{
public:
	template<typename TT>
	void print()
	{}
};

/////////////////////////////////////////////////////////////////////////////////////////////////////

15.1 이동의 의미와 스마트 포인터.

스마트 포인터는 메모리가 동적할당되었을때, 자동으로 메모리를 지워주는 역할

이동의 의미는 메모리가 중복으로 지워지는 현상을 막기위해 메모리 소유권을 이전해주는 의미 .

/////////////////////////////////////////////////////////////////////////////////////////////////////

15.2 오른쪽 값 참조 R value reference

int x = 5;
const int cx = 6;

// L-value reference
int& lr1 = x;			//가능
int& lr2 = cx;			//불가능  const는 const로 넣어줘야함.
int& lr3 = 5;			//불가능  5와 같은 r value는 애초에 메모리를 안가지고 있기때문에 레퍼런스 불가능.

const int& lr4 = x;		//가능
const int& lr5 = cx;	//가능
const int& lr6 = 5;		// 이때는 가능 왜냐면 const로 막았기 때문에 딱 5로만 사용을 할 것이라서 

// R-value reference
int&& rr1 = x;			//불가능
int&& rr2 = cx;			//불가능
int&& rr3 = 5;			// 가능 
int&& rrr = getValue()	// 가능

const int&& rr4 = x;	//불가능
const int&& rr5 = cx;	//불가능
const int&& rr6 = 5;	//가능		r-value 레퍼런스는 무조건 메모리없는애들만 저장가능.

void doSomething(int& lref)
{
	cout << "L-value" << endl;
}

void doSomething(int&& ref)			//파라미터를 L-value로 받아오는 것과 , R-value 로 받아오는 것도 다르게 취급. 오버로딩 인정해줌.	
{
	cout << "R-value" << endl;		
}

// R-value를 파라미터로 가져오는 함수는 move가 가능함. 왜냐면 어차피 한번쓰고 말것이기 때문
// 반면 L-value는 move를 하면 나중에 문제가 생길 수 있음.

/////////////////////////////////////////////////////////////////////////////////////////////////////

15.4 std::move 

std::move(res)				// move는 res라는 L-value를 R-value로 리턴해줌. 그러면 R-value가 파라미터로 들어가고
							// 얕은복사를 하게끔 만들어줌. 그리고 res의 값은 nullptr로 바뀜. 그래서 res를 move하고나면
							// res는 더이상 쓸수 없고 옮겨준 쪽에서 작업을 해줘야함

/////////////////////////////////////////////////////////////////////////////////////////////////////
15.5 std::unique_ptr
	이걸 쓰면 동적할당된 메모리를 끝날때 자동으로 지워줌.
	unique_ptr은 메모리에 대한 소유권을 한 놈만 가지고 있을 수 있음. 그래서 unique_ptr로 선언된 놈들은 복사가 안댐.

	int main()
{
	Resource* res = new Resource(1000000);

	std::unique_ptr<int> upi(new int); // 기본 자료형

	//std::unique_ptr<Resource> res = new Resource(1000000);  // 이거는 안댐
	std::unique_ptr<Resource> res(new Resource(1000000));

	//std::unique_ptr<Resource> res1 = std::make_unique<Resource>(5);
	auto res1 = std::make_unique<Resource>(5);				// 이렇게 쓰는거 권장.

	res = res1;										// unique_ptr은 이렇게 assignment 쓰는거 불가능 copy semantics 불가
	res = std::move(res1);							// 이렇게 move semantics 만 가능.

}
/////////////////////////////////////////////////////////////////////////////////////////////////////

15.6 std::shared_ptr
unique_ptr 과는 다르게 shared_ptr은 메모리에 대한 소유권을 여러놈들이 가질 수 있음.
근데 내부적으로 몇놈이 공유하고 있는지 숫자로 세고있고, 마지막 놈까지 소멸될때까지 기다렸다가
마지막 놈도 끝나면 그때 메모리를 지움. 

Resource * res = new Resource(3);			// Resource(3) 하면 요소 3개짜리 배열 만들라는 생성자 있음.
res->setAll(1);								// 모두 1로 초기화, setAll 함수 구현되어있음.
std::shared_ptr<Resource> ptr1(res);

auto ptr1 = std::make_shared<Resource>(3);	//위에 방법보다는 이렇게 하는게 더 나음.
											// 위에 방법은 만약에 shared_ptr<Resource> ptr2(res) 이렇게 하면
											// ptr2와 ptr1이 같은 메모리 주소를 가지고 있다는 거를 모르기때문에
											// 문제가 발생할 수 있다. 메모리를 이미 지웠는데 어떤놈이 소유권가지고 있었으면
											// 그놈은 그 포인터를 사용할 수 없게 되는 문제.

/////////////////////////////////////////////////////////////////////////////////////////////////////

15.7 순환 의존성 문제와 std::weak_ptr

class Person
{
	std::string m_name;
	std::shared_ptr<Person> m_partner;
	//std::weak_ptr<Person> m_partner;  // 순환의존성 문제를 해결하기 위해 만들어진 포인터. 이 포인터는 shared_ptr로 다시 변경후에
										// 사용이 가능하다. m_partner.lock() 을 해줘야 shared_ptr로 변환됨.
};

int main()
{
	auto ptr = std::make_shared<Person>("Lucy");
	auto ptr2 = std::make_shared<Person>("Ricky");

	partnerUp(ptr, ptr2);			// 이 함수는 ptr 객체 안에 ptr2를 갖게 하고 ptr2 객체 안에 ptr을 멤버로 갖게 하는 함수.
}									// 이렇게 되면, 순환 의존성 때문에 서로 ptr, ptr2가 메모리 공유 카운트에 속해져 있어서 
									// 메모리를 제대로 못지우는 문제가 나타남.



/////////////////////////////////////////////////////////////////////////////////////////////////////
16.1 표준 템플릿 라이브러리, 컨테이너 STL, container

컨테이너란 vector, list ,deque 와 같은 배열들을 말하는 것임.

include <vector>
<deque>
vector랑 똑같은데 push_front 기능이 있음
deque<int> deq;

deq.push_back(i)
deq.push_front(i)

< set >
set<string> str_set;

str_set.insert("hello");
str_set.insert("world");
str_set.insert("hello");

insert 기능은 같은 놈이 들어오면 무시해버림, hello 가 또들어오니까 무시.

<map>
map : key / value

std::map<char, int> map;		// char 타입(key)과 int 타입(value)을 맵핑

map['a'] = 10;
map['b'] = 20;

cout << map['a'] << endl;		// 10 출력 

map['a'] = 100;			//  수정도 가능

for (auto& e : map)
	cout << e.first << " " << e.second << " ";   // e.first는 'a' key , e.second는 100 value

std::multimap<char, int> map;

map.insert(std::pair('a', 10));
map.insert(std::pair('a', 100));				// multimap은 하나의 key에 여러 value 넣기 가능

cout << map.count('a') << endl;					// 'a' key에 몇개의 value가 있는지 카운트



<stack>
<queue>



/////////////////////////////////////////////////////////////////////////////////////////////////////

16.2 STL 반복자 iterator

반복자라는거는 컨테이너들의 모든 요소들에 대해서 쭉 훑어보려고 쓰는 것을 말한다. 
이때 vector 든 list 든 deque 든 iterator는 모든 컨테이너에 대해서 호환이 된다.

vector<int> container;
for (int i = 0; i < 10; ++i)
	container.push_back(i);

vector<int>::const_iterator itr;		// const_iterator 말고 그냥 iterator도 됨.
itr = container.begin();

while (itr != container.end())			// itr(container 의 첫번째 요소가 , 마지막 요소가 될때까지 출력 모든 요소 출력.
{
	cout << *itr << " ";

	++itr						
}
cout << endl;	

for (auto& e : container)
	cout << e << " ";

for (auto itr = container.begin(); itr != container.end(); ++itr)
	cout << *itr << " ";

/////////////////////////////////////////////////////////////////////////////////////////////////////

16.3 STL algorithms

vector<int> container;
for (int i = 0; i < 10; ++i)
	container.push_back(i);

auto itr = min_element(container.begin(), container.end());		//제일 작은거 찾아줌 max_element
cout << *itr << endl;

itr = find(container.begin(), container.end(), 3);			//3이 어딨는지 찾아라. 이때 itr은 3이 있는 자리를 가리키게됨.
container.insert(itr, 128);									// 이렇게 하면 3이 있는 자리에 128을 넣게됨. 즉 3번째 요소가 128이되고
															// 4번째 요소가 3이됨

sort(container.begin(), container.end());

reverse(container.begin(), container.end());

/////////////////////////////////////////////////////////////////////////////////////////////////////

19.1 람다함수(익명함수) std::function
//람다는 함수를 따로만들필요없이 함수포인터로 넘겨서 바로 기능할 수 있게 해줌.

auto func = [](const int& i) -> void {cout << "hello, world" << endl;}

[](const int& i) -> void {cout << "Hello, World" << endl;}(1234);			// 익명 함수.	->void 이거는 리턴타입

{
	string name = "jack jack";
	[&name]() {cout << name << endl;} ();		// name을 익명함수 바디안에서 사용가능 [&] 이렇게 써도됨.
}

vector<int> v;
v.push_back(1);
v.push_back(2);

auto func2 = [](int val) {cout << val << endl;}		// 리턴타입이 void 인 경우에 ->void 생략 가능.
for_each(v.begin(), v.end(), func2);			 //vector v의 요소를 모두 출력하는 익명함수.

for_each(v.begin(), v.end(), [](int val) {cout << val << endl;});  // 보통 이렇게 씀.


std::function<void(int)> func3 = func2;		// 파라미터에 int 형이 들어가는 리턴타입이 void인 함수의 포인터 func3 는 func2 이다.
func3(123);


class Object
{
public:
	void hello(const string& s)
	{
		cout << "hello" << s << endl;
	}
};
int main()
{
	Object instance;
	auto f = std::bind(&Object::hello, &instance, std::placeholders::_1);

	auto f2 = [&instance](const string& a) {instance.hello(a);};    // f는 f2랑 똑같은 말임.

	f("World");
}
/////////////////////////////////////////////////////////////////////////////////////////////////////
19.2 여러개의 리턴값 반환하기 

#include <tuple>

//auto my_func()						// auto를 쓰면 알아서 리턴값 여러개 반환가능
tuple<int, int> my_func()
{
	return tuple<int, int>(123, 456);
	// return tuple(123,456);			// 중간에 자료형 없어도 됨.
}

int main()
{
	tuple<int, int> result = my_func();
	//auto result = my_func();				// 받을때도 auto로 받기
	cout << get<0>(result) << " " << get<1>(result) << endl;

	auto [a, b] = my_func();				// auto로 변수선언하면서 받기.
	cout << a << b << endl;

}

/////////////////////////////////////////////////////////////////////////////////////////////////////
19.3 std::thread 멀티쓰레딩 기초

cout << std::thread::hardware_concurrency() << endl;			// 코어 몇개인지 알려줌
cout << std::this_thread::get_id() << endl;						// 지금 실행되고 있는 함수의 쓰레드 아이디

int main()
{
	const int num_pro = std::thread::hardware_concurrency();


	std::thread t1 = std::thread([]() {							//main() 함수의 쓰레드가 실행중인 상태에서 새로운 쓰레드 등장.
		cout << std::this_thread::get_id() << endl;				//이때 main() 함수는 다른 쓰레드 코드를 실행시키고 그냥 끝나버림.
		while (true) {}});									//새로운 쓰레드 t1가 끝나기도 전에 main함수가 끝나면 안되기때문에

	std::thread t2 = std::thread([]() {
		cout << std::this_thread::get_id() << endl;
		while (true) {}});

	t1.join();												//t1.join() 을 해줘야 메인함수가 t1이 끝날때까지 기다려줌.
	t2.join();
															// std::thread()   () 안에는 함수포인터나 함수를 넣어주면 되고, 함수에
															// 파라미터가 있으면 (함수, 파라미터에 들어갈 값) 이렇게 해주면 됨.
	
	//////////
	

	vector<std::thread> my_threads;							// vector로 쓰레드개수를 동적할당.
	my_threads.resize(num_pro);

	for (auto& e : my_threads)
		e = std::thread([]() {
		cout << std::this_thread::get_id() << endl;
		while (true) {}});

	for (auto& e : my_threads)
		e.join();

	//////////

#include <mutex>

	mutex mtx;

	auto work_func = [](const string& name) 
	{
		for (int i = 0; i < 5; ++i)
		{
			std::this_thread::sleep_for(std::chrono::milliseconds(100));

			mtx.lock();							// 여기서 lock을 걸면 밑에 있는 코드를 실행할때 다른 쓰레드가 밑에코드실행못하게
												// 막아버림.
			//std::lock_guard lock(mtx);		// 이거는 unlock을 해줄 필요없이 이것만 써주면 됨.
			//std::scoped_lock lock(mtx);		// 이게 lock_guard 보다 더 좋다고함. 여기 {} 범위를 벗어나면 자동으로 unlock
												// 그래서 범위가 넓은 , 즉 코드실행이 많은 쪽 영역에서 lock을 걸면 속도가 현저히 느려짐.
			cout << name << " " << std::this_thread::get_id() << "is working" << i << endl;
			mtx.unlock();						// 다시 풀어주면  다음 쓰레드가 코드 실행, 
		}
	}

	std::thread t1 = std::thread(work_func, "jackjack");   // 
	std::thread t2 = std::thread(work_func, "dash");

	t1.join();
	t2.join();


}


/////////////////////////////////////////////////////////////////////////////////////////////////////
19.4 레이스 컨디션, std::atomic, 


레이스 컨디션이란 , 쓰레딩과정에서 한 쓰레드가 작업중에 다른 쓰레드가 끼어들게 될때 나타나는 문제를 말한다.
#include <atomic>

int main()
{
	int shared_memory(0);
	//atomic<int> shared_memory(0);

	auto count_func = [&]()
	{
		for (int i = 0; i < 1000; ++i)
		{
			this_thread::sleep_for(chrono::milliseconds(1));

			shared_memory++;
		}
	};

	std::thread t1 = thread(count_func);		
	std::thread t2 = thread(count_func);

	t1.join();
	t2.join();							// 이렇게 하면 원래 2000이 나와야되는데 그거보다 작은값이 나와버림
										// 그 이유는 한 쓰레드가 shared_memory 값을 가져오고, 그 값에 ++를 하고,
										// 다시 그값을 shared_memory 값에 저장하는 3단계 동안 다른 쓰레드가 중간에
										// 껴버리는 현상이 있기 때문.
										// atomic은 이 3단계 과정을 하나로 묶어주는 역할을 함. 그래서 쓰레드끼리 중간에
										// 끼지가 않음.
										// 대신 무분별하게 쓰면 속도가 느려짐.

}

/////////////////////////////////////////////////////////////////////////////////////////////////////

19.5 작업 기반 비동기 프로그래밍  async, future, promise 

int main()
{
	int result;
	std::thread t([&] {result = 1 + 2;});
	t.join();
	cout << result << endl;
}
{	//std::future<int> fut = ...
	auto fut = std::async([] {return 1 + 2;});			// thread 보다 async를 더 좋아함. 차이는 async는 리턴을 사용, thread를 업그레이드 시킨
	cout << fut.get() << endl;							// get()은 위에 쓰레드가 작업을 다 마치고 리턴값을 줄때까지 기다림.	
														// 그리고 무조건 auto fut 이걸로 받아줘야함. 안받아주면 쓰레드 효과 사라짐.
}
{
	std::promise<int> prom;
	auto fut = prom.get_future();

	auto t = std::thread([](std::promise<int>&& prom)
	{
		prom.set_value(1 + 2);							// prom 값을 여기서 정해줌.
	}, std::move(prom));								// move로 prom을 R-value로 바꿔준거를 파라미터값으로 넣어줌.

	cout << fut.get() << endl;
	t.join();
}

/////////////////////////////////////////////////////////////////////////////////////////////////////
19.6 멀티쓰레딩 예제(벡터 내적)  // 다시봐야됨. 예제 적어가면서 구체적으로

내적이란

vector<int> v0{ 1,2,3 };
vector<int> v1{ 4,5,6 };

내적 = (1 * 4) + (2 * 5) + (3 * 6);

cout << "std::inner_product" << endl;
{
	const auto sta = chrono::steady_clock::now();

	const auto sum = std::inner_product(v0.begin(), v0.end(), v1.begin(), 0ull);	//벡터 v0과 v1의 내적 구하기.

	const std::chrono::duration<double> dur = std::chrono::steady_clock::now() - sta;  // 계산에 걸린 시간.

	cout << dur.count() << endl;
	cout << sum << endl;
	
}


std::transform_reduce(std::execution::par, v0.begin(), v0.end(), v1.begin, 0ull);			//병렬
//std::transform_reduce(std::execution::seq, v0.begin(), v0.end(), v1.begin, 0ull);			//직렬처리



/////////////////////////////////////////////////////////////////////////////////////////////////////
19.7 완벽한 전달과 std::forward

struct Mystruct
{};

void func(Mystruct& s)
{
	cout << "pass by L-ref" << endl;
}

void func(Mystruct&& s)
{
	cout << "pass by R-ref" << endl;
}

template<typename T>
void func_wrapper(T t)
{
	func(t);
}


int main()
{
	Mystruct s;

	func(s);				// L-value로 
	func(Mystruct());		// R-value로

	func_wrapper(s);			//템플릿화 된 함수는 파라미터에 값이 들어올때 L,R value 구분을 못하게 됨. 그냥 L-value로 들어감.
	func_wrapper(Mystruct());

}

template<typename T>
void func_wrapper(T&& t)			// 파라미터는 && 이걸로 받야야함.
{
	func(std::forward<T>(t));		//forward의 역할은 L-value로 들어온거는 L-value로 R-value로 들어온건 R-value로 리턴.
}

/// <summary>
/// ////////////
/// </summary>

class Customvector
{
public:
	unsigned n_data = 0;
	int* ptr = nullptr;

	Customvector(const unsigned& _n_data, const int& _init = 0)
	{
		cout << "Constructor" << endl;

		init(_n_data, _init);
	}

	Customvector(Customvector& l_input)
	{
		cout << "Copy constructor" << endl;

		init(l_input.n_data);

		for (unsigned i = 0; i < n_data; ++i)
			ptr[i] = l_input.ptr[i];
	}

	Customvector(Customvector&& r_input)
	{
		cout << "Move constructor" << endl;

		n_data = r_input.n_data;
		ptr = r_input.ptr;

		r_input.n_data = 0;
		r_input.ptr = nullptr;
	}

	~Customvector()
	{
		delete[] ptr;
	}

	void init(const unsigned& _n_data, const int& _init = 0)
	{
		n_data = _n_data;
		ptr = new int[n_data];
		for (unsigned i = 0; i < n_data; ++i)
			ptr[i] = _init;
	}
};

void doSomething(Customvector& vec)
{
	cout << "Pass by L-reference" << endl;
	Customvector new_vec(vec);
}

void doSomething(Customvector&& vec)
{
	cout << "Pass by R-reference" << endl;
	Customvector new_vec(std::move(vec));		// 파라미터가 && 으로 들어온다하더라도 여기에서 std::move를 써서 R-value 화 해줘야함.
}

int main()
{
	Customvector my_vec(10, 1024);

	Customvector temp(my_vec);					// copy constructor, l-value
	Customvector temp(std::move(my_vec));		// move constructor, r-value

	cout << my_vec.n_data << endl;				

	doSomething(my_vec);
	doSomething(Customvector(10, 8));			
}

/////////////////////////////////////////////////////////////////////////////////////////////////////
19.8 자료형 추론 auto, decltype

https://modoocode.com/294

class Examples
{
public:

	void ex1()
	{
		std::vector<int> vect;
		for (std::vector<int>::iterator itr = vect.begin(); itr != vect.end(); ++itr)
			cout << *itr;
		for (auto itr = vect.begin(); itr != vect.end(); itr++)
			cout << *itr;
		for (auto itr : vect)
			cout << itr;
	}

	void ex2()
	{
		int x = int();
		auto auto_x = x;				// auto_x  는 int 형
		const int& crx = x;				
		auto auto_crx1 = crx;			// auto_crx1 은 int형, crx는 분명 const int& 형인데 int형으로 나오는 이유는 auto는
										// 앞에 const와 & 를 모두 빼고 판단함.
		const auto& auto_crx2 = crx;	// 그래서 선언할때 아예 이렇게 선언해야 const int& 형으로 됨.

		volatile int vx = 1024;			//volatile은 값이 자주바뀌기 때문에 최적화할때 빼달라는 뜻
		auto avx = vx;
		volatile auto vavx = vx;
	}

	template<class T>
	void func_ex3(T arg)				// 여기서 파라미터를 (const T& arg) 이렇게 해야지 밑에 함수에 있는 crx 데이터형으로 들어감.
	{}

	void ex3()
	{
		const int& crx = 123;

		func_ex3(crx);				// crx를 넣으면 데이터형이 그냥 int형으로 들어감
	}

	void ex4()
	{
		const int c = 0;
		auto& rc = c;				//레퍼런스로 가져올때는 위에 그대로 가져옴 const int 형으로 
									// 왜냐면 레퍼런스 자체가 c의 별명을 만드는것이기 때문에 데이터형도 같아야함
									// 반대로 레퍼런스를 빼면 아예 메모리주소가 다른 변수를 하나 더 만드는 것이기 때문에
									// 그냥 int 형으로 가져올 것임.		
	}

	void ex5()
	{
		int i = 42;
		auto&& ri_1 = i;			// 이 경우에는 i가 R-value 이기때문에 auto가 알아서 바꿔서 ri_1을 l-value로 만듬
		auto&& ri_2 = 42;			// 42는 r-value 이기때문에 그대로 ri_2는 r-value가 됨.
	}

	void ex6()
	{
		int x = 42;
		const int* p1 = &x;
		auto p2 = p1;			// p2는 const int* 형, 
		//*p2 = 43				//error
	}

	template<typename T, typename S>
	void func_ex7(T lhs, S rhs)
	{
		auto prod1 = lhs * rhs;					// 그냥 auto로 선언하는방법 

		typedef decltype(lhs* rhs) product_type;		// 이런식으로 typedef decltype으로 데이터형을 직접 만드는법

		product_type prod2 = lhs * rhs;

		decltype(lhs * rhs) prod3 = lhs * rhs;			// typedef 안하고 그냥 이렇게 선언해도 됨.
	}

	template<typename T, typename S>
	auto func_ex8(T lhs, S rhs) -> decltype(lhs* rhs)	// return 타입은 모르니까 auto로 설정.
	{
		return lhs * rhs;
	}

	struct S
	{
		int m_x;

		S()
		{
			m_x = 42;
		}
	};

	void ex9()
	{
		int x;
		const int cx = 42;
		const int& crx = x;
		const S* p = new S();

		auto a = x;
		auto b = cx;
		auto c = crx;
		auto d = p;				//포인터이기때문에 d는 const S* 형
		auto e = p->m_x;		// e는 그냥 int 형

		typedef decltype(x) x_type;
		typedef decltype(cx) cx_type;
		typedef decltype(crx) crx_type;
		typedef decltype(p->m_x) m_x_type;						// 그냥 int형

		typedef decltype((x)) x_with_parens_type;				//()를 붙이면 & 레퍼런스 형으로 바꿔서 가져옴.
		typedef decltype((cx)) cx_with_parens_type;
		typedef decltype((crx)) crx_with_parens_type;
		typedef decltype((p->m_x)) m_w_with_parens_type;		//얘는 const int& 형으로 가져옴 const가 추가됨.

	}

	const S foo()
	{
		return S();
	}

	const int& foobar()
	{
		return 123;
	}

	void ex10()
	{
		std::vector<int> vect = { 42, 43 };

		auto a = foo();							// a는 S 형
		typedef decltype(foo())	foo_type;		// foo_type은 const S 형

		auto b = foobar();						// int 형
		typedef decltype(foobar())	foobar_type;	// const int& 형

		auto itr = vect.begin();				// itr은 std::vector<int> 형
		typedef decltype(vect.begin()) iterator_type;

		auto first_element = vect[0];			// int 형
		decltype(vect[1]) second_element = vect[1];  // int& 형 , 왜냐면 vect[1] 이런게 리턴타입이 int& 형이기 때문에
	}

	void ex11()
	{
		int x = 0;
		int y = 0;
		const int cx = 42;
		const int cy = 43;
		double d1 = 3.14;
		double d2 = 2.72;

		typedef decltype(x* y) prod_xy_type;			//int 형
		auto a = x * y;									// int

		typedef decltype(cx*cy) prod_cxcy_type;			//int 형 곱셈한거는 r-value이기 때문에 int형으로
		auto b = cx * cy;								// int

		typedef decltype(d1 < d2 ? d1 : d2) cond_type;	// decltype 삼항연산자에서 2개 데이터형이 같으면 &가 붙어서 나옴. double &
		auto c = d1 < d2 ? d1 : d2;						// 여기는 그냥 double
		
		typedef decltype(x < d2 ? x : d2) cond_type_mixed;	// int double 섞여있을때는 double로  여기는 & 안붙네
		auto d = x < d2 ? x : d2;							// double
	}

};

generic lambda

원래 함수 파라미터로 auto가 못들어가는데 람다는 들어갈 수 있음.

/////////////////////////////////////////////////////////////////////////////////////////////////////
20.1 프로파일링 하기 

디버그 > 창 > 진단도구 

로컬 windows 디버거 모드 클릭

cpu profile 클릭 

어떤 함수가 cpu를 많이 쓰고있는지 퍼센티지로 나옴

exe PID 누르면 자세한 분석창 나옴.

이때 called function 누르면 제일 많이 쓰는놈 빨간색으로 표시해서 보여줌

메모리 분석. 
memory uasge에서 스냅샷 누르면 allocation, heap size 이렇게 나오는데 이거는 한줄한줄 실행할때마다의 차이를 보여줌
allocation은 메모리 공간이 몇개 추가됬냐, heap size는 메모리크기가 얼마나 증가하고 감소했냐.



릴리즈 모드 분석.

디버그 > 성능 프로파일러(performance profiler) >  performance wizard > cpu sampling > one or more available projects



/////////////////////////////////////////////////////////////////////////////////////////////////////
20.2 git 사용법

git cmd 

dir - 현재 위치에 존재하는 모든 것들 보여줌
explorer . - 현재위치의 탐색기 열어줌
cd 폴더이름 - 입력한 폴더로 들어감. 폴더이름 조금쓰고 tab 누르면 자동완성 

유저네임 등록
git config --global user.name "내 github 닉네임"

만약 여러개의 닉네임을 쓸거고 교체하고 싶으면 자격 증명 관리자로 들어가서 windows 자격증명에서 githumb 제거 후 다시 등록

git에 있는 코드를 내 컴퓨터로 복사하기

git clone 깃주소 

git add 파일이름.  // 새로운 파일을 만들었으면 git에 파일 추가하기
git status 
git commit -m "my commit message"	//commit 제목
git push							// 진짜 git에 업데이트하기 
git pull							// git에 업데이트된 내용 내 컴퓨터에 업데이트하기

git commit 파일이름 -m "커밋내용"	// 내컴퓨터에서 내용수정했으면 다시 git에 업데이트하기
git push 

git rm 파일이름 
git commit -m "커밋내용"
git putc							// 파일 지우고 git에 업데이트하기
/////////////////////////////////////////////////////////////////////////////////////////////////////
20.3 visual studio에서 깃헙 사용하기 



/////////////////////////////////////////////////////////////////////////////////////////////////////
20.4 Vcpkg 설치 

vcpkg 폴더에 들어가서 vcpkg.exe install	라이브러리이름(boost:x64-windows)
/////////////////////////////////////////////////////////////////////////////////////////////////////

20.5 TCP IP 네트워킹 

#include "include.h"


//Server 

using namespace std;
using boost::asio::ip::tcp;

int main()
{
	try
	{
		boost::asio::io_service io_service;

		tcp::endpoint endpoint(tcp::v4(), 13);				// tcp 버전 4, port 넘버 13 (채널?) endpoint는 통신할때의 맨끝?
		tcp::acceptor acceptor(io_service, endpoint);		// endpoint 연결해서 받음.

		cout << "Server started" << endl;

		for (;;)	 // while(true)
		{
			const std::string message_to_send = "hello from server";

			boost::asio::ip::tcp::iostream stream;

			cout << "check 1" << endl;

			boost::system::error_code ec;
			acceptor.accept(*stream.rdbuf(), ec);

			cout << "check 2" << endl;

			if (!ec)
			{
				//receive message from client
				std::string line;
				std::getline(stream, line);
				cout << line << endl;

				//send message to client
				stream << message_to_send;
				stream << endl;					// send std::endl to end getline of client


			}
		}
	}
	catch (std::exception& e)
	{
		std::cerr << e.what() << endl;
	}

	return 0;
}


//Client 

using namespace std;
using boost::asio::ip::tcp;

int main(int argc, char* argv[])			//client 프로젝트 설정들어가서 , 디버깅 > command argument 에 통신할 컴퓨터의 ip 적기
{											// 127.0.0.1  내컴퓨터
	try
	{
		if (argc != 2)						// ip를 적으면 main 파라미터에 ip 들어가고 , ip가 없으면 예외 발생.
		{
			std::cerr << "usage : client <host>" << std::endl;
			return 1;
		}

		tcp::iostream stream(argv[1], std::to_string(int(13)));			//ip 적으면 argv[1] 여기에 주소 들어옴.
		if (!stream)						// stream이 안만들어지면 예외 발생.
		{
			std::cout << "unable to connect" << stream.error().message() << std::endl;
			return 1;
		}

		//send message to server
		stream << "hello from client";
		stream << std::endl;			// 전화 끊는거라고 생각하면됨. 상대방이 getline으로 받고있기때문에 endl 하면 stream 끊김.

		//receive message from server
		std::string line;
		std::getline(stream, line);
		cout << line << endl;
	}

	catch (std::exception& e)
	{
		cout << "exception: " << e.what() << endl;
	}

	return 0;
}



/////////////////////////////////////////////////////////////////////////////////////////////////////
0. std::future, std::promise, std::async

https://modoocode.com/284#page-heading-0

#include "include.h"


using std::string;

void worker(std::promise<string>* p) {
	// 약속을 이행하는 모습. 해당 결과는 future 에 들어간다.
	p->set_value("some data");
	//set_value 함수는 promise 객체안에 있는 future 객체에게 데이터 set
}
int main() {
	std::promise<string> p;
	//promise 객체는 future 객체를 멤버로 가지고 있음.

	// 미래에 string 데이터를 돌려 주겠다는 약속.
	std::future<string> data = p.get_future();
	//get_future 함수는 promise 객체 안에 있는 future 객체를 불러오는 함수

	std::thread t(worker, &p);

	// 미래에 약속된 데이터를 받을 때 까지 기다린다.
	data.wait();

	// wait 이 리턴했다는 뜻이 future 에 데이터가 준비되었다는 의미.
	// 참고로 wait 없이 그냥 get 해도 wait 한 것과 같다.
	std::cout << "받은 데이터 : " << data.get() << std::endl;
	//future 에서 get 을 호출하면, 설정된 객체가 이동 됩니다. 따라서 절대로 get 을 두 번 호출하면 안됩니다.

	t.join();
}
/////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////