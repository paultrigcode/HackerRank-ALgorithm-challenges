function simpleArraySum(ar) {
	var sum = ar.reduce(function(a, b){
        return a + b;
    }, 0);
 	return sum

}

console.log(simpleArraySum([1,2,3,4]))
