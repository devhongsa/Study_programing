#pragma once


그 외 및 복습.


std::vector<int> a;						// int형으로 이루어진 동적배열을 a 변수에 담겠다.
std::initializer_list<something> a;		// something 형으로 (자료형이든, 구조체든, 클래스든) 이루어진 list를 a 변수에 담겠다.

std::ref(v0);
std::reference_wrapper<v0의 type> v0;   // 이거랑 위랑 똑같은말. std::ref(v0)이 어떤 함수에 파라미터로 들어갈때는
										// v0의 값을 함수안에서 바꾸고 싶을때 쓴다. 그냥 v0을 집어넣으면 , 복사가 되기때문에
										// 메모리 낭비가 심해지고 실제 v0의 값이 바뀌지도 않음.


std::unordered_map<char, int> a;		// map이랑 똑같은 key: value; 근데 찾는게 더 빠르대, 중복된 데이터 허용 안함.

//class 안에 static 함수를 선언하는 이유는 밖에서 객체를 생성안하고 Something::static함수 이렇게 쓸수있기 때문에.

std::find vs std::find_if
std::find(범위시작, 범위 끝, 찾을값)		// find는 예를들어 벡터안에 찾을값이 존재하면 그 위치를 리턴하고 없으면 마지막값 리턴
std::find_if(범위시작, 범위 끝, 조건함수)	// find_if는 벡터안에 요소를 조건함수(bool 함수)에 넣어서 true 를 리턴하는 요소 위치를 찾음.


typedef double distance_t;  // double 이라는 자료형을 distance_t 라고도 쓸수있게 함.
using distance_t = double;  // 같은 얘기임. using을 쓰는 방법도 있다.

/////////
int student_scores[20] = { 1,2,3,4,5 };

int*& ref = student_scores;					// 배열은 포인터라고해서 바로 레퍼런스 선언할수없음
int* ptr = student_scores;					// 포인터 변수를 만들어 준다음에 

int*& ref = ptr;							// 레퍼런스 만들어줄수 있음.

void printArray(int my_array[])				// 이거는 printArray(int *my_array) 이거랑 같음.
cout << *(ptr + 1) << endl;  //  이렇게 하면 2 가 나옴, my_array[1] 값 

int* ptr = new int(7);		// int 사이즈의 메모리를 하나 할당해주세요의 뜻임. 역참조하면 7 나옴. new를 쓰면 주소를 주기때문에 포인터로 값을 받아야함
int* my_array = new int[length]();     // new로 메모리를 동적 할당 받는 경우에는 주소를 받기 때문에 *array 포인터로 받아야함.
										// () 이거는 모든 값을 0으로 초기화 해주겠다는 뜻.
										// {11, 22, 33,44 } 이렇게 하면 차례로 값을 넣어준뒤 나머지는 0으로 초기화

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

int& ref = 3;			// 레퍼런스 선언할때 상수값으로 초기화 불가능
const int& ref = 3;		// const 붙여주면 가능하긴함.


int(*fcnptr)(int) = func;  // 함수포인터를 선언하는 방법.  func 파라미터의 자료형이 int니까  (*fcnptr)(int) 이렇게 넣어줘야함
								// const int 면 const int 넣어줘야함.
cout << fcnptr(1) << endl;		//fcnptr(1) == func(1) 

typedef bool(*fcnptr_t)(int);  //이런식으로 줄일 수 있음.파라미터로 쓸때 fcnptr_t fcnptr 이렇게 쓰면됨.
using fcnptr_t = bool(*)(int);  //bool 자료형의 함수포인터 선언을 요약해준 것이 fcnptr_t 이다.
#include <functional> 
std::function<bool(int)>;		//마찬가지로 std::function<bool(int)> = fcnptr_t 이거랑 같음



/////////////

7.16 생략부호 ellipsis

double findAverage(int count, ...)    //필요하면 검색해서 다시 공부.


//const int& getDay()     이렇게 하면 복사하지 않고 레퍼런스를 가져오기때문에 메모리 사용 덜함.
int getDay()
{
	return m_day;
}

////////////////////////////////////////////////////
void doSomething()
{
	static int a = 1;     /// static으로 변수 선언을 하면 같은 메모리 주소를 계속 쓰기 때문에 함수밖으로 나갔다와도 a =1로 초기화 안함.
	++a;
	cout << a << endl;
}

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

//////////////////////////////////////
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

//////////////////////////////////////////

9.2 입출력 연산자 오버로딩(<< , >> )

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


클래스 멤버 함수 뒤에 const.
{
	요약하자면 const가 뒤에 붙은 함수에는 2가지 기능이 존재한다.

		객체 내부 변수 변경 불가.
		const 함수만 호출 가능.
		이러한 기능을 가지고 있어 getter나 bool 반환값에서 많이 사용되며 이로 인해 함수 내부의 변수 변경을 방지 할 수 있다.
}


/////////////////////////////////////////////////////////////////

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
	Cat cat("my cat")

		Animal* ptr_animal = &cat;

	ptr_animal->speak();			// 이렇게 하면 my cat Meow 가 아니라 my cat ??? 이 출력이됨.
									// 즉 Animal 클래스의 포인터에 자식 객체주소를 넣으면 마치 부모클래스 인 것처럼 작동함.

									//이때 Animal 부모 클래스의 speak() 함수 앞에 virtual 을 쓰면 my cat Meow를 출력함.
}

12.4 가상 소멸자

virtual ~A()

base 클래스인 A를

A a;

delete a 해줄 때 자식 클래스까지 소멸자를 실행시켜줌 virtual 안쓰면 부모클래스만 소멸되고
자식 클래스는 소멸이 되지 않아서 메모리 leak이 발생할 수 있음.


virtual void speak() const = 0;		// virtual을 붙이고 함수 바디를 없애버린것을 순수 가상 함수라고 부른다.
										// 이러면 Animal ani; 같은 Animal 객체를 생성할 수가 없게됨.
										// 이렇게 순수 가상 함수를 만드는 뜻은 부모클래스에서는 어떻게 할지 모르겠고, 자식 클래스에서는
										// 꼭 제대로된 override 함수를 구현해라 라는 뜻임. 만약 자식클래스에서 speak() 함수를 구현안하면
										// 컴파일 에러가 떠서 만들라고 강제함.

인터페이스 클래스란 부모클래스인데 클래스 안에 순수가상함수밖에 없는 클래스를 말한다.
즉 자식클래스는 어떤 함수를 구현해야된다라는 정보만 전달하고 있는 인터페이스 클래스이다.

이때 void doSomething(인터페이스 클래스& c) {} 이런 함수를 만들게 되면, 자식 클래스가 많더라도
일일히 파라미터에 자식클래스 타입을 적지 않고 부모클래스(인터페이스클래스) 레퍼런스만 파라미터로 넣게되면

파라미터에 자식클래스의 객체를 넣어도, override 함수가 다 구현이 되어있기때문에 편리하게 사용할 수 있다.


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
/////////////////////////////////////////////////////
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

////////////////////////////////////////////////////////
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

/// <summary>
/// ////////////////////////////////////////////////
/// </summary>
auto func2 = [](int val) {cout << val << endl;}		// 리턴타입이 void 인 경우에 ->void 생략 가능.
for_each(v.begin(), v.end(), func2);			 //vector v의 요소를 모두 출력하는 익명함수.

for_each(v.begin(), v.end(), [](int val) {cout << val << endl;});  // 보통 이렇게 씀.




main함수 파라미터
https://m.blog.naver.com/sharonichoya/220501242693
//// main(int argc, char* argv[])     argc는 메인함수에 들어갈 정보 갯수, argv는 실행경로가 들어가있음.


emplace_back 
https://shaeod.tistory.com/630

reinterpret_cast 
https://hwan-shell.tistory.com/219


isObject()    // json key들중에서 중괄호 value를 가지고 있으면 isObject

for 문에서 continue 만나면 다음 타임으로 바로 넘어감.


컨테이너.join("\n")  // 줄바꿈을 하는 이유는 통신을 위해서, join은 컨테이너 요소 마다 중간중간 뭘 넣겠다는 의미.

std::transform
https://modoocode.com/275

///////////////////////////////////////////////////////
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


//////////////////////////

signal, slot , connect 
https://hydroponicglass.tistory.com/265