function timeConversion(s) {
    var a = s.split(':')
    console.log(a)
    var b = a[2].slice(-2)
    console.log(b)
    if (parseInt(a[0]) < 12 && b =='PM'){
    	a[0] = parseInt(a[0])+12
		a[2] = a[2].replace(b,'')
    }
    else if(parseInt(a[0]) ==12 &&  b =="AM"){
		a[0] = parseInt(a[0]) - 12 + '0'
		a[2] = a[2].replace(b,'')
	}
	else {
		a[2] = a[2].replace(b,'')
	}

	return a.join(':')
}

console.log(timeConversion('07:05:45PM'))