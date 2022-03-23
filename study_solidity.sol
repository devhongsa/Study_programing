https://kimsfamily.kr/328     블록체인 교육 블로그 , erc20 토큰만들기 등.


// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.7.0 < 0.9.0;

contract hello{
    string public hi = "Hello solidity";

//boolean type
bool public b = true;

//bytes type
bytes4 public bt = 0x12345678;
bytes public bt2 = "STRING";

// address : 컨트랙 주소; 

//int uint

// 1 ether = 10^9 Gwei = 10^18 wei
// Gwei는 가스비 , 복잡하고 긴 smart contract 일수록 가스비용 더 나옴
// smart contract를 배포하고 실행할때마다 gas 비용이 계속 나오기 때문에
// 개발과정에서 어떻게 하면 gas비용을 최소화해서 smart contract를 만들 수 있을 지 고민해야됨.

uint256 public value = 1 ether;
uint256 public value2 = 1 wei;
uint256 public value3 = 1 gwei;
uint public a = 10;

function changeA1() public{
    a = 5;
}

function changeA2(uint256 _value) public{
    a = _value;
}

// return값이 있는 함수의 경우 정의를 할때 이렇게 해줘야함
function changeA3(uint256 _value) public returns(uint256) {
    a = _value;
    return a;
}

/// 접근 지정자 
// public : 모든 곳에서 접근가능, 배포했을때 유저인터페이스에서 테스트 가능, public 안쓰면 버튼안나옴
// public으로 지정한 변수들은 remix에서 콜함수로 저절로 만들어지는데 call 함수들은 트랜잭션이 없고 즉시 호출되기 때문에 gas 소비도 없다.
// 그래서 public으로 지정한 변수들을 굳이 get function을 만들어서 호출안해도 됨. 저절로 호출함수 만들어짐.

// external : public 처럼 모든곳에서 접근 가능하나, external함수가 정의된 스마트컨트랙 내에서는 다른 함수에서 external함수 호출불가
// private : 오직 private이 정의된 자기 컨트랙에서만 가능(private이 정의된 컨트랙을 상속 받은 자식도 불가능)
// internal : private 처럼 오직 internal로 정의된 함수의 스마트컨트랙 내에서만 접근가능하고, 이 스마트컨트랙을 상속 
// 받은 자식도 접근 가능

uint256 public v = 5;
uint256 private v2 = 10;            // private으로 하면 배포했을때 v2는 접근하지못함. 여기 컨트랙안에서만 접근가능

}


contract Public_example{
    uint256 public a = 3;

    function changeA(uint256 _value) public {
        a = _value;
    }

    function get_a() view public returns(uint256) {
        return a;
    }
}

//view? : function 밖에 있는 변수들을 읽을 수 있으나 변경 불가능, 블록체인상에 기록되지 않음. 읽기전용함수
//pure : funcftion 밖에 있는 변수들을 읽지도 못하고, 변경도 불가능. 외부변수를 가져오지않고 오직 자기function의 파라미터를 가지고 리턴하는 함수.

contract Public_example_2{
    Public_example instance = new Public_example();     // 다른 contract을 쓰고 싶을때 객체형성

    function changeA_2(uint256 _value) public{
        instance.changeA(_value);
    }
    function use_public_example_a() view public returns(uint256) {
        return instance.get_a();
        // return instance.a();         // 그냥 변수를 불러올때도 () 붙여야됨
    }
}

contract study{
    //storage : 함수밖의 대부분의 변수, 함수들이 저장되며, 영속적으로 저장이 되어 많을 수록 가스 비용이 비싸짐
    //memory : 함수안의 변수들, 함수의 파라미터, 리턴값, 레퍼런스 타입이 주로 저장이 됨. 함수내에서만 유효하기때문에 블록체인에 저장 x
    // storage 보다 가스비용이 저렴함. 영속적이지 않음.
    //colldata : 주로 external function의 파라미터에서 사용 됨.
    //stack : EVM( ethereum cirtual machine) 에서 stack data를 관리할때 쓰는 영역, 1024Mb 제한적 

    function get_string(string memory _str) public pure returns(string memory) {
        return _str;
    }
//string은 기본 데이터타입이 아니고 배열 개념이기 때문에 저런식으로 memory를 붙여줘야함
}


//constructor?
//constructor에는 public, private, external 같은 visibility를 안넣어줘도됨.

contract A
{
    string public name;
    uint256 public age;

    constructor(string memory _name, uint256 _age)
    {
        name = _name;
        age = _age;
    }

    function change(string memory _name, uint256 _age) public
    {
        name = _name;
        age = _age;
    }
}

contract B
{
    A instance = new A("Alice", 52);            //인스턴스를 쓰면 가스소모량이 많이 높아진다

    function change(string memory _name, uint256 _age) public
    {
        instance.change(_name, _age);
    }

    function get() public view returns(string memory, uint)
    {
        return (instance.name(), instance.age());   // 여러개 return값 가능
    }
}

/// 상속 , overriding

contract Father
{
    string family_name = "Kim";
    string given_name = "Jungsu";
    uint256 money = 100;

    constructor(string memory _given_name)
    {
        given_name = _given_name;
    }

    function getMoney() view public virtual returns(uint256)
    {
        return money;
    }
}
//여기서 virtual은 자식컨트랙트에서 이 함수를 override 할 것이라는 뜻. 
contract Mother
{
    uint256 money2 = 200;

    function getMoney() view public virtual returns(uint256)
    {
        return money2;
    }
}

contract Son is Father("James"), Mother
{
    //constructor() Father("James"){}               //이런식으로 초기화 가능

    uint256 public earning = 0;

    function work() public
    {
        earning += 100;
    }

    function getMoney() view public override(Father, Mother) returns(uint256)
    {
        return money + money2;
    }
}

// event

contract Event1
{
    event info(string name, uint256 money);

    function sendMoney() public
    {
        emit info("Hongsa", 1000);
    }
}

contract Event2
{
    event numberTracker(uint256 num, string str);
    event numberTracker2(uint256 indexed num, string str);   //index가 지정된 num은 후에 필터기능으로 특정인덱스
                                                             //부분의 데이터 뽑아보기 가능

    uint256 num = 0;

    function PushEvent(string memory _str) public
    {
        emit numberTracker(num, _str);
        emit numberTracker2(num, _str);
        num++;
    }
}

// super 
contract Father2
{
    event FatherName(string name);
    function who() public virtual
    {
        emit FatherName("KimDaeho");
    }
}

contract Son2 is Father2
{
    event sonName(string name);
    function who() public override
    {
        super.who();                //Father2의 객체생성없이 super로 부모컨트랙 함수 사용가능
        emit sonName("KimJin");     // 만약 2개 이상의 컨트랙을 상속시 가장 마지막에 상속받은 컨트랙의 who를 실행.
    }
}


// mapping?

contract lec17
{
    mapping(uint256 => uint256) private ageList;   // key값과 value 값의 데이터타입 명시,  //mapping은 length의 기능이 없음.
    
    function setAgeList(uint256 _index, uint256 _age) public
    {
        ageList[_index] = _age;
    }

    function getAge(uint256 _index) public view returns(uint256)
    {
        return ageList[_index];
    }

}

// Array 배열

//솔리디티에서는 array보다는 mapping을 더 선호한다고함. 왜냐면 array는 for문 순환을 사용할 수 있지만.
// Dos 공격에서 취약하기 때문에 어떤 해커가 for문을 무한히 반복하게되면 엄청난 가스와 과부하가 일어날 수 있음.

contract lec18
{
    uint256[] public ageArray;
    uint256[10] public ageFixedSizeArray;     // 배열 length 제한
    string[] public nameArray = ["kal", "Jhon", "Kerri"];  

    function AgeLength() public view returns(uint256){
        return ageArray.length;
    }

    function AgePush(uint256 _age) public{
        ageArray.push(_age);
    }

    function AgeGet(uint256 _index) public view returns(uint256) {
        return ageArray[_index];
    }

    function AgePop() public {
        ageArray.pop();                  // 가장 최신 인덱스 값 삭제  length도 줄어듬
    }

    function AgeDelete(uint256 _index) public {
        delete ageArray[_index];                    //해당 인덱스값을 default 값 0으로 바꿔주고 length는 그대로
    }

    function AgeChange(uint256 _index, uint256 _age) public
    {
        ageArray[_index] = _age;
    }

    function GetmyArray() public view returns(uint256[]){       //Array 전체를 리턴하기
        return ageArray;
    }

}

// struct 구조체

contract lec20
{
    struct Character
    {
        uint256 age;
        string name;
        string job;
    }

    mapping(uint256 => Character) public CharacterMapping;
    Character[] public CharacterArray;

    function createCharacter(uint256 _age, string memory _name, string memory _job) pure public returns(Character memory)
    {
        return Character(_age, _name, _job);
    }

}

// if 문
contract lec21{
    string private outcome = "";
    function isIt5(uint256 _number) public returns(string memory){
        if(_number == 5){
            outcome = "yes, it is 5";
            return outcome;
        }
        else if(_number <5){
            return outcome;
        }
        else{
            return outcome;
        }
    }
}


// for, while , do-while

contract lec22
{
    event CountryIndexName(uint256 indexed _index, string _name);
    string[] private countryList = ["south", "north", "usa", "china", "japan"];

    function forLoopEvents() public
    {
        for (uint256 i = 0; i < countryList.length; i++)
        {
            emit CountryIndexName(i, countryListp[i]);
        }
    }
}


// solidity에서 string type은 비교가 불가하다.
keccak256(bytes(string)) == keccak256(bytes(string2))       // 그래서 이런식으로 string을 bytes로 변환한 후에 keccak256이라는 내장함수를 이용해서
                                                            // 해시값으로 만들어주고나서 비교를 해야함.


// 에러핸들러 : require?, revert?, assert?, try/catch

0.4.22 ~0.7.x 버전
assert : gas를 다 소비한 후, 특정한 조건에 부합하지 않으면(false일 때) 에러를 발생시킨다.
revert : 조건없이 에러를 발생시키고, gas를 환불 시켜준다.
require : 특정한 조건에 부합하지 않으면(false일 때) 에러를 발생시키고, gas를 환불 시켜준다.

function assertNow() public pure
{
    assert(false);              //test에서 주로 사용   0.8.x 버전부터는 assert는 가스비를 환불받고, panic error를 발생시킴 solidity doc 참고
}

function revertNow() public pure
{
    revert("error!!");          // if문을 혼합해서 사용하거나, require을 쓴다
}

function requireNow() public pure
{
    require(false, "occurred"); //require 주의사항은 require 안에있는 조건문이 false일때 오류를 발생시키는것. if문이랑 반대임.
}

// try/catch
// assert/revert/require 은 에러를 발생시키고 프로그램을 끝내지만 try/catch는 프로그램을 종료시키지 않고 어떠한 대처를 하게 함.

catch Error(string memory reason)
catch Panic(uint errorCode)
catch()

// 외부 스마트 컨트랙의 함수를 부를때 : 다른 스마트컨트랙을 인스턴스화 하여서, try/catch문이 있는 스마트컨트랙의 함수를 불러와서 사용
// 외부 스마트 컨트랙을 생성 할 때  : 다른 스마트컨트랙을 인스턴스화 생성 할 때 씀
// 스마트컨트랙 내에서 함수를 부를때 : this를 통해 try/catch를 씀

contract math
{
    function division(uint256 _num1, uint256 _num2) public pure returns (uint256)
    {
        require(_num10<10, "num1 should not be more than 10");
        return _num1/_num2;
    }
}

contract character2
{
    string private name;
    string private power;

    constructor(string memory _name, uint256 _power)
    {
        name = _name;
        power = _power;
    }
}

contract runner
{
    event catchErr(string _name, string _err);
    event catchPanic(string _name, uint256 _err);
    event catchLowLevelErr(string _name, bytes _err);

    event catchOnly(string _name, string _err);

    math public mathInstance = new math();

    function playTryCatch(uint256 _num1, uint256 _num2) public returns(uint256, bool)
    {
        ///
        try mathInstance.division(_num1,_num2) returns(uint256 value)
        {
            return(value, true);
        }
        catch Error(string memory _err)
        {
            emit catchErr("revert/require", _err);
            return(0,false);
        }
        catch Panic(uint256 _errorCode)
        {
            emit catchPanic("assertError/Panic", _errorCode);
            return (0,false);
        }
        catch (bytes memory _errorCode)
        {
            emit catchLowLevelErr("LowlevelError", _errorCode);
            return (0,false);
        }
        ///
    }

    function playTryCatch2(string memory _name, uint256 _power) public returns(bool)
    {
        ///
        try new character2(_name, _power)
        {
            return(true);
        }
        catch
        {
            emit catchOnly("catch", "Errors!!");
            return(false);
        }
        ///
    }
}


// 함수의 리턴값 표기
// 함수 정의할때 returns(uint256) // returns(uint256 total) , 변수명을 써주냐 안써주냐의 차이는
// 써주면 total이라는 변수를 함수 안에서 바로 사용가능하고, 리턴값이 많을때 변수명으로 구분해줌으로써 혼동을 덜어준다.


//modifier?
// 에러발생 조건이 동일하고 이 에러조건이 여러 함수들에 각각 있다고 가정하면, 조건을 바꾸려면 모든 함수에서 다 바꿔줘야하는데
// modifier는 그런 수고를 덜어준다.
contract lec30
{
    // 파라미터가 없으면 ()이거 생략가능
    modifier onlyAdults
    {
        revert("you are not allowed to pay for the cigarette");
        _; //modifier를 쓰는 함수의 내용이 위치하는 자리. revert 에러가 함수내용위에 위치할건지 아래에 위치할건지 정하는거
    }

    function BuyCigarette() public onlyAdults returns(string memory)
    {
        return "Your payment is succeeded";
    }

    //파라미터가 있는 경우
    modifier onlyAdults2(uint256 _age)
    {
        require(_age > 13, "you are not allowed to pay for the cigarette");
        _;
    }

    function BuyCigarette2(uint256 _age) public onlyAdults(_age) returns(string memory) 
    {
        return "Your payment is succeeded";
    }

    //modifier 다른 활용방법
    uint256 public num = 5;
    modifier numChange
    {
        _;
        num = 10;
    }
    function numChangeFunction() public numChange
    {
        num = 15;
    }
    // 이렇게 되면 num =15; 가 먼저 실행되고 modifier num = 10; 이 실행이 되니까 num = 10이 되있음.
}


//payable, msg.value, 이더전송
// payable은 이더/토큰과 상호작용시 필요한 키워드이다. send,transfer, call를 이용하여 이더를 보낼때 payable이라는 키워드 필요
// 주로 함수, 주소, 생성자에 붙여서 사용

// msg.value 는 송금보낸 코인의 값

// 이더를 보내는 3가지 방법
// 1. send? : 2300 gas를 소비, 성공여부를 true or false로 리턴
// 2. transfer? : 2300 gas를 소비, 실패시 에러를 발생 
// 3. call? : 가변적인 gas를 소비 (gas값 지정 가능), 성공여부를 true or false로 리턴
//             재진입(reentrancy) 공격 위험성 있음


contract lec31
{
    event howMuch(uint256 _value);

    function sendNow(address payable _to) public payable
    {
        bool sent = _to.send(msg.value);
        require(sent,"Failed to send token");
        emit howMuch(msg.value);
    }

    function transferNow(address payable _to) public payable
    {
        _to.transfer(msg.value);
        emit howMuch(msg.value);
    }

    function callNow(address payable _to) public payable
    {
        // ~ 0.7
        //(bool sent, ) = _to.call.gas(1000).value(msg.value)("");
        //require(sent, "Failed to send token")


        // 0.7 ~
        (bool sent,) = _to.call{value : msg.value , gas : 1000}("");
        require(sent, "Failed to send token")
        emit howMuch(msg.value)
    }

}

// 주소.balance : 해당 주소의 현재 갖고있는 이더의 잔액
// msg.sender : 스마트컨트랙을 사용하는 주체   call vs delegate call 에서 주요 내용 

contract MobileBanking{
    address owner;
    constructor() payable               
    {                                   // 생성자에 payable 을 넣으면 스마트컨트랙을 배포할때 스마트컨트랙주소로 코인 전송가능
        owner = msg.sender;             // owner를 현재 스마트컨트랙을 이용하는 주체로 설정
    }

    modifier onlyOwner 
    {
        require(msg.sender == owner, "Only Owner!");        // onlyOwner를 함수에 붙여서 적용 
    }

    event Sendifo(address _msgSender, uint256 _currentValue);
    event MyCurrentValue(address _msgSender, uint256 _value);
    event CurrentValueOfSomeone(address _msgSender, address _to, uint256 _value);

    function sendEther(address payable _to) public payable
    {
        require(msg.sender == owner, "Only Owner!");                // owner가 아닌 주체가 스마트컨트랙의 sendEther함수를 이용하려고 하면 에러발생.
        require(msg.sender.balance>=msg.value, "Your balance is not enough");
        _to.transfer(msg.value);
        emit SendInfo(msg.sender, (msg.sender).balance);
    }

    function checkValueNow() public
    {
        emit MyCurrentValue(msg.sender, msg.sender.balance);
    }

    function checkUserMoney(address _to) public 
    {
        emit CurrentValueOfSomeone(msg.sender, _to , _to.balance);
    }
}


// fallback?
// fallback 함수는 이름 그대로 대비책 함수 
// 특징
// 1. 무기명함수
// 2. external 필수
// 3. payable 
// 왜 쓰는가?
// 1. 스마트 컨트랙이 이더를 받을 수 있게 한다.
// 2. 스마트 컨트랙이 이더를 받고 난 후 어떠한 행동을 할 수 있게 한다.
// 3. call은 외부 스마트컨트랙의 함수를 부르는 기능이 있는데, 만약 call이 없는 함수를 부를때, 어떠한 행동을 할 수 있게 한다.

//0.6 이전
// function() external payable{}

contract Bank{
    event JustFallbackWithFunds(address _from, uint256 _value, string message);

    function() external payable{
        emit JustFallbackWithFunds(msg.sender, msg.value, "JustFallbackWithfunds is called")  
    }
    // Bank 컨트랙 입장에서는 msg.sender가 You의 컨트랙주소가 됨. (* 만약 delegate call이면 Bank에서도 msg.sender가 You의 msg.sender가 됨)
    // 실제로 보내는 주소가 sender로 나오지 않음.
    // You 컨트랙 입장에서는 msg.sender는 실제로 보내는 주소가 나옴.
}

contract You{

    function DepositWithSend(address payable _to) public payable{
        bool success = _to.send(msg.value);
        require(success, "Failled");
    }

    function DepositWithTransfer(address payable _to) public payable{
        _to.transfer(msg.value);
    }

    function DepositWithCall(address payable _to) public payable{
        (bool sent,) = _to.call.value(msg.value)("");   // 0.7 이전 call 함수 사용 
        require(sent, "Failed to send eth")
    }

    function JustGiveMessage(address _to) public{
        (bool sent, ) = _to.call("HI");
        require(sent, "Failed to send eth");
    }

    function JustGiveMessageWithFunds(address payable _to) public payable{
        (bool sent, ) = _to.call.value(msg.value)("HI");
        require(sent, "Failed to send eth");
    } 
}

//0.6 이후
//receive 와 fallback으로 나뉨
//receive는 이더만 보낼때, fallback은 이더를 보내고 함수까지 호출할때 
//fallback() external{}           // 함수만 호출될때
//fallback() external payable{}   //함수도 호출되고 , 이더도 보내질때 
//receive() external payable{}    // 이더만 보내질때

contract Bank{

    event JustFallback(address _from, string message);
    event ReceiveFallback(address _from, uint256 _value, string message);
    event JustFallbackWithFunds(address _from, uint256 _value, string message);

    fallback() external{
        emit JustFallback(msg.sender, "JustFallback is called");
    }

    receive() external payable{
        emit ReceiveFallback(msg.sender, msg.value, "ReceiveFallback is called");
    }

    fallback() external payable{
        emit JustFallbackWithFunds(msg.sender, msg.value, "JustFallbackWithFunds is called");
    }
}

contract You{

    function DepositWithSend(address payable _to) public payable{       // send, transfer은 2300 gas만 소비할 수 있기때문에, 오류날수 있음.
        bool success = _to.send(msg.value);                             // receive 함수에서 스트링을 지워주면 gas소비량이 낮아져서 전송가능
        require(success, "Failled");
    }

    function DepositWithTransfer(address payable _to) public payable{
        _to.transfer(msg.value);
    }

    function DepositWithCall(address payable _to) public payable{
        (bool sent,) = _to.call{value : msg.value}("");   // 0.7 이후 call 함수 사용 
        require(sent, "Failed to send eth")
    }

    function JustGiveMessage(address _to) public{
        (bool sent, ) = _to.call("HI");
        require(sent, "Failed to send eth");
    }

    function JustGiveMessageWithFunds(address payable _to) public payable{
        (bool sent, ) = _to.call{value : msg.value}("HI");
        require(sent, "Failed to send eth");
    } 
}


// call? 

contract Addr{
    function addNumber(uint256 _num1, uint256 _num2) public pure returns(uint256){
        return _num1 + _num2;
    }
}

contract caller{
    event calledFunction(bool _success, bytes _output);

    function callMethod(address _contractAddr, uint256 _num1, uint256 _num2) public {
        (bool success, bytes memory outputFromCalledFunction) = _contractAddr.call(
            abi.encodeWithSignature("addNumber(uint256,uint256)", _num1, _num2));

        require(success, "Failed to call function");
        emit calledFunction(success, outputFromCalledFunction);
    }
}

//delegate call?
//delegate call은 스마트컨트랙 업그레이드 할때 필요함. 그냥 call을 쓴다면, 스마트컨트랙 업그레이드 할때
//스마트컨트랙을 전부 재배포를 해야되고, 기존 스마트컨트랙에 저장되어있던 정보는 다 날라가게됨.
// 근데 이 정보들은 블록체인상에 남아있기때문에 다 긁어올순 있지만 비용이 엄청남.
// 그리고 재배포됨으로써 스마트컨트랙 주소가 바뀌는데 이거를 모든 고객에게 전달하기에는 또 비용이 나오고 비효율적임.
// 그래서 upgradable 스마트컨트랙을 만들고 delegate call을 사용해서 고정되어있는 스마트컨트랙에 정보가 저장되게끔 하는것임.

contract add{                   //upgradable smart contract
    uint256 public num = 0;
    event Info(address _addr, uint256 _num);

    function plusOne() public{
        num = num + 1;
        emit Info(msg.sender,num);
    }
}

contract caller{                
    uint256 public num = 0;
    function callNow(address _contractAddr) public payable{                 // add의 num이 바뀜
        (bool success,) = _contractAddr.call(abi.encodeWithSignature("plusOne()"));
        require(success, "Failed to transfer eth");
    }

    function delegateCallNow(address _contractAddr) public payable{         // caller의 num이 바뀜
        (bool success,) = _contractAddr.delegatecall(abi.encodeWithSignature("plusOne()"));
    }
}


// enum? 

contract lec38{

    enum CarStatus{
        TurnOff,
        TurnON,
        Driving,
        Stop
    }

    CarStatus public carStatus;

    constructor(){
        carStatus = CarStatus.TurnOff;
    }

    event carCurrentStatus(CarStatus _carStatus, uint256 _carStatusInInt);

    function turnOnCar() public{
        require(carStatus == CarStatus.TurnOff, "To turn on, your car must be turned off");
        carStatus = CarStatus.TurnOn;
        emit carCurrentStatus(carStatus, uint256(carStatus));       //carStatus 는 숫자로 나오긴하지만 int 타입이 아님, 그래서 uint256() 으로 형변환
    }

    function DrivingCar() public{
        require(carStatus == CarStatus.TurnOn, "To drive a car, your car must be turned on");
        carStatus = CarStatus.Driving;
        emit carCurrentStatus(carStatus, uint256(carStatus));
    }

    function StopCar() public{
        require(carStatus == CarStatus.Driving, "To drive a car, your car must be turned on");
        carStatus = CarStatus.Stop;
        emit carCurrentStatus(carStatus, uint256(carStatus));
    }

    function CheckStatus() public view returns(CarStatus){
        return carStatus;
    }
}

//interface?
//1. interface 안에 정의된 함수는 external로 표시
// interface 안에 정의된 함수는 아직 body가 없고 함수이름만 구현된 상태임.
//2. enum, structs 가능 
//3. 변수, 생성자 불가 

interface ItemInfo{
    struct item{
        string name;
        uint256 price;
    }
    function addItemInfo(string memory _name, uint256 _price) external;
    function getItemInfo(uint256 _index) external view returns(item memory);
}

contract lec39 is ItemInfo{
    item[] public itemList;
    uint256[] public a;
    function addItemInfo(string memory _name, uint256 _price) override public{
        itemList.push(item(_name,_price));
    }
    function getItemInfo(uint256 _index) override public view returns(item memory){
        return itemList[_index];
    }
}
//leg39에는 ItemInfo에 정의된 함수 addItemInfo, getItemInfo 함수가 무조건 정의되어 있어야한다. 이때 override도 붙여야함.
//정의가 안되어있으면 에러가 뜸. 

//library?
// 장점 : 재사용성, 가스소비 절약, 데이터타입 적용
// 단점 : fallback 함수 사용불가, 상속 불가, payable 함수 정의 불가.

library SafeMath{
    function add(uint8 a, uint8 b)internal pure returns (uint8){
        require(a+b >= a, "SafeMath : addition overflow");
        return a+b;
    }
}

contract lec40{
    using SafeMath for uint8;
    uint8 public a;

    function becomeOverflow(uint8 _num1, uint8 _num2) public{
        a = _num1.add(_num2);
    }
}
//using SafeMath for uint8 이거는 SafeMath에 구현된 함수를 사용할때   a.add(b) 이런식으로 uint8에 .add()를 붙여서 사용할 수 있게 해줌.

//import?

//import "./lec41_1.sol"  저장위치가 같을때  ./
//import "../"

string(abi.encodePacked(n,n2,n3);)     //string 여러개를 합쳐주는





//// 블록체인 인 액션 ////

블록체인 기능이 필요한 애플리케이션의 특성 
1. 중개자가 없는 P2P 트랜잭션
2. 신뢰 범위를 넘어서는 서로 알지 못하는 피어 간에 작동
3. 보편적으로 타임스탬프를 가진 변조 불가능한 장부에서 확인, 검증, 저장이 필요한 경우
4. 규칙과 정책에 의해 가이드된 자율적인 오퍼레이션을 가진 경우


함수안에서 로컬 변수로 구조체를 정의할 때, memory 타입인지 storage 타입인지 명시적으로 선언해주어야한다.




//solidity vs C++

//솔리디티의 contract는 C++의 class랑 같은 개념

//솔리디티에서 함수 생성시
//function 함수이름(파라미터) public view(pure) returns(리턴값 데이터타입)

//C++에서 함수 생성시
//함수리턴타입 함수이름(파라미터) {}

//struct 구조체 생성시 C++ 은 {};, solidity는 {}

// 객체만들기 
// C++ : Classname a;
// sol : Classname public a = new Classname();
 