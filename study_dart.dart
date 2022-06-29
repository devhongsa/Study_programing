//main 함수는 코드를 실행시키면 자동으로 가장 먼저 실행되는 함수임.
void main() {				
	print('hello code factory');
	var name = 'hongsa';
	print(name);

	name = 'flutter';

	int num = 10;
	double num2 = 2.5;
	bool isTrue = true;
	String name2 = 'hi';

	print('${name}')    //스트링안에 변수쓰는거 가능.

	//var는 모든 데이터타입을 아우를수 있지만, 웬만하면 데이터타입을 정확하게 명시해서 변수선언해주는 것이 좋음.
	//데이터타입이 아주 복잡할 경우에 var 를 씀.


	dynamic vs var 
	// dynamic으로 선언하면 나중에 변수의 데이터타입을 변경할 수 있지만 var은 변경이 불가능함.


	String? name = 'hongsa';
	// ?를 붙여주면 변수에 null값을 넣어줄 수 있음.

  //파이널, 컨스트 
	final vs const 
	final String name4 = 'hihi';
	const Stirng name3 = 'hhhhh';
	final name5 = 'hhiiii';       //final과 const는 데이터타입 선언안해도 var 기능을 수행해줌.

	final DateTime now = DateTime.now();      //O
	const DateTime now2 = DateTime.now();    //X
	// 런타임때 값이 결정되는 경우에는 const를 쓸수가 없다. const는 빌드타임때 값이 결정되어 있어야함.



	num ++;    // 1더하기 
	num --:

	num ??= 3.0;   //만약 num이 null값이면 3.0으로 바꿔라 

	print(num is int);  // true 리턴
	print(num is! int); // false 리턴


	List<String> blackPink = ['제니', '지수'];
	blackPink[0];
	blackPink.length;
	blackPink.add('로제');
	blackPink.remove('로제');
	blackPink.indexOf('로제');

	Map<String, Stirng> dict = {
	'Harry' : '해리포터'
	}

	dict.addAll({
		'Spiderman' : '스파이더맨'
	})

	dict['Spiderman']
	dict['Hulk'] = '헐크';
	dict.remove('Harry');
	dict.keys;
	dict.values;

	final Set<String> names = {
		'hi',
		'hello0',
		'hi'
	}
	//set은 중복값 없애주는 list 
	names.contains('hi')  //true 리턴



	int number = 2;

	if(number % 2 == 0){
		print('짝수입니다.')
	}else{
		print('홀수입니다.')
	}


	switch(number % 3){
		case 0:
			print('나머지가 0입니다.');
			break;
		
		case 1:
			print('나머지가 1입니다.');
			break;

		default:
			print('나머지가 2입니다.');
			break;
	}


	List<int> numbers = [1,2,3,4,5]
	int total = 0;

	for(int i = 0; i < 10; i++){
		print(i);
	}

	for(int i=0; i<numbers.length; i++){
		total += numbers[i];
	}

	for(int number in numbers){
		total += number;
	}

	While(total<10){
		total += 1;
	}


	enum Status{
		approved,
		pending,
		rejected,
	}

	Status status = Status.pending;
	if(status == Status.approved){
		print('승인입니다.');
	}

}

int addNumbers(int x, [int y=0, int z=0]){
	print('함수실행');
	return x+y+z;
}
//함수 파라미터에 []이거를 써주면, 함수실행할때 []안에 있는 파라미터를 안보내줘도 실행이 됨.
//만약 []안에 있는 변수에 디폴트값을 안써주면, 에러가남. null값때문에 

int addNumbers({
	required int x,				//named parameter 설정, 나중에 함수 실행할때 파라미터 순서를 바꿔도 되는 방법.
	required int y,       //required를 쓸때는 {}로 감싸줘야함.
	int z=30,
}) => x+y+z;				//arrow 펑션

addNumbers(x:10,y:20,z:30) //named parameter는 이런식으로 명시를 해주고 실행을해줘야함. 파라미터 순서가 상관이 없음.

typedef Operation = int Function(int x, int y, int z); 
int add(int x, int y, int z) => x+y+z;
int subtract(int x, int y, int z) => x-y-z;
int calculate(int x, int y, int z, Operation operation){
	return operation(x,y,z);
}

int result = calculate(4,5,6, subtract);  //이런식으로 typedef 사용 


//class _Idol				//클래스, 함수, 변수이름 앞에 _ 를 넣으면 private으로 선언한다는 뜻, 이 클래스가 선언된 dart파일외에 외부에서 Idol 클래스를 사용하지못함.
class Idol {
	final String name;					//final로 선언을 해줘서 한번 객체를 생성하면 바꾸지 못하게 만드는 것이 버그방지에 좋음.
	final List<String> members;

	Idol(Stirng name, List<String> members): this.name = name, this.members = members;   //생성자
	const Idol(this.name, this.members)   // 위에 생성자랑 똑같은 뜻.

	void sayHello(){
		print('hi we are ${this.name}');
	}

	void introduce(){
		print('hihihihihihihihihi we are ${this.members}');
	}

	String get firstMember{
		return this.members[0];
	}

	set firstMember(String name){		//set은 현대에와서 거의 안씀 왜냐면 클래스 변수자체를 대부분 final로 설정하기때문에 set의 의미가 없음.
		this.members[0] = name;
	}
}

void main(){
	Idol blackPink = new const Idol('블랙핑크', ['지수','로제']);    //new를 안넣어줘도 됨.
	Idol blackPink2 = new const Idol('블랙핑크', ['지수','로제']);   //const로 객체를 생성했을때 만약 내용이 모두 똑같다면 blackPink = blackPink2 임.
	// const로 생성안한다면 다른 blackPink != blackPink2 임.

	blackPink.firstMember;
	blackPink.firstMember = 'hongsa'
}
////////////////////////////////////////////////////////////////////
///상속

void main(){
	Idol apink = new Idol(name: '에이핑크', membersCount: 5);

	apink.sayName();
	apink.sayMembersCount();

  BoyGroup bts = BoyGroup('BTS', 7);
  bts.sayName();
}

class Idol{
	String name;
	int membersCount;

	Idol({
		required this.name,
		required this.membersCount,
	});

	void sayName(){
		print('저는 ${this.name}입니다.')
	}

	void sayMembersCount(){
		print('${this.name}은 ${this.membersCount}명의 멤버가 있습니다.')
	}
	
}

class BoyGroup extends Idol{
  BoyGroup(
    String name,
    int membersCount,
  ): super(        //super는 부모클래스를 말하는것임.
    name: name,     // name:name 이렇게 하는 이유는 Idol 부모클래스의 생성자에서 required로 선언됐기때문
    membersCount: membersCount    //이뜻은 BoyGroup으로 객체를 생성하면 부모클래스의 생성자를 실행시키게 됨. 부모클래스 객체변수 설정
  );                              //이렇게 되면 자식클래스에서 부모클래스 함수를 호출하면 BoyGroup의 name과 membersCount 변수사용가능

  void sayMale(){     //자식클래스에서 따로 만든 함수는 부모클래스에서 사용할 수 없다.
    print('저는 남자 아이돌입니다.');
  }
}


////////////////////////////////////////////////////////////////////
//override
void main() {
  TimesTwo tt = TimesTwo(2);
}
// method =  function (class안에있는 펑션)
// override - 덮어쓰다 (우선시하다)


class TimesTwo{
  final int number;

  TimesTwo(
    this.number,
  );

  int calculate(){
    //return number * 2;   만일 class안에 number라는 변수가 이거 하나뿐이라면 this 생략가능. 함수안에 number라는 변수 없을시
    return this.number * 2;
  }
}

class TimesFour extends TimesTwo{
  TimesFour(
    int number
  ) : super(number);

  @override
  int calculate(){
    return super.number * 4;
    //return this.number * 4;
    //return number * 4;      두가지 경우 다 문제없긴 함.
    //return super.calculate() * 2 
  }
}

////////////////////////////////////////////////////////////////////
//static 
void main(){
  Employee seulgi = Employee('슬기');
  Employee chorong = Employee('초롱');

  Employee.building = '오투타워';
  Employee.printBuilding(); 

  //seulgi.building;      이렇게는 안됨 인스턴스는 static으로 선언된 변수나 함수에 접근할 수 없음.

}

class Employee {
  // static은 instance에 귀속되지 않고 class에 귀속된다.
  // instance라는거는 이 class로 만들어진 새로운 객체를 말하는거임.
  static String? building;

  final String name;

  Employee(
    this.name,
  );

  void printName(){
    print('제 이름은 $name 입니다.');
  }

  static void printBuilding(){
    print('저는 $building 건물에서 근무합니다.');
  }
}

////////////////////////////////////////////////////////////////////
//interface : 인터페이스의 목적은 어떤 클래스를 만들때 인터페이스 클래스의 변수, 속성을 강제하기 위함이다. 이렇게 만들어라
void main(){

}

abstract class IdolInterface{     //abstract는 인터페이스 클래스를 실수로 인스턴스화하는걸 방지해줌.
  String name;

  IdolInterface(this.name);

  void sayName(){}      //상세하게 구현안해줘도 됨. 인터페이스 클래스는 클래스 양식만 써놓은거라고 보면됨 
}
//interface class를 하나 만들어준다.

class BoyGroup implements IdolInterface{
  String name;

  BoyGroup(this.name);

  void sayName(){
    print('제 이름은 $name 입니다.')
  }
}
//BoyGroup은 IdolInterface라는 class를 인터페이스로 설정하면, IdolInterface클래스에 구성된 변수, 함수, 생성자를 BoyGroup에서도 선언을 해줘야한다.

////////////////////////////////////////////////////////////////////
// generic : 타입을 외부에서 받을때 사용
void main(){
  Lecture<String, String> lecture1 = Lecture('123'. 'lecture1');
  lecture1.printIdType();   //String

  Lecture<int, String> lecture2 = Lecture(123, 'lecture2');
  lecture2.printIdType();   //int
}

class Lecture<T, X>{
  final T id;
  final X name;

  Lecture(this.id, this.name);

  void printIdType(){
    print(id.runtimeType);
  }
}

////////////////////////////////////////////////////////////////////
void main(){
  List<String> blackPink = ['로제', '지수', '리사', '제니', '제니'];

  print(blackPink);
  print(blackPink.asMap());
  print(blackPink.toSet());

  Map blackPinkMap = blackPink.asMap();

  print(blackPinkMap.keys.toList());
  print(blackPinkMap.values.toList());

  Set blackPinkSet = Set.from(blackPink);   //중복값 삭제해주기 

  print(blackPinkSet.toList());

  ////

  final newBlackPink = blackPink.map((x){       //x에 blackPink 요소가 차례대로 들어옴.
    return '블랙핑크 $x';
  })

  final newBlackPink = blackPink.map((x) => '블랙핑크 $x');   // 똑같은 의미
  
  print(newBlackPink);      //(블랙핑크 로제, 블랙핑크 지수, ..)  iterable 형태로 리턴 .toList()로 형변환 해야됨.

  ////
  String number = '13579';

  final parsed = number.split('').map((x)=>'$x.jpg').toList();

  print(parsed)  // [1.jpg, 3.jpg, ...]

  ////
  Map<String, String> harryPotter = {
    'Harry' : '해리포터',
    'Ron' : '론 위즐리'
  };

  final result = harryPotter.map((key, value)=> MapEntry(
    'character $key',
    '캐릭터 $value'
  ));

  print(result);    // {character Harry : 캐릭터 해리포터, ...}

  final keys = harryPotter.keys.map((x)=> 'HPC $x').toList();

  ////
  List<Map<String, String>> people = [
    {
      'name' : '로제',
      'group' : '블랙핑크'
    },
    {
      'name' : '지수',
      'group' : '블랙핑크'
    },
    {
      'name' : 'RM',
      'group' : 'BTS'
    },
    {
      'name' : '뷔',
      'group' : 'BTS'
    },
  ];

  final blackPink = people.where((x)=> x['group'] == '블랙핑크');

  print(blackPink);     //({name : 로제, group: 블랙핑크},{name:지수, group: 블랙핑크})

  ////
  List<int> numbers = [1,3,5,7,9];

  final result = numbers.reduce((prev,next) => prev + next);
  //1+3, 4+5, 9+7, 16+9
  print(result)   //25 
  // reduce는 list의 데이터타입과 같은 타입만 리턴하기때문에 다른 데이터타입을 리턴하려고 하면 에러가남.

  List<String> words = [
    '안녕하세요',
    '저는',
    '코드팩토리입니다.'
  ];

  final count = words.fold<int>(''.length,(prev,next)=> prev.length + next.length);
  // fold는 reduce와 달리 다른 데이터타입을 리턴할 수 있음. 

  ////
  List<int> even = [1,2,3,4];
  List<int> odd = [5,6,7,8];

  print([...even,...odd]);   //...은 리스트안에 요소를 다 풀겠다는 뜻.
}

////////////////////////////////////////////////////////////////////
void main(){
  List<Map<String, String>> people = [
    {
      'name' : '로제',
      'group' : '블랙핑크'
    },
    {
      'name' : '지수',
      'group' : '블랙핑크'
    },
    {
      'name' : 'RM',
      'group' : 'BTS'
    },
    {
      'name' : '뷔',
      'group' : 'BTS'
    },
  ];

  final parsedPeople = people.map((x) =>
  Person(
    name: x['name']!,
    group: x['group']!
  )).toList();

  for(Person person in ParsedPeople){
    print(person.name);
    print(person.group);
  }
  // 이렇게 하면 Person person = Person(name:지수, group:블랙핑크) 이렇게 되는건가?

  final bts = parsedPeople.where((x)=>x.group == 'BTS');
  print(bts);   // (Person(name:RM, group:BTS), ...)
}


class Person {
  final String name;
  final String group; 

  Person({
    required this.name,
    required this.group,
  });

  @override 
  String toString(){
    return 'Person(name:$name, group:$group)';
  }
}

////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
///async 

void main(){
  //Future - 미래에 받아올 값
  Future<String> name = Future.value('코드팩토리');
  Future<int> number = Future.value(1);
  Future<bool> isTrue = Future.value(true);

  print('함수 시작')

  //delayed 
  //1번 파라미터 : 지연할 기간 Duration
  //2번 파라미터 : 지연 시간이 지난 후 실행할 함수
  Future.delayed(Duration(seconds:2), (){
    print('Delay 끝');
  });


  /////
  addNumbers(1,1);
  addNumbers(2,2);

  addNumbers2(1,1);
  addNumbers2(2,2);
  //이 두가지 경우는 코드진행순서가 다름.
}

void addNumbers(int number1, int number2){
  print('계산 시작 : $number1 + $number2');

  Future.delayed(Duration(seconds:2),(){
    print('계산 완료 : $number1 + $number2 = ${number1 + number2}');
  });
  //2초동안 기다리는 것이아닌 다음 코드를 실행하러 넘어감. 2초후에 다시 돌아와서 실행시킴.

  print('함수 완료');
}

void addNumbers2(int number1, int number2) async {
  print('계산 시작 : $number1 + $number2');

  await Future.delayed(Duration(seconds:2),(){
    print('계산 완료 : $number1 + $number2 = ${number1 + number2}');
  });
  //2초동안 기다리는 것이아닌 다음 코드를 실행하러 넘어감. 2초후에 다시 돌아와서 실행시킴.

  print('함수 완료');
}



//////////////////////////////////////////////////////////////////////////
void main() async{
  //Future - 미래에 받아올 값
  Future<String> name = Future.value('코드팩토리');
  Future<int> number = Future.value(1);
  Future<bool> isTrue = Future.value(true);

  await addNumbers(1,1);          //이러면 첫번째 await 함수가 다 끝날때까지 기다렸다가 다음 코드 실행.
  await addNumbers(2,2);

}

//await를 쓰려면 리턴값이 Future이여야 하기때문에 Future<void>로 함수선언.
Future<void> addNumbers(int number1, int number2) async {
  print('계산 시작 : $number1 + $number2');

  await Future.delayed(Duration(seconds:2),(){
    print('계산 완료 : $number1 + $number2 = ${number1 + number2}');
  });
  //2초동안 기다리는 것이아닌 다음 코드를 실행하러 넘어감. 2초후에 다시 돌아와서 실행시킴.

  print('함수 완료');
}


//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
///// stream 

import 'dart:async';

void main(){
  final controller = StreamController();
  final stream = controller.stream;

  final streamListener1 = stream.listen((val){
    print('Listener1 : $val');
  });

  controller.sink.add(1);
}



void main(){
  final controller = StreamController();
  final stream = controller.stream.asBroadcastStream();       //여러 listener가 있을때 asBroadcastStream 사용 

  final streamListener1 = stream.where((val)=>val % 2 == 0).listen((val){
    print('Listener1 : $val');
  });

  final streamListener2 = stream.where((val)=>val % 2 == 1).listen((val){
    print('Listener2 : $val');
  });

  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);

}
//////////////////////////////////////////////////////////////////////////

import 'dart:async';

void main(){
  calculate(1).listen((val){
    print('calculate(1) : $val');
  })

  calculate(4).listen((val){
    print('calculate(4) : $val');
  })

  playAllStream().listen((val){
    print(val);
  });

}

Stream<int> playAllStream()async*{
  yield* calculate(1);            //yield* 이면 calculate가 모든 값을 리턴할때까지 기다림.
  yield* calculate(1000);
}

Stream<int> calculate(int number) async* {
  for(int i =0; i < 5; i++){
    yield i * number;
    await Future.delayed(Duration(seconds:1));
  }
}

////////////////////////////////////////////////
DateTime? 

DateTime now = DateTime.now();
now.year;
now.month;
now.day;
now.hour;
now.minutes;
now.seconds;
now.milliseconds;

Duration?

Duration duration = Duration(seconds: 60);

duration.inDays;     // 0
duration.inHours;
duration.inMinutes;  // 1
duration.inSeconds   // 60
duration.inMilliseconds 

DateTime specificDay = DateTime(2017, 11, 23);   
final difference = now.difference(specificDay)  // now - specifiDay  Duration 반환
now.isAfter(specificDay)    // 특정날짜보다 나우가 이후 날짜인지 true
now.isBefore()

now.add(Duration(hours:10));   //  날짜연산
now.subtract(Duration(seconds: 20))