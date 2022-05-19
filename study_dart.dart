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


	final vs const 
	final String name4 = 'hihi';
	const Stirng name3 = 'hhhhh';
	final name5 = 'hhiiii';       //final과 const는 데이터타입 선언안해도 var 기능을 수행해줌.

	final DateTime now = DateTime.now();
	const DateTime now2 = DateTime.now();    
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
	required int x,				//named parameter 설정
	required int y,
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

	set firstMember(String name){		//set은 현대에와서 거의 안씀 왜냐면 클래스 변수자체를 final로 설정하기때문에 set의 의미가 없음.
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

