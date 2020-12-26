function compareTriplets(a, b) {
	var i;
	var allice = 0;
	var bob = 0;
	for (i = 0; i < a.length; i++) {
		if(a[i] > b[i]){
			allice+=1;
		}
		else if(b[i] >a[i]){
			bob+=1;
		}
		else {
			

		}


	}
	return [allice,bob]


}

console.log(compareTriplets([52,32,12],[33,44,23]))