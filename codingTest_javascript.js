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
    new Set(lst).forEach((item)=>{
        result.push(item);
    })

    //result = Array.from(new Set(lst))   바로 리스트로 바꾸기

    return result;
}

console.log(test9(1,100))



//let count = arr.filter(element => 'a' === element).length;            // 배열 요소 갯수 구하기 .

// let date = new Date('2021-01-17')
// date.getDay()    // 숫자로 리턴 0~6 