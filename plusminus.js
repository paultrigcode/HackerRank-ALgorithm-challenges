function plusMinus(arr) {
	var positive =[]
	var negative =[]
	var zero =[]
	for (i = 0; i < arr.length; i++) {
		if (arr[i] > 0){
			positive.push(arr[i])

		}
		else if(arr[i] < 0){
			negative.push(arr[i])
		}
		else{
			zero.push(arr[i])
		}
	}
	console.log(positive.length/arr.length);
	console.log(negative.length/arr.length)
	console.log(zero.length/arr.length)


}


console.log(plusMinus([-9,-2,1,0]))