def sum_evens(p):
	sum = 0
	for a in p:
		if a % 2 == 0:
			sum += a
	return sum

print sum_evens([1,2,3,4,5])
print sum_evens([7,21,-9])
print sum_evens([0.5,4])