def compareTriplets(a, b):
	result = [0,0]
	for i in range(len(a)):
		if a[i] > b[i]:
			result[0]+=1
		elif b[i] > a[i]:
			result[1]+=1
	return result

print(compareTriplets([23,4,74],[22,42,11]))
