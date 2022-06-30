function test1(num){
    let result = "";

    for(i = 0; i<num; i++){
        result += '*';              // 자바스크립트는 문자열 곱하기 안됨. 저렇게 더해줘야함.
    }
    console.log(result)
    return result;
}

function test2(num1, num2){
    let result = [];

    let minNum = Math.min(num1,num2);    // Math.min

    for(i=minNum; i<=num2; i++){
        result.push(i);                     // list.push(i)   파라미터 여러개 못넣음
    }

    console.log(result)
    return result;
}

function test3(lst){
    let result = 0;

    let sum = lst.reduce((ac,num)=>{            //reduce 콜백함수 
        return ac + num;
    });

    //result = Math.round(sum/lst.length);
    result = (sum/lst.length).toFixed(2);           //숫자.toFixed(3)

    console.log(result)
    return result;
}

function test4(lst){

    let result = 0;

    let maxNum = 0;

    for(i=0; i<lst.length; i++){
        if (lst[i] > maxNum) {
            maxNum = lst[i]
            result = i+1
        };
    }

    console.log(result)
    return result
}

function test5(num1,num2){
    let result = [];
    let subNum = 0;

    result = result.concat([num1,num2]);                //list.concat(lst)

    while (true){
       //subNum = result[-2] - result[-1];
       //자바스크립트는 리스트 요소 -1번째 이런거 안됨.
       subNum = result[result.length-2] - result[result.length-1];                  
        if (subNum >= 0){
            result.push(subNum);
        }
        else break;
    }

    console.log(result)
    return result;
}

function test6(num){
    if (num%4 == 0 && num%100 != 0){                // 조건문 &&  ||
        return true;
    }

    else if (num%400 == 0){
        return true;
    }

    else {
        return false;
    }
}

function test7(num1, num2){
    if (num1 % 5 !=0){
        return num2;
    }
    withdraw = num1 + 0.5;
    if (num2 < withdraw){
        return num2 
    }
    else {
        return num2 - withdraw
    }
}

function test8(num1,num2){
    let result = 1;
    for (i = 0; i < num2; i++){
        result *= num1;
    }

    return result;
}

function test9(obj){

    //let permit;
    //permit = user.height>=150
    //return permit

    if (obj.height < 150){
        return false
    }
    else return true
}

function test10(lst){
    let result = [];
    new Set(lst).forEach((item)=>{              //forEach
        result.push(item);
    })

    //result = Array.from(new Set(lst))   바로 리스트로 바꾸기

    return result;
}

function test11(lst){
    let newList = []

    for(item in lst){
        newList.unshift(lst[item])
    }
    return newList
}

console.log(test11([1,2,3,4]))



let count = arr.filter(element => 'a' === element).length;            // 배열 요소 갯수 구하기 .

let date = new Date('2021-01-17')
date.getDay()    // 숫자로 리턴 0~6 


// 문자열 
str.charAt(0);
str.indexOf('c')
str.toUpperCase()
str.toLowerCase()
str.includes('co') //대소문자 구분함
str.startsWith('c')  //true return 
str.endsWith('n')   //false return
str = str.replace('c', 'j') // 문자치환  처음만나는 c만 바꿈 
str = str.replace(/c/g,'i') //정규표현식, 모든 c를 i로 바꿈 
str.slice(0,3)
str.slice(4) //4부터 쭉 
str.slice(-3) // 뒤에서 3번째부터 쭉 
str.split(' ')  //리스트로 반환 


//배열 array 리스트, list
var member = ['egoing', 'k8805', 'sorialgi'];

member.push('f');           // 배열 맨뒤에 추가

li = member.concat(['e','f']);  //배열과 배열 합치기

member.unshift('z');  // 배열 맨앞에 넣기

member.splice(1)        //member 인덱스 1부터 쭉 긁어서 리스트 리턴, 기존 member도 짤려있음 
member.splice(1,1)      // 인덱스 1만 가져옴 
member.splice(1, 0, 'd');  //1번 인덱스에 'd' 추가 기존 1에 있던 값은 뒤로 밀림.
member.splice(1,1,'x','y'); // 1번 인덱스부터 x ,y 추가 기존 1에 있던 값은 삭제됨.

member.slice(1)         // 인덱스1부터 쭉 출력 
member.slice(1,3)       // 인덱스 1부터 2까지 출력 

let shift = member.shift();   // 맨앞에 있는 요소 제거  , shift 에는 제거된 요소가 리턴된다. 그리고 member는 맨앞요소가 제거되어있음. 새로할당안해줘도됨
member.pop();       //member의 맨뒤에 요소 제거되고, 맨뒤에 요소 리턴 
member.sort();      //요소 정렬
member.reverse();   //요소 역정렬

member.includes('egoing')       //true false 리턴
member.indexOf('egoing')        // 첫번째 index 리턴 

//a-b는 오름차순 b-a는 내림차순 
arr.sort((a, b) => a-b);

arr.find((user)=>(user === 'there')) // 만족하는 값 하나만 리턴
arr.filter((user)=> user.length >= 3)// 만족하는 모든 값 배열로 리턴 

member.join(',')  //각요소 사이사이마다 , 포함되서 스트링으로 리턴 

//map
const arr = ["there", "are", "you", "are", "how", "hello!"];
let arr2 = arr.map((item)=>item.toUpperCase());            // ["THERE", "ARE", ...]

//reduce
let sum = nums.reduce(function(accumulator, item, index, array){
    console.log(accumulator, item, index);
    call_count++;
    return accumulator + item;
}, 0);

//object 
let obj = {}        //자바스크립트 객체의 키값에 숫자가 들어갈 수 없음. 문자열이나, 변수이름이 들어갈 수 있음.

//단축평가 
//왼쪽값이 true일경우 왼쪽값 반환 그렇지 않으면 오른쪽값 반환 
'apple' || 'banana'   // apple 반환 
false || 'apple'        // apple 반환




/////프로그래머스 완전탐색, 모의고사 lv.1
// function solution(answers) {
//     var answer = [];
//     let supo1 = [];
//     let supo2 = [];
//     let supo3 = [];
    
//     let supo1Num = 1;
    
//     let supo2Num = 3;
//     const supo2lst = [1,3,4,5];
    
//     let supo3Num = 0;
//     const supo3lst = [3,1,2,4,5]
    
//     let correctNum = [0,0,0];
    
//     for (i=0; i<answers.length; i++){
//         //supo1
//         if (supo1Num == answers[i]) {
//             correctNum[0] += 1
//             supo1Num<5?supo1Num+=1:supo1Num=1
//         }
//         else supo1Num<5?supo1Num+=1:supo1Num=1
        
//         //supo2
//         if (i==0 || i % 2 == 0){
//             if (answers[i] == 2){
//                 correctNum[1] +=1
//                 supo2Num<3?supo2Num+=1:supo2Num=0
//             }
//         }
//         else{
//             if (answers[i] == supo2lst[supo2Num]){
//                 correctNum[1] +=1
//                 supo2Num<3?supo2Num+=1:supo2Num=0
//             }
//             else supo2Num<3?supo2Num+=1:supo2Num=0
//         }
        
//         //supo3
//         if (answers[i] == supo3lst[supo3Num]){
//             correctNum[2] +=1
//             if (i % 2 == 1) supo3Num<4?supo3Num += 1:supo3Num=0
//         }
//         else {
//             if (i % 2 == 1) supo3Num<4?supo3Num += 1:supo3Num=0
//         }
//     }
    
//     let maxNum = Math.max(...correctNum)
    
//     answer = correctNum.reduce((cur,num,idx) => {
//        if (num == maxNum) {
//            cur.push(idx+1)
//        }
//         return cur
//     },[])
    
    
//     return answer;
// }