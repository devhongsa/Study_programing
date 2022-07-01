function solution(N, stages) {
    var answer = [];
    let obj = {}
    let rateList = []
    
    for(n=1; n<N+1;n++){
        let cnt = stages.reduce((cul,val)=>{
            if (n == val) return cul+1
            else return cul
        },0)
        rateList.push(cnt/stages.length);
        while (stages.includes(n)){
            stages.splice(stages.indexOf(n),1)
        }
    }
    
    let newList = Array.from(new Set(rateList))
    newList.sort((a,b)=>b-a)
    console.log(newList)

    for (i=0; i<newList.length; i++){
        obj[String(newList[i])] = []
    }
    
    console.log(obj)

    for (i=0; i<rateList.length; i++){
        obj[String(rateList[i])].push(i+1)
        console.log( obj[String(rateList[i])])
        obj[String(rateList[i])].sort((a,b)=>a-b)
    }
    
    for (i=0; i<newList.length; i++){
        answer.concat(obj[String(newList[i])])
    }
    
    return answer;
}

let result = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])