def timeConversion(s):
	a = s.split(':')
	b = s[-2:]
	print(b)
	if int(a[0]) < 12 and b =='PM':
		a[0] = str(int(a[0])+12)
		a[2] = a[2].replace(b,'')
	elif int(a[0]) ==12 and  b =="AM":
		a[0] = str(int(a[0]) - 12) + '0'
		a[2] = a[2].replace(b,'')
	else:
		a[2] = a[2].replace(b,'')

	return ":".join(a)

print(timeConversion('06:40:03AM')) 