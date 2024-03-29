https://developer.mozilla.org/en-US/docs/Web/JavaScript




//연산
nums = [-1,2,6,7,4,23]
Math.max(1,-1,3,5,6)
Math.max(...nums)
Math.min(1,-1) 
Math.abs()
Math.pow(3,2);     //제곱   혹은 3**2
Math.round(10.6);  //반올림
Math.ceil(10.2);   //올림
Math.floor(10.5);  //내림
Math.sqrt(9);      //제곱근
Math.random();     // 0~1 범위 랜덤 숫자
3.1235.toFixed(3)  // 반올림
3.12314.toPrecision(4)

// ...? 
const [head, ...rest] = [1,2,3]    // head => 1 , rest => [2,3]
let jsonData = {'key' : 'value'}
let jsonData2 = {'key' : 'value2'}

function foo(head, ...rest){
    console.log(head)   // 1 
    console.log(rest)   // [2,3,4]
}

{jsonData, ...jsonData2}   => {'key' : 'value2'}    // key값이 중복되면 마지막에 넣었던 ...jsonData2 값으로 대체됨. 

% 
&&  //and
||  //or


typeof 1
typeof "abc"

"abc".length  //문자열 길이


//undefined vs null 
//undefined은 변수가 생성은 되어있는데 아직 초기화가 안된것을 말함.
//null은 변수도 있고 안에 값이 있는데 그 값이 '아무것도 없음'임 


//데이터 형변환
parseInt('13');
parseInt('assdf');  // NaN 
parseFloat('avc');
Number('abced')     //float이나 int로 형변환 해줌 
Number.toString()
String(number)

isNaN('string');   //true 
isNaN(15);          //false 

== vs ===
=== : //datatype 까지 고려한 연산자. 이걸 사용해라.
alert(undefined == null);  //true
alert(undefined === null); //false

undefined 는 undefined 라는 데이터타입;
null 도 null이라는 데이터타입;

alert(NaN === NaN); //false




//prompt

prompt("당신의 이름은?")     /// C++ 에서 std::cin >> x 


//document.write

document.write("coding everybody <br>")

//for문

for(var i = 0; i < 1000; i++){
    document.write("coding everybody" +i+"<br>")        // 숫자랑 스트링 같이 출력가능
}

end: for(var i = 0; i < 1000; i++){
    document.write("coding everybody" +i+"<br>")        // 숫자랑 스트링 같이 출력가능

    break end;      //이거는 보통 다중 for문에서 한방에 모든 for문을 끝내고 싶을때 사용한다.
}

lst = [1,2,3,4]
for(item in lst){
    console.log(item);          // for in 구문은 item이 인덱스값이다.  for of 로 하면 item은  lst의 요소값이다. 
}


//함수 function

function numbering(){
    document.write(1);
}

numbering();

function get_argument(arg, arg2){
    return arg + arg2;
}

alert(get_argument(1,"min"));

//다른 함수정의
const numbering = function(){
    document.write(1);  
}
//arrow 펑션
const arrowfunc = (x,y) => x+y;

//익명함수 
(function(){
    document.write(1);
})();  

const func = function(){
    console.log(arguments[0] + arguments[1]);
}
func(1,2)    //함수에 파라미터를 지정하지않아도 arguments라는 키워드를 통해 넘긴 값을 불러올수있음  

//재귀함수 
//자기가 자기를 호출하는 함수, 조건문을 통해 재귀를 멈추는 코드 필요 

//callback 함수 
function add(x,y){
    return x+y;
}
function calculator(callback, x, y){
    return callback(x,y);
}

//배열 array 리스트, list
var member = ['egoing', 'k8805', 'sorialgi'];

member.push('f');           // 배열 맨뒤에 추가

li = member.concat(['e','f']);  //배열과 배열 합치기

member.unshift('z');  // 배열 맨앞에 넣기

member.splice(1)        //member 요소 1부터 쭉 긁어서 리스트 리턴, 기존 member도 짤려있음 
member.splice(1,1)      // 요소 1만 가져옴 
member.splice(1, 0, 'd');  //1번 인덱스에 'd' 추가 기존 1에 있던 값은 뒤로 밀림.
member.splice(1,1,'x','y'); // 1번 인덱스부터 x ,y 추가 기존 1에 있던 값은 삭제됨.

member.slice(1)         // 요소1부터 쭉 출력 
member.slice(1,3)       // 요소 1부터 2까지 출력 

member.shift();   // 맨앞에 있는 요소 제거
member.pop();       //member의 맨뒤에 요소 제거되고, 맨뒤에 요소 리턴 
member.sort();      //요소 정렬
member.reverse();   //요소 역정렬

member.sort(function);  // 내가 정의한 정렬기준으로 정렬할 수 있음. 생활코딩 javascript 사전에서 참고
member.join(',')  //각요소 사이사이마다 , 포함되서 스트링으로 리턴 


//객체(object)  파이선에서는 딕셔너리

var grades = {'egoing':10, 'k88': 6, 'sori' : 8};
const gradesTwo = {egoing : 10, k88 : 6, sori : "gi"};
//object를 const로 설정해도 객체안의 값을 변경할 수 있음. 안되는건 gradesTwo 변수를 객체가 아닌 다른 타입으로 바꾸는게 안댐. gradesTwo = true;

grades['egoing'];  // 10 
grades.egoing;      // 10 

var grades = {};
gradeds['egoing'] = 10;


for (var key in grades){
    document.write("key :" + key + "value :" + grades[key] + "<br/>");
    document.write("<li>key :" + key + "value :" + grades[key] + "</li>");   // 리스트로 보여주기 
}

//객체 지향 프로그래밍
var grades = {
    'list' : {'egoing' : 10, 'k88' : 8, 'sori' : 6},
    'show' : function(){
        alert('hello world');           // value에 함수도 들어갈수 있음.
    }
}

var grades = {
    'list' : {'egoing' : 10, 'k88' : 8, 'sori' : 6},
    'show' : function(){
        for(var name in this.list){
            console.log(name, this.list[name]);         //여기서 this라는 것은 이 펑션을 소유한 객체를 말함.즉 grades
        }
    }
}

grades['show']();    // 함수 실행
grades.show();      


// 모듈화 
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <script src="greeting.js"></script>        //파이선으로 치면 import 기능.
  <title>Document</title>
</head>
<body>
    <script>
        alert(welcome());               //greeting 파일안에있는 welcome 함수 실행
    </script>
  
</body>
</html>


//node.js의 모듈화
//javascript 강의 모듈파트에서 참고  https://opentutorials.org/course/743/4750

//라이브러리 사용법
라이브러리 코드 받고, html 저장되어있는 디렉토리로 가서 js파일만들고 코드복사.
<head> 부분에 <script type="text/javascript" src ="jquery.js"></script> 이런식으로 import.
</head>


//정규표현식  (필요한 정보를 추출,test,치환 하는 방법)
var pattern = /a/;
var pattern = new RegExp('a');

pattern.exec('abcde');   // a가 담긴 배열 리턴.
'abcde'.match(pattern);  // a 리턴
'abcde'.replace(pattern, 'A');  // a를 A로 치환

var pattern = /a./;
pattern.exec('abcde');  // ab가 담긴 배열리턴 
pattern.exec('bcde');   // null 리턴

pattern.test('abcde');  // true 리턴
pattern.test('bcde');   // false 리턴

//옵션(i,g)

var xi = /a/;
'Abcde'.match(xi);      //null 리턴

var oi = /a/i;          // i는 대소문자 구분을 안하고 찾게만듬.
'Abcde'.match(oi);      // A 리턴

var xg = /a/;
'abcdea'.match(xg);      // ["a"]  리턴

var og = /a/g;           //중복으로 다 찾아줌
'abcdea'.match(og);      // ["a","a"] 리턴

var ig = /a/ig;         // 대소문자구분안하고, 중복되는 것도 다 찾아줌.

//캡쳐

var pattern = /(\w+)\s(\w+)/;     // () : 그룹화 , w : (A~Z, a~z, 0~9) 의 문자, + : 2개이상 , s : 공백
var str = "coding everybody";
var result = str.replace(patter, "$2, $1")
console.log(result);     // everybody, coding

//자세한 정규표현식 수업은 생활코딩 강좌 참고  https://opentutorials.org/course/909/5142


// 중괄호 범위 ***
javascript 에서는 함수안에서의 변수선언만이 지역변수로 생성된다.

for (i in range){
    var name = "name";
}

C++ 에서는 for문의 중괄화 안에 선언된 name이 중괄호 밖에서는 사용될 수 없지만.
javascript 에서는 사용가능하다. 즉 함수안에서 선언된 변수만이 지역변수로 인정된다.

//
var i = 5;

function a(){
    var i = 10;
    b();
}

function b(){
    document.write(i);
}

a();            // 이경우에는 5를 출력하게된다. 즉 함수가 사용될때가아닌 함수가 정의될때의 전역변수를 찾기때문.


// 함수2
function cal(func, num){     // javascript에서는 함수도 값으로 인식하기때문에, 함수의 파라미터로 함수가 들어갈수있음.
    return func(num);       // C++ 같은 경우에 함수 파라미터로 함수가 들어가려면 함수포인터로 넣어줘야함
}

//리턴값으로 함수사용
function cal(mode){
    var funcs = {
        'plus' : function(left, right){return left + right},
        'minus' : function(left, right){return left - right}
    }
    return funcs[mode];
}
alert(cal('plus')(2,1));
alert(cal('minus')(2,1));

// 배열에 함수
var process = {
    function(input){return input + 10;},
    function(input){return input * input;},
    function(input){return input / 2;}
}

var input = 1;
for (var i = 0; i < process.length; i++){
    input = process[i](input);
}
alert(input);

//콜백함수 활용
function sortNumber(a,b){
    // 위의 예제와 비교해서 a와 b의 순서를 바꾸면 정렬순서가 반대가 된다.
    return b-a;
}
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
alert(numbers.sort(sortNumber)); // array, [20,10,9,8,7,6,5,4,3,2,1]

//ajax (asynchronous javascript and Xml)
//ajax란 웹페이지에서 어떤 버튼을 눌렀을때 새로운 웹페이지를 다운받아 새로운 url로 가는 것이아닌, 기존 url에서 
//웹서버와 웹페이지가 내부적으로 비동기적으로 통신하면서, 새로운 정보를 불러와주는 기술을 말한다.
<!DOCTYPE html>
<html>
<head>
<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
</head>
<body>
<script type="text/javascript">
    $.get('./datasource.json.js', function(result){         //여기 $.get는 jquery가 제공하는 특수한 객체기능. datasource.json.js 안에 있는 정보를가져와서
        console.log(result);                                // 콜백함수의 result로 인자를 전달해줌.
    }, 'json');
</script>
</body>
</html>

//클로저 closure 내부함수 외부함수
자바스크립트는 함수안에 함수를 정의할 수 있음
함수안에서 정의된 함수를 내부함수라고하고, 내부함수를 감싸고 있는 함수를 외부함수라고 한다.
//ex1
function outter(){
    var title = 'coding everybody';
    return function(){
        alert(title);
    }
}
inner = outter();
inner();

//ex2
function and(x){
    return function print(y){
        return x + ' and ' + y
    }
}

const saltAnd = and('salt')      //saltAnd 는 내부함수 and함수는 외부함수 
console.log(saltAnd('pepper'))  // salt and pepper 


// private variable 
function factory_movie(title){
    return {
        get_title : function (){
            return title;
        },
        set_title : function(_title){
            title = _title
        }
    }
}
ghost = factory_movie('Ghost in the shell');
matrix = factory_movie('Matrix');
 
alert(ghost.get_title());
alert(matrix.get_title());
 
ghost.set_title('공각기동대');    //title이라는 변수는 set_title, get_title을 통해서만 접근가능하게됨. private

alert(ghost.get_title());
alert(matrix.get_title());


//클로저 응용
var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(id) {
        return function(){
            return id;
        }
    }(i);
}
for(var index in arr) {
    console.log(arr[index]());
}

/* 결과
0
1
2
3
4
*/


//argument
//자바스크립트는 함수에 파라미터가 없어도, 함수를 호출할때 인자를 넣어도 오류를 안일으킴.
function sum(){
    var i, _sum = 0;    
    for(i = 0; i < arguments.length; i++){
        document.write(i+' : '+arguments[i]+'<br />');
        _sum += arguments[i];
    }   
    return _sum;
}
document.write('result : ' + sum(1,2,3,4));     // 1,2,3,4는 arguments라는 특수한 배열변수로 들어가게됨


//
function zero(){
    console.log(
        'zero.length', zero.length,
        'arguments', arguments.length
    );
}
function one(arg1){
    console.log(
        'one.length', one.length,
        'arguments', arguments.length
    );
}
function two(arg1, arg2){
    console.log(
        'two.length', two.length,
        'arguments', arguments.length
    );
}
zero(); // zero.length 0 arguments 0 
one('val1', 'val2');  // one.length 1 arguments 2       //만약 누군가 함수를 의도대로 쓰지 않았다면 이 구별법을 통해 에러를 발생시키는것이 가능
two('val1');  // two.length 2 arguments 1


//apply
o1 = {val1:1, val2:2, val3:3}
o2 = {v1:10, v2:50, v3:100, v4:25}
function sum(){
    var _sum = 0;
    for(var name in this){
        _sum += this[name];
    }
    return _sum;
}
alert(sum.apply(o1)) // 6               //this를 o1으로 적용
alert(sum.apply(o2)) // 185


//객체지향 

var person = {};        //객체생성
person.name = 'egoing'  // 여기서 name은 속성(property)
person.introduce = function(){
    return 'My name is' + this.name;        //여기서 introduce는 메소드. 객체가 가지고있는 변수는 프로퍼티, 함수는 메소드라고 부른다.
}

//생성자와 new
//자바스크립트에는 클래스의 개념이 없기때문에, 함수안에서 this를 활용해서 생성자를 만들어야한다.

function Person(){}
var p0 = persen();          // p0을 호출하면 undefined
var p = new Person();       // p를 호출하면 {} 리턴. 즉 new를 통해 객체를 형성        
p.name = 'egoing';
p.introduce = function(){
    return 'My name is '+this.name; 
}
document.write(p.introduce());

//
function Person(name){
    this.name = name;                   // 함수안에서 this를 통해 생성자를 만들어주면, 함수밖에서 객체내용을 일일히 계속 만들필요가 없어짐.
    this.introduce = function(){
        return 'My name is '+this.name; 
    }   
}
var p1 = new Person('egoing');
document.write(p1.introduce()+"<br />");
 
var p2 = new Person('leezche');
document.write(p2.introduce());

new.target // new를 써서 객체를 형성했는지 확인

// 전역객체
function func(){
    alert('hello?')
}

func();
window.func();  // func함수도 사실 window라는 객체의 메소드였음.

//this?

function func(){
    if(window === this){
        document.write("window === this");
    }
}

func(); // window === this

var o = {
    func : function(){
        if (o === this){
            document.write("o === this");
        }
    }
}

o.func(); //o === this    

/// 즉 메소드 함수안에있는 this는 그 메소드 함수가 소속되어있는 객체를 말한다.

var funcThis = null;
function Func(){
    funcThis = this;
}

var o2 = new Func();    // o2라는 객체에 Func()가 메소드로 들어감. funcThis === o2


function sum(x,y){return x+y;};
var sum2 = new Function('x','y','return x+y;');
sum2(1,2)       // 3

var a = {};
var a2 = new Object;

var a = [1,2,3];
var a2 = new Array(1,2,3);

//apply와 this
var o = {}
var p = {}
function func(){
    switch(this){
        case o:
            document.write('o<br />');
            break;
        case p:
            document.write('p<br />');
            break;
        case window:
            document.write('window<br />');
            break;          
    }
}
func();             //'window'
func.apply(o);      // o
func.apply(p);      // p

//상속  tree라고 생각하면 됨. prototype이라는거는 Person이라는 객체안에 다른 객체(함수든 변수든) 넣는것을 말함.
function Person(name){
    this.name = name;
}
Person.prototype.name=null;
Person.prototype.introduce = function(){
    return 'My name is '+this.name; 
}
 
function Programmer(name){
    this.name = name;
}
Programmer.prototype = new Person();
Programmer.prototype.coding = function(){
    return "hello world";
}       //기능 추가  

var p1 = new Programmer('egoing');
document.write(p1.introduce()+"<br />");

//prototype
function Ultra(){}
Ultra.prototype.ultraProp = true;
 
function Super(){}
Super.prototype = new Ultra();
 
function Sub(){}
Sub.prototype = new Super();
 
var o = new Sub();
console.log(o.ultraProp);

객체 o에서 ultraProp를 찾는다.
없다면 Sub.prototype.ultraProp를 찾는다.
없다면 Super.prototype.ultraProp를 찾는다.
없다면 Ultra.prototype.ultraProp를 찾는다.



// 표준 내장 객체

Object      //모든 표준 내장 객체의 부모. Object의 prototype을 사용자 정의하면 모든 내장 객체에서 사용가능.
Function
Array
String
Boolean
Number
Math
Date
RegExp

var arr = new Array('seoul','new york','ladarkh','pusan', 'Tsukuba');
function getRandomValueFromArray(haystack){
    var index = Math.floor(haystack.length*Math.random());
    return haystack[index]; 
}
console.log(getRandomValueFromArray(arr));

// Array라는 표준 내장 객체에 prototype으로 random 메소드 추가 (사용자 정의)
Array.prototype.rand = function(){
    var index = Math.floor(this.length*Math.random());
    return this[index];
}
var arr = new Array('seoul','new york','ladarkh','pusan', 'Tsukuba');
console.log(arr.rand());

//prototype의 유뮤에 따라 사용법이 다름   https://developer.mozilla.org/en-US/docs/Web/JavaScript
// Object.keys()
var arr = ["a", "b", "c"];
console.log(Object.keys(arr));

//Object.prototype.toString()
var o = new Object(1,2,3);
console.log(o.toString());

var a = new Array(1,2,3);
console.log(a.toString())


//Object 확장.
Object.prototype.contain = function(neddle) {       
    for(var name in this){
        if(this[name] === neddle){
            return true;
        }
    }
    return false;
}
var o = {'name':'egoing', 'city':'seoul'}
console.log(o.contain('egoing'));
var a = ['egoing','leezche','grapittie'];
console.log(a.contain('leezche'));
// Object 확장의 위험성
for (var name in o){
    console.log(name);   // name, city, cotain   contain이라는 것도 포함되서 출력되어버림. Object에 추가한 contain도 출력됨.
    o.hasOwnProperty(name)   //이렇게 하면 o라는 객체 자체가 name이라는 요소를 가지고 있냐 (T/F) 부모인 Object의 요소는 상관없이.
}

//데이터타입
//원시데이터타입
숫자        Number
문자열      String
불리언      Boolean
null        //레퍼객체없음
undefined   //레퍼객체없음

var str = 'coding';
str.length;  // str을 마치 객체처럼 쓸수있는 이유는 내부적으로 문자열이라는 원시데이터타입을 String이라는 객체로 잠시 변환시켜주기때문(레퍼객체)
            // str = new String('coding')
str.charAt(0);
str.indexOf('c')
str.toUpperCase()
str.toLowerCase()
str.includes('co') //대소문자 구분함
str.startsWith('c')  //true return 
str.endsWith('n')   //false return
str.replace('c', 'j') // 문자치환  처음만나는 c만 바꿈 
str.replace(/c/g,'i') //정규표현식, 모든 c를 i로 바꿈 
str.slice(0,3)
str.slice(4) //4부터 쭉 
str.slice(-3) // 뒤에서 3번째부터 쭉 
str.split(' ')  //리스트로 반환 

str.prop = 'everybody'; // 오류 없이 지나감.
console.log(str.prop);  //undefined  str.prop를 다시 사용하려고 하면 undefinde 뜸 . 그이유는 잠깐동안만 객체화를 하고 다시 원시데이터로 돌려놓기때문.


//참조, 복제
//원시데이터인 경우
var a = 1;
var b = a;
//이때 a,b는 메모리 공간 공유 x  복제임.

//객체인 경우 
var a = {'id':1};
var b = a;
// 이 경우는 b.id =2 이렇게 변경했을 경우 a.id 도 2로 바뀜 //참조.

var a = {'id':1};
var b = a;
b = {'id':2};
// 그런데 b에 새로운 객체를 만들어서 대입해주면, a와 b는 별개의 객체가 된다.


// jquery 





// javascript vs C++

C++ 에서는 for문의 중괄호 안에서 선언된 name이 중괄호 밖에서는 사용이 불가능하지만,
javascript 에서는 사용가능하다. 즉 javascript는 함수안에서 선언된 변수만이 지역변수로 인정된다.


function cal(mode){

    var funcs = {
        'plus' : function(left, right){return left + right},
        'minus' : function(left, right){return left - right}
    }

    return funcs[mode];             //반환값으로 함수 사용
}

alert(cal('plus')(2,1))  // 2+1 



// var, let, const

let hong = 1;
{
    let hong = 2;
}
//let은 스코프안에서 지역변수로 선언가능. 스코프 밖에 hong과 안에 hong은 다른 변수임.
// const도 마찬가지이지만, const같은 경우 재할당이 불가능함.  주로 const를 default로 쓰고 let은 변경해야될 변수에 씀.
// var은 스코프안에서 재선언하면 재할당하는 기능으로 대체됨. var은 이제 쓰지마셈


// 일반 함수
var foo = function () { console.log("foo") }; // foo
// 화살표 함수
var bar = () => console.log("bar"); // bar

// 매개변수가 없는 경우
var foo = () => console.log('bar');
foo(); // bar

// 매개변수가 하나인 경우
var foo = x => x;
foo('bar'); // bar

// 매개변수가 여려개인 경우
var foo = (a, b) => a + b; // 간단하게 한줄로 표현할 땐 "{}" 없이 값이 반환됩니다.
foo(1, 2); // 3

var foo = (a, b) => { return a + b }; 
foo(1, 2); // 3

var foo = (a, b) => { a + b }; // "{}"를 사용했는데 return이 없을 때 
foo(1, 2); // undefined

var foo = (a, b) => { // 여러줄 썼을 때
	var c = 3;
	return a + b + c;
}
foo(1, 2, 3) // 6
/*
"{}"를 사용하면 값을 반환할 때 return을 사용해야합니다.
"{}"를 사용하지 않으면 undefied를 반환합니다.
"{}"을 사용할 때는 여러줄을 썼을 때 사용합니다.
*/

// 객체를 반환할 때
var foo = () => ( { a: 1, b: 2, c: 3 } );
foo(); // { a: 1, b: 2, c: 3 };

//콜백함수에서 화살표함수
// ES5
var numbers = [1, 4, 9];
var oddArr = numbers.filter(function (x) { return x % 2 !== 0;});
console.log(oddArr); // [1, 9]
// ES6
var numbers = [1, 4, 9];
var oddArr = numbers.filter( x => (x % 2) !== 0 );
console.log(oddArr); // [1, 9]


//map
const arr = ["there", "are", "you", "are", "how", "hello!"];
let arr2 = arr.map((item)=>item.toUpperCase());            // ["THERE", "ARE", ...]
//map은 전체 요소를 다 돌면서 요소값을 변화시킴.
//forEach 와 차이점은 map은 리턴값이 리스트인것임.

arr.find((user)=>(user === 'there')) // 만족하는 값 하나만 리턴
arr.filter((user)=> user.length >= 3)// 만족하는 모든 값 배열로 리턴 
arr.flat()      // 고차원 배열을 평평하게 펴줌

let nums = [1,2,3,4,5];
let call_count = 0;

let sum = nums.reduce(function(accumulator, item, index, array){
    console.log(accumulator, item, index);
    call_count++;
    return accumulator + item;
}, 0);


let map = new Map();

map.set("name", "john");        //key,value 
map.set(123,456)
 
map.get('name')     // john

map.delte('name')
map.clear()

for (let item of map.keys()){
    console.log(item)
}
for (let item of map.values()){
    console.log(item)
}
for (let item of map){
    console.log(item)
}


let set = new Set();
let num = new Set([1,2,3,4,5]);
let str = new Set("Hello!");    // {h e l o !} 이거를 다시 리스트로 넣어줘야함.

set.add(1).add(1)    // {1}
set.has(1)          // true 
set.delete(1)

// Promise 

new Promise((resolve,reject) => {               
    console.log('Inside promise')
    reject(new Error('First reject'))               //reject 나오면 밑에 resolve는 실행되지 않음, 반대로 resolve가 먼저 나오면 reject는 실행되지 않음 
    console.log('after reject')                     // 하지만 reject이후에 다른 코드들은 실행이됨 resolve만 실행x 
    resolve('First resolve')
}).catch((error)=>{                                 //reject로 인해 에러 캣치
    console.log('error', error)
}).then((value) => {                                
    console.log('Inside first then')
    console.log('value', value)                     // 위에서 resolve가 실행되지 못했기 때문에 value는 undefined
})                                                  // 만약 then과 catch 자리가 바뀌면 then은 실행되지 못함. 


new Promise((resolve,reject)=>{
    console.log('before timeout')
    setTimeout(()=>{
        resolve(Math.random())
        console.log('after resolve')
    }, 1000)
}).then((value)=>{
    console.log('value', value)                     // resolve 값이 여기로 옴.
})
// before timeount => after resolve => value 0.30940


// Async , await 
function p() {
	return new Promise((resolve, reject) => {
	    resolve('hello'); 
        // or reject(new Error('error');
	});
}
p().then((n) => console.log(n));

async function p2(){ // async을 지정해주면 Promise를 리턴하는 함수로 만들어준다.
    return 'hello2'; //리턴값은 Promise{<resolved>: "hello2"} 자동 resolve해준다는걸 알 수있다.
    // reject는 throw 에러를 날리면 된다.
  }
p2().then((n) => console.log(n));


//
async function p2() {
    let promise = new Promise((resolve, reject) => {
      setTimeout(() => resolve("완료!"), 2000)
    })
  
    return promise
  }
  
  async function main() {
    let getGreeting = p2()              //이 코드가 없으면 총 4초가 걸림.
    let getGreeting2 = p2()
    let a = await getGreeting
    let b = await getGreeting2
    console.log(a, b)
    console.log("end")
  }
  
main()
  

// optional chaining  ?. 

let user = {}

console.log(user?.address?.street)    // undefined 
//user 객체안에 address가 없으면 undefined 리턴함. 에러를 일으키지 않음. 














































//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////nomad coder/////////////

//웹사이트는 html 파일을 열고, html은 js와 css 의 코드를 끌어와서 웹사이트에 보여주는 접착제 역할을 한다.
//웹사이트에서 직접 js파일과 css파일을 열면 그냥 코드만 보여줌. 



//index.html이 가져오는 app.js에서 
document.location;                          //현재 웹페이지 사용자의 위치 가져오기  document라는건 html 전체코드를 말하는거임.
document.title;                             //웹페이지 title 가져오기
document.body;                              //웹페이지 body 가져오기 
document.head;                              //웹페이지 head 가져오기


const title = document.getElementById("title");           //id가 title인 태그를 모두 가져오기. //byclassname, bytagname 등 여러가지 있음.

console.dir(title);                 //id가 title인 태그의 자세한 정보 (object) 출력. 여기에서는 다양한 event들도 (on으로시작하는) 볼수있음.(click,mouseenter..)

title.innerText = "Got you!";            //태그 안에 내용을 변경해버림. 

const titletwo = document.querySelector(".hello h1");      //.hello는 클래스가 hello인 태그를 가져오고, h1은 class가 hello인 태그 안에 있는 h1을 가져옴.   
                                                          // 만약 hello클래스가 여러개라면 첫번째 hello 클래스를 가져옴.
document.querySelectorAll(".hello h1");                  //이렇게 하면 모든 hello 클래스 안에 있는 h1을 리스트로 가져옴.  

/////////
const title = document.querySelector(".hello h1");

console.log(title);

title.style.color = "blue";                 //style도 바꿀수 있음. javascript에서 바꿀수 있지만 기본 style은 css에 맡기는것이 좋음.
                                            //js에서 style 바꿀때는 스트링으로 감싸줘서 입력해야함.
function handleTitleClick(){
    console.log("title was clicked!");
}

title.addEventListener("click", handleTitleClick)             //누군가 title을 클릭하는거를 보고있다가 클릭되면, 두번째 인자 함수 실행. 함수뒤에()넣지말기.
title.onclick = handleTitleClick;                           //위에랑 똑같은 말임.


//event 모음
click 
mouseenter 
mouseleave 
resize 
copy 


function handleWindowResize(){
    document.body.style.backgroundColor = "tomato";
}

function handleWindowOnline(){
    alert("All Gooood!")
}

function handleWindowOffline(){
    alert("SOS no Wifi")
}

window.addEventListener("resize", handleWindowResize);                  //window 창의 사이즈를 변경하는 이벤트발생시 함수실행.
window.addEventListener("online", handleWindowOnline);
window.addEventListener("offline", handleWindowOffline);



1. element를 찾아서 선택해라
2. event를 listen 해라 
3. event에 따른 리액션(펑션)을 구현해라. 

title.classList.contains("active")      //어떤 태그의 클래스에 active가 포함되어있으면 true리턴.
title.classList.remove("active");     //클래스 active를 없애기
title.classList.add("active");        // 클래스에 active 추가하기.  
title.classList.toggle("active");       //클래스에 active가 있으면 없애고 없으면 active 추가하는기능.

title.className;


/////////////////////

const loginForm = document.getElementById("login-form");    // id가 login-form인 div 태그 가져오기
const loginInput = loginForm.querySelector("input");        // 그 안에 input 태그 가져오기
const loginInput = loginForm.querySelector("#login-form input");   //id가 login-form인 태그 안에 있는 input 태그 element 가져오기.         
const loginButton = loginForm.querySelector("button");      // 그 안에 button 태그 가져오기

loginInput.value            //login input 안에 입력한 내용 



///
<body>
    <form id="login-form">
        <input
            required
            maxlength="15"
            type="text"
            placeholder="what is your name?" 
        />
        <input type="submit" value="Log In" />

    </form>
</body>
///
//input 안에 required maxlength 이런거 쓰려면 div 말고 form 안에 input이 있어야함 그래야 submit도 가능함.



localStorage.setItem("username","hongsa");
localStorage.getItem("username");
localStorage.removeItem("username");


// const date = new Date();
// const date = new Date(2021,0,1);         //// 1월은 0부터 시작 
// const date = new Date('2020-01-01');     ////스트링 보내면 date객체로 변환
// const date_str = Date();    ////스트링으로 출력 
// 날짜객체 생성.

// date.getDate(); 
// date.getFullYear();
// date.getMonth();
// date.getDay();
// date.getHours();
// date.getMinutes();
// date.getSeconds();
// date.getTime()  //ms 로 리턴 



//"1".padStart(2,"0");          //만약 string이 2글자가 아니라면 앞에 "0" 추가 

setInterval(getClock, 1000);    //1초마다 getClock 함수 실행. 
setTimeout(getClock, 1000);     //1초후에 getClock 함수 실행.



const randomImg = images[Math.floor(Math.random()*images.length)];
const bgimg = document.createElement("img");      //img 태그 형성. 
bgimg.src = `img/${randomImg}`;

document.body.appendChild(bgimg);       //<img src="img/0.jpg">  body 제일 뒤쪽에 삽입.
document.body.prepend(bgimg);           // body 제일 앞쪽에 삽입


////////////////
const todoForm = document.querySelector("#todo-form");
const todoList = document.querySelector("#todo-list");

function handleToDoSubmit(event){
    event.preventDefault();               //html은 기본적으로 submit하면 자동으로 새로고침하기때문에, preventDefault로 새로고침 막음.
}

todoForm.addEventListener("submit", handleToDoSubmit);



////////
function deleteTodo(event){
    const li = event.target.parentElement;      //button이 클릭됬을때 event를 알려주는데. parentElement는 button이라는 태그가 속해져 있는
    li.remove();                               // 부모 태그를 알려준다.                                               
}

button.addEventListener("click", deleteTodo);


//////////////
function makeList(item){
    console.log(item);
}

const toDos = [];    // or {} 
const stringArray = JSON.stringify(toDos);              //array나 object를 string으로 변환시켜줌.
const parsedArray = JSON.parse(stringArray);             //stringify 된 array나 object를 다시 원래대로 돌려줌.
                                                        // 깊은복사를 할때 이방법을 씀 문자열화 했다가 다시 json으로 변환해서 깊은복사
parsedArray.forEach(makeList);                          // 각 요소마다 루프를 돌면서 makeList 함수 실행. makeList함수에 item argument 넣어줘야 돌아감.
                                                        // item에 parsedArray에 각 요소가 차례대로 들어가면서 실행됨
parsedArray.forEach((item)=>console.log(item));         // 위에랑 똑같은 의미, 익명함수로 함수만들필요없이 바로 작동.                                                        
////////////

navigator.geolocation.getCurrentPosition(onGeoOk,onGeoError);  //현재위치를 받는걸 성공하면 첫번째 인자함수실행하고 데이터를 argument로 넘겨줌.
                                                                // 실패하면 두번째 인자함수 실행.

const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`

fetch(url).then(response=>response.json()).then(data=> {        //then은 fetch라는 함수가 실행되려면 몇초가 걸릴지 모르니까 실행완료하면
    const name = data.name;                                     // 그다음에 뭘해라 라는 뜻임. data에는 response를 json으로 바꾼 데이터가 들어오게됨.
    const weather = data.weather[0].main;
});



//string.slice(0,25)   string의 index 0부터25까지만 


//////////////////1만 시간 법칙 js 코드 ///////////////////////

const startButton = document.querySelector(".start_btn");
const shareButton = document.querySelector(".share_btn");
const openButton = document.querySelector(".modal_btn");
const closeButton = document.querySelector(".close_btn");

const result = document.querySelector(".result");
const modal = document.querySelector("#modal");
const loading = document.querySelector(".result_loading");




function saveValue() {
    localStorage.setItem("field_value", field_value.value);
}

function calculator() {
    const field_value = document.querySelector("#field_value");
    let time_value = document.querySelector("#time_value");
    let time_value_int = Number(time_value.value);

    const field_result = document.querySelector(".field_result");
    const time_result = document.querySelector(".time_result");

    if (field_value.value == "") {
        alert("입력되지 않았습니다.");
        field_value.focus();                //이 태그로 커서 포커싱 하기.
        return false;
    } else if (time_value.value == "") {
        alert('입력되지 않았습니다.');
        time_value.focus();
        return false;
    } else if (time_value_int > 24) {
        alert('잘못된 값입니다. 24이하의 값을 입력해 주세요.')
        return false;
    } else {
        result.style.display = 'none';
        loading.style.display = 'flex';
    }

    setTimeout(function () {
        result.style.display = 'flex';
        loading.style.display = 'none';
        field_result.innerText = field_value.value;
        time_result.innerText = parseInt((10000 / time_value_int), 10);
    }, 1800);
}

function openModal() {
    modal.style.display = 'flex';
}

function closeModal() {
    modal.style.display = 'none';
}

window.onclick = function(event){                   //바깥쪽 window를 클릭했을때 창 닫기.
    if(event.target == modal){
        closeModal();
    }
}

function copyUrl() {                                //url 복사하는 코드 
    let url = window.location.href;
    let tmp = document.createElement('input');

    document.body.appendChild(tmp);
    tmp.value = url;
    tmp.select();
    document.execCommand("copy");
    document.body.removeChild(tmp);

    alert("URL이 복사되었습니다.");
}

shareButton.addEventListener('click', copyUrl);
openButton.addEventListener('click', openModal);
closeButton.addEventListener('click', closeModal);
startButton.addEventListener('click', calculator);

import { string } from "prop-types";
//////////////////////////////////////////////////////////////////////

import web3 from "web3"         //최근규격
const web3 = require("web3")

export default a;               //최근규격 
module.exports = a;

//////////////////////////////////////////////////////////////////////
str='abc,def,ghi'
str.split(',')
// 결과 [abc,def,ghi]  리스트 리턴 