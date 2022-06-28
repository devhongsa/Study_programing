function solution(N, M, amount, value, stomach) {
    let items = {};
  	for(i=0; i<value.length; i++){
    	items[value[i]] = amount[i];
    }
  	let sortList = value.sort(function(a, b)  {
      if(a > b) return -1;
      if(a === b) return 0;
      if(a < b) return 1;
    });
  	let sumStomach = 0;
  	for(i of stomach){
    	sumStomach += i;
    }
  	
  	let sumAmount = 0;
  	let result = 0;
  	
  	for(v of sortList){

        if((sumAmount+items[v]) < sumStomach){
      	result += items[v]*v
        sumAmount += items[v]
        console.log(result, sumAmount)
      }
        else{
            console.log(sumStomach, sumAmount)
      	    result += (sumStomach-sumAmount)*v;
            sumAmount = sumStomach 
            console.log('hi', result)
            break;
      }
    }
  	
    return result;
}

result = solution(4,5,[7,10,4,5],[5,4,3,1],[4,6,2,5,3])
console.log(result)