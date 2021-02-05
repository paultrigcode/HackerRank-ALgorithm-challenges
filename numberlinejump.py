def kangaroo(x1, v1, x2, v2):
	if  x2 > x1 and v2>v1:
		return "NO"
	elif x2>x1 and v2<v1:
		a = []
		b = []
		i =0
		check =  any(item in a for item in b)
		while check == False:
			g = x1+v1
			h = x2+v2
			a.append(g)
			b.append(h)
		if len(a) == len(b):
			return "YES"
		else:
			return "NO"

	else:
		return "YES"

print(kangaroo(0 ,3, 4, 2))