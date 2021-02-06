def kangaroo(x1, v1, x2, v2):
	if  x2 > x1 and v2>v1:
		return "NO"
	elif x2>x1 and v2<v1:
		a = []
		b = []
		i =0
		check =False
		# check =  any(item in a for item in b)
		while check == False:
			x1 =x1+v1
			x2 = x2+v2
			a.append(x1)
			b.append(x2)
			# print(a)
			# print(b)
			if a[i] == b[i] and len(a) == len(b):
				check = True
				break
			else:
				i+=1

		return "YES"

	elif x2<x1 and v2>v1 :
		a = []
		b = []
		i =0
		check =False
		# check =  any(item in a for item in b)
		while check == False:
			x1 =x1+v1
			x2 = x2+v2
			a.append(x1)
			b.append(x2)
			# print(a)
			# print(b)
			if a[i] == b[i] and len(a) == len(b):
				check = True
				break
			else:
				i+=1
		return "YES"
	else:
		return "NO"
print(kangaroo(0 ,3, 4, 2))