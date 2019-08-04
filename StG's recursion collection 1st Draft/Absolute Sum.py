def rec_AbSum(p):
    # 'In other... words, return the sum of the absolute values of \
    #  the numbers in a list. Use the built-in abs (e.g. abs(-5) == 5).'
    if len(p) == 1:
    	return abs(p[0])
    else:
    	return rec_AbSum(p[1:]) + abs(p[0])


def iter_AbSum(p):
	sum = 0
	for a in p:
		sum += abs(a)
	return sum

A = [-5,4,-3,2,-1]

print iter_AbSum(A)
print rec_AbSum(A)