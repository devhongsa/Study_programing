function solution(answers) {
    var answer = [];
    let supo1 = [];
    let supo2 = [];
    let supo3 = [];
    
    let supo1Num = 1;
    
    let supo2Num = 3;
    const supo2lst = [1,3,4,5];
    
    let supo3Num = 0;
    const supo3lst = [3,1,2,4,5]
    
    let correctNum = [0,0,0];
    
    for (i=0; i<answers.length; i++){
        //supo1
        if (supo1Num == answers[i]) {
            correctNum[0] += 1
            supo1Num<5?supo1Num+=1:supo1Num=1
        }
        else supo1Num<5?supo1Num+=1:supo1Num=1
        
        //supo2
        if (i==0 || i % 2 == 0){
            if (answers[i] == 2){
                correctNum[1] +=1
                supo2Num<3?supo2Num+=1:supo2Num=0
            }
        }
        else{
            if (answers[i] == supo2lst[supo2Num]){
                correctNum[1] +=1
                supo2Num<3?supo2Num+=1:supo2Num=0
            }
            else supo2Num<3?supo2Num+=1:supo2Num=0
        }
        
        //supo3
        if (answers[i] == supo3lst[supo3Num]){
            correctNum[2] +=1
            if (supo3Num % 2 == 1) supo3Num<4?supo3Num += 1:supo3Num=0
        }
        else {
            if (supo3Num % 2 == 1) supo3Num<4?supo3Num += 1:supo3Num=0
        }
    }
    console.log(correctNum)
    let maxNum = Math.max(...correctNum)
    
    answer = correctNum.reduce((cur,num,idx) => {
		console.log(num, maxNum)
       if (num == maxNum) {
           cur.push(idx+1)
       }
	   console.log(cur)
        return cur
    },[])
    
	console.log(answer)
    return answer;
}

let result = solution([1, 3, 2, 4, 2])